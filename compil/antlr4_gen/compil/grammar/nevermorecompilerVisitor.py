# Generated from compil/grammar/nevermorecompiler.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .nevermorecompilerParser import nevermorecompilerParser
else:
    from nevermorecompilerParser import nevermorecompilerParser

# This class defines a complete generic visitor for a parse tree produced by nevermorecompilerParser.

class nevermorecompilerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by nevermorecompilerParser#prog.
    def visitProg(self, ctx:nevermorecompilerParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#stat.
    def visitStat(self, ctx:nevermorecompilerParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#ifStatement.
    def visitIfStatement(self, ctx:nevermorecompilerParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#ifElseStatement.
    def visitIfElseStatement(self, ctx:nevermorecompilerParser.IfElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#ifBody.
    def visitIfBody(self, ctx:nevermorecompilerParser.IfBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#elseBody.
    def visitElseBody(self, ctx:nevermorecompilerParser.ElseBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#forStatement.
    def visitForStatement(self, ctx:nevermorecompilerParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#forModify.
    def visitForModify(self, ctx:nevermorecompilerParser.ForModifyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#forInit.
    def visitForInit(self, ctx:nevermorecompilerParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#forBody.
    def visitForBody(self, ctx:nevermorecompilerParser.ForBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#whileStatement.
    def visitWhileStatement(self, ctx:nevermorecompilerParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:nevermorecompilerParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#whileBody.
    def visitWhileBody(self, ctx:nevermorecompilerParser.WhileBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#expr.
    def visitExpr(self, ctx:nevermorecompilerParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#printState.
    def visitPrintState(self, ctx:nevermorecompilerParser.PrintStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#printBody.
    def visitPrintBody(self, ctx:nevermorecompilerParser.PrintBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#globalStatement.
    def visitGlobalStatement(self, ctx:nevermorecompilerParser.GlobalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#globalBody.
    def visitGlobalBody(self, ctx:nevermorecompilerParser.GlobalBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#equation.
    def visitEquation(self, ctx:nevermorecompilerParser.EquationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#relop.
    def visitRelop(self, ctx:nevermorecompilerParser.RelopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:nevermorecompilerParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#type.
    def visitType(self, ctx:nevermorecompilerParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#functionStatement.
    def visitFunctionStatement(self, ctx:nevermorecompilerParser.FunctionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#ret.
    def visitRet(self, ctx:nevermorecompilerParser.RetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#functionArgs.
    def visitFunctionArgs(self, ctx:nevermorecompilerParser.FunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#functionBody.
    def visitFunctionBody(self, ctx:nevermorecompilerParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#functionName.
    def visitFunctionName(self, ctx:nevermorecompilerParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#funcType.
    def visitFuncType(self, ctx:nevermorecompilerParser.FuncTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#functionExpr.
    def visitFunctionExpr(self, ctx:nevermorecompilerParser.FunctionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#functionParams.
    def visitFunctionParams(self, ctx:nevermorecompilerParser.FunctionParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nevermorecompilerParser#functionCall.
    def visitFunctionCall(self, ctx:nevermorecompilerParser.FunctionCallContext):
        return self.visitChildren(ctx)



del nevermorecompilerParser