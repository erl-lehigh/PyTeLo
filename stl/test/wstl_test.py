from antlr4 import InputStream, CommonTokenStream

import numpy as np

import sys
sys.path.append('..')

from stl import Operation, RelOperation, STLFormula
from wstlLexer import wstlLexer
from wstlParser import wstlParser
from wstlVisitor import wstlVisitor

from wstl import WSTLAbstractSyntaxTreeExtractor

from wstl2milp import wstl2milp

from gurobipy import *


# Create a new model
m = Model("mip1")

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

lexer = wstlLexer(InputStream("&&^weight1 (F[1, 4]^weight2 (x >= 2), x > 0.1)"))
tokens = CommonTokenStream(lexer)
parser = wstlParser(tokens)
t = parser.wstlProperty()

# Get AST from parse tree
weights = {'weight1': lambda x: 0.5, 'weight2': lambda x: 0.25}
ast = WSTLAbstractSyntaxTreeExtractor(weights).visit(t)

# Translate WSTL to MILP and retrieve integer variable for the formula
wstl_milp = wstl2milp(ast, model=m)
z_formula, rho_formula = wstl_milp.translate()

# Get/create state variables
varname = 'x'
end_time = 4
x = [wstl_milp.variables[varname].get(time, m.addVar(lb= -GRB.INFINITY,
                                                     ub= GRB.INFINITY))
     for time in range(end_time + 1)]
m.update()

# Add dynamics constraints
for time in range(end_time): # example of state transition (system dynamics)
    m.addConstr(x[time+1] == x[time] - 0.1)

for time in range(end_time + 1): # example if state constraints (e.g., safety)
    m.addConstr(x[time] >= 0)

# Set objective
m.setObjective(rho_formula, GRB.MAXIMIZE)
m.update()

m.write('milp.mps')

# Solve problem
m.optimize()

if (m.status == 2):
    y = np.array([x[i].X for i in range(end_time+1)], dtype=np.float)
else:
    print("cannot solve...")
    y = None

# Print solution
print(y)
