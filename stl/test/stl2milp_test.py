#!/usr/bin/env python3

"""
 Copyright (C) 2015-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.

 @author: Sadra Sadradinni, Cristian-Ioan Vasile
"""
from antlr4 import InputStream, CommonTokenStream

import sys
sys.path.append('..')

import gurobipy as grb

import matplotlib.pyplot as plt

from stl import Operation, RelOperation, STLFormula
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor

from stl import STLAbstractSyntaxTreeExtractor

from stl2milp import stl2milp

# formula = "(x > 10) && F[0, 2] y > 2 || G[1, 6] z > 8"
# formula = "G[2,4] F[1,3](x>=3)"
# formula = "(x <= 10) && F[0, 2] y > 2 && G[1, 6] (z < 8) && G[1,6] (z > 3)"

# Define the formula that you want to apply 
formula = 'G[0,10] x >= 3 && G[2,4] F[20,24] (y >= 2) && G[21, 26] (z <= 4) && G[21,26] (z >= 3)'
# formula = 'G[0,6] x >= 3 && G[0,6] (y >= 2) && G[0, 6] (z >= 1)'


# Stl2milp Initialization
lexer = stlLexer(InputStream(formula))
tokens = CommonTokenStream(lexer)
parser = stlParser(tokens)
t = parser.stlProperty()
print(t.toStringTree())
ast = STLAbstractSyntaxTreeExtractor().visit(t)

print('AST:', str(ast))

stl_milp = stl2milp(ast, ranges={'x': [-4, 5], 'y': [-4, 5], 'z': [-4, 5]}, robust=True)
stl_milp.M = 20

# Define the matrixes that used for linear system 
# M = [[1, 2, 3], [4, 5, 6],[7, 8, 9]] 
# B = [[7, 8, 9], [4, 5, 6],[1, 2, 3]] 
M = [[1, 0, 0], [0, 1, 0],[0, 0, 1]] 
B = [[1, 0, 0], [0, 1, 0],[0, 0, 1]] 

# system variables and the time period 
period = 30
x = dict()
y = dict()
z = dict()
u = dict()
v = dict()
w = dict()

for k in range(period):
    name = "x_{}".format(k) 
    x[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
    name = "y_{}".format(k)
    y[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
    name = "z_{}".format(k) 
    z[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
    name = "u_{}".format(k)
    u[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-3, ub=2, name=name)
    name = "v_{}".format(k)
    v[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-2, ub=3, name=name)
    name = "w_{}".format(k)
    w[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-3, ub=3, name=name)

# use system variables in STL spec encoding
stl_milp.variables['x'] = x
stl_milp.variables['y'] = y
stl_milp.variables['z'] = z
stl_milp.variables['u'] = u
stl_milp.variables['v'] = v
stl_milp.variables['w'] = w


# system constraints
for k in range(period-1):
    stl_milp.model.addConstr(x[k+1] == M[0][0] * x[k] + M[0][1] * y[k] + M[0][2] * z[k] + \
        B[0][0] * u[k] + B[0][1] * v[k] + B[0][2] * w[k])
    stl_milp.model.addConstr(y[k+1] == M[1][0] * x[k] + M[1][1] * y[k] + M[1][2] * z[k] + \
        B[1][0] * u[k] + B[1][1] * v[k] + B[1][2] * w[k])
    stl_milp.model.addConstr(z[k+1] == M[2][0] * x[k] + M[2][1] * y[k] + M[2][2] * z[k] + \
        B[2][0] * u[k] + B[2][1] * v[k] + B[2][2] * w[k])

# add the specification (STL) constraints
stl_milp.translate(satisfaction=True)

# x = stl_milp.variables['x']
# n = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=1, ub=2, name="n") 
# stl_milp.model.addConstr(x[1] == x[0] + n)

# Solve the problem with gurobi 
stl_milp.model.optimize()

# Print the solutions of the variables 
print('Vars')
for var in stl_milp.model.getVars():
    print(var.VarName, ':', var.x)

print('Constraints')
for constr in stl_milp.model.getConstrs():
    print(':', str(constr))

print('Objective')
obj = stl_milp.model.getObjective()
print(str(obj), ':', obj.getValue())

stl_milp.model.write('stl2milp.lp')

# Plot the variables with time changes
t = stl_milp.variables['y'].keys()

x_vals = [var.x for var in stl_milp.variables['x'].values()]
y_vals = [var.x for var in stl_milp.variables['y'].values()]
z_vals = [var.x for var in stl_milp.variables['z'].values()]
u_vals = [var.x for var in stl_milp.variables['u'].values()]
v_vals = [var.x for var in stl_milp.variables['v'].values()]
w_vals = [var.x for var in stl_milp.variables['w'].values()]

fig, axs = plt.subplots(3, 2)
fig.suptitle('subplots')
axs[0][0].plot(t, x_vals)
axs[0][0].set_title('x vs t')
axs[1][0].plot(t, y_vals)
axs[1][0].set_title('y vs t')
axs[2][0].plot(t, z_vals)
axs[2][0].set_title('z vs t')
axs[0][1].plot(t, u_vals)
axs[0][1].set_title('u vs t')
axs[1][1].plot(t, v_vals)
axs[1][1].set_title('v vs t')
axs[2][1].plot(t, w_vals)
axs[2][1].set_title('w vs t')
fig.tight_layout()
plt.show()

