import sys
import time 
import random
import matplotlib.pyplot as plt
sys.path.append('../')
from antlr4 import InputStream, CommonTokenStream
from stl import Operation, RelOperation, STLFormula
from wstlLexer import wstlLexer
from wstlParser import wstlParser
from wstlVisitor import wstlVisitor
import gurobipy as grb
from wstl import WSTLAbstractSyntaxTreeExtractor
from stl import STLAbstractSyntaxTreeExtractor
from wstl2milp import wstl2milp
from stl2milp import stl2milp
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor
from stl import STLAbstractSyntaxTreeExtractor
import numpy as np
from scipy.ndimage.filters import gaussian_filter1d

def stl_synthesis_control(formula, vars_ub=10, vars_lb=-10):
    
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
        u[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                     ub=vars_ub, name=name)
        name = "v_{}".format(k)
        v[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                     ub=vars_ub, name=name)
        name = "w_{}".format(k)
        w[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                     ub=vars_ub, name=name)
    # use system variables in STL spec encoding
    stl_milp.variables['x'] = x
    stl_milp.variables['y'] = y
    stl_milp.variables['z'] = z
    stl_milp.variables['u'] = u
    stl_milp.variables['v'] = v
    stl_milp.variables['w'] = w
    
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

def wstl_synthesis_control(wstl_formula, weights, vars_ub=10, vars_lb=-10, 
                           type='short'):
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
        name = "z_{}".format(k) 
        z[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                      ub=vars_ub, name=name)
        name = "u_{}".format(k)
        u[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                      ub=vars_ub, name=name)
        name = "v_{}".format(k)
        v[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                      ub=vars_ub, name=name)
        name = "w_{}".format(k)
        w[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                      ub=vars_ub, name=name)

    # use system variables in STL spec encoding
    wstl_milp.variables['x'] = x
    wstl_milp.variables['y'] = y
    wstl_milp.variables['z'] = z
    wstl_milp.variables['u'] = u
    wstl_milp.variables['v'] = v
    wstl_milp.variables['w'] = w

    wstl_milp.model.addConstr(x[0] == -9)
    wstl_milp.model.addConstr(y[0] == -9)
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



if __name__ == '__main__':
    random.seed(0)
    temp_op = ['G', 'F']
    logic = ['&&', '||']
    vars = ['x', 'y', 'z', 'u', 'v', 'w']
    pi = lambda x,y: random.randint(x,y)
    comp_op = ['>=', '<=']

    weights = {'weight0': lambda x: 1, 'weight1': lambda x:random.random(), 
               'weight2': lambda k:[.9, .9, .9, .1][k], 'weight3': lambda x: 1}

    aux=pi(-7,7)
    stl_specification = ('(G[0,1] {}{}{})').format(vars[-1], comp_op[-1], aux)
    wstl_specification = ('&&^weight0 (G[0,1]^weight0({}{}{})').format(vars[-1], 
                                                           comp_op[-1], aux)+')'
    wstl_specification2= ('&&^weight1 (G[0,1]^weight1({}{}{})').format(vars[-1], 
                                                           comp_op[-1], aux)+')'
    n_ = 4 + 200
    randomseeds = 1
    stl_time = np.zeros((randomseeds, n_))
    wstl_time = np.zeros((randomseeds, n_))
    wstl_time2 = np.zeros((randomseeds, n_))
   
    obj_list_2 = []
    obj_list = []
    
    

    for i in range(randomseeds):
        random.seed(10)
        for n in range(4,n_):
            L2 = random.choice(logic)
            T = random.choice(temp_op)
            s1 = random.choice(vars)
            s2 = random.choice(vars)
            op1 = random.choice(comp_op)
            op2 = random.choice(comp_op)
            pi1 = str(pi(-8,8))
            pi2 = str(pi(-8,8))
            lb = n
            ub = n + 5
            stl_specification += (' && ('+T+'[{},{}] ('+s1+op1+pi1+' '+L2+' '+
                                    s2+op2+pi2+'))').format(lb,ub)
            wstl_specification = wstl_specification[:-1]
            wstl_specification2 = wstl_specification2[:-1]
            wstl_specification += (', ('+T+'[{},{}]^weight0 ( '+L2+'^weight0('
                                +s1+op1+pi1+','+s2+op2+pi2+'))))').format(lb,ub)
            wstl_specification2 += (', ('+T+'[{},{}]^weight1 ( '+L2+'^weight1('
                                +s1+op1+pi1+','+s2+op2+pi2+'))))').format(lb,ub)

            stl_start = time.time()
            obj_1 = stl_synthesis_control(stl_specification)
            stl_end = time.time()
            stl_time[i][n] = stl_end-stl_start

            wstl_start = time.time()
            obj_2 = wstl_synthesis_control(wstl_specification, weights)
            wstl_end = time.time()
            wstl_time[i][n] = wstl_end-wstl_start

            wstl_start2 = time.time()
            obj_2 = wstl_synthesis_control(wstl_specification, weights)
            wstl_end2 = time.time()
            wstl_time2[i][n] = wstl_end2-wstl_start2

        # print(wstl_specification)
    stl_max = np.max(stl_time, axis=0)
    wstl_max = np.max(wstl_time, axis=0)
    wstl2_max = np.max(wstl_time2, axis=0)

    stl_min = np.min(stl_time, axis=0)
    wstl_min = np.min(wstl_time, axis=0)
    wstl2_min = np.min(wstl_time2, axis=0)

    stl_av = np.mean(stl_time, axis=0)
    wstl_av = np.mean(wstl_time, axis=0)
    wstl2_av = np.mean(wstl_time2, axis=0)

    print(stl_max)
    print('done')
    plt.figure()
    plt.grid()
    plt.plot(range(n_), gaussian_filter1d(stl_max, sigma=2), '-b', linewidth=4, label='stl')
    # plt.plot(range(n_), stl_av,  '-b',linewidth=4, label='stl_av')
    # plt.plot(range(n_), stl_min, '-b',linewidth=4, label='stl_min')
    plt.plot(range(n_), gaussian_filter1d(wstl_max, sigma=2), '--r',  linewidth=4, label='wstl_1')
    # plt.plot(range(n_), wstl_av, '--r',  linewidth=4, label='wstl_av')
    # plt.plot(range(n_), wstl_min, '--r',  linewidth=4, label='wstl_min')
    plt.plot(range(n_), gaussian_filter1d(wstl2_max, sigma=2), 'g', linewidth=4, label='wstl2_rand')
    # plt.plot(range(n_), wstl2_av, 'g', linewidth=4, label='wstl2_av')
    # plt.plot(range(n_), wstl2_min, 'g', linewidth=4, label='wstl2_min')
    
    plt.legend()
    plt.xticks(fontsize=44)
    plt.yticks(fontsize=44)
    plt.ylabel('time', fontsize=50)
    plt.xlabel('n', fontsize=50)
    plt.show() 
    