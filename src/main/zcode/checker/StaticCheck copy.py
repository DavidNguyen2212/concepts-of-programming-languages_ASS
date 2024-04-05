# """
# ^NAME : Võ Tiến
# ^FB : https://www.facebook.com/profile.php?id=100056605580171
# ^GROUP: https://www.facebook.com/groups/211867931379013/
# ^DAY : 25/3/2024
# """
# # from main.zcode.utils.AST import *
# # from main.zcode.utils.Visitor import *
# # from main.zcode.utils.Utils import Utils
# # from StaticError import *
# # from functools import reduce

# from AST import *
# from Visitor import *
# from Utils import Utils
# from StaticError import *
# from functools import reduce

# class Zcode:
#     pass

# class FuncZcode(Zcode):
#     def __init__(self, param = [], typ = None, body = False):
#         self.param = param
#         self.typ = typ
#         self.body = body

# class VarZcode(Zcode):
#     def __init__(self, typ = None):
#         self.typ = typ    
        
# """
# Kiến thức cần 
# List : https://www.w3schools.com/python/python_lists.asp
# Dict : https://www.w3schools.com/python/python_dictionaries.asp
# type() : https://www.w3schools.com/python/python_datatypes.asp
# isinstance() : https://www.w3schools.com/python/ref_func_isinstance.asp
# """
# """
# ^NAME : Võ Tiến
# ^FB : https://www.facebook.com/profile.php?id=100056605580171
# ^GROUP: https://www.facebook.com/groups/211867931379013/
# ^DAY : 25/3/2024
# """
# class Infer:
#     @classmethod
#     def inferVar(cls, param, nameToInfer, typeToInfer):
#         for env in param:
#             if nameToInfer in env.keys(): 
#                 env[nameToInfer] = typeToInfer
#                 return typeToInfer
#     @classmethod
#     def inferFunc(cls, listFunc, nameToInfer, typeToInfer):
#         for env in listFunc:
#             if nameToInfer.name in env.keys(): 
#                 env[nameToInfer.name].typ = typeToInfer
#                 return typeToInfer
            
# class StaticChecker(BaseVisitor, Utils):
#     def __init__(self,ast, ):
#         self.ast = ast
#         self.BlockFor = 0
#         self.function = None #! hàm hiện tại đang được dùng để kiểm tra static
#         self.Return = False #! kiểm tra hàm hiện tại có return hay không
        
#         #! lưu danh sách các hàm dưới dạng Dict 
#         self.listFunction = [{
#                 "readNumber" : FuncZcode([], NumberType(), True),
#                 "readBool" : FuncZcode([], BoolType(), True),
#                 "readString" : FuncZcode([], StringType(), True),
#                 "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
#                 "writeBool" : FuncZcode([BoolType()], VoidType(), True),
#                 "writeString" : FuncZcode([StringType()], VoidType(), True)
#                 }]
        
#     def check(self):
#         self.visit(self.ast, [{}])
#         return None
    
#     def compareType(self, LHS, RHS):
#         if type(LHS) is type(RHS): 
#             if type(RHS) is not ArrayType:
#                 return True
#             else:
#                 if len(LHS.size) == len(RHS.size):
#                     # return all([x == y for x,y in zip(LHS.size, RHS.size)])
#                     return all(list(map(lambda x,y: x == y, LHS.size, RHS.size))) 
#                 return False
#         return False
    

#     def compareListType(self, listLHS, listRHS):
#         if len(listLHS) == len(listRHS):
#             return all(list(map(self.compareType, listLHS, listRHS)))
#         return False 
    
    
#     def visitProgram(self, ast, param):
#         #! duyệt qua các biến và hàm toàn cục
#         for i in ast.decl: self.visit(i, param)
        
#         # TODO_1: No definition for func
#         for key, value in self.listFunction[0].items():
#             if type(value) is FuncZcode:
#                 if not value.body:
#                     raise NoDefinition(key)
        
#         # TODO_2: No entrypoint - main
#         get_main = self.listFunction[0].get("main")
#         if get_main is None:
#             raise NoEntryPoint()
#         elif type(get_main.typ) is not VoidType or get_main.param != []:
#             raise NoEntryPoint()

#     def visitVarDecl(self, ast, param):
#         if ast.name.name in param[0]:
#             # print("PARAM[O]: ", param)
#             # print("PARAM[1]: ", param[-1])
#             # print("XYZT")
#             raise Redeclared(Variable(), ast.name.name)

#         # Sau khi kiểm tra không có trùng lặp
#         # Gán varType cho param đó nếu kiểu là đã biết
#         # Nếu là var hoặc dynamic ta tạm cho nó là VarZcode
#         param[0][ast.name.name] = ast.varType if ast.varType is not None else VarZcode()

#         # Xử lý varInit nếu tồn tại: var decl, norm decl và dynamic decl
#         if ast.varInit is not None:
#             right_type = self.visit(ast.varInit, param)
#             left_type = self.visit(ast.name, param)
#             # print("Right type: ", right_type.typ)
#             # print("Left type: ", left_type)
#             if (isinstance(right_type, VarZcode) or isinstance(right_type, FuncZcode)) and (isinstance(left_type, VarZcode) or isinstance(left_type, FuncZcode)):
#                 print("heref")
#                 raise TypeCannotBeInferred(ast)
            
#             elif isinstance(right_type, Zcode):
#                 if type(right_type) is VarZcode:
#                     right_type = Infer.inferVar(param, ast.varInit.name, left_type)
#                 else:
#                     right_type = Infer.inferFunc(self.listFunction, ast.varInit.name, left_type)

#             elif isinstance(left_type, VarZcode):
#                 print("here2")
#                 for env in param:
#                     if ast.name.name in env.keys():
#                         env[ast.name.name] = right_type
#                     break

#             elif not self.compareType(left_type, right_type):
#                 raise TypeMismatchInStatement(ast)
        
#         # Nếu không tồn tại var Init
#         else:
#             # có thể là hoặc dynamic
#             if ast.modifier is not None:
#                 param[0][ast.name.name] = VarZcode(ast.varType)
#             # hoặc norm decl 
#             else: 
#                 param[0][ast.name.name] = ast.varType
        
#         return param

#     def visitFuncDecl(self, ast, param):
#         if ast.name.name in self.listFunction[0]:
#             func = self.listFunction[0].get(ast.name.name)
#             if func.body:
#                 raise Redeclared(Function(), ast.name.name)
#             elif not func.body and ast.body is None: 
#                 raise Redeclared(Function(), ast.name.name)
        
#         listParam = {} #! dạng Dict có name khi visit dùng self.visit(ast.body, [listParam] + param)
#         typeParam = [] #! dạng mảng không cần name truyền agrc vào FuncZcode
        
#         for vardecl in ast.param:
#             name = vardecl.name.name
#             if name in listParam:
#                 raise Redeclared(Parameter(), name)
#             else:
#                 listParam[name] = vardecl.varType
#                 typeParam.append(vardecl.varType)
        
#         func = self.listFunction[0].get(ast.name.name) if self.listFunction[0].get(ast.name.name) is not None else []
#         self.Return = False #! kiểm tra hàm hiện tại có return hay không
#         # Nếu method đã tồn tại trước khi khai báo 1 phần => Kiểm tra lại tham số có giống không
#         if type(func) is FuncZcode and not func.body:
#             # print("Func param: ", func.param)
#             if not self.compareListType(func.param, typeParam):
#                 raise Redeclared(Function(), ast.name.name)
        
#         if ast.body:
#             # self.listFunction[0][ast.name.name] = FuncZcode(ast.param, None, True)
#             try_get_func = self.listFunction[0].get(ast.name.name)
#             if try_get_func is not None and try_get_func.typ is not None:
#                 self.listFunction[0][ast.name.name] = FuncZcode(typeParam, try_get_func.typ, True)
#             else:
#                 self.listFunction[0][ast.name.name] = FuncZcode(typeParam, None, True)
#             self.function = self.listFunction[0][ast.name.name]
#             self.visit(ast.body, [listParam] + param)
#             self.function = None
#             # if self.listFunction[0][ast.name.name].typ is None:
#             #     self.listFunction[0][ast.name.name].typ = VoidType()
#             #! hàm này không có return
#             if not self.Return:
#                 #! type cũng chưa có luôn ta xác định nó VoidType
#                 if self.listFunction[0][ast.name.name].typ is None:
#                     self.listFunction[0][ast.name.name].typ = VoidType()
#                 #! type đã có so sánh nó với VoidType
#                 elif not self.compareType(self.listFunction[0][ast.name.name].typ, VoidType()): 
#                     raise TypeMismatchInStatement(Return(None))

#         else:
#             # self.listFunction[0][ast.name.name] = FuncZcode(ast.param, None, False)
#             self.listFunction[0][ast.name.name] = FuncZcode(typeParam, None, False)

#         # return param

        
#         return self.listFunction

#     def visitId(self, ast, param):
#         for env in param:
#             if env.get(ast.name) is not None:
#                 # Nếu nó là một cái Type thì trả về type đó
#                 if isinstance(env.get(ast.name), Type):
#                     return env.get(ast.name)
#                 # Trả về biến giả định nếu nó chưa xác định
#                 return VarZcode()   
#             # if env.get(ast.name) is None:
#             #     continue
#             # else:
#             #     # Nếu nó là một cái Type thì trả về type đó
#             #     if isinstance(env.get(ast.name), Type):
#             #         return env.get(ast.name)
#             #     # Trả về typ nếu nó đang ở dạng VarZcode
#             #     return VarZcode()   
#             #     # return env[ast.name].typ if env[ast.name].typ is not None else VarZcode() 
                  
#         else:
#             print("Undeclare tai day")
#             raise Undeclared(Identifier(), ast.name)
   

#     def visitCallExpr(self, ast, param):
#         funcDecl = ''
#         for env in self.listFunction:
#             if env.get(ast.name.name) is not None:
#                 funcDecl = env[ast.name.name]
#                 break
#         else:
#             print("Undeclare tai day Function")
#             raise Undeclared(Function(), ast.name.name)
        
#         listLHS = funcDecl.param
#         listRHS = ast.args
            
#         if len(listRHS) != len(listLHS):
#             print("Raise here")
#             raise TypeMismatchInExpression(ast)
#         for i in range(len(listLHS)):
#             LHS = self.visit(listLHS[i], param)
#             RHS = self.visit(listRHS[i], param)

#             # Vế phải trả về một VarZcode -> dynamic -> cần infer nó
#             if isinstance(RHS, VarZcode):
#                 for env in param:
#                     if listRHS[i].name in env.keys(): 
#                         env[listRHS[i].name] = LHS
#                         break
#             elif not self.compareType(LHS, RHS):
#                 print("Mistmatch here")
#                 raise TypeMismatchInExpression(ast)
            
#         if funcDecl.typ is None:
#             return funcDecl
#         if self.compareType(funcDecl.typ, VoidType()):
#             print("Raise here")
#             raise TypeMismatchInExpression(ast)
#         return funcDecl.typ

#     def visitCallStmt(self, ast, param):
#         funcDecl = ''

#         for env in self.listFunction:
#             # if env.get(ast.name.name) is not None and self.compareType(env[ast.name.name], FuncZcode):
#             if env.get(ast.name.name) is not None:
#                 funcDecl = env[ast.name.name]
#                 break
#         else:
#             # print("Ham: ", self.listFunction[0])
#             print("Undeclare func tai stmt call")
#             raise Undeclared(Function(), ast.name.name)
        
#         # list of formal param
#         listLHS = funcDecl.param
#         # print("lhs: ", listLHS)
#         # list of applied param
#         listRHS = ast.args
#         # print("rhs: ", listRHS)
 
#         if len(listRHS) != len(listLHS):
#             print("Raise here")

#             raise TypeMismatchInStatement(ast)
#         for i in range(len(listLHS)):
#             LHS = self.visit(listLHS[i], param)
#             RHS = self.visit(listRHS[i], param)

#             # Vế phải trả về một VarZcode -> dynamic -> cần infer nó
#             if isinstance(RHS, VarZcode):
#                 for env in param:
#                     if listRHS[i].name in env.keys(): 
#                         env[listRHS[i].name] = LHS
#                         break
#             elif not self.compareType(LHS, RHS):
#                 print("Mistmatch here")
#                 raise TypeMismatchInStatement(ast)
#             # if type(RHS) is Zcode:
#             #     for env in param:
#             #         if ast.name.name in env.keys(): 
#             #             # Chấm được name vì nếu Vế phải trả về một VarZcode chỉ có thể là một biến (dynamic)
#             #             env[listRHS[i].name] = LHS
#             #             break
#             #     # RHS.typ = LHS
#             # elif not self.compareType(LHS, RHS):
#             #     print("Mistmatch here")
#             #     raise TypeMismatchInStatement(ast)
            
#         if funcDecl.typ is None:
#             return funcDecl
#         if not self.compareType(funcDecl.typ, VoidType()):
#             raise TypeMismatchInStatement(ast)
#         return funcDecl.typ
    

#     def visitIf(self, ast, param):
#         # Validate If 
#         LHS = BoolType()
#         RHS = self.visit(ast.expr, param)
#         print("RHS: ", ast.expr)
#         if isinstance(RHS, VarZcode):
#             # for env in param:
#             #     if ast.expr.name in env.keys(): 
#             #         env[ast.expr.name] = LHS
#             #         break
#             RHS = Infer.inferVar(param, ast.expr.name, LHS)
#         elif isinstance(RHS, FuncZcode):
#             RHS = Infer.inferFunc(self.listFunction, ast.expr.name, LHS)
#         if not self.compareType(LHS, RHS):
#             print("Mistmatch o day 3")
#             raise TypeMismatchInStatement(ast)

#         then_part = self.visit(ast.thenStmt, [{}] + param)
   
#         for Tuple in ast.elifStmt:
#             elif_env = [{}] + param
#             RHS = self.visit(Tuple[0], elif_env)
#             if isinstance(RHS, VarZcode):
#                 for env in param:
#                     if ast.expr.name in env.keys(): 
#                         env[ast.expr.name] = LHS
#                         break
#             elif not self.compareType(LHS, RHS):
#                 print("Mistmatch o day")
#                 raise TypeMismatchInStatement(ast)
#             # if not self.compareType(LHS, RHS):
#             #     raise TypeMismatchInStatement(ast)
#             elif_stmt = self.visit(Tuple[1], elif_env)
                    
#         if ast.elseStmt is not None:
#             else_part = self.visit(ast.elseStmt, [{}] + param)

     
#     def visitFor(self, ast, param):
#         """
#             TODO giống phần kiểm tra TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
#             ^ ast.name có LHS = NumberType(), RHS = .....
#             ^ ast.condExpr có LHS = BoolType(), RHS = .....
#             ^ ast.updExpr có LHS = NumberType(), RHS = .....
#         """        
#         # Validate the iterable variable 
#         LHS = NumberType()
#         RHS = self.visit(ast.name, param)
#         # print("RHS: ", ast.name)
#         if isinstance(RHS, VarZcode):
#             for env in param:
#                 if ast.name.name in env.keys(): 
#                     env[ast.name.name] = LHS
#                     break
#         elif not self.compareType(LHS, RHS):
#             print("Mistmatch o day")
#             raise TypeMismatchInStatement(ast)

#         # Cond expr
#         LHS = BoolType()
#         RHS = self.visit(ast.condExpr, param)
#         if isinstance(RHS, VarZcode):
#             for env in param:
#                 if ast.condExpr.name in env.keys(): 
#                     env[ast.condExpr.name] = LHS
#                     break
#         elif not self.compareType(LHS, RHS):
#             print("Mistmatch o day 1")
#             raise TypeMismatchInStatement(ast)
        
#         # Upd expr
#         LHS = NumberType()
#         RHS = self.visit(ast.updExpr, param)
#         # print("RHS: ", ast.name)
#         if isinstance(RHS, VarZcode):
#             for env in param:
#                 if ast.updExpr.name in env.keys(): 
#                     env[ast.updExpr.name] = LHS
#                     break
#         elif not self.compareType(LHS, RHS):
#             print("Mistmatch o day 2")
#             raise TypeMismatchInStatement(ast)
        
        
#         self.BlockFor += 1 #! vào trong vòng for nào anh em
#         self.visit(ast.body, [{}] + param) #! tăng tầm vực mới
#         self.BlockFor -= 1 #! cút khỏi vòng for nào anh em
    

#     def visitReturn(self, ast, param):
#         if ast.expr is None:
#             self.function.typ = VoidType()
#             self.Return = False
#         else:
#             self.Return = True
#             LHS = self.function.typ
#             RHS = self.visit(ast.expr, param)
#             print("LHS: ", LHS)
#             print("RHS: ", RHS)
#             if isinstance(RHS, Type) and LHS is None:
#                 print("CC")
#                 self.function.typ = RHS
#             elif isinstance(RHS, Zcode) and LHS is not None:
#                 RHS = LHS
#             elif isinstance(RHS, Zcode) and LHS is None:
#                 raise TypeCannotBeInferred(ast)
#             elif not self.compareType(LHS, RHS):
#                 raise TypeMismatchInStatement(ast)


#     def visitAssign(self, ast, param):
#         LHS = self.visit(ast.lhs, param)
#         RHS = self.visit(ast.rhs, param)
#         print("lhs: ", LHS)
#         print("rhs: ", RHS)
#         if isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
#             raise TypeCannotBeInferred(ast)
#         elif type(LHS) is VarZcode:
#             for env in param:
#                 if ast.lhs.name in env.keys(): 
#                     env[ast.lhs.name] = RHS
#                     break
#         elif type(RHS) is VarZcode:
#             for env in param:
#                 if ast.rhs.name in env.keys(): 
#                     env[ast.rhs.name] = LHS
#                     break
#         elif not self.compareType(LHS, RHS):
#             raise TypeMismatchInStatement(ast)

#     def visitBinaryOp(self, ast, param):      
#         left_type = self.visit(ast.left, param)
#         right_type = self.visit(ast.right, param)

#         if ast.op in ['+', '-', '*', '/', '%']:
#             if isinstance(left_type, Zcode):
#                 left_type = Infer.inferVar(param, ast.left.name, NumberType())
#             if isinstance(right_type, Zcode): 
#                 right_type = Infer.inferVar(param, ast.right.name, NumberType())
#             if type(left_type) is NumberType and type(right_type) is NumberType:
#                 return NumberType()
#             raise TypeMismatchInExpression(ast)

#         elif ast.op in ['and', 'or']:
#             if isinstance(left_type, Zcode):
#                 left_type = Infer.inferVar(param, ast.left.name, BoolType())
#             if isinstance(right_type, Zcode):
#                 right_type = Infer.inferVar(param, ast.right.name, BoolType())
#             if type(left_type) is BoolType and type(right_type) is BoolType:
#                 return BoolType()
#             raise TypeMismatchInExpression(ast)
        
#         elif ast.op == '...':
#             if isinstance(left_type, Zcode):
#                 left_type = Infer.inferVar(param, ast.left.name, StringType())
#             if isinstance(right_type, Zcode):
#                 right_type = Infer.inferVar(param, ast.right.name, StringType())
#             if type(left_type) is StringType and type(right_type) is StringType:
#                 return StringType()
#             raise TypeMismatchInExpression(ast)

#         elif ast.op in ['=', '!=', '<', '>', '>=', '<=']:
#             if isinstance(left_type, Zcode):
#                 left_type = Infer.inferVar(param, ast.left.name, NumberType())
#             if isinstance(right_type, Zcode): 
#                 right_type = Infer.inferVar(param, ast.right.name, NumberType())
#             if type(left_type) is NumberType and type(right_type) is NumberType:
#                 return BoolType()
#             raise TypeMismatchInExpression(ast)
        
#         elif ast.op == '==':
#             if isinstance(left_type, Zcode):
#                 left_type = Infer.inferVar(param, ast.left.name, StringType())
#             if isinstance(right_type, Zcode):
#                 right_type = Infer.inferVar(param, ast.right.name, StringType())
#             if type(left_type) is StringType and type(right_type) is StringType:
#                 return BoolType()
#             raise TypeMismatchInExpression(ast)
        

#     def visitUnaryOp(self, ast, param):
#         this_type = self.visit(ast.operand, param)

#         if ast.op in ['+', '-']:
#             if isinstance(this_type, Zcode):
#                 this_type = Infer.inferVar(param, ast.operand.name, NumberType())
#             if type(this_type) is NumberType:
#                 return NumberType()
#             raise TypeMismatchInExpression(ast)

#         elif ast.op in ['not']:
#             if isinstance(this_type, Zcode):
#                 this_type = Infer.inferVar(param, ast.operand.name, BoolType())
#             if type(this_type) is BoolType():
#                 return BoolType()
#             raise TypeMismatchInExpression(ast)


#     def visitArrayCell(self, ast, param):
#         """
#             TODO kiểm tra TypeMismatchInExpression
#             ^ Phần type ast.arr phải là array type ->  TypeMismatchInExpression -> không thể suy diễn kiểu biết arraytype phần tham số đâu :((, nên hỏi thầy đi nha 
#         """ 
#         arrType = self.visit(ast.arr, param)
#         if type(arrType) is not ArrayType:
#             raise TypeMismatchInExpression(ast)
        
#         """
#             TODO kiểm tra TypeMismatchInExpression
#             ^ Phần ast.idx với LHS = NumberType(), RHS = .... từng phần tử trong ast.idx
#         """         
#         LHS = NumberType()
#         for i in range(len(ast.idx)):
#             RHS = self.visit(ast.idx[i], param)
#             if isinstance(RHS, Zcode):
#                 RHS = Infer.inferVar(param, ast.idx[i].name, NumberType())
#             if not self.compareType(LHS, RHS):
#                 raise TypeMismatchInExpression(ast)
        
#         left = self.visit(ast.arr, param)
#         if len(left.size) < len(ast.idx):
#             raise TypeMismatchInExpression(ast)
#         elif len(left.size) == len(ast.idx):
#             return type(left.eleType)
#         else:
#             new_size = left.size[len(ast.idx) : ]
#             return ArrayType(new_size ,left.eleType)
#         """
#             TODO kiểm tra TypeMismatchInExpression kiểm tra len(left.size) và len(ast.idx) 
#             ^ left là sau khi visit ast.arr: Expr 
#             ^ len(left.size) < len(ast.idx) -> trả về lỗi TypeMismatchInExpression ví dụ
#             number a[1,2]
#             var c <- a[1,2,3]
#             ^ len(left.size) = len(ast.idx) -> trả về type eleType không phải là arraytype
#             number a[1,2]
#             var c <- a[1,2] -> c : numbertype
#             ^ len(left.size) > len(ast.idx) -> trả về arraytype cắt đi đoạn ban đầu
#             number a[1,2,3]
#             var c <- a[1] -> c : number c[2,3]                   
#         """ 

#     """phần này sẽ là cố định do ngắn quá :(( """
#     def visitArrayLiteral(self, ast, param):
#         #! code chỉ mang tính tham khảo, do BTL này không yêu cầu lỗi khác nhau ArrayLiteral nên thầy ko cho TypeCannotBeInferred
#         for item in ast.value: self.visit(item, param)
#         typ = self.visit(ast.value[0], param)
        
#         #! đệ quy
#         if type(typ) in [StringType, BoolType, NumberType]:
#             return ArrayType([len(ast.value)], typ)
#         return ArrayType([len(ast.value)] + typ.size, typ.eleType)
    
#     def visitBlock(self, ast, param):
#         # print("Param before block: ", param)
#         for item in ast.stmt:
#             #! trường hợp gặp block
#             if type(item) is Block:
#                 env = [{}] + param
#                 self.visit(item, env)
#             else: 
#                 self.visit(item, param)
#         return param
            
#     def visitContinue(self, ast, param):
#         #! kiểm tra đang ở vòng for hay không
#         if self.BlockFor == 0: raise MustInLoop(ast)

#     def visitBreak(self, ast, param):
#         #! kiểm tra đang ở vòng for hay không
#         if self.BlockFor == 0: raise MustInLoop(ast)   
#     def visitNumberType(self, ast, param): return ast
#     def visitBoolType(self, ast, param): return ast
#     def visitStringType(self, ast, param): return ast
#     def visitArrayType(self, ast, param): return ast
#     def visitNumberLiteral(self, ast, param): return NumberType()
#     def visitBooleanLiteral(self, ast, param): return BoolType()
#     def visitStringLiteral(self, ast, param): return StringType()
