// Generated from mtl.g4 by ANTLR 4.7.1

'''
 Copyright (C) 2015-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
'''

import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link mtlParser}.
 */
public interface mtlListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by the {@code booleanPred}
	 * labeled alternative in {@link mtlParser#mtlProperty}.
	 * @param ctx the parse tree
	 */
	void enterBooleanPred(mtlParser.BooleanPredContext ctx);
	/**
	 * Exit a parse tree produced by the {@code booleanPred}
	 * labeled alternative in {@link mtlParser#mtlProperty}.
	 * @param ctx the parse tree
	 */
	void exitBooleanPred(mtlParser.BooleanPredContext ctx);
	/**
	 * Enter a parse tree produced by the {@code formula}
	 * labeled alternative in {@link mtlParser#mtlProperty}.
	 * @param ctx the parse tree
	 */
	void enterFormula(mtlParser.FormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code formula}
	 * labeled alternative in {@link mtlParser#mtlProperty}.
	 * @param ctx the parse tree
	 */
	void exitFormula(mtlParser.FormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parprop}
	 * labeled alternative in {@link mtlParser#mtlProperty}.
	 * @param ctx the parse tree
	 */
	void enterParprop(mtlParser.ParpropContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parprop}
	 * labeled alternative in {@link mtlParser#mtlProperty}.
	 * @param ctx the parse tree
	 */
	void exitParprop(mtlParser.ParpropContext ctx);
	/**
	 * Enter a parse tree produced by {@link mtlParser#booleanExpr}.
	 * @param ctx the parse tree
	 */
	void enterBooleanExpr(mtlParser.BooleanExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link mtlParser#booleanExpr}.
	 * @param ctx the parse tree
	 */
	void exitBooleanExpr(mtlParser.BooleanExprContext ctx);
}