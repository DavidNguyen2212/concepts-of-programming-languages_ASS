# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_list.
    def visitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vars_decl.
    def visitVars_decl(self, ctx:ZCodeParser.Vars_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#norm_decl.
    def visitNorm_decl(self, ctx:ZCodeParser.Norm_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_decl.
    def visitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dynamic_decl.
    def visitDynamic_decl(self, ctx:ZCodeParser.Dynamic_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funs_decl.
    def visitFuns_decl(self, ctx:ZCodeParser.Funs_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#formal_params.
    def visitFormal_params(self, ctx:ZCodeParser.Formal_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#formal_pms_prm.
    def visitFormal_pms_prm(self, ctx:ZCodeParser.Formal_pms_prmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#formal_pm.
    def visitFormal_pm(self, ctx:ZCodeParser.Formal_pmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_type.
    def visitArray_type(self, ctx:ZCodeParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dim_list.
    def visitDim_list(self, ctx:ZCodeParser.Dim_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_ele.
    def visitArray_ele(self, ctx:ZCodeParser.Array_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtlist.
    def visitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtprime.
    def visitStmtprime(self, ctx:ZCodeParser.StmtprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_stmt.
    def visitAssign_stmt(self, ctx:ZCodeParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_ops.
    def visitIndex_ops(self, ctx:ZCodeParser.Index_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#fun_call.
    def visitFun_call(self, ctx:ZCodeParser.Fun_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp.
    def visitExp(self, ctx:ZCodeParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp1.
    def visitExp1(self, ctx:ZCodeParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp2.
    def visitExp2(self, ctx:ZCodeParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp3.
    def visitExp3(self, ctx:ZCodeParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp4.
    def visitExp4(self, ctx:ZCodeParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp5.
    def visitExp5(self, ctx:ZCodeParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp6.
    def visitExp6(self, ctx:ZCodeParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp7.
    def visitExp7(self, ctx:ZCodeParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp8.
    def visitExp8(self, ctx:ZCodeParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_val.
    def visitArray_val(self, ctx:ZCodeParser.Array_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#scalar_type.
    def visitScalar_type(self, ctx:ZCodeParser.Scalar_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_list.
    def visitArray_list(self, ctx:ZCodeParser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#builtins_call.
    def visitBuiltins_call(self, ctx:ZCodeParser.Builtins_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#readNumber.
    def visitReadNumber(self, ctx:ZCodeParser.ReadNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#writeNumber.
    def visitWriteNumber(self, ctx:ZCodeParser.WriteNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#readBool.
    def visitReadBool(self, ctx:ZCodeParser.ReadBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#writeBool.
    def visitWriteBool(self, ctx:ZCodeParser.WriteBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#readString.
    def visitReadString(self, ctx:ZCodeParser.ReadStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#writeString.
    def visitWriteString(self, ctx:ZCodeParser.WriteStringContext):
        return self.visitChildren(ctx)



del ZCodeParser