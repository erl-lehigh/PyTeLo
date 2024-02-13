// Generated from mtl.g4 by ANTLR 4.7.1

'''
 Copyright (C) 2015-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
'''

import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link mtlParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface mtlVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by the {@code booleanPred}
	 * labeled alternative in {@link mtlParser#mtlProperty}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBooleanPred(mtlParser.BooleanPredContext ctx);
	/**
	 * Visit a parse tree produced by the {@code formula}
	 * labeled alternative in {@link mtlParser#mtlProperty}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFormula(mtlParser.FormulaContext ctx);
	/**
	 * Visit a parse tree produced by the {@code parprop}
	 * labeled alternative in {@link mtlParser#mtlProperty}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParprop(mtlParser.ParpropContext ctx);
	/**
	 * Visit a parse tree produced by {@link mtlParser#booleanExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBooleanExpr(mtlParser.BooleanExprContext ctx);
}