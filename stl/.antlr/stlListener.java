// Generated from /home/gustavo/lehigh/erl/PyTeLo/stl/stl.g4 by ANTLR 4.13.1

'''
 Copyright (C) 2015-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
'''

import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link stlParser}.
 */
public interface stlListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by the {@code booleanPred}
	 * labeled alternative in {@link stlParser#stlProperty}.
	 * @param ctx the parse tree
	 */
	void enterBooleanPred(stlParser.BooleanPredContext ctx);
	/**
	 * Exit a parse tree produced by the {@code booleanPred}
	 * labeled alternative in {@link stlParser#stlProperty}.
	 * @param ctx the parse tree
	 */
	void exitBooleanPred(stlParser.BooleanPredContext ctx);
	/**
	 * Enter a parse tree produced by the {@code formula}
	 * labeled alternative in {@link stlParser#stlProperty}.
	 * @param ctx the parse tree
	 */
	void enterFormula(stlParser.FormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code formula}
	 * labeled alternative in {@link stlParser#stlProperty}.
	 * @param ctx the parse tree
	 */
	void exitFormula(stlParser.FormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parprop}
	 * labeled alternative in {@link stlParser#stlProperty}.
	 * @param ctx the parse tree
	 */
	void enterParprop(stlParser.ParpropContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parprop}
	 * labeled alternative in {@link stlParser#stlProperty}.
	 * @param ctx the parse tree
	 */
	void exitParprop(stlParser.ParpropContext ctx);
	/**
	 * Enter a parse tree produced by {@link stlParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(stlParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link stlParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(stlParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link stlParser#booleanExpr}.
	 * @param ctx the parse tree
	 */
	void enterBooleanExpr(stlParser.BooleanExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link stlParser#booleanExpr}.
	 * @param ctx the parse tree
	 */
	void exitBooleanExpr(stlParser.BooleanExprContext ctx);
}