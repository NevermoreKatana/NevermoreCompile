# Generated from compil/grammar/nevermorecompiler.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .nevermorecompilerParser import nevermorecompilerParser
else:
    from nevermorecompilerParser import nevermorecompilerParser

# This class defines a complete listener for a parse tree produced by nevermorecompilerParser.
class nevermorecompilerListener(ParseTreeListener):

    # Enter a parse tree produced by nevermorecompilerParser#prog.
    def enterProg(self, ctx:nevermorecompilerParser.ProgContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#prog.
    def exitProg(self, ctx:nevermorecompilerParser.ProgContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#stat.
    def enterStat(self, ctx:nevermorecompilerParser.StatContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#stat.
    def exitStat(self, ctx:nevermorecompilerParser.StatContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#ifStatement.
    def enterIfStatement(self, ctx:nevermorecompilerParser.IfStatementContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#ifStatement.
    def exitIfStatement(self, ctx:nevermorecompilerParser.IfStatementContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#ifElseStatement.
    def enterIfElseStatement(self, ctx:nevermorecompilerParser.IfElseStatementContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#ifElseStatement.
    def exitIfElseStatement(self, ctx:nevermorecompilerParser.IfElseStatementContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#ifBody.
    def enterIfBody(self, ctx:nevermorecompilerParser.IfBodyContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#ifBody.
    def exitIfBody(self, ctx:nevermorecompilerParser.IfBodyContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#elseBody.
    def enterElseBody(self, ctx:nevermorecompilerParser.ElseBodyContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#elseBody.
    def exitElseBody(self, ctx:nevermorecompilerParser.ElseBodyContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#forStatement.
    def enterForStatement(self, ctx:nevermorecompilerParser.ForStatementContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#forStatement.
    def exitForStatement(self, ctx:nevermorecompilerParser.ForStatementContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#forModify.
    def enterForModify(self, ctx:nevermorecompilerParser.ForModifyContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#forModify.
    def exitForModify(self, ctx:nevermorecompilerParser.ForModifyContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#forInit.
    def enterForInit(self, ctx:nevermorecompilerParser.ForInitContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#forInit.
    def exitForInit(self, ctx:nevermorecompilerParser.ForInitContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#forBody.
    def enterForBody(self, ctx:nevermorecompilerParser.ForBodyContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#forBody.
    def exitForBody(self, ctx:nevermorecompilerParser.ForBodyContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#whileStatement.
    def enterWhileStatement(self, ctx:nevermorecompilerParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#whileStatement.
    def exitWhileStatement(self, ctx:nevermorecompilerParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:nevermorecompilerParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:nevermorecompilerParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#whileBody.
    def enterWhileBody(self, ctx:nevermorecompilerParser.WhileBodyContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#whileBody.
    def exitWhileBody(self, ctx:nevermorecompilerParser.WhileBodyContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#expr.
    def enterExpr(self, ctx:nevermorecompilerParser.ExprContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#expr.
    def exitExpr(self, ctx:nevermorecompilerParser.ExprContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#printState.
    def enterPrintState(self, ctx:nevermorecompilerParser.PrintStateContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#printState.
    def exitPrintState(self, ctx:nevermorecompilerParser.PrintStateContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#printBody.
    def enterPrintBody(self, ctx:nevermorecompilerParser.PrintBodyContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#printBody.
    def exitPrintBody(self, ctx:nevermorecompilerParser.PrintBodyContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#globalStatement.
    def enterGlobalStatement(self, ctx:nevermorecompilerParser.GlobalStatementContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#globalStatement.
    def exitGlobalStatement(self, ctx:nevermorecompilerParser.GlobalStatementContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#globalBody.
    def enterGlobalBody(self, ctx:nevermorecompilerParser.GlobalBodyContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#globalBody.
    def exitGlobalBody(self, ctx:nevermorecompilerParser.GlobalBodyContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#equation.
    def enterEquation(self, ctx:nevermorecompilerParser.EquationContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#equation.
    def exitEquation(self, ctx:nevermorecompilerParser.EquationContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#relop.
    def enterRelop(self, ctx:nevermorecompilerParser.RelopContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#relop.
    def exitRelop(self, ctx:nevermorecompilerParser.RelopContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:nevermorecompilerParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:nevermorecompilerParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#type.
    def enterType(self, ctx:nevermorecompilerParser.TypeContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#type.
    def exitType(self, ctx:nevermorecompilerParser.TypeContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#functionStatement.
    def enterFunctionStatement(self, ctx:nevermorecompilerParser.FunctionStatementContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#functionStatement.
    def exitFunctionStatement(self, ctx:nevermorecompilerParser.FunctionStatementContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#ret.
    def enterRet(self, ctx:nevermorecompilerParser.RetContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#ret.
    def exitRet(self, ctx:nevermorecompilerParser.RetContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#functionArgs.
    def enterFunctionArgs(self, ctx:nevermorecompilerParser.FunctionArgsContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#functionArgs.
    def exitFunctionArgs(self, ctx:nevermorecompilerParser.FunctionArgsContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#functionBody.
    def enterFunctionBody(self, ctx:nevermorecompilerParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#functionBody.
    def exitFunctionBody(self, ctx:nevermorecompilerParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#functionName.
    def enterFunctionName(self, ctx:nevermorecompilerParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#functionName.
    def exitFunctionName(self, ctx:nevermorecompilerParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#funcType.
    def enterFuncType(self, ctx:nevermorecompilerParser.FuncTypeContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#funcType.
    def exitFuncType(self, ctx:nevermorecompilerParser.FuncTypeContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#functionExpr.
    def enterFunctionExpr(self, ctx:nevermorecompilerParser.FunctionExprContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#functionExpr.
    def exitFunctionExpr(self, ctx:nevermorecompilerParser.FunctionExprContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#functionParams.
    def enterFunctionParams(self, ctx:nevermorecompilerParser.FunctionParamsContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#functionParams.
    def exitFunctionParams(self, ctx:nevermorecompilerParser.FunctionParamsContext):
        pass


    # Enter a parse tree produced by nevermorecompilerParser#functionCall.
    def enterFunctionCall(self, ctx:nevermorecompilerParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by nevermorecompilerParser#functionCall.
    def exitFunctionCall(self, ctx:nevermorecompilerParser.FunctionCallContext):
        pass



del nevermorecompilerParser