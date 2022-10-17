from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
import numpy as np
import time

def stl_zone(ap, T, l, u, a, b): 
    # atomic proposition, Temporal operator, lower bound, upper bound, agent_x, agent_y
    if ap == "A":
        if T == "G":
            phi = " (G[{},{}](({}<=-6) && ({}<=-6))) ".format(l,u,a,b)
        elif T == "F":
            phi = " (F[{},{}](({}<=-6) && ({}<=-6))) ".format(l,u,a,b)
        else:
            raise NotImplementedError
    
    elif ap == "B":
        if T == "G":
            phi = " (G[{},{}](({}>=6) && ({}<=-6))) ".format(l,u,a,b)
        elif T == "F":
            phi = " (F[{},{}](({}>=6) && ({}<=-6))) ".format(l,u,a,b)
        else:
            raise NotImplementedError
    
    elif ap == "C":
        if T == "G":
            phi = " (G[{},{}](({}>=6) && ({}>=6))) ".format(l,u,a,b)
        elif T == "F":
            phi = " (F[{},{}](({}>=6) && ({}>=6))) ".format(l,u,a,b)
        else:
            raise NotImplementedError
    
    elif ap == "D":
        if T == "G": 
            phi = " (G[{},{}](({}<=-6) && ({}>=6))) ".format(l,u,a,b)
        elif T == "F":
            phi = " (F[{},{}](({}<=-6) && ({}>=6))) ".format(l,u,a,b)
        else:
            raise NotImplementedError
    
    elif ap == "O":
        if T == "G": 
            phi = " (G[{},{}]( ({}>= 3) || ({}<=-3) || ({}>=3) || ({}<=-3))) ".format(l,u,a,a,b,b)
        elif T == "F":
            phi = " (F[{},{}]( ({}>= 3) || ({}<=-3) || ({}>=3) || ({}<=-3))) ".format(l,u,a,a,b,b)
        else:
            raise NotImplementedError
    
    elif ap == "E":
        if T == "G": 
            phi = " (G[{},{}]( ({}<= 1) && ({}>=-1) && ({}<=1) && ({}>=-1))) ".format(l,u,a,a,b,b)
        elif T == "F":
            phi = " (F[{},{}]( ({}>= 3) || ({}<=-3) || ({}>=3) || ({}<=-3))) ".format(l,u,a,a,b,b)
        else:
            raise NotImplementedError
    else:
        raise NotImplementedError
    return phi

def wstl_zone(ap, T, l, u, a, b): 
    '''atomic proposition, Temporal operator, lower bound, upper bound, 
        agent_x, agent_y, weights'''
    if ap == "A":
        if T == "G":
            phi = " (G[{},{}]^weight0 (&&^weight0 (({}<=-6),({}<=-6) ))) ".format(l,u,a,b)
        elif T == "F":
            phi = " (F[{},{}]^weight0 (&&^weight0 (({}<=-6),({}<=-6) ))) ".format(l,u,a,b)
        else:
            raise NotImplementedError
    
    elif ap == "B":
        if T == "G":
            phi = " (G[{},{}]^weight0 (&&^weight0 (({}>=6),({}<=-6) ))) ".format(l,u,a,b)
        elif T == "F":
            phi = " (F[{},{}]^weight0 (&&^weight0 (({}>=6),({}<=-6) ))) ".format(l,u,a,b)
        else:
            raise NotImplementedError
    
    elif ap == "C":
        if T == "G":
            phi = " (G[{},{}]^weight0 (&&^weight0 (({}>=6),({}>=6) ))) ".format(l,u,a,b)
        elif T == "F":
            phi = " (F[{},{}]^weight0 (&&^weight0 (({}>=6),({}>=6) ))) ".format(l,u,a,b)
        else:
            raise NotImplementedError
    
    elif ap == "D":
        if T == "G": 
            phi = " (G[{},{}]^weight0 (&&^weight0 (({}<=-6),({}>=6) ))) ".format(l,u,a,b)
        elif T == "F":
            phi = " (G[{},{}]^weight0 (&&^weight0 (({}<=-6),({}>=6) ))) ".format(l,u,a,b)
        else:
            raise NotImplementedError
    
    elif ap == "O":
        if T == "G": 
            phi = " (G[{},{}]^weight0( ||^weight0( ({}>= 3),({}<=-3),({}>=3),({}<=-3) ))) ".format(l,u,a,a,b,b)
        elif T == "F":
            phi = " (F[{},{}]^weight0( ||^weight0( ({}>= 3),({}<=-3),({}>=3),({}<=-3) ))) ".format(l,u,a,a,b,b)
        else:
            raise NotImplementedError
    
    elif ap == "E":
        if T == "G": 
            phi = " (G[{},{}]^weight0( ||^weight0( ({}>= 3),({}<=-3),({}>=3),({}<=-3) ))) ".format(l,u,a,a,b,b)
        elif T == "F":
            phi = " (F[{},{}]^weight0( ||^weight0( ({}>= 3),({}<=-3),({}>=3),({}<=-3) ))) ".format(l,u,a,a,b,b)
        else:
            raise NotImplementedError
    else:
        raise NotImplementedError
    return phi
    
def environment(x, y, x2, y2):
    # Desired locations 
    lvertices1 = []
    lcodes1 = []
    lvertices2 = []
    lcodes2 = []
    lvertices3 = []
    lcodes3 = []
    lvertices4 = []
    lcodes4 = []

    lcodes1 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    lvertices1 += [(5.5, -9.5), (9.5, -9.5), (9.5, -5.5), (5.5, -5.5), (0, 0)]

    lcodes2 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    lvertices2 += [(-9.5, -9.5), (-5.5, -9.5), (-5.5, -5.5), (-9.5, -5.5), (0, 0)]

    lcodes3 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    lvertices3 += [(5.5, 5.5), (9.5, 5.5), (9.5, 9.5), (5.5, 9.5), (0, 0)]

    lcodes4 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    lvertices4 += [(-9.5, 5.5), (-5.5, 5.5), (-5.5, 9.5), (-9.5, 9.5), (0, 0)]



    lpath1 = Path(lvertices1, lcodes1)
    lpath2 = Path(lvertices2, lcodes2)
    lpath3 = Path(lvertices3, lcodes3)
    lpath4 = Path(lvertices4, lcodes4)

    lpathpatch1 = PathPatch(lpath1, facecolor='skyblue', edgecolor='k')
    lpathpatch2 = PathPatch(lpath2, facecolor='wheat', edgecolor='k')
    lpathpatch3 = PathPatch(lpath3, facecolor='plum', edgecolor='k')
    lpathpatch4 = PathPatch(lpath4, facecolor='lightcyan', edgecolor='k')



    #obstacles
    overtices = []
    ocodes = []
    ocodes += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    overtices += [(-2.2, -2.2), (2.2, -2.2), (2.2, 2.2), (-2.2, 2.2), (0, 0)]
    opath = Path(overtices, ocodes)
    opathpatch = PathPatch(opath, facecolor='gray', edgecolor='k', linewidth='3')

    # Envieronment border
    vertices = []
    codes = []

    codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    vertices = [(-10, -10), (10, -10), (10, 10), (-10, 10), (0, 0)]

    path = Path(vertices, codes)

    pathpatch = PathPatch(path, facecolor='NONE', edgecolor='k', linewidth='8')

    fig, ax = plt.subplots()
    ax.text(-9, -9, 'A', fontsize=90)
    ax.text(6, 6, 'C', fontsize=90)
    ax.text(-9, 6, 'D', fontsize=90)
    ax.text(6, -9, 'B', fontsize=90)
    ax.text(-1.3, -1.3, 'E', fontsize=90)
    ax.add_patch(lpathpatch1)
    ax.add_patch(lpathpatch2)
    ax.add_patch(lpathpatch3)
    ax.add_patch(lpathpatch4)
    ax.add_patch(pathpatch)
    ax.add_patch(opathpatch)
    ax.plot(x, y,'r', linewidth=5.5, label = "STL" )
    ax.plot(x[0], y[0],'r', marker='*', markersize=28)
    ax.plot(x[-1], y[-1],'r', marker='s', markersize=20)
    ax.plot(x2, y2,'--b', linewidth=5.5, label = "WSTL")
    ax.plot(x2[0], y2[0],'b', marker='*', markersize=28)
    ax.plot(x2[-1], y2[-1],'b', marker='s', markersize=20)
    ax.legend(fontsize = 'xx-large')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlim([-11, 11])
    plt.ylim([-11, 11])
    plt.axis('equal')
    plt.show()

def environment_comp(x, y, x2, y2, x3, y3, x4, y4):
    # Desired locations 
    lvertices1 = []
    lcodes1 = []
    lvertices2 = []
    lcodes2 = []
    lvertices3 = []
    lcodes3 = []
    lvertices4 = []
    lcodes4 = []

    lcodes1 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    lvertices1 += [(5.5, -9.5), (9.5, -9.5), (9.5, -5.5), (5.5, -5.5), (0, 0)]

    lcodes2 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    lvertices2 += [(-9.5, -9.5), (-5.5, -9.5), (-5.5, -5.5), (-9.5, -5.5), (0, 0)]

    lcodes3 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    lvertices3 += [(5.5, 5.5), (9.5, 5.5), (9.5, 9.5), (5.5, 9.5), (0, 0)]

    lcodes4 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    lvertices4 += [(-9.5, 5.5), (-5.5, 5.5), (-5.5, 9.5), (-9.5, 9.5), (0, 0)]



    lpath1 = Path(lvertices1, lcodes1)
    lpath2 = Path(lvertices2, lcodes2)
    lpath3 = Path(lvertices3, lcodes3)
    lpath4 = Path(lvertices4, lcodes4)

    lpathpatch1 = PathPatch(lpath1, facecolor='skyblue', edgecolor='k')
    lpathpatch2 = PathPatch(lpath2, facecolor='wheat', edgecolor='k')
    lpathpatch3 = PathPatch(lpath3, facecolor='plum', edgecolor='k')
    lpathpatch4 = PathPatch(lpath4, facecolor='lightcyan', edgecolor='k')



    #obstacles
    overtices = []
    ocodes = []
    ocodes += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    overtices += [(-2.2, -2.2), (2.2, -2.2), (2.2, 2.2), (-2.2, 2.2), (0, 0)]
    opath = Path(overtices, ocodes)
    opathpatch = PathPatch(opath, facecolor='gray', edgecolor='k', linewidth='3')

    # Envieronment border
    vertices = []
    codes = []

    codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    vertices = [(-10, -10), (10, -10), (10, 10), (-10, 10), (0, 0)]

    path = Path(vertices, codes)

    pathpatch = PathPatch(path, facecolor='NONE', edgecolor='k', linewidth='8')

    fig, ax = plt.subplots()
    ax.text(-9, -9, 'A', fontsize=90)
    ax.text(6, 6, 'C', fontsize=90)
    ax.text(-9, 6, 'D', fontsize=90)
    ax.text(6, -9, 'B', fontsize=90)
    ax.text(-1.3, -1.3, 'E', fontsize=90)
    ax.add_patch(lpathpatch1)
    ax.add_patch(lpathpatch2)
    ax.add_patch(lpathpatch3)
    ax.add_patch(lpathpatch4)
    ax.add_patch(pathpatch)
    ax.add_patch(opathpatch)
    ax.plot(x, y,'r', linewidth=5.5, label = "STL" )
    ax.plot(x[0], y[0],'r', marker='*', markersize=28)
    ax.plot(x[-1], y[-1],'r', marker='s', markersize=20)
    ax.plot(x2, y2,'--b', linewidth=5.5, label = "WSTL")
    ax.plot(x2[0], y2[0],'b', marker='*', markersize=28)
    ax.plot(x2[-1], y2[-1],'b', marker='s', markersize=20)
    ax.plot(x3, y3, 'cornflowerblue',linewidth=5.5, label = "WSTL_B")
    ax.plot(x3[0], y3[0], 'cornflowerblue',marker='*', markersize=28)
    ax.plot(x3[-1], y3[-1], 'cornflowerblue',marker='s', markersize=20)
    ax.plot(x4, y4, 'steelblue',linewidth=5.5, label = "WSTL_D")
    ax.plot(x4[0], y4[0], 'steelblue',marker='*', markersize=28)
    ax.plot(x4[-1], y4[-1], 'steelblue',marker='s', markersize=20)
    ax.legend(fontsize = 'xx-large')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlim([-11, 11])
    plt.ylim([-11, 11])
    plt.axis('equal')
    plt.show()
if __name__ == '__main__':
    x = range(20)
    y = range(20)
    d = np.ones(100)*7
    a = np.ones(100)*9
    
    start = time.time()
    environment(x, y, d, a)
    end = time.time()
    print(end - start)
   
