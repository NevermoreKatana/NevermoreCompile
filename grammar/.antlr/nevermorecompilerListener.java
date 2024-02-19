// Generated from /home/katana/NevermoreCompile/grammar/nevermorecompiler.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link nevermorecompilerParser}.
 */
public interface nevermorecompilerListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(nevermorecompilerParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(nevermorecompilerParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(nevermorecompilerParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(nevermorecompilerParser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(nevermorecompilerParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(nevermorecompilerParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#ifElseStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfElseStatement(nevermorecompilerParser.IfElseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#ifElseStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfElseStatement(nevermorecompilerParser.IfElseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#ifBody}.
	 * @param ctx the parse tree
	 */
	void enterIfBody(nevermorecompilerParser.IfBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#ifBody}.
	 * @param ctx the parse tree
	 */
	void exitIfBody(nevermorecompilerParser.IfBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#elseBody}.
	 * @param ctx the parse tree
	 */
	void enterElseBody(nevermorecompilerParser.ElseBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#elseBody}.
	 * @param ctx the parse tree
	 */
	void exitElseBody(nevermorecompilerParser.ElseBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void enterForStatement(nevermorecompilerParser.ForStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void exitForStatement(nevermorecompilerParser.ForStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#forModify}.
	 * @param ctx the parse tree
	 */
	void enterForModify(nevermorecompilerParser.ForModifyContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#forModify}.
	 * @param ctx the parse tree
	 */
	void exitForModify(nevermorecompilerParser.ForModifyContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#forInit}.
	 * @param ctx the parse tree
	 */
	void enterForInit(nevermorecompilerParser.ForInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#forInit}.
	 * @param ctx the parse tree
	 */
	void exitForInit(nevermorecompilerParser.ForInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#forBody}.
	 * @param ctx the parse tree
	 */
	void enterForBody(nevermorecompilerParser.ForBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#forBody}.
	 * @param ctx the parse tree
	 */
	void exitForBody(nevermorecompilerParser.ForBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(nevermorecompilerParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(nevermorecompilerParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#doWhileStatement}.
	 * @param ctx the parse tree
	 */
	void enterDoWhileStatement(nevermorecompilerParser.DoWhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#doWhileStatement}.
	 * @param ctx the parse tree
	 */
	void exitDoWhileStatement(nevermorecompilerParser.DoWhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#whileBody}.
	 * @param ctx the parse tree
	 */
	void enterWhileBody(nevermorecompilerParser.WhileBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#whileBody}.
	 * @param ctx the parse tree
	 */
	void exitWhileBody(nevermorecompilerParser.WhileBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(nevermorecompilerParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(nevermorecompilerParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#printState}.
	 * @param ctx the parse tree
	 */
	void enterPrintState(nevermorecompilerParser.PrintStateContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#printState}.
	 * @param ctx the parse tree
	 */
	void exitPrintState(nevermorecompilerParser.PrintStateContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#printBody}.
	 * @param ctx the parse tree
	 */
	void enterPrintBody(nevermorecompilerParser.PrintBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#printBody}.
	 * @param ctx the parse tree
	 */
	void exitPrintBody(nevermorecompilerParser.PrintBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#globalStatement}.
	 * @param ctx the parse tree
	 */
	void enterGlobalStatement(nevermorecompilerParser.GlobalStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#globalStatement}.
	 * @param ctx the parse tree
	 */
	void exitGlobalStatement(nevermorecompilerParser.GlobalStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#globalBody}.
	 * @param ctx the parse tree
	 */
	void enterGlobalBody(nevermorecompilerParser.GlobalBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#globalBody}.
	 * @param ctx the parse tree
	 */
	void exitGlobalBody(nevermorecompilerParser.GlobalBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#equation}.
	 * @param ctx the parse tree
	 */
	void enterEquation(nevermorecompilerParser.EquationContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#equation}.
	 * @param ctx the parse tree
	 */
	void exitEquation(nevermorecompilerParser.EquationContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#relop}.
	 * @param ctx the parse tree
	 */
	void enterRelop(nevermorecompilerParser.RelopContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#relop}.
	 * @param ctx the parse tree
	 */
	void exitRelop(nevermorecompilerParser.RelopContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentStatement(nevermorecompilerParser.AssignmentStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentStatement(nevermorecompilerParser.AssignmentStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link nevermorecompilerParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(nevermorecompilerParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link nevermorecompilerParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(nevermorecompilerParser.TypeContext ctx);
}