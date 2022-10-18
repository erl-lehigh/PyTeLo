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
from short_wstl2milp import short_wstl2milp
from stl2milp import stl2milp
# from gurobipy import *
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor
from stl import STLAbstractSyntaxTreeExtractor
from environment import stl_zone, wstl_zone, environment_trajec

def stl_synthesis_control(formula, A, B, vars_ub, vars_lb, control_ub, 
                          control_lb):
    
    lexer = stlLexer(InputStream(formula))
    tokens = CommonTokenStream(lexer)
    parser = stlParser(tokens)
    t = parser.stlProperty()
    ast = STLAbstractSyntaxTreeExtractor().visit(t)

    stl_milp = stl2milp(ast, robust=True)
    
    time_bound = int(ast.bound()) + 1
    x = dict()
    y = dict()
    z = dict()
    u = dict()
    v = dict()
    w = dict()

    #creating the Gurobi Variables 
    for k in range(time_bound):
        name = "x_{}".format(k) 
        x[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                     ub=vars_ub, name=name)
        name = "y_{}".format(k)
        y[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                     ub=vars_ub, name=name)
        name = "z_{}".format(k) 
        z[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                     ub=vars_ub, name=name)
        name = "u_{}".format(k)
        u[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=control_lb, 
                                     ub=control_ub, name=name)
        name = "v_{}".format(k)
        v[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=control_lb, 
                                     ub=control_ub, name=name)
        name = "w_{}".format(k)
        w[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=control_lb, 
                                     ub=control_ub, name=name)
    # use system variables in STL spec encoding
    stl_milp.variables['x'] = x
    stl_milp.variables['y'] = y
    stl_milp.variables['z'] = z
    stl_milp.variables['u'] = u
    stl_milp.variables['v'] = v
    stl_milp.variables['w'] = w

    # system constraints x[k+1] = A X[k]+ B U[k]
    for k in range(time_bound-1):
        stl_milp.model.addConstr(x[k+1] == A[0][0] * x[k] + A[0][1] * y[k] +
                                           A[0][2] * z[k] + B[0][0] * u[k] + 
                                           B[0][1] * v[k] + B[0][2] * w[k] )

        stl_milp.model.addConstr(y[k+1] == A[1][0] * x[k] + A[1][1] * y[k] + 
                                           A[1][2] * z[k] + B[1][0] * u[k] + 
                                           B[1][1] * v[k] + B[1][2] * w[k] )

        stl_milp.model.addConstr(z[k+1] == A[2][0] * x[k] + A[2][1] * y[k] + 
                                           A[2][2] * z[k] + B[2][0] * u[k] + 
                                           B[2][1] * v[k] + B[2][2] * w[k] )
    
    #initial conditions
    stl_milp.model.addConstr(x[0] == -9)
    stl_milp.model.addConstr(y[0] == -9)
    stl_milp.model.addConstr(z[0] == 0)
    stl_milp.model.addConstr(u[0] == 0)
    stl_milp.model.addConstr(v[0] == 0)
    stl_milp.model.addConstr(w[0] == 0)
    # add the specification (STL) constraints
    stl_milp.translate(satisfaction=True)
    # Solve the problem with gurobi 
    stl_milp.model.optimize()
    return stl_milp

def wstl_synthesis_control(wstl_formula, weights, A, B, vars_ub, vars_lb, 
                           control_ub, control_lb, type='short'):
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
        name = "z_{}".format(k) 
        z[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                      ub=vars_ub, name=name)
        name = "u_{}".format(k)
        u[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=control_lb, 
                                      ub=control_ub, name=name)
        name = "v_{}".format(k)
        v[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=control_lb, 
                                      ub=control_ub, name=name)
        name = "w_{}".format(k)
        w[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=control_lb, 
                                      ub=control_ub, name=name)

    # use system variables in STL spec encoding
    wstl_milp.variables['x'] = x
    wstl_milp.variables['y'] = y
    wstl_milp.variables['z'] = z
    wstl_milp.variables['u'] = u
    wstl_milp.variables['v'] = v
    wstl_milp.variables['w'] = w


    # system constraints
    for k in range(time_bound-1):
        wstl_milp.model.addConstr(x[k+1] == A[0][0] * x[k] + A[0][1] * y[k] + 
                                            A[0][2] * z[k] + B[0][0] * u[k] + 
                                            B[0][1] * v[k] + B[0][2] * w[k] )

        wstl_milp.model.addConstr(y[k+1] == A[1][0] * x[k] + A[1][1] * y[k] + 
                                            A[1][2] * z[k] + B[1][0] * u[k] + 
                                            B[1][1] * v[k] + B[1][2] * w[k])

        wstl_milp.model.addConstr(z[k+1] == A[2][0] * x[k] + A[2][1] * y[k] + 
                                            A[2][2] * z[k] + B[2][0] * u[k] + 
                                            B[2][1] * v[k] + B[2][2] * w[k])

    wstl_milp.model.addConstr(x[0] == -5)
    wstl_milp.model.addConstr(y[0] == -1)
    wstl_milp.model.addConstr(z[0] == 0)
    wstl_milp.model.addConstr(u[0] == 0)
    wstl_milp.model.addConstr(v[0] == 0)
    wstl_milp.model.addConstr(w[0] == 0)

    z_formula, rho_formula = wstl_milp.translate(satisfaction=True)
    wstl_milp.model.setObjective(rho_formula, grb.GRB.MAXIMIZE)
    wstl_milp.model.update()

    if type == 'long':
        wstl_milp.model.write('long_milp.lp')
    else:
        wstl_milp.model.write('short_milp.lp')

    # Solve problem
    wstl_milp.model.optimize()
    return wstl_milp

def visualize(stl_milp, wstl_milp, wstl_milp_b, wstl_milp_d, wstl_milp_e):
    t = stl_milp.variables['x'].keys()
    t2 = wstl_milp.variables['x'].keys()

    stl_x = [var.x for var in stl_milp.variables['x'].values()]
    stl_y = [var.x for var in stl_milp.variables['y'].values()] 
    wstl_x = [var.x for var in wstl_milp.variables['x'].values()]
    wstl_y = [var.x for var in wstl_milp.variables['y'].values()]
    wstl_x_b = [var.x for var in wstl_milp_b.variables['x'].values()]
    wstl_y_b = [var.x for var in wstl_milp_b.variables['y'].values()]
    wstl_x_d = [var.x for var in wstl_milp_d.variables['x'].values()]
    wstl_y_d = [var.x for var in wstl_milp_d.variables['y'].values()]
    wstl_x_e = [var.x for var in wstl_milp_e.variables['x'].values()]
    wstl_y_e = [var.x for var in wstl_milp_e.variables['y'].values()]
    environment_trajec(stl_x, stl_y, wstl_x, wstl_y, wstl_x_b, wstl_y_b, wstl_x_d, 
                wstl_y_d, wstl_x_e, wstl_y_e)


if __name__ == '__main__':
    #Formulas
    # formula = 'G[5,10] x >= 3 && G[5,10] (y <= -2) && G[5, 10] (z >= 1)'    
    # wstl_formula = "&&^weight2 ( G[5,10]^weight0  (x>=3),G[5,10]^weight3 \
    #                 (y<=-2), G[5,10]^weight3 (z>=1) )"
    obstacle = "&&" + stl_zone("O", "G", 0, 30, "x", "y")
    formula = '(' + stl_zone("C", "G", 10, 15, "x", "y") + ' && '+\
                  stl_zone("D", "G", 25, 30, "x", "y") + ' && '+ \
                    stl_zone("A", "G", 0, 1, "x", "y") + obstacle + ')'

    # formula = '(' + stl_zone("C", "F", 5, 6, "x", "y") + obstacle + ')'
    # wstl_formula= 
    wstl_obs = wstl_zone("O", "G", 1, 7, "x", "y")
    # wstl_formula = '&&^weight2 ('+wstl_zone("C", "G", 10, 15, "x", "y")+ \
    #                 ','+wstl_zone("D", "G", 25, 30, "x", "y")+ \
    #                 ','+wstl_zone("A", "G", 0, 1, "x", "y")+','+wstl_obs+')'
    wstl_formula = '&&^weight2 ('+wstl_zone("C", "G", 8, 18, "x", "y")+ \
                    ','+wstl_obs+')'

    # wstl_formula = '&&^weight2 ('+','+wstl_zone("C", "F", 5, 6, "x", "y")+','+wstl_obs+')'
    # wstl_formula = '&&^weight0 ( G[0,2]^weight0 (||^weight0 ( ) ), F[2,2] )'

    # NOTE: Case same weights wstl=stl
    # weights = {'weight0': lambda x: 1, 'weight1': lambda x:10, 
    #            'weight2': lambda k:[1, 1, 1, 1][k], 'weight3': lambda x: 1}

    # NOTE: case where there is higher weight to areas than avoiding the obstacle
    # weights = {'weight0': lambda x: 1, 'weight1': lambda x:10, 
    #            'weight2': lambda k:[.1, .1, .1, .8][k], 'weight3': lambda x: 1}

    # NOTE: case where there is higher weight to avoiding the obstacle
    weights = {'weight0': lambda x: 1, 'weight1': lambda x:10, 
               'weight2': lambda k:[1, .1, .1, .1, 1][k], 'weight3': lambda x: 1}
    weights2 = {'weight0': lambda x: 1, 'weight1': lambda x:10, 
               'weight2': lambda k:[2, .9, .1, .1, 1][k], 'weight3': lambda x: 1}
    weights3 = {'weight0': lambda x: 1, 'weight1': lambda x:10, 
               'weight2': lambda k:[1, .8, .1, .1, 1][k], 'weight3': lambda x: 1}
    weights4 = {'weight0': lambda x: 1, 'weight1': lambda x:10, 
               'weight2': lambda k:[.1, 2, .1, .1, 1][k], 'weight3': lambda x: 1}

    # Define the matrixes that used for linear system 
    A = [[1, 0, 0], [0, 1, 0],[0, 0, 1]] 
    B = [[1, 0, 0], [0, 1, 0],[0, 0, 1]] 
    vars_ub = 9
    vars_lb = -9
    control_ub = 2
    control_lb = -2

    # Translate WSTL to MILP and retrieve integer variable for the formula
    stl_start = time.time()
    stl_milp = wstl_synthesis_control(wstl_formula, weights, A, B, vars_ub, 
                                       vars_lb, control_ub, control_lb)
    stl_end = time.time()
    stl_time = stl_end - stl_start

    wstl_start = time.time()
    wstl_milp = wstl_synthesis_control(wstl_formula, weights2, A, B, vars_ub, 
                                       vars_lb, control_ub, control_lb)
    wstl_end = time.time()
    wstl_milp_b = wstl_synthesis_control(wstl_formula, weights3, A, B, vars_ub, 
                                       vars_lb, control_ub, control_lb)
    wstl_milp_d = wstl_synthesis_control(wstl_formula, weights4, A, B, vars_ub, 
                                       vars_lb, control_ub, control_lb)
    wstl_time = wstl_end - wstl_start
    wstl_milp_e = wstl_synthesis_control(wstl_formula, weights4, A, B, vars_ub, 
                                       vars_lb, 3, -3)

    print(formula, 'Time needed:', stl_time)
    print(wstl_formula, 'Time needed:', wstl_time)   
    visualize(stl_milp, wstl_milp, wstl_milp_b, wstl_milp_d, wstl_milp_e)
 
    
    

