from antlr4 import InputStream, CommonTokenStream

import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.append('../')

from stl import Operation, RelOperation, STLFormula
from wstlLexer import wstlLexer
from wstlParser import wstlParser
from wstlVisitor import wstlVisitor

from wstl import WSTLAbstractSyntaxTreeExtractor
from stl import STLAbstractSyntaxTreeExtractor
from long_wstl2milp import long_wstl2milp
from short_wstl2milp import short_wstl2milp
from stl2milp import stl2milp
from gurobipy import *
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor
from stl import STLAbstractSyntaxTreeExtractor




def wstl_solve(wstl_formula, weights, type='short', varname='x', end_time = 15):
    # Get/create state variables
    lexer = wstlLexer(InputStream(wstl_formula))
    tokens = CommonTokenStream(lexer)
    parser = wstlParser(tokens)
    t = parser.wstlProperty()
    ast = WSTLAbstractSyntaxTreeExtractor(weights).visit(t)
    if type == 'long':
        wstl_milp = long_wstl2milp(ast)
    elif type == 'short':
        wstl_milp = short_wstl2milp(ast)
    else:
        raise NotImplementedError
    z_formula, rho_formula = wstl_milp.translate()
    x = [wstl_milp.variables[varname].get(time, wstl_milp.model.addVar(lb=-GRB.INFINITY,
                                                         ub=GRB.INFINITY))
         for time in range(end_time + 1)]
    wstl_milp.model.update()

    # Add dynamics constraints
    # for time in range(end_time): # example of state transition (system dynamics)
    #     m.addConstr(x[time+1] == x[time] + 0.1)

    for time in range(end_time + 1):  # example if state constraints (e.g., safety)
        wstl_milp.model.addConstr(x[time] >= 0)

    # Set objective
    wstl_milp.model.setObjective(rho_formula, GRB.MAXIMIZE)
    wstl_milp.model.update()
    if type == 'long':
        wstl_milp.model.write('long_milp.lp')
    else:
        wstl_milp.model.write('short_milp.lp')

    # Solve problem
    wstl_milp.model.optimize()

    if (wstl_milp.model.status == 2):
        y = np.array([x[i].X for i in range(end_time + 1)], dtype=np.float)
    else:
        print("cannot solve...")
        y = None

    return y

def stl_solve(stl_formula, varname='x', end_time=15):
    lexer = stlLexer(InputStream(stl_formula))
    tokens = CommonTokenStream(lexer)
    parser = stlParser(tokens)
    t = parser.stlProperty()
    print(t.toStringTree())
    ast = STLAbstractSyntaxTreeExtractor().visit(t)
    print("AST:", ast)

    stl_milp = stl2milp(ast, ranges={'x': [0, 10]}, robust=True)
    
    stl_milp.translate(satisfaction=True)
    x = [stl_milp.variables[varname].get(time, stl_milp.model.addVar(lb=-GRB.INFINITY,
                                                         ub=GRB.INFINITY))
                                        for time in range(end_time + 1)]
    stl_milp.model.update()
    # Set objective
    stl_milp.model.write('stl_milp.lp')
    # Solve problem
    stl_milp.model.optimize()
    y = [var.X for var in stl_milp.variables['x'].values()]
    print("y_stl:", y)
    return y

def visualize(end_time, x1, x2, x3):
    t = [i for i in range(0, end_time + 1)]
    print("t;", t)
    # Print solution
    fig, ax = plt.subplots()
    ax.grid()
    ax.plot(t, x1, '-r', label='long' )
    ax.plot(t, x2, '--b',  label='short')
    t_stl = np.arange(len(x3))
    ax.plot(t_stl, x3, '*g',  label='the OG')
    ax.legend()
    ax.set_title('x vs t')
    plt.show()

if __name__ == '__main__':
    # wstl_formula = "||^weight1 (F[5, 10]^weight2 (x <= 2), x>=5)"
    # wstl_formula = " ||^weight1 ((x >= 6), (x <= 5)^weight2)"
    # wstl_formula = "(x >= 7) ||^weight2 (x <= 2)^weight2 "
    # wstl_formula = "(x >= 7) ||^weight3 (x<=2)"
    # wstl_formula = "||^weight1 ( G[5, 10]^weight3 (x >= 7), G[5, 10]^weight2 (x<=3))"
    # stl_formula = " (G[5, 10] (x>=8) || G[5, 10] (x <= 3))"

    # Eventually
    # wstl_formula = "(F[0,2]^weight1  (x<=3))"
    wstl_formula = "&&^weight2 (F[0,2]^weight1  (x<=5), F[0,2]^weight2 (x<=2), F[0,4]^weight3 (x>=9))"

    #Always
    # wstl_formula = "(G[0,2]^weight1  (x>=3))"
    #wstl_formula = "&&^weight2 (G[0,2]^weight1  (x<=5), G[0,2]^weight2 (x<=2), G[0,4]^weight3 (x>=9))"

    # Disjunctions
    # wstl_formula = " ||^weight2 (||^weight1 ( (x<=3), (x>=6)) , (x>=2))"
    # wstl_formula = " ||^weight2 (||^weight1 ( (x<=4), (x>=8)) , (x<=3))"
    # wstl_formula = " ||^weight2 ((x>=3), ||^weight1 ( (x>=4), (x<=8)))"

    #conjunctions
    # wstl_formula = " &&^weight2 (&&^weight1 ( (x<=3), (x>=6)) , (x>=2))"
    # wstl_formula = " &&^weight2 (&&^weight1 ( (x<=4), (x>=8)) , (x<=3))"
    # wstl_formula = " &&^weight2 ((x>=3), &&^weight1 ( (x>=4), (x<=8)))"

    #predicates
    # wstl_formula = " (x<=8)"
    # wstl_formula = " (x>=8)"
    stl_formula = "((x <= 8) && (x >= 4)) && (x >= 3)"
    # Get AST from parse tree
    end_time = 15

    weights = {'weight1': lambda x: 10, 'weight2': lambda x: 1, 'weight3': lambda x: 5}

    # Translate WSTL to MILP and retrieve integer variable for the formula
    x1=wstl_solve(wstl_formula, weights, type='long')

    x2 = wstl_solve(wstl_formula, weights,type='short' )
    x3 = stl_solve(stl_formula)
    print("long", x1)
    print("short:", x2)
    print("stl:", x3)
    # visualize(end_time, x1,x2,x3)



# Parse the WSTL formula string
# lexer = wstlLexer(InputStream("<>[1, 3]^weight1 (y <= 2)"))
# lexer = wstlLexer(InputStream("[][1, 3]^weight1 (y <= 2)"))
# lexer = wstlLexer(InputStream("(y > 1) U[1, 3]^weight1 (y <= 2)"))
# lexer = wstlLexer(InputStream("(y > 1) &^weight1 (y <= 2)"))
# lexer = wstlLexer(InputStream("(y > 1) &^weight1 (y <= 2) &^weight2 (y > 3)"))
# lexer = wstlLexer(InputStream("(y > 1) |^weight1 (y <= 2) |^weight2 (y > 3)"))
# lexer = wstlLexer(InputStream("(y > 1) |^weight1 (y <= 2)"))
# lexer = wstlLexer(InputStream("(y > 1) &^weight1 (y <= 2) |^weight2 (y > 3)"))
# lexer = wstlLexer(InputStream("&&^weight1 (F[2, 5] (y <= 2), y > 3, x < 0.2)"))