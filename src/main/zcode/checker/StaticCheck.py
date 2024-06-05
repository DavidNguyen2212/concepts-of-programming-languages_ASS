from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

# Author: An Nguyen Duc
# Nop ngay 21/04/2024
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
        
class ArrayZcode(Type):
    #* eleType: List[Type], Type ở đây có thể là Zcode, ArrayZcode
    def __init__(self, eleType):
        self.eleType = eleType

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
    
    def setTypeArray(self, typeArray, arrayZcode, param = None):
        #* Trường hợp size khác nhau
        # TH 1 chiều
        if typeArray.size[0] != len(arrayZcode.value):
            return False

        if len(typeArray.size) == 1:
            for member in arrayZcode.value:
                member_type = self.visit(member, param)
                if isinstance(member_type, Zcode):
                    if type(member_type) is VarZcode:
                        Infer.inferVar(param, member.name, typeArray.eleType)
                    elif type(member_type) is FuncZcode:
                        Infer.inferFunc(self.listFunction, member.name.name, typeArray.eleType)
                if isinstance(member_type, ArrayZcode):
                    return False
            
        else:
            for member in arrayZcode.value:
                member_type = self.visit(member, param)
                if isinstance(member_type, Zcode):
                    if type(member_type) is VarZcode:
                        member_type = Infer.inferVar(param, member.name, ArrayType(typeArray.size[1:], typeArray.eleType))
                    elif type(member_type) is FuncZcode:
                        member_type = Infer.inferFunc(self.listFunction, member.name.name, ArrayType(typeArray.size[1:], typeArray.eleType))
                if isinstance(member_type, ArrayZcode):
                    self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType), member, param)

        return True

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
            
            elif isinstance(left_type, Zcode) and isinstance(right_type, ArrayZcode):
                raise TypeCannotBeInferred(ast)

            elif not isinstance(left_type, Zcode) and isinstance(right_type, ArrayZcode):
                if type(left_type) in [BoolType, NumberType, StringType]:
                    raise TypeMismatchInStatement(ast)
                
                if type(left_type) is ArrayType: 
                    setResult = self.setTypeArray(left_type, ast.varInit, param)

                    if not setResult:
                        raise TypeMismatchInStatement(ast)
                    else:
                        right_type = self.visit(ast.varInit, param)
                
            elif isinstance(right_type, ArrayType) and type(right_type.eleType) is VarZcode:
                if type(left_type) is NumberType:
                    right_type.eleType = left_type
                    right_type = Infer.inferVar(param, ast.varInit.arr.name, right_type)
                    right_type = left_type
                elif type(left_type) is VarZcode:
                    raise TypeCannotBeInferred(ast)

            # Vế phải ZCode => gọi hàm suy diễn cho mỗi TH (infer Biến / infer Hàm)
            elif isinstance(right_type, Zcode):
                if type(right_type) is VarZcode:
                    right_type = Infer.inferVar(param, ast.varInit.name, left_type)
                else:
                    right_type = Infer.inferFunc(self.listFunction, ast.varInit.name.name, left_type)

            # Vế trái ZCode => gọi hàm suy diễn cho biến, còn hàm thì không cho phép
            elif isinstance(left_type, Zcode) and type(left_type) is not ArrayZcode:
                if type(left_type) is VarZcode:
                    left_type = Infer.inferVar(param, ast.name.name, right_type)
                else:
                    raise TypeCannotBeInferred(ast)

            # Kiểu đã nhận biết được ở 2 vế
            if not self.compareType(left_type, right_type):
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
            if isinstance(RHS, ArrayZcode):
                set_result = self.setTypeArray(LHS, listRHS[i], param)
                if set_result:
                    RHS = LHS
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
            if isinstance(RHS, ArrayZcode):
                set_result = self.setTypeArray(LHS, listRHS[i], param)
                if set_result:
                    RHS = LHS
            if not self.compareType(LHS, RHS):
                raise TypeMismatchInStatement(ast)
            
        if funcDecl.typ is None:
            funcDecl.typ = VoidType()
            return funcDecl.typ
        if not self.compareType(funcDecl.typ, VoidType()):
            raise TypeMismatchInStatement(ast)    

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
            RHS = Infer.inferFunc(self.listFunction, ast.condExpr.name.name, LHS)
        elif not self.compareType(LHS, RHS):
            raise TypeMismatchInStatement(ast)
        
        # Upd expr
        LHS = NumberType()
        RHS = self.visit(ast.updExpr, param)
        if isinstance(RHS, VarZcode):
            RHS = Infer.inferVar(param, ast.updExpr.name, LHS)
        elif isinstance(RHS, FuncZcode):
            RHS = Infer.inferFunc(self.listFunction, ast.condExpr.name.name, LHS)
        if not self.compareType(LHS, RHS):
            raise TypeMismatchInStatement(ast)
        
        self.BlockFor += 1 #! vào trong vòng for nào anh em
        self.visit(ast.body, [{}] + param) #! tăng tầm vực mới
        self.BlockFor -= 1 #! cút khỏi vòng for nào anh em
    

    def visitReturn(self, ast, param):
        # Return lần 2
        if self.Return == True:
            LHS = self.function.typ
            RHS = self.visit(ast.expr, param)
            if isinstance(RHS, Type) and LHS is None:
                if type(RHS) is not VoidType:
                    self.function.typ = RHS
                    return
                else:
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
            elif isinstance(RHS, ArrayZcode):
                set_result = self.setTypeArray(LHS, ast.expr, param)
                if set_result:
                    return
                else:
                    raise TypeMismatchInStatement(ast)
            if not self.compareType(LHS, RHS):
                raise TypeMismatchInStatement(ast)
            return 
        if ast.expr is None:
            self.function.typ = VoidType()
            self.Return = False
        else:
            self.Return = True
            LHS = self.function.typ
            RHS = self.visit(ast.expr, param)
            if isinstance(RHS, Type) and LHS is None:
                if type(RHS) not in [VoidType, ArrayZcode] :
                    self.function.typ = RHS
                    return
                else:
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

        if isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            raise TypeCannotBeInferred(ast)
        if isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
            raise TypeCannotBeInferred(ast)
        if isinstance(LHS, ArrayZcode) and isinstance(RHS, Zcode):
            raise TypeCannotBeInferred(ast)
        if isinstance(LHS, ArrayZcode) and isinstance(RHS, ArrayZcode):
            raise TypeCannotBeInferred(ast)

        if type(LHS) is VarZcode:
            LHS = Infer.inferVar(param, ast.lhs.name, RHS)
            RHS = self.visit(ast.rhs, param)
        if isinstance(RHS, Zcode):
            if type(RHS) is VarZcode:
                RHS = Infer.inferVar(param, ast.rhs.name, LHS)
            elif type(RHS) is FuncZcode:
                RHS = Infer.inferFunc(self.listFunction, ast.rhs.name.name, LHS)
            LHS = self.visit(ast.lhs, param)

        if not self.compareType(LHS, RHS):
            raise TypeMismatchInStatement(ast)

    def visitBinaryOp(self, ast, param): 
        left_type = self.visit(ast.left, param)
        right_type = self.visit(ast.right, param)

        if ast.op in ['+', '-', '*', '/', '%']:
            if isinstance(left_type, Zcode):
                left_type = Infer.inferVar(param, ast.left.name, NumberType())
                right_type = self.visit(ast.right, param)

            if isinstance(right_type, Zcode): 
                if type(right_type) is VarZcode:
                    right_type = Infer.inferVar(param, ast.right.name, NumberType())
                elif type(right_type) is FuncZcode:
                    right_type = Infer.inferFunc(self.listFunction, ast.right.name.name, NumberType())
                left_type = self.visit(ast.left, param)

            if type(left_type) is NumberType and type(right_type) is NumberType:
                return NumberType()
            raise TypeMismatchInExpression(ast)

        elif ast.op in ['and', 'or']:
            if isinstance(left_type, VarZcode):
                left_type = Infer.inferVar(param, ast.left.name, BoolType())
                right_type = self.visit(ast.right, param)
            if isinstance(right_type, Zcode): 
                if type(right_type) is VarZcode:
                    right_type = Infer.inferVar(param, ast.right.name, BoolType())
                elif type(right_type) is FuncZcode:
                    right_type = Infer.inferFunc(self.listFunction, ast.right.name.name, BoolType())
                left_type = self.visit(ast.left, param)
            if type(left_type) is BoolType and type(right_type) is BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
        
        elif ast.op == '...':
            if isinstance(left_type, Zcode):
                left_type = Infer.inferVar(param, ast.left.name, StringType())
                right_type = self.visit(ast.right, param)
            if isinstance(right_type, Zcode): 
                if type(right_type) is VarZcode:
                    right_type = Infer.inferVar(param, ast.right.name, StringType())
                elif type(right_type) is FuncZcode:
                    right_type = Infer.inferFunc(self.listFunction, ast.right.name.name, StringType())
                left_type = self.visit(ast.left, param)
            if type(left_type) is StringType and type(right_type) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ast)

        elif ast.op in ['=', '!=', '<', '>', '>=', '<=']:
            if isinstance(left_type, Zcode):
                left_type = Infer.inferVar(param, ast.left.name, NumberType())
                right_type = self.visit(ast.right, param)
            if isinstance(right_type, Zcode): 
                if type(right_type) is VarZcode:
                    right_type = Infer.inferVar(param, ast.right.name, NumberType())
                elif type(right_type) is FuncZcode:
                    right_type = Infer.inferFunc(self.listFunction, ast.right.name.name, NumberType())
                left_type = self.visit(ast.left, param)
            if type(left_type) is NumberType and type(right_type) is NumberType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
        
        elif ast.op == '==':
            if isinstance(left_type, Zcode):
                left_type = Infer.inferVar(param, ast.left.name, StringType())
                right_type = self.visit(ast.right, param)
            if isinstance(right_type, Zcode): 
                if type(right_type) is VarZcode:
                    right_type = Infer.inferVar(param, ast.right.name, StringType())
                elif type(right_type) is FuncZcode:
                    right_type = Infer.inferFunc(self.listFunction, ast.right.name.name, StringType())
                left_type = self.visit(ast.left, param)
            if type(left_type) is StringType and type(right_type) is StringType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
        

    def visitUnaryOp(self, ast, param):
        this_type = self.visit(ast.operand, param)

        if ast.op in ['+', '-']:
            if isinstance(this_type, Zcode):
                if type(this_type) is VarZcode:
                    this_type = Infer.inferVar(param, ast.operand.name, NumberType())
                elif type(this_type) is FuncZcode:
                    this_type = Infer.inferFunc(self.listFunction, ast.operand.name.name, NumberType())
            if type(this_type) is NumberType:
                return NumberType()
            raise TypeMismatchInExpression(ast)

        elif ast.op in ['not']:
            if isinstance(this_type, Zcode):
                if type(this_type) is VarZcode:
                    this_type = Infer.inferVar(param, ast.operand.name, BoolType())
                elif type(this_type) is FuncZcode:
                    this_type = Infer.inferFunc(self.listFunction, ast.operand.name.name, BoolType())
            if type(this_type) is BoolType():
                return BoolType()
            raise TypeMismatchInExpression(ast)


    def visitArrayCell(self, ast, param):
        arrType = self.visit(ast.arr, param)
        if type(arrType) is not ArrayType and not isinstance(arrType, Zcode):
            raise TypeMismatchInExpression(ast)
 
        LHS = NumberType()
        for i in range(len(ast.idx)):
            RHS = self.visit(ast.idx[i], param)
            if isinstance(RHS, Zcode):
                if type(RHS) is VarZcode:
                    RHS = Infer.inferVar(param, ast.idx[i].name, NumberType())
                elif type(RHS) is FuncZcode:
                    RHS = Infer.inferFunc(self.listFunction, ast.idx[i].name.name, NumberType())
            if not self.compareType(LHS, RHS):
                raise TypeMismatchInExpression(ast)
        
        left = self.visit(ast.arr, param)
        if type(left) is VarZcode:

            # return ArrayType(new_size ,left.eleType)
            idx =  self.visit(ast.idx[0], param)
            if type(idx) is ArrayType:
                left = Infer.inferVar(param, ast.arr.name, ArrayType([len(ast.idx)] + idx.size, VarZcode()))
            else:
                left = Infer.inferVar(param, ast.arr.name, ArrayType([len(ast.idx)], VarZcode()))
            return left
        
        if len(left.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        elif len(left.size) == len(ast.idx):
            return type(left.eleType)
        else:
            new_size = left.size[len(ast.idx) : ]
            return ArrayType(new_size ,left.eleType)

    def visitArrayLiteral(self, ast, param):
        #* bước 1 chọn được type đã xác định kiểm trong ast.value (typ không phải là Zcode và ArrayZcode)
        typ = None
        for item in ast.value:
            checkTyp = self.visit(item, param)
            if not (isinstance(checkTyp, Zcode) or isinstance(checkTyp, ArrayZcode)):
                typ = checkTyp
                break
        eleType = []
        #* Bước 2: xét kiểu từng phần tử
        #^ TH1 : typ is None nghĩa là trong array chỉ gồm Zcode và ArrayZcode nên return ArrayZcode
        if typ is None:
            # TODO implement
            eleType = reduce(lambda prev, curr: prev + [self.visit(curr, param)], ast.value, [])
            return ArrayZcode(eleType)
        #^ TH2 : typ in [StringType, BoolType, NumberType] duyệt qua ast.value nếu typ từng phần tử có ArrayZcode hay là comparType bị khác thì nén TypeMismatchInExpression
        elif type(typ) in [StringType, BoolType, NumberType]:
            for expr in ast.value:
                expr_typ = self.visit(expr, param)
                if type(expr_typ) is VarZcode:
                    Infer.inferVar(param, expr.name, typ)
                    expr_typ = typ
                elif type(expr_typ) is FuncZcode:
                    Infer.inferFunc(self.listFunction, expr.name.name, typ)
                    expr_typ = typ
                if type(expr_typ) is ArrayZcode or not self.compareType(expr_typ, typ):
                    raise TypeMismatchInExpression(ast)
            return ArrayType([len(ast.value)], typ)

        else:
            for expr in ast.value:
                expr_typ = self.visit(expr, param)
                if type(expr_typ) is ArrayZcode:
                    if self.setTypeArray(typ, expr, param):
                        expr_typ = typ
                if type(expr_typ) is VarZcode:
                    Infer.inferVar(param, expr.name, typ)
                    expr_typ = typ
                elif type(expr_typ) is FuncZcode:
                    Infer.inferFunc(self.listFunction, expr.name.name, typ) 
                    expr_typ = typ
                if not self.compareType(expr_typ, typ):
                    raise TypeMismatchInExpression(ast) 
            return ArrayType([len(ast.value)] + expr_typ.size, expr_typ.eleType)


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
