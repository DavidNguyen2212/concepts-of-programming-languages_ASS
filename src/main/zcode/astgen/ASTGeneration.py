#from main.zcode.parser.ZCodeVisitor import ZCodeVisitor
#from main.zcode.parser.ZCodeParser import ZCodeParser
#from main.zcode.utils.AST import *
from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    # program			: (COMMENT NEWLINE | NEWLINE)* decl_list EOF;
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decl_list()))

    # decl_list 		: decl decl_list | decl;
    def visitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        return [self.visit(ctx.decl())] + self.visit(ctx.decl_list()) 

    # decl			: vars_decl | funs_decl;
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        if ctx.vars_decl():
            return self.visit(ctx.vars_decl())
        return self.visit(ctx.funs_decl())

    # ignore			: NEWLINE+;
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return None

    # vars_decl		: (norm_decl | var_decl | dynamic_decl) ignore; 
    def visitVars_decl(self, ctx:ZCodeParser.Vars_declContext):
        if ctx.norm_decl():
            return self.visit(ctx.norm_decl())
        elif ctx.var_decl():
            return self.visit(ctx.var_decl())
        else:
            return self.visit(ctx.dynamic_decl())

    # norm_decl 	: (scalar_type ID | scalar_type array_type) (ASSIGN exp)?;
    def visitNorm_decl(self, ctx:ZCodeParser.Norm_declContext):
        if ctx.ASSIGN():
            if ctx.ID():
                return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.scalar_type()), None, self.visit(ctx.exp()))
            else:
                array_type = self.visit(ctx.array_type())
                return VarDecl(array_type[0], ArrayType(array_type[1], self.visit(ctx.scalar_type())), None, self.visit(ctx.exp()))
        else:
            if ctx.ID():
                return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.scalar_type()))
            else:
                array_type = self.visit(ctx.array_type())
                return VarDecl(array_type[0], ArrayType(array_type[1], self.visit(ctx.scalar_type())))

    # var_decl		: VAR ID ASSIGN exp;
    def visitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        return VarDecl(Id(ctx.ID().getText()), None, "var", self.visit(ctx.exp()))

    # dynamic_decl	: DYNAMIC ID (ASSIGN exp)?;
    def visitDynamic_decl(self, ctx:ZCodeParser.Dynamic_declContext):
        if ctx.ASSIGN():
            return VarDecl(Id(ctx.ID().getText()), None, "dynamic", self.visit(ctx.exp()))
        return VarDecl(Id(ctx.ID().getText()), None, "dynamic", None)
    
    # funs_decl		: FUNC ID LP formal_params RP (ignore? block_stmt | ignore? return_stmt | ignore); 
    def visitFuns_decl(self, ctx:ZCodeParser.Funs_declContext):
        name = ctx.ID().getText()
        param = self.visit(ctx.formal_params())
        if ctx.block_stmt():
            return FuncDecl(Id(name), param, self.visit(ctx.block_stmt()))
        elif ctx.return_stmt():
            return FuncDecl(Id(name), param, self.visit(ctx.return_stmt()))
        else:
            return FuncDecl(Id(name), param)

    # formal_params 	: formal_pms_prm | ;
    def visitFormal_params(self, ctx:ZCodeParser.Formal_paramsContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.formal_pms_prm())

    # formal_pms_prm	: formal_pm COMMA formal_pms_prm | formal_pm;
    def visitFormal_pms_prm(self, ctx:ZCodeParser.Formal_pms_prmContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.formal_pm())]
        return [self.visit(ctx.formal_pm())] + self.visit(ctx.formal_pms_prm())

    # formal_pm		: scalar_type ID | scalar_type array_type;
    def visitFormal_pm(self, ctx:ZCodeParser.Formal_pmContext):
        if ctx.ID():
            return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.scalar_type()))
        array_type = self.visit(ctx.array_type())
        return VarDecl(array_type[0], ArrayType(array_type[1], self.visit(ctx.scalar_type())))
    
    # array_type 		: ID LS dim_list RS;
    def visitArray_type(self, ctx:ZCodeParser.Array_typeContext):
        return Id(ctx.ID().getText()), self.visit(ctx.dim_list())

    # dim_list 		: NUM_LIT COMMA dim_list | NUM_LIT;
    def visitDim_list(self, ctx:ZCodeParser.Dim_listContext):
        if not ctx.COMMA():
            return [float(ctx.NUM_LIT().getText())]
        return [float(ctx.NUM_LIT().getText())] + self.visit(ctx.dim_list())

    # array_ele		: (ID | fun_call) LS index_ops RS;
    def visitArray_ele(self, ctx:ZCodeParser.Array_eleContext):
        if ctx.ID():
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.index_ops()))
        return ArrayCell(self.visit(ctx.fun_call()), self.visit(ctx.index_ops()))
        
    # stmt			: block_stmt | if_stmt | for_stmt 
	#			| assign_stmt | continue_stmt | break_stmt
	#			| return_stmt | call_stmt | vars_decl;
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        if ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.call_stmt():
            return self.visit(ctx.call_stmt())
        else:
            return self.visit(ctx.vars_decl())

    # block_stmt 		: BEGIN ignore stmtlist END ignore;
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return Block(self.visit(ctx.stmtlist()))
    
    # stmtlist 		: stmtprime | ;
    def visitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.stmtprime())

    # stmtprime		: stmt stmtprime | stmt;
    def visitStmtprime(self, ctx:ZCodeParser.StmtprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.stmt())]
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmtprime())
    
    # Tách If thành 2 phần 
    # if_stmt : IF exp statement elif_list (ELSE statement)?;
    def visitIf_stmt(self, ctx: ZCodeParser.If_stmtContext):
        if not ctx.ELSE():
            return If(self.visit(ctx.exp()), self.visit(ctx.stmt(0)), self.visit(ctx.elif_list()), None)
        return If(self.visit(ctx.exp()), self.visit(ctx.stmt(0)), self.visit(ctx.elif_list()), self.visit(ctx.stmt(1)))

    # elif_list: ELIF expression ignore? statement elif_list | ;
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [(self.visit(ctx.exp()), self.visit(ctx.stmt()))] + self.visit(ctx.elif_list())

    # for_stmt		: FOR ID UNTIL exp BY exp ignore? stmt;
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), self.visit(ctx.stmt()))

    # assign_stmt 	: (ID | ID LS index_ops RS) ASSIGN exp ignore;
    def visitAssign_stmt(self, ctx:ZCodeParser.Assign_stmtContext):
        if ctx.getChildCount() == 4:
            return Assign(Id(ctx.ID().getText()), self.visit(ctx.exp()))
        lhs = ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.index_ops()))
        return Assign(lhs, self.visit(ctx.exp()))

    # index_ops		: exp | exp COMMA index_ops;
    def visitIndex_ops(self, ctx:ZCodeParser.Index_opsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.exp())]
        return [self.visit(ctx.exp())] + self.visit(ctx.index_ops())
    
    # continue_stmt 	: CONTINUE ignore;
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return Continue()
    
    # break_stmt 		: BREAK ignore;
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return Break()


    # return_stmt		: RETURN exp? ignore;
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        if not ctx.exp():
            return Return()
        return Return(self.visit(ctx.exp()))

    # call_stmt		: fun_call ignore;
    def visitCall_stmt(self, ctx:ZCodeParser.Call_stmtContext):
        fun_call_part = self.visit(ctx.fun_call())
        return CallStmt(fun_call_part.name, fun_call_part.args)

    # fun_call		: ID LP index_ops? RP;
    def visitFun_call(self, ctx:ZCodeParser.Fun_callContext):
        if ctx.getChildCount() == 4:
            return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.index_ops()))
        return CallExpr(Id(ctx.ID().getText()), [])
    
    # exp 		: exp1 CONCAT exp1 | exp1;
    def visitExp(self, ctx:ZCodeParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        left = self.visit(ctx.exp1(0))
        right = self.visit(ctx.exp1(1))
        return BinaryOp(ctx.CONCAT().getText(), left, right)


    # exp1		: exp2 (EQ_NUM | EQ_STR | DIFFER | LT | GT | LE | GE) exp2 | exp2;
    def visitExp1(self, ctx:ZCodeParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2(0))
        left = self.visit(ctx.exp2(0))
        right = self.visit(ctx.exp2(1))
        if ctx.EQ_NUM():
            return BinaryOp(ctx.EQ_NUM().getText(), left, right)
        elif ctx.EQ_STR():
            return BinaryOp(ctx.EQ_STR().getText(), left, right)
        elif ctx.DIFFER():
            return BinaryOp(ctx.DIFFER().getText(), left, right)
        elif ctx.LT():
            return BinaryOp(ctx.LT().getText(), left, right)
        elif ctx.GT():
            return BinaryOp(ctx.GT().getText(), left, right)
        elif ctx.LE():
            return BinaryOp(ctx.LE().getText(), left, right)
        return BinaryOp(ctx.GE().getText(), left, right)


    # exp2		: exp2 (AND | OR) exp3 | exp3;
    def visitExp2(self, ctx:ZCodeParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        left = self.visit(ctx.exp2())
        right = self.visit(ctx.exp3())
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), left, right)
        return BinaryOp(ctx.OR().getText(), left, right) 


    # exp3		: exp3 (PLUS | MINUS) exp4 | exp4;
    def visitExp3(self, ctx:ZCodeParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        left = self.visit(ctx.exp3())
        right = self.visit(ctx.exp4())
        if ctx.PLUS():
            return BinaryOp(ctx.PLUS().getText(), left, right)
        return BinaryOp(ctx.MINUS().getText(), left, right)


    # exp4		: exp4 (MUL | DIV | MOD) exp5 | exp5;
    def visitExp4(self, ctx:ZCodeParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        left = self.visit(ctx.exp4())
        right = self.visit(ctx.exp5())
        if ctx.MUL():
            return BinaryOp(ctx.MUL().getText(), left, right)
        elif ctx.DIV():
            return BinaryOp(ctx.DIV().getText(), left, right)
        return BinaryOp(ctx.MOD().getText(), left, right)

    # exp5		: NOT exp5 | exp6;
    def visitExp5(self, ctx:ZCodeParser.Exp5Context):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.exp5()))
        return self.visit(ctx.exp6())

    # exp6		: MINUS exp6 | exp7;
    def visitExp6(self, ctx:ZCodeParser.Exp6Context):
        if ctx.MINUS():
            return UnaryOp(ctx.MINUS().getText(), self.visit(ctx.exp6()))
        return self.visit(ctx.exp7()) 

    # exp7		: (ID | ID LP index_ops? RP) LS index_ops RS | exp8;
    def visitExp7(self, ctx:ZCodeParser.Exp7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp8())
        elif ctx.getChildCount() == 4:
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.index_ops(0)))
        elif len(ctx.index_ops()) == 2:
            return ArrayCell(CallExpr(Id(ctx.ID().getText()), self.visit(ctx.index_ops(0))), self.visit(ctx.index_ops(1)))
        return ArrayCell(CallExpr(Id(ctx.ID().getText()), []), self.visit(ctx.index_ops(0)))

    # exp8		: array_val | LP exp RP | ID | fun_call;
    def visitExp8(self, ctx:ZCodeParser.Exp8Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.array_val():
            return self.visit(ctx.array_val())
        else:
            return self.visit(ctx.fun_call())

    # array_val 	: array_list | NUM_LIT | TRUE | FALSE | STR_LIT;
    def visitArray_val(self, ctx: ZCodeParser.Array_valContext):
        if ctx.NUM_LIT():
            return NumberLiteral(float(ctx.NUM_LIT().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.STR_LIT():
            return StringLiteral(ctx.STR_LIT().getText())
        return self.visit(ctx.array_list())

    # array_list	: LS index_ops RS;
    def visitArray_list(self, ctx: ZCodeParser.Array_listContext):
        return ArrayLiteral(self.visit(ctx.index_ops()))

    # scalar_type	: NUMBER | BOOL | STRING;
    def visitScalar_type(self, ctx: ZCodeParser.Scalar_typeContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        else:
            return StringType()
    