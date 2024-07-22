import matplotlib.pyplot as plt
import gurobipy as grb
import sys

sys.path.append('../')

from stl import to_ast as stl2ast
from wstl import to_ast as wstl2ast
from wstl2milp import wstl2milp
from stl2milp import stl2milp

def stl_synthesis_control(formula, vars_ub, vars_lb):

    ast = stl2ast(formula)
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

def wstl_synthesis_control(wstl_formula, weights, vars_ub, vars_lb):
    
    ast = wstl2ast(wstl_formula, weights)
    wstl_milp = wstl2milp(ast)

    time_bound = int(ast.bound()) + 1
    # system variables and the time period 
    x = dict()
    y = dict()

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

   
    wstl_milp.model.write('wstl_milp.lp')

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
    
    

