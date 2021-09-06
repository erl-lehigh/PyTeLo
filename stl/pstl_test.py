#!/usr/bin/env python3

"""
 Copyright (C) 2015-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
 @author: Weizhou Zhou, Cristian-Ioan Vasile
"""
from antlr4 import InputStream, CommonTokenStream

import sys
sys.path.append('..')
from gurobipy import Model as GRBModel
from gurobipy import GRB
import gurobipy as grb

import matplotlib.pyplot as plt

from stl import Operation, RelOperation, STLFormula
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor

from stl import STLAbstractSyntaxTreeExtractor
from pstl2milp import pstl2milp
# from stl2milp import stl2milp


def stl_milp_solver(x_init, y_init, formula):
     # create MILP
    # stl_milp = GRBModel('milp')
# x_init, y_init, z_init = 2, 2, -3
    # Define the general range for x y z 
    # stl_milp = pstl2milp(ast, ranges={'x': [-4, 5], 'y': [-4, 5], 'z': [-4, 5]})
    stl_milp = pstl2milp(formula, ranges={'x': [-4, 5], 'y': [-4, 5]})
    stl_milp.M = 20

    # Define the matrixes that used for linear system 
    # M = [[1, 2, 3], [4, 5, 6],[7, 8, 9]] 
    # B = [[7, 8, 9], [4, 5, 6],[1, 2, 3]] 
    M = [[1, 0], [0, 1]] 
    B = [[1, 0], [0, 1]]
    # system variables and the time period 
    period = 25
    x = dict()
    y = dict()
    # z = dict()
    u = dict()
    v = dict()
    # w = dict()

    for k in range(period):
        name = "x_{}".format(k) 
        x[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "y_{}".format(k)
        y[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        # name = "z_{}".format(k) 
        # z[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "u_{}".format(k)
        u[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        name = "v_{}".format(k)
        v[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        # name = "w_{}".format(k)
        # w[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-3, ub=3, name=name)

    # use system variables in STL spec encoding
    stl_milp.variables['x'] = x
    stl_milp.variables['y'] = y
    # stl_milp.variables['z'] = z
    stl_milp.variables['u'] = u
    stl_milp.variables['v'] = v
    # stl_milp.variables['w'] = w

    # define the inital states for each mpc step 
    stl_milp.model.addConstr(x[0] == x_init)
    stl_milp.model.addConstr(y[0] == y_init)
    # stl_milp.model.addConstr(z[0] == z_init)

    # system constraints
    for k in range(period-1):
        # stl_milp.model.addConstr(x[k+1] == M[0][0] * x[k] + M[0][1] * y[k] + M[0][2] * z[k] + \
        #     B[0][0] * u[k] + B[0][1] * v[k] + B[0][2] * w[k])
        # stl_milp.model.addConstr(y[k+1] == M[1][0] * x[k] + M[1][1] * y[k] + M[1][2] * z[k] + \
        #     B[1][0] * u[k] + B[1][1] * v[k] + B[1][2] * w[k])
        # stl_milp.model.addConstr(z[k+1] == M[2][0] * x[k] + M[2][1] * y[k] + M[2][2] * z[k] + \
        #     B[2][0] * u[k] + B[2][1] * v[k] + B[2][2] * w[k])
        stl_milp.model.addConstr(x[k+1] == M[0][0] * x[k] + M[0][1] * y[k] + B[0][0] * u[k] + B[0][1] * v[k])
        stl_milp.model.addConstr(y[k+1] == M[1][0] * x[k] + M[1][1] * y[k] + B[1][0] * u[k] + B[1][1] * v[k])
        
    # add the specification (STL) constraints
    z = stl_milp.translate()

    # Solve the problem with gurobi 
    stl_milp.model.setObjective(z, GRB.MAXIMIZE)
    stl_milp.model.update()
    stl_milp.model.optimize()
    stl_milp.model.write('model_test.lp')


    x_vals = [var.x for var in stl_milp.variables['x'].values()]
    y_vals = [var.x for var in stl_milp.variables['y'].values()]
    # z_vals = [var.x for var in stl_milp.variables['z'].values()]
    # stl_milp.pstl2lp(formula, t)

    return x_vals[1], y_vals[1]
    # return x_vals[1], y_vals[1], z_vals[1]
#print(stl_milp_solver(2, 2, -3))

def main():
    # formula = "G[0,6](x <= 4) && G[0, 6] (y <= 4) && G[0,6](x >= 1) && G[0, 6] (y >= 1) && G[8,20](x >= 2) && G[8, 20] (y >= 1) && G[8,20](x <= 3) && G[8, 20] (y <= 2)"
    # formula = "G[5,30] ((x>=2) && (y>=2))"
    # formula = "G[2,6](x <= 3) && G[2,6](x >= 1) && G[2,6](y <= 3) && G[2,6](y >= 1) "
    # formula = "G[0,6](x > 3) && F[0, 2] (y >= 4)"
    # formula = "G[2,4] F[1,3](x>=3)"
    # formula = "(x <= 10) && F[0, 2] y > 2 && G[1, 6] (z < 8) && G[1,6] (z > 3)"
    formula = "G[2,4] (x>=4)"
    # Define the formula that you want to apply 
    # formula = 'G[0,10] x >= 3 && G[2,4] F[20,24] (y > 2) && G[21, 26] (z < 8) && G[21,26] (z > 3)'
    #formula = 'G[0,2] x >= 3 && F[0,6] (y >= 4) && G[0, 2] (z >= 1)'

    # Define the matrixes that used for linear system 
    # M = [[1, 2, 3], [4, 5, 6],[7, 8, 9]] 
    # B = [[7, 8, 9], [4, 5, 6],[1, 2, 3]] 
    M = [[1, 0], [0, 1]] 
    B = [[1, 0], [0, 1]] 


    # Stl2milp Initialization
    lexer = stlLexer(InputStream(formula))
    tokens = CommonTokenStream(lexer)
    parser = stlParser(tokens)
    t = parser.stlProperty()
    print(t.toStringTree())
    ast = STLAbstractSyntaxTreeExtractor().visit(t)

    print('AST:', str(ast))
    
    steps = 30
    x_init, y_init = 0, 0
    x = [0 if i != 0 else x_init for i in range(steps)]
    y = [0 if i != 0 else y_init for i in range(steps)]
    # z = [0 if i != 0 else z_init for i in range(steps)]
    t = [i for i in range(steps)]

    for i in range(1, steps):
        x[i], y[i]= stl_milp_solver(x[i - 1], y[i - 1], ast)

    fig, axs = plt.subplots(2)
    fig.suptitle('subplots')
    axs[0].plot(t, x)
    axs[0].set_title('x vs t')
    axs[1].plot(t, y)
    axs[1].set_title('y vs t')
    fig.tight_layout()
    plt.show()
    


if __name__ =='__main__':
    main()