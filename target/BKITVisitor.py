# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declare.
    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varList.
    def visitVarList(self, ctx:BKITParser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declare.
    def visitFunc_declare(self, ctx:BKITParser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramList.
    def visitParamList(self, ctx:BKITParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp0.
    def visitExp0(self, ctx:BKITParser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp7.
    def visitExp7(self, ctx:BKITParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp8.
    def visitExp8(self, ctx:BKITParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#rela_op.
    def visitRela_op(self, ctx:BKITParser.Rela_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logic_op.
    def visitLogic_op(self, ctx:BKITParser.Logic_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#add_op.
    def visitAdd_op(self, ctx:BKITParser.Add_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#mul_op.
    def visitMul_op(self, ctx:BKITParser.Mul_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#not_op.
    def visitNot_op(self, ctx:BKITParser.Not_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dec_op.
    def visitDec_op(self, ctx:BKITParser.Dec_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_op.
    def visitIndex_op(self, ctx:BKITParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#addexpr.
    def visitAddexpr(self, ctx:BKITParser.AddexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcexpr.
    def visitFuncexpr(self, ctx:BKITParser.FuncexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#openrands.
    def visitOpenrands(self, ctx:BKITParser.OpenrandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_call.
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elseIf_stmt.
    def visitElseIf_stmt(self, ctx:BKITParser.ElseIf_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#doWhile_stmt.
    def visitDoWhile_stmt(self, ctx:BKITParser.DoWhile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#argumentList.
    def visitArgumentList(self, ctx:BKITParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#argument.
    def visitArgument(self, ctx:BKITParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return self.visitChildren(ctx)



del BKITParser