from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode:
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    
        
class Infer:
    @classmethod
    def inferVar(cls, param, nameToInfer, typeToInfer):
        for env in param:
            if nameToInfer in env.keys(): 
                env[nameToInfer] = typeToInfer
                return typeToInfer
    @classmethod
    def inferFunc(cls, listFunc, nameToInfer, typeToInfer):
        for env in listFunc:
            if nameToInfer in env.keys(): 
                env[nameToInfer].typ = typeToInfer
                return typeToInfer
            
class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast, ):
        self.ast = ast
        self.BlockFor = 0
        self.function = None #! hàm hiện tại đang được dùng để kiểm tra static
        self.Return = False #! kiểm tra hàm hiện tại có return hay không
        
        #! lưu danh sách các hàm dưới dạng Dict 
        self.listFunction = [{
                "readNumber" : FuncZcode([], NumberType(), True),
                "readBool" : FuncZcode([], BoolType(), True),
                "readString" : FuncZcode([], StringType(), True),
                "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
                "writeBool" : FuncZcode([BoolType()], VoidType(), True),
                "writeString" : FuncZcode([StringType()], VoidType(), True)
                }]
        
    def check(self):
        self.visit(self.ast, [{}])
        return None
    
    def compareType(self, LHS, RHS):
        if type(LHS) is type(RHS): 
            if type(RHS) is not ArrayType:
                return True
            else:
                if type(LHS.eleType) is not type(RHS.eleType):
                    return False
                if len(LHS.size) == len(RHS.size):
                    # return all([x == y for x,y in zip(LHS.size, RHS.size)])
                    return all(list(map(lambda x,y: x == y, LHS.size, RHS.size))) 
                return False
        return False
    

    def compareListType(self, listLHS, listRHS):
        if len(listLHS) == len(listRHS):
            return all(list(map(self.compareType, listLHS, listRHS)))
        return False 
    
    
    def visitProgram(self, ast, param):
        #! duyệt qua các biến và hàm toàn cục
        # for i in ast.decl: self.visit(i, param)
        reduce(lambda _, ele: self.visit(ele, param), ast.decl, [])
        
        # No definition for function
        for key, value in self.listFunction[0].items():
            if type(value) is FuncZcode:
                if not value.body:
                    raise NoDefinition(key)
        
        # No entrypoint - main
        get_main = self.listFunction[0].get("main")
        if get_main is None:
            raise NoEntryPoint()
        elif type(get_main.typ) is not VoidType or get_main.param != []:
            raise NoEntryPoint()

    def visitVarDecl(self, ast, param):
        # Kiểm tra không có trùng lặp
        if ast.name.name in param[0]:
            raise Redeclared(Variable(), ast.name.name)

        # Gán varType cho param đó nếu kiểu là đã biết
        # Nếu là var hoặc dynamic ta tạm cho nó là VarZcode
        param[0][ast.name.name] = ast.varType if ast.varType is not None else VarZcode()

        # Xử lý varInit nếu tồn tại: var decl, norm decl và dynamic decl
        if ast.varInit is not None:
            right_type = self.visit(ast.varInit, param)
            left_type = self.visit(ast.name, param)
            # Nếu cùng là VarZcode hoặc FuncZcode không cho phép suy diễn
            if (type(left_type) is VarZcode and type(right_type) is VarZcode) or \
            (type(left_type) is FuncZcode and type(right_type) is FuncZcode):
                raise TypeCannotBeInferred(ast)
            
            # Vế phải ZCode => gọi hàm suy diễn cho mỗi TH (infer Biến / infer Hàm)
            elif isinstance(right_type, Zcode):
                if type(right_type) is VarZcode:
                    right_type = Infer.inferVar(param, ast.varInit.name, left_type)
                else:
                    right_type = Infer.inferFunc(self.listFunction, ast.varInit.name.name, left_type)

            # Vế trái ZCode => gọi hàm suy diễn cho biến, còn hàm thì không cho phép
            elif isinstance(left_type, Zcode):
                if type(left_type) is VarZcode:
                    left_type = Infer.inferVar(param, ast.name.name, right_type)
                else:
                    raise TypeCannotBeInferred(ast)

            # Kiểu đã nhận biết được ở 2 vế
            elif not self.compareType(left_type, right_type):
                raise TypeMismatchInStatement(ast)
        
        # Nếu không tồn tại var Init
        else:
            # có thể là hoặc dynamic
            if ast.modifier is not None:
                param[0][ast.name.name] = VarZcode(ast.varType)
            # hoặc norm decl 
            else: 
                param[0][ast.name.name] = ast.varType
        
        return param

    def visitFuncDecl(self, ast, param):
        # Kiểm tra trùng lặp
        if ast.name.name in self.listFunction[0]:
            # Gọi cái đã có ra thử
            func = self.listFunction[0].get(ast.name.name)
            # Nếu nó đã có body chứng tỏ Redeclared
            if func.body:
                raise Redeclared(Function(), ast.name.name)
            # Nếu đã chưa có body và cái mới cũng chưa có body bắt luôn Redeclared
            elif not func.body and ast.body is None: 
                raise Redeclared(Function(), ast.name.name)
        
        listParam = {} #! dạng Dict có name khi visit dùng self.visit(ast.body, [listParam] + param)
        typeParam = [] #! dạng mảng không cần name truyền agrc vào FuncZcode
        
        for vardecl in ast.param:
            name = vardecl.name.name
            if name in listParam:
                raise Redeclared(Parameter(), name)
            else:
                listParam[name] = vardecl.varType
                typeParam.append(vardecl.varType)
        
        func = self.listFunction[0].get(ast.name.name)
        self.Return = False #! kiểm tra hàm hiện tại có return hay không

        # Nếu method đã tồn tại trước khi khai báo 1 phần => Kiểm tra lại tham số có giống không
        if type(func) is FuncZcode and not func.body:
            # print("Func: ", func.param)
            # print("Type param: ", typeParam)
            # print("Type param: ", func.param[0])

            if not self.compareListType(func.param, typeParam):
                raise Redeclared(Function(), ast.name.name)
        
        if ast.body:
            # if func is not None and func.typ is not None:
            if func is not None:
                # self.listFunction[0][ast.name.name] = FuncZcode(typeParam, func.typ, True)
                func.body = True
            else:
                self.listFunction[0][ast.name.name] = FuncZcode(typeParam, None, True)
            self.function = self.listFunction[0][ast.name.name]
            self.visit(ast.body, [listParam] + param)
            self.function = None
            #! hàm này không có return
            if not self.Return:
                #! type cũng chưa có luôn ta xác định nó VoidType
                if self.listFunction[0][ast.name.name].typ is None:
                    self.listFunction[0][ast.name.name].typ = VoidType()
                #! type đã có so sánh nó với VoidType
                elif not self.compareType(self.listFunction[0][ast.name.name].typ, VoidType()): 
                    raise TypeMismatchInStatement(Return(None))

        else:
            self.listFunction[0][ast.name.name] = FuncZcode(typeParam, None, False)

        return self.listFunction

    def visitId(self, ast, param):
        for env in param:
            if env.get(ast.name) is not None:
                # Nếu nó là một cái Type thì trả về type đó
                if isinstance(env.get(ast.name), Type):
                    return env.get(ast.name)
                # Trả về biến giả định nếu nó chưa xác định
                return VarZcode()   
        else:
            raise Undeclared(Identifier(), ast.name)
   

    def visitCallExpr(self, ast, param):
        funcDecl = ''
        for env in self.listFunction:
            if env.get(ast.name.name) is not None:
                funcDecl = env[ast.name.name]
                break
        else:
            raise Undeclared(Function(), ast.name.name)
        
        listLHS = funcDecl.param
        listRHS = ast.args
            
        if len(listRHS) != len(listLHS):
            raise TypeMismatchInExpression(ast)
        for i in range(len(listLHS)):
            LHS = self.visit(listLHS[i], param)
            RHS = self.visit(listRHS[i], param)
            # RHS trả về một VarZcode -> dynamic -> cần infer nó
            if isinstance(RHS, VarZcode):
                RHS = Infer.inferVar(param, listRHS[i].name, LHS)
            if not self.compareType(LHS, RHS):
                raise TypeMismatchInExpression(ast)
            
        if funcDecl.typ is None:
            return funcDecl
        if self.compareType(funcDecl.typ, VoidType()):
            raise TypeMismatchInExpression(ast)
        return funcDecl.typ

    def visitCallStmt(self, ast, param):
        funcDecl = ''

        for env in self.listFunction:
            if env.get(ast.name.name) is not None:
                funcDecl = env[ast.name.name]
                break
        else:
            raise Undeclared(Function(), ast.name.name)
        
        # list of formal param
        listLHS = funcDecl.param
        # list of applied param
        listRHS = ast.args
 
        if len(listRHS) != len(listLHS):
            raise TypeMismatchInStatement(ast)
        for i in range(len(listLHS)):
            LHS = self.visit(listLHS[i], param)
            RHS = self.visit(listRHS[i], param)
            # RHS trả về một VarZcode -> dynamic -> cần infer nó
            if isinstance(RHS, VarZcode):
                RHS = Infer.inferVar(param, listRHS[i].name, LHS)
            if not self.compareType(LHS, RHS):
                raise TypeMismatchInStatement(ast)
            
        if funcDecl.typ is None:
            funcDecl.typ = VoidType()
            return funcDecl.typ
        if not self.compareType(funcDecl.typ, VoidType()):
            raise TypeMismatchInStatement(ast)
        # return funcDecl.typ
    

    def visitIf(self, ast, param):
        # Kiểm tra điều kiện If
        LHS = BoolType()
        RHS = self.visit(ast.expr, param)
        if isinstance(RHS, VarZcode):
            RHS = Infer.inferVar(param, ast.expr.name, LHS)
        elif isinstance(RHS, FuncZcode):
            RHS = Infer.inferFunc(self.listFunction, ast.expr.name.name, LHS)
        if not self.compareType(LHS, RHS):
            raise TypeMismatchInStatement(ast)

        # Đi thăm then 
        self.visit(ast.thenStmt, [{}] + param)
   
        # Đi thăm các bộ elif
        for Tuple in ast.elifStmt:
            elif_env = [{}] + param
            RHS = self.visit(Tuple[0], elif_env)
            if isinstance(RHS, VarZcode):
                RHS = Infer.inferVar(elif_env, ast.expr.name, LHS)
            if not self.compareType(LHS, RHS):
                raise TypeMismatchInStatement(ast)
            self.visit(Tuple[1], elif_env)
                    
        # Đi thăm else nếu có
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, [{}] + param)

     
    def visitFor(self, ast, param):    
        # Validate the iterable variable 
        LHS = NumberType()
        RHS = self.visit(ast.name, param)
        if isinstance(RHS, VarZcode):
            RHS = Infer.inferVar(param, ast.name.name, LHS)
        if not self.compareType(LHS, RHS):
            raise TypeMismatchInStatement(ast)

        # Cond expr
        LHS = BoolType()
        RHS = self.visit(ast.condExpr, param)
        if isinstance(RHS, VarZcode):
            RHS = Infer.inferVar(param, ast.condExpr.name, LHS)
        elif isinstance(RHS, FuncZcode):
            RHS.typ = BoolType()
            # RHS = Infer.inferVar(param, ast.condExpr.name, LHS)
        elif not self.compareType(LHS, RHS):
            raise TypeMismatchInStatement(ast)
        
        # Upd expr
        LHS = NumberType()
        RHS = self.visit(ast.updExpr, param)
        # print("RHS: ", ast.name)
        if isinstance(RHS, VarZcode):
            RHS = Infer.inferVar(param, ast.updExpr.name, LHS)
        elif isinstance(RHS, FuncZcode):
            RHS.typ = NumberType()
        elif not self.compareType(LHS, RHS):
            raise TypeMismatchInStatement(ast)
        
        self.BlockFor += 1 #! vào trong vòng for nào anh em
        self.visit(ast.body, [{}] + param) #! tăng tầm vực mới
        self.BlockFor -= 1 #! cút khỏi vòng for nào anh em
    

    def visitReturn(self, ast, param):
        if ast.expr is None:
            self.function.typ = VoidType()
            self.Return = False
        else:
            self.Return = True
            LHS = self.function.typ
            RHS = self.visit(ast.expr, param)
            print("lhs: ", LHS)
            print("rhs: ", RHS)
            if isinstance(RHS, Type) and LHS is None:
                if type(RHS) is not VoidType:
                    self.function.typ = RHS
                    return
                else:
                    print("CCChj")
                    raise TypeCannotBeInferred(ast)
            if isinstance(RHS, Zcode) and LHS is not None:
                if type(RHS) is VarZcode:
                    RHS = Infer.inferVar(param, ast.expr.name, LHS)
                else:
                    RHS = Infer.inferFunc(self.listFunction, ast.expr.name.name, LHS)
                return
            elif isinstance(RHS, Zcode) and LHS is None:
                if type(RHS) is VarZcode:
                    raise TypeCannotBeInferred(ast)
                elif RHS.typ is not None:
                    RHS = Infer.inferFunc(self.listFunction, ast.expr.name.name, RHS.typ)
                    LHS = RHS
                    self.function.typ = RHS
                else:
                    raise TypeCannotBeInferred(ast)
            if not self.compareType(LHS, RHS):
                raise TypeMismatchInStatement(ast)


    def visitAssign(self, ast, param):
        LHS = self.visit(ast.lhs, param)
        RHS = self.visit(ast.rhs, param)
        # print("lhs: ", LHS)
        # print("rhs: ", RHS)
        if isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            raise TypeCannotBeInferred(ast)
        elif type(LHS) is VarZcode:
            for env in param:
                if ast.lhs.name in env.keys(): 
                    env[ast.lhs.name] = RHS
                    break
        elif type(RHS) is VarZcode:
            for env in param:
                if ast.rhs.name in env.keys(): 
                    env[ast.rhs.name] = LHS
                    break
        elif not self.compareType(LHS, RHS):
            raise TypeMismatchInStatement(ast)

    def visitBinaryOp(self, ast, param):      
        left_type = self.visit(ast.left, param)
        right_type = self.visit(ast.right, param)

        if ast.op in ['+', '-', '*', '/', '%']:
            if isinstance(left_type, Zcode):
                left_type = Infer.inferVar(param, ast.left.name, NumberType())
            if isinstance(right_type, Zcode): 
                right_type = Infer.inferVar(param, ast.right.name, NumberType())
            if type(left_type) is NumberType and type(right_type) is NumberType:
                return NumberType()
            raise TypeMismatchInExpression(ast)

        elif ast.op in ['and', 'or']:
            if isinstance(left_type, Zcode):
                left_type = Infer.inferVar(param, ast.left.name, BoolType())
            if isinstance(right_type, Zcode):
                right_type = Infer.inferVar(param, ast.right.name, BoolType())
            if type(left_type) is BoolType and type(right_type) is BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
        
        elif ast.op == '...':
            if isinstance(left_type, Zcode):
                left_type = Infer.inferVar(param, ast.left.name, StringType())
            if isinstance(right_type, Zcode):
                right_type = Infer.inferVar(param, ast.right.name, StringType())
            if type(left_type) is StringType and type(right_type) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ast)

        elif ast.op in ['=', '!=', '<', '>', '>=', '<=']:
            if isinstance(left_type, Zcode):
                left_type = Infer.inferVar(param, ast.left.name, NumberType())
            if isinstance(right_type, Zcode): 
                right_type = Infer.inferVar(param, ast.right.name, NumberType())
            if type(left_type) is NumberType and type(right_type) is NumberType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
        
        elif ast.op == '==':
            if isinstance(left_type, Zcode):
                left_type = Infer.inferVar(param, ast.left.name, StringType())
            if isinstance(right_type, Zcode):
                right_type = Infer.inferVar(param, ast.right.name, StringType())
            if type(left_type) is StringType and type(right_type) is StringType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
        

    def visitUnaryOp(self, ast, param):
        this_type = self.visit(ast.operand, param)

        if ast.op in ['+', '-']:
            if isinstance(this_type, Zcode):
                this_type = Infer.inferVar(param, ast.operand.name, NumberType())
            if type(this_type) is NumberType:
                return NumberType()
            raise TypeMismatchInExpression(ast)

        elif ast.op in ['not']:
            if isinstance(this_type, Zcode):
                this_type = Infer.inferVar(param, ast.operand.name, BoolType())
            if type(this_type) is BoolType():
                return BoolType()
            raise TypeMismatchInExpression(ast)


    def visitArrayCell(self, ast, param):
        arrType = self.visit(ast.arr, param)
        if type(arrType) is not ArrayType:
            raise TypeMismatchInExpression(ast)
 
        LHS = NumberType()
        for i in range(len(ast.idx)):
            RHS = self.visit(ast.idx[i], param)
            if isinstance(RHS, Zcode):
                RHS = Infer.inferVar(param, ast.idx[i].name, NumberType())
            if not self.compareType(LHS, RHS):
                raise TypeMismatchInExpression(ast)
        
        left = self.visit(ast.arr, param)
        if len(left.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        elif len(left.size) == len(ast.idx):
            return type(left.eleType)
        else:
            new_size = left.size[len(ast.idx) : ]
            return ArrayType(new_size ,left.eleType)

    """phần này sẽ là cố định do ngắn quá :(( """
    def visitArrayLiteral(self, ast, param):
        #! code chỉ mang tính tham khảo, do BTL này không yêu cầu lỗi khác nhau ArrayLiteral nên thầy ko cho TypeCannotBeInferred
        for item in ast.value: self.visit(item, param)
        typ = self.visit(ast.value[0], param)
        
        #! đệ quy
        if type(typ) in [StringType, BoolType, NumberType]:
            return ArrayType([len(ast.value)], typ)
        return ArrayType([len(ast.value)] + typ.size, typ.eleType)
    
    def visitBlock(self, ast, param):
        for item in ast.stmt:
            #! trường hợp gặp block
            if type(item) is Block:
                env = [{}] + param
                self.visit(item, env)
            else: 
                self.visit(item, param)
        return param
            
    def visitContinue(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)   
    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()
