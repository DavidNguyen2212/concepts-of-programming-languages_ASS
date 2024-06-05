from Emitter import *
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class CodeGenerator:
    def gen(self, ast, path):
        # ast: AST
        # dir_: String
        gc = CodeGenVisitor(ast, path)
        gc.visit(ast, None)

class Access():
    def __init__(self, frame, symbol, isLeft, checkTypeLHS_RHS = False):
        self.frame = frame #* không gian stack và local cần dùng để chạy 1 hàm
        self.symbol = symbol #* giống phần param ở BTL3 nhưng này hiện thực list<list>> (có thể dùng list<dict> như btl3)
        self.isLeft = isLeft #* hiện tại vế trên trái hay bên phải để xác định get và put cho biến
        self.checkTypeLHS_RHS = checkTypeLHS_RHS  #* kiểm tra kiểu đúng không

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, path):
        self.astTree = astTree
        self.path = path
        self.className = "ZCodeClass"
        self.emit = Emitter(self.path + "/" + self.className  + ".j")
        self.Listfunction = []
        self.function = None
        self.Return = False
        self.arrayCell = "" 
    
    def printListfunction(self):
        print(f"self.function: {str(self.function)}" )
        print(f"self.Return  : {str(self.Return)}" )
        print(f"listFunction :")
        for item in self.Listfunction:
            print(f"         : {str(item)}" )

    
    #* CẬP NHẬT TYPE
    def LHS_RHS(self, LHS, RHS, o):
        #* TRUYỀN checkTypeLHS_RHS = False -> nghĩa là chúng ta xét type trước, trước khi lấy stack
        _, rhsType = self.visit(RHS, Access(o.frame, o.symbol, False, True))
        _, lhsType = self.visit(LHS, Access(o.frame, o.symbol, True, True))
        # Nếu lhsType là Zcode => gán typ bằng kiểu phải, setType
        if isinstance(lhsType, Zcode):
            lhsType.typ = rhsType
            self.emit.setType(lhsType) #* cập nhật lại type vì trước đó type là None
            
        elif isinstance(rhsType, Zcode):
           rhsType.typ = lhsType
           self.emit.setType(rhsType) #* cập nhật lại type vì trước đó type là None
    

    def visitProgram(self, ast:Program, o):
        #* khởi tạo chương trình ZCodeClass
        starter_code = self.emit.emitPROLOG(self.className, "java.lang.Object")
        self.emit.printout(starter_code)
    
        #* cập nhật biến toàn cục và function, và khởi tạo self.emit.emitATTRIBUTE cho biến toàn cục
        Symbol = [[]]
        Main = None
        function = None
        for item in ast.decl:
            if type(item) is VarDecl:
                index = -1
                # Symbol[0] đang nạp vào các biến toàn cục
                Symbol[0].append(VarZcode(item.name.name, item.varType, -1, True if item.varInit else False))
                # Sử dụng emit attribute cho biến toàn cục, 2 biến cuối cho mặc định vì btl ko sài
                # Nếu là var/dynamic thì lấy luôn kiểu của thằng phía trên nó luôn
                globalvar_code = self.emit.emitATTRIBUTE(item.name.name, item.varType if item.varType else Symbol[0][-1], False, self.className)
                self.emit.printout(globalvar_code)
                # Lấy vị trí hàng vừa khởi tạo lưu vào line trong buff
                Symbol[0][-1].line = self.emit.printIndexNew()

            elif type(item) is FuncDecl and item.body is not None:
                # Duyệt qua item là func và chỉ xét lần đề cập kèm hiện thực body
                # Đưa vào khởi tạo tên, typ là None tại chưa xét kiểu, list kiểu của param
                self.Listfunction += [FuncZcode(item.name.name, None, [i.varType for i in item.param])]
                # Nếu hàm là main thì gán cho biến function và Main
                if item.name.name == "main":
                    function = self.Listfunction[-1]
                    Main = item
        
        #* hàm khởi tạo trong Zcode (constructor bắt buộc)
        # Chính là .method public <init>()V
        frame = Frame("<init>", VoidType)
        method_code = self.emit.emitMETHOD(lexeme="<init>", in_=FuncZcode("init", VoidType(), []), isStatic=False, frame=frame)
        self.emit.printout(method_code)
        # Đi vào hàm khởi tạo
        frame.enterScope(True) # sau khi gọi enterScope sẽ tạo ra 2 label khởi đầu và kết thúc
        # Trong hình của Tiến là Label0 và Label1
        setStartLabel_code = self.emit.emitLABEL(frame.getStartLabel(), frame)
        self.emit.printout(setStartLabel_code)
        
        # Tạo ra đối ẩn this (dưới dạng khởi tạo biến cục bộ dùng emitVAR)
        createThis_code = self.emit.emitVAR(frame.getNewIndex(), "this", Zcode(), frame.getStartLabel(), frame.getEndLabel(), frame) 
        self.emit.printout(createThis_code)

        # Đọc biến cục bộ các kiểu num bool string (đọc this), kiểu là ZCodeClass
        readThis_code = self.emit.emitREADVAR("this", self.className, 0, frame)
        self.emit.printout(readThis_code)
        # Invoke đặc biệt của hàm khởi tạo
        invokeInit_code = self.emit.emitINVOKESPECIAL(frame)
        self.emit.printout(invokeInit_code) 
        # Tạo dòng return
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))

        # Tạo endLabel
        setEndLabel_code = self.emit.emitLABEL(frame.getEndLabel(), frame)
        self.emit.printout(setEndLabel_code)

        # Kết thúc method, xác định limit stack, limit locals
        ender_code = self.emit.emitENDMETHOD(frame)
        self.emit.printout(ender_code)
        frame.exitScope()


        #* hàm khởi tạo biến static Zcode (constructor cho static)
        # Một frame là một cục code lớn
        frame = Frame("<clinit>", VoidType)
        method_code = self.emit.emitMETHOD(lexeme="<clinit>", in_=FuncZcode("clinit", VoidType(), []), isStatic=True, frame=frame)
        self.emit.printout(method_code)

        frame.enterScope(True)
        # Đặt startLabel
        setStartLabel_code = self.emit.emitLABEL(frame.getStartLabel(), frame)
        self.emit.printout(setStartLabel_code)

        #* có 2 TH là khởi tạo và khởi tạo array
        for var in ast.decl:
            # Ví dụ number a <- 0
            if type(var) is VarDecl and var.varInit is not None:
                # Tạo code (hiện thực cho Assign)
                self.visit(Assign(var.name, var.varInit), Access(frame, Symbol, False))

            # Ví dụ bool b[2] 
            elif type(var) is VarDecl and type(var.varType) is ArrayType:
                # Trường hợp này đúng là mảng 1 chiều
                if len(var.varType.size) == 1:
                    # Chỉ lấy code không lấy kiểu vì là expression
                    visit_Dimcode = self.visit(NumberLiteral(var.varType.size[0]), Access(frame, Symbol, False))[0]
                    self.emit.printout(visit_Dimcode)
                    # Chuyển float thành int
                    self.emit.printout(self.emit.emitF2I(frame))
                    # Tạo ra array một chiều
                    array1_code = self.emit.emitNEWARRAY(var.varType.eleType, frame)
                    self.emit.printout(array1_code)
                    # cập nhật giá trị của biến toàn cục (array này)
                    # kết quả: putstatic ZCodeClass.b [Z
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + var.name.name, var.varType, frame))

                else:
                    # Trường hợp mảng nhiều chiều xét từng cái
                    for i in var.varType.size:
                        # Emit và F2I cho từng cái
                        self.emit.printout(self.visit(NumberLiteral(i), Access(frame, Symbol, False))[0])
                        self.emit.printout(self.emit.emitF2I(frame))
                    # tạo ra array nhiều chiều
                    self.emit.printout(self.emit.emitMULTIANEWARRAY(var.varType, frame))
                    # cập nhật giá trị của biến toàn cục (array này)
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + var.name.name, var.varType, frame))
        
        return_code = self.emit.emitRETURN(VoidType(), frame)
        self.emit.printout(return_code) 
        setEndLabel_code = self.emit.emitLABEL(frame.getEndLabel(), frame)
        self.emit.printout(setEndLabel_code)  
        ender_code = self.emit.emitENDMETHOD(frame)
        self.emit.printout(ender_code)
        frame.exitScope()    
    
        
        #* khởi tạo các hàm static
        i = 0
        for item in ast.decl:
            # Nếu không phải hàm main
            if type(item) is FuncDecl and item.body is not None and item.name.name != "main":
                self.function = self.Listfunction[i]
                self.visit(item, Symbol)
            if type(item) is FuncDecl and item.body is not None:
                i += 1
                
        
        #* khởi tạo hàm main
        # Tạo cục code riêng cho main
        frame = Frame("main", VoidType)
        # Tạo dòng .method, để ý main là hàm static
        method_code = self.emit.emitMETHOD(lexeme="main", in_=FuncZcode("main", VoidType(), [ArrayType([1], StringType())]), isStatic=True, frame=frame)
        self.emit.printout(method_code)

        frame.enterScope(True)
        # Đặt Label
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # Khởi tạo biến cục bộ string args[]
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        index = frame.getNewIndex()

        # Tạo biến for
        typeParam = [VarZcode("for", NumberType(), index, True)]
        for_code = self.emit.emitVAR(index, "for", NumberType(), frame.getStartLabel(), frame.getEndLabel(), frame)
        self.emit.printout(for_code)
        self.function = function    # hàm đang xét: main

        self.visit(Main.body, Access(frame, [typeParam] + Symbol, False))
        # Return code
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        # Label kết thúc main
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame)) 
        # End method  
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()  
        # ghi vào file .j để thực hiện biên dịch  
        self.emit.emitEPILOG()
    
    def visitVarDecl(self, ast, o):
        """#TODO: Implement
        #* tạo emitVAR và o.symbol[0].append, cập nhật o.symbol[0][-1].line
        #* if ast.varInit is not None:
            #* elf.visit(Assign(ast.name, ast.varInit), o) 
        #* elif type(ast.varType) is ArrayType:
            #* giống phần khai báo biến static gần giống ý tưởng
        """
        frame = o.frame
        fill_type = ast.varType if ast.varType is not None else None
        idx = frame.getNewIndex()
        var_code = self.emit.emitVAR(idx, ast.name.name, fill_type, frame.getStartLabel(), frame.getEndLabel() , frame)
        self.emit.printout(var_code)
        o.symbol[0].append(VarZcode(ast.name.name, fill_type, idx, True if ast.varInit else False))
        o.symbol[0][-1].line = self.emit.printIndexNew()
        
        if ast.varInit is not None:
            self.visit(Assign(ast.name, ast.varInit), o)
        elif type(ast.varType) is ArrayType:
            if len(ast.varType.size) == 1:
                self.emit.printout(self.visit(NumberLiteral(ast.varType.size[0]), Access(frame, o.symbol, True))[0])
                self.emit.printout(self.emit.emitF2I(frame))
                self.emit.printout(self.emit.emitNEWARRAY(ast.varType.eleType, frame))
                self.emit.printout(self.emit.emitASTORE(ast.varType.eleType, frame))
            else:
                for i in ast.varType.size:
                    self.emit.printout(self.visit(NumberLiteral(i), Access(frame, o.symbol, True))[0])
                    self.emit.printout(self.emit.emitF2I(frame))    
                self.emit.printout(self.emit.emitMULTIANEWARRAY(ast.varType, frame))
                self.emit.printout(self.emit.emitASTORE(ast.varType.eleType, frame))

                              
    def visitFuncDecl(self, ast, o):
        self.Return = False
        """TODO: Implement
        #* giống hàm main, nhưng phần này có param
        """
        self.Listfunction += [FuncZcode(ast.name.name, None, [i.varType for i in ast.param])]
        #* khởi tạo Hàm
        frame = o.frame
        typeParamFunc = [] 
        for vardecl in ast.param:
            typeParam.append(vardecl.varType)
        self.emit.printout(self.emit.emitMETHOD(lexeme=ast.name.name, in_=FuncZcode(ast.name.name, VoidType(), typeParamFunc), isStatic=True, frame=frame))
        
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        if len(ast.param) > 0:
            for vardecl in ast.param:
                each_param_code =  self.emit.emitVAR(frame.getNewIndex(), vardecl.name.name, vardecl.varType, frame.getStartLabel(), frame.getEndLabel(), frame)
                self.emit.printout(each_param_code)

        index = frame.getNewIndex()
        typeParam = [VarZcode("for", NumberType(), index, True)]
        self.emit.printout(self.emit.emitVAR(index, "for", NumberType(), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.function = self.Listfunction[-1]
        self.visit(ast.body, Access(frame, typeParamFunc + [typeParam] + o.symbol, False))
        if self.Return:
            self.emit.printout(self.emit.emitRETURN(self.function.typ), frame)
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))   
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()    
        self.emit.emitEPILOG()
     

    def visitId(self, ast, o):
        frame = o.frame
        Symbol = o.symbol
        
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            for item in Symbol:
                for sym in item:
                    if sym.name == ast.name:
                            return None, sym.typ if sym.typ else sym
        """#TODO : gọi emitINVOKESTATIC
        #* biến cục bộ dùng emitREADVAR, emitWRITEVAR tùy isleft
        #* biến toàn cục (static)  dùng emitPUTSTATIC, emitGETSTATIC tùy isleft
        """                                 
        # code = self.emit.emitINVOKESTATIC()
        for item in Symbol[-1]:
            if item.name == ast.name:   # biến toàn cục
                if o.isLeft:
                    code = self.emit.emitPUTSTATIC(self.className + "." + ast.name, item.typ, frame)
                else:
                    code = self.emit.emitGETSTATIC(self.className + "." + ast.name, item.typ, frame)
                return code, item.typ
        # Chắc là biến cục bộ
        for env in Symbol:
            for vardecl in env:
                if vardecl.name == ast.name:
                    if o.isLeft:
                        code = self.emit.emitREADVAR(ast.name, vardecl.typ, vardecl.index, frame)
                    else:
                        code = self.emit.emitWRITEVAR(ast.name, vardecl.typ, vardecl.index, frame)
                    return code, vardecl.typ



    def visitCallExpr(self, ast, o):
        #* phần io -> gọi qua class io.java trong phần lib
        if ast.name.name in ["readNumber", "readBool", "readString"]:
            if ast.name.name == "readNumber": 
                if o.checkTypeLHS_RHS: return None, NumberType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, NumberType(), []), o.frame), NumberType
            elif ast.name.name == "readBool": 
                if o.checkTypeLHS_RHS: return None, BoolType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, BoolType(), []), o.frame), NumberType
            elif ast.name.name == "readString": 
                if o.checkTypeLHS_RHS: return None, StringType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, StringType(), []), o.frame), NumberType

        #* tìm function trong self.Listfunction
        function = None
        for item in self.Listfunction:
            if item.name == ast.name.name:
                function = item
                
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            for i in range(len(function.param)):
                self.LHS_RHS(function.param[i], ast.args[i], o)
            return None, function.typ if function.typ else function            
            
        typeParam = []
        ret_code = None
        for idx, arg in enumerate(ast.args):
            code, argtyp = self.visit(arg, Access(o.frame, o.symbol, False))
            ret_code = code if idx == 0 else (ret_code + code)
            typeParam.append(argtyp)
        ret_code += self.emit.emitINVOKESTATIC(self.className + '/' + ast.name.name, 
        FuncZcode(ast.name.name, function.typ if function is not None else None, typeParam), o.frame)
        return ret_code, function.typ
        """#TODO : gọi emitINVOKESTATIC
        ví dụ : 
        .line 12 -> foo(1,true)
        0: iconst_1
        1: iconst_1
        2: invokestatic ZCodeClass/foo(IZ)V        
        """
     

    def visitBinaryOp(self, ast, o):
        op = ast.op
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            if op in ['+', '-', '*', '/', '%']:
                self.LHS_RHS(ast.left, NumberType(), o)
                self.LHS_RHS(ast.right, NumberType(), o)
                return None, NumberType()
            elif op in ['=', '!=', '<', '>', '>=', '<=']:
                self.LHS_RHS(ast.left, NumberType(), o)
                self.LHS_RHS(ast.right, NumberType(), o)
                return None, BoolType()
            elif op in ['and', 'or']:
                self.LHS_RHS(ast.left, BoolType(), o)
                self.LHS_RHS(ast.right, BoolType(), o)
                return None, BoolType()
            elif op in ['==']:
                self.LHS_RHS(ast.left, StringType(), o)
                self.LHS_RHS(ast.right, StringType(), o)
                return None, BoolType()
            elif op in ['...']:
                self.LHS_RHS(ast.left, StringType(), o)
                self.LHS_RHS(ast.right, StringType(), o)
                return None, StringType()
        
        codeLeft, _ = self.visit(ast.left, o)
        codeRight, _ = self.visit(ast.right, o)
        """#TODO emitADDOP, emitMULOP, emitREOP, emitANDOP,emitOROP, emitREOP, emitINVOKEVIRTUAL (dùng java/lang/String/concat và java/lang/String/equals)
        #^ mọi năm có tính toán lười cho and và or năm này thấy thầy ko mô tả lạ thật :((
        #* khó nhất chắc là % ta dùng như sau 
            codeLeft
            codeRight
            codeLeft
            codeRight
            '/'
            emitF2I -> ép kiểu sang int
            emitI2F -> từ in ép kiểu ngược lại
            '*'
            '-'
        """
        # add
        if op in ['+', '-']:
            op_code = self.emit.emitADDOP(op, NumberType(), o.frame)
            rt = NumberType()
        elif op in ['*', '/']:
            op_code = self.emit.emitMULOP(op, NumberType(), o.frame)
            rt = NumberType()
        elif op == '%':
            op_code1 = self.emit.emitMULOP("/", NumberType(), o.frame)
            emitf2i = self.emit.emitF2I(o.frame)
            emiti2f = self.emit.emitI2F(o.frame)
            op_code2 = self.emit.emitMULOP("*", NumberType(), o.frame)
            op_code3 = self.emit.emitADDOP("-", NumberType(), o.frame)
            op_code = codeLeft + codeRight + op_code1 + emitf2i + emiti2f + op_code2 + op_code3
            rt = NumberType()
        elif op == 'and':
            op_code = self.emit.emitANDOP(o.frame)
            rt = BoolType()
        elif op == 'or':
            op_code = self.emit.emitOROP(o.frame)
            rt = BoolType()
        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            op_code = self.emit.emitREOP(op, NumberType(), o.frame)
            rt = BoolType()
        elif op == "==":    # equals -> virtual
            op_code = self.emit.emitINVOKEVIRTUAL(op, StringType(), o.frame)
            rt = BoolType()
        elif op == "...":
            op_code = self.emit.emitINVOKEVIRTUAL(op, StringType(), o.frame)
            rt = StringType()
        
        return codeLeft + codeRight + op_code, rt


    def visitUnaryOp(self, ast, o):
        op = ast.op
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            if op in ['-']:
                self.LHS_RHS(ast.operand, NumberType(), o)
                return None, NumberType()
            elif op in ['not']:
                self.LHS_RHS(ast.operand, BoolType(), o)
                return None, BoolType()
        """#TODO mitNEGOP, emitNOT
        """
        this_code, _ = self.visit(ast.operand, o)
        if op == '-':
            op_code = self.emit.emitNEGOP(NumberType(), o.frame)
            rt = NumberType()
        elif op == 'not':
            op_code = self.emit.emitNOT(BoolType(), o.frame)
            rt = BoolType()
        
        return op_code + this_code, rt

    
    def visitArrayLiteral(self, ast, o):
        frame = o.frame
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            mainTyp = None
            for item in ast.value:
                _, checkTyp = self.visit(item, o)
                if mainTyp is None and isinstance(checkTyp, (BoolType, StringType, NumberType, ArrayType)):
                    mainTyp = checkTyp
                    break
        
            for item in ast.value:
                self.LHS_RHS(mainTyp, item, o)
            
            if isinstance(mainTyp, (BoolType, StringType, NumberType)):
                return None, ArrayType([len(ast.value)], mainTyp)
            return None, ArrayType([float(len(ast.value))] + mainTyp.size, mainTyp.eleType)

        """#TODO:
        #* trường hợp mảng 1 chiều
            emitPUSHCONST -> giá trị khởi tạo của mảng
            emitF2I -> ép kiểu sang int
            emitNEWARRAY -> khởi tạo mảng
            for
                emitDUP -> nhân 2 ở đây là địa chỉ của mảng khởi tạo phía trên
                emitPUSHCONST -> giá trị index trong mảng
                emitF2I
                visit -> giá trị biến
                emitASTORE -> lưu trữ
    
        #* trường hợp mảng nhiều chiều
            emitPUSHCONST -> giá trị khởi tạo của mảng
            emitF2I -> ép kiểu sang int
            emitANEWARRAY -> khởi tạo mảng
            for
                emitDUP -> nhân 2 ở đây là địa chỉ của mảng khởi tạo phía trên
                emitPUSHCONST -> giá trị index trong mảng
                emitF2I
                visit -> giá trị biến
                emitASTORE -> lưu trữ             
        """
       
    def visitArrayCell(self, ast, o):
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            _, arr = self.visit(ast.arr, Access(o.frame, o.symbol, False, False))
            for i in ast.idx:
                self.LHS_RHS(NumberType(), i, o)
            if len(arr.size) == len(ast.idx): return None, arr.eleType
            return None, ArrayType(arr.size[len(ast.idx):], arr.eleType)   


        """#TODO: implement
        #* trường trả về giá trị khác mảng
            visit(ast.arr) -> lấy ra get/put/read/write
            for 0 -> size - 1
               giá trị tại index
               f2i
               aload
            giá trị tại index = -1
            f2i
            float/bload/aload(string)  (nếu o.isLeft thì bỏ qua không gọi mà gán self.arrayCell = typ)  
    
        #* trường hợp tra về magnr
            visit(ast.arr) -> lấy ra get/put/read/write
            for 0 -> size - 1
               giá trị tại index
               f2i
               aload
            giá trị tại index = -1
            f2i
            aload -> địa chỉ   (nếu o.isLeft thì bỏ qua không gọi mà gán self.arrayCell = typ)            
        """
        
       
        
    def visitNumberLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, NumberType(), o.frame) if not o.checkTypeLHS_RHS else None, NumberType()
    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, BoolType(), o.frame) if not o.checkTypeLHS_RHS else None, BoolType()
    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), o.frame) if not o.checkTypeLHS_RHS else None, StringType()
    def visitArrayType(self, ast, param): return None, ast
    def visitNumberType(self, ast, param): return None, NumberType()
    def visitVoidType(self, ast, param): return None, VoidType()
    def visitBoolType(self, ast, param): return None, BoolType()
    def visitStringType(self, ast, param): return None, StringType()
    def visitFuncZcode(self, ast, param): return None, ast.typ if ast.typ else ast
    def visitVarZcode(self, ast, param): return None, ast.typ if ast.typ else ast
    
    
    def visitReturn(self, ast, o):
        #* CHECK TYPE BTL3
        self.LHS_RHS(self.function, ast.expr if ast.expr else VoidType(),o)
        
        self.Return = True #* đã có return
        frame = o.frame
        
        """#TODO emitRETURN
        #* TH1 : nếu  ast.expr is None
        return
        
        #* TH2 : Ngc lại vd : return 1
        iconst_1
        freturn
        """
        if ast.expr is None:
            return_code = self.emit.emitRETURN(VoidType(), o.frame)
            self.emit.printout(return_code)
        else:
            return_code, return_typ = self.visit(ast.expr, o)
            return_code += self.emit.emitRETURN(return_typ, o.frame)
            self.emit.printout(return_code)


    def visitAssign(self, ast, o):
        self.LHS_RHS(ast.lhs, ast.rhs, o)
        frame = o.frame
        rhsCode, _ = self.visit(ast.rhs, Access(frame, o.symbol, False))
        # lhsCode, _ = self.visit(ast.lhs, Access(frame, o.symbol, True))
        lhsCode, lhsTyp = self.visit(ast.lhs, Access(frame, o.symbol, True))
        
        """#TODO
        TH1 : LHS = ArrayCell
        lhsCode
        rhsCode
        self.emit.emitASTORE(self.arrayCell, frame))
        
        TH2 : 
        lhsCode
        rhsCode        
        """
        if type(lhsTyp) is ArrayCell:
            self.emit.printout(rhsCode)
            self.emit.printout(lhsCode)
            self.emit.emitASTORE(self.arrayCell, frame)
        else:
            self.emit.printout(rhsCode)
            self.emit.printout(lhsCode)
  
    
    def visitCallStmt(self, ast, o):
        #* phần io
        if ast.name.name in ["writeNumber", "writeBool", "writeString"]:
            if ast.name.name == "writeNumber": self.LHS_RHS(NumberType(), ast.args[0], o)
            elif ast.name.name == "writeBool": self.LHS_RHS(BoolType(), ast.args[0], o)
            elif ast.name.name == "writeString": self.LHS_RHS(StringType(), ast.args[0], o)
            
            argsCode, argsType = self.visit(ast.args[0], o)
            self.emit.printout(argsCode)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, VoidType(), [argsType]), o.frame))
            return

        """#TODO giống call expr"""
        #* tìm function trong self.Listfunction
        function = None
        for item in self.Listfunction:
            if item.name == ast.name.name:
                function = item
                
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            for i in range(len(function.param)):
                self.LHS_RHS(function.param[i], ast.args[i], o)
            return
            # return None, function.typ if function.typ else function            
            
        typeParam = []
        ret_code = None
        for idx, arg in enumerate(ast.args):
            code, argtyp = self.visit(arg, Access(o.frame, o.symbol, False))
            ret_code = code if idx == 0 else (ret_code + code)
            typeParam.append(argtyp)
        ret_code += self.emit.emitINVOKESTATIC(self.className + '/' + ast.name.name, 
        FuncZcode(ast.name.name, VoidType(), typeParam), o.frame)
        self.emit.printout(ret_code)
          
    def visitBlock(self, ast, o):
        symbolnew = [[]] + o.symbol #! tăng tầm vực
        o.frame.enterScope(False) #* tầm vực mới, vì biến khởi tạo sẽ được xóa khi kết thúc tầm vực nên cần scope
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame)) #* đánh số tầm vực mới
        for item in ast.stmt: 
            self.visit(item,Access(o.frame, symbolnew, False))   
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame)) #* đánh số tầm vực mới
        o.frame.exitScope()  #* kết thức tầm vực
       
    def visitIf(self, ast, o):
        #* CHECK TYPE BTL3       
        self.LHS_RHS(BoolType(), ast.expr, o)        
        for item in ast.elifStmt:
            self.LHS_RHS(BoolType(), item[0], o)   
        
        frame = o.frame
        ec, et = self.visit(ast.expr, Access(frame, o.symbol, False))
        self.emit.printout(ec)
        endIf_Label = frame.getNewLabel()
        fail_code = self.emit.emitIFFALSE(endIf_Label, frame)
        self.emit.printout(fail_code)

        # visit body
        self.visit(ast.thenStmt, o)
        # goto exit
        label_exit = frame.getNewLabel()
        code = self.emit.emitGOTO(label_exit, frame)
        self.emit.printout(code)
        # Đặt label endif
        code = self.emit.emitLABEL(endIf_Label, frame)

        """_enterLoop_
            điều kiện if -> nhảy đến đặt label end if
                |
            visit body
                |
            goto exit
                |
            đặt label end if
                |
            nếu có eilf -> for
                        tạo lable mới
                            |
                        điều kiện -> nhảy lable mới
                            | 
                        visit
                            |
                        goto exit
                            |
                        đặt đến lable mới
                            |
            -- end for
                |
            nếu có else
                            |
                          visit
                            |
            lable exit
        """
        if ast.elifStmt is not None:
            for tupleEx_St in ast.elifStmt:
                endTuple_Label = frame.getNewLabel()
                ec, et = self.visit(tupleEx_St[0], Access(frame, o.symbol, False))
                self.emit.printout(ec)
                failTuple_code = self.emit.emitIFFALSE(endTuple_Label, frame)
                self.emit.printout(failTuple_code)
                self.visit(tupleEx_St[1], o)
                # goto exit
                code = self.emit.emitGOTO(label_exit, frame)
                self.emit.printout(code)
                code = self.emit.emitLABEL(endTuple_Label, frame)
                self.emit.printout(code)

        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, o)

        code = self.emit.emitLABEL(label_exit, frame)
        self.emit.printout(code)
        #TODO: implement

        
    def visitFor(self, ast, o):
        
        #* CHECK TYPE BTL3
        """_typID_"""        
        self.LHS_RHS(NumberType(), ast.name, o)        
        
        """_typCondExpr_"""    
        self.LHS_RHS(BoolType(), ast.condExpr, o) 

        """_typUpdExpr_"""            
        self.LHS_RHS(NumberType(), ast.updExpr, o) 

        frame = o.frame
        self.visit(ast.name, o)

        """_enterLoop_
            gán for <- ast.name
                |
            tạo Loop
                |
            lable_new
                |
            kiểm tra exp để goto đến lable_Break
                |
            visit body
                |
            đặt lable continue
                |
            gọi phép gán Assign(ast.name, BinaryOp('+', ast.name, ast.updExpr))
                |
            goto đến lable_new
                |
            đặt lable_Break
                |
            end loop
                |
            gán for <- ast.name
            
        """
        self.visit(Assign(Id("for"), ast.name), o)
        # Tạo loop
        frame.enterLoop()
        label_new = frame.getNewLabel()
        code = self.emit.emitLABEL(label_new, frame)
        contLabel = frame.getContinueLabel()
        brekLabel = frame.getBreakLabel()
        ec, et = self.visit(ast.condExpr, Access(frame, o.symbol, False))
        self.emit.printout(ec)

        code = self.emit.emitIFFALSE(brekLabel, frame)
        self.emit.printout(code)

        # visit khối lệnh
        self.visit(ast.body, o)

        # Đặt label continue
        code = self.emit.emitLABEL(contLabel, frame)
        self.emit.printout(code)

        Assign(ast.name, BinaryOp('+', ast.name, ast.updExpr))
        code = self.emit.emitGOTO(label_new, frame)
        self.emit.printout(code)

        code = self.emit.emitLABEL(brekLabel, frame)
        self.emit.printout(code)

        #TODO implement
        self.visit(Assign(ast.name, Id("for")), o)

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
        

