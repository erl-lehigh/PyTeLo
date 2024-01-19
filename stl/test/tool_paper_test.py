from antlr4 import InputStream, CommonTokenStream
import time
import numpy as np
import matplotlib.pyplot as plt
import gurobipy as grb
import sys

sys.path.append('../')

from stl import Operation, RelOperation, STLFormula
from wstlLexer import wstlLexer
from wstlParser import wstlParser
from wstlVisitor import wstlVisitor

from wstl import WSTLAbstractSyntaxTreeExtractor
from stl import STLAbstractSyntaxTreeExtractor
from long_wstl2milp import long_wstl2milp
from wstl2milp import wstl2milp
from stl2milp import stl2milp
# from gurobipy import *
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor
from stl import STLAbstractSyntaxTreeExtractor


def stl_synthesis_control(formula, vars_ub, vars_lb):
    
    lexer = stlLexer(InputStream(formula))
    tokens = CommonTokenStream(lexer)
    parser = stlParser(tokens)
    t = parser.stlProperty()
    ast = STLAbstractSyntaxTreeExtractor().visit(t)

    stl_milp = stl2milp(ast, robust=True)
    
    time_bound = int(ast.bound()) + 1
    x = dict()
    y = dict()

    #creating the Gurobi Variables 
    for k in range(time_bound):
        name = "x_{}".format(k) 
        x[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                     ub=vars_ub, name=name)
        name = "y_{}".format(k)
        y[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                     ub=vars_ub, name=name)
        
    # use system variables in STL spec encoding
    stl_milp.variables['x'] = x
    stl_milp.variables['y'] = y
    
    #initial conditions
    stl_milp.model.addConstr(x[0] == 0)
    stl_milp.model.addConstr(y[0] == 0)
    # add the specification (STL) constraints
    stl_milp.translate(satisfaction=True)
    # Solve the problem with gurobi 
    stl_milp.model.optimize()
    x_vals = [var.x for var in stl_milp.variables['x'].values()]
    y_vals = [var.x for var in stl_milp.variables['y'].values()]
    return x_vals, y_vals

def wstl_synthesis_control(wstl_formula, weights, vars_ub, vars_lb, type='short'):
    lexer = wstlLexer(InputStream(wstl_formula))
    tokens = CommonTokenStream(lexer)
    parser = wstlParser(tokens)
    t = parser.wstlProperty()
    ast = WSTLAbstractSyntaxTreeExtractor(weights).visit(t)
    if type == 'long':
        wstl_milp = long_wstl2milp(ast)
    elif type == 'short':
        wstl_milp = wstl2milp(ast)
    else:
        raise NotImplementedError

    time_bound = int(ast.bound()) + 1
    # system variables and the time period 
    x = dict()
    y = dict()
    z = dict()
    u = dict()
    v = dict()
    w = dict()

    for k in range(time_bound):
        name = "x_{}".format(k) 
        x[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                      ub=vars_ub, name=name)
        name = "y_{}".format(k)
        y[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                      ub=vars_ub, name=name)


    # use system variables in STL spec encoding
    wstl_milp.variables['x'] = x
    wstl_milp.variables['y'] = y

    wstl_milp.model.addConstr(x[0] == 0)
    wstl_milp.model.addConstr(y[0] == 0)

    z_formula, rho_formula = wstl_milp.translate(satisfaction=True)
    wstl_milp.model.setObjective(rho_formula, grb.GRB.MAXIMIZE)
    wstl_milp.model.update()

    if type == 'long':
        wstl_milp.model.write('long_milp.lp')
    else:
        wstl_milp.model.write('short_milp.lp')

    # Solve problem
    wstl_milp.model.optimize()
    x_vals = [var.x for var in wstl_milp.variables['x'].values()]
    y_vals = [var.x for var in wstl_milp.variables['y'].values()]
    return x_vals, y_vals


def visualize(x, y):
    t = [i for i in range(len(y))]
    fig, ax = plt.subplots()
    ax.grid()
    plt.rcParams['font.size'] = '20'
    ax.plot(t, x, '-r', label='$s_1$', linewidth=3)
    ax.plot(t, y, '-b',  label='$s_2$', linewidth=3)   
    ax.legend(fontsize = 'xx-large')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel("Time",fontsize=25)
    plt.ylabel("$\| s_i \|$",fontsize=25) 
    plt.show()


if __name__ == '__main__':
    #Formulas
    stl_formula = '((G[1,5] (x>=7) || G[1,5] (y<=2)) && \
                    (F[5,10] (x<=3) || F[5,10] (y>=8)))'
    
    wstl_formula = '&&^weight1 ( ||^weight2 (G[1,5]^weight3 (x>=7), \
                    G[1,5]^weight3 (y<=2)), ||^weight2 (G[5,10]^weight4 (x<=3),\
                     G[5,10]^weight4 (y>=8)))'


    # NOTE: case where there is higher weight to avoiding the obstacle
    weights = {'weight1': lambda k: [.5, .5][k],  
               'weight2': lambda k: [.2, .8][k], 
               'weight3': lambda k: [.1, .1, .2, .3, .4, .5][k], 
               'weight4': lambda k: [.1, .1, .2, .3, .4, .5, .5, .4, .3, .2, .1,][k]}


    vars_ub = 10
    vars_lb = 0

    # Translate WSTL to MILP and retrieve integer variable for the formula
    
    stl_x, stl_y = stl_synthesis_control(stl_formula, vars_ub, vars_lb,)
    visualize(stl_x, stl_y)

    wstl_x, wstl_y = wstl_synthesis_control(wstl_formula, weights, vars_ub, vars_lb)
    visualize(wstl_x, wstl_y)
    
    

