import numpy as np 
from random import randint
from collections import OrderedDict, namedtuple

def sets():
    set = {('hola', 1)}
# set = {}
    set = set.union([('chao',2), ('test',3)])
    set = set.union([ ('for',f) for f in range(4, 9)])
    # for w in set:   
    #     print(w[0], w[1])
    return set
    

def test():
    word = sets()
    # word, t = zip(*sets())
    for w in word:  
        print((w[0], w[1]))
    

if __name__ =='__main__':

    set1 = frozenset({'a', 'b', 'c'})
    set2 = frozenset({'d', 'e', 'f'})
    set3 = frozenset({'t', 'h'})

    weights = [0.3, 0.5, 0.2]

    mrho = {
    "rho1" : OrderedDict({1 : set1, 2: 0.5, 3: 1}),
    "rho2" : OrderedDict({1 : set2, 2: 0.3, 3: 2}),
    "rho3" : OrderedDict({1 : set3, 2: 0.2, 3: 3})
    }
    # print(mrho.values())
    # for r in mrho.values():
        
    #     k = r.keys()
    #     v = set(r.values())
    #     # print(type(v), v)
    #     var = 'b'
    #     if var in r[k[0]]:
    #         print("rho:", r[k[1]], r[k[2]])
    #     # print(v)

    
    Rho = namedtuple('Rho','set weight id')

    args = [set1,0.5,1]

    rho1 = Rho(*args)
    rho2 = Rho(set=set2,weight=0.3,id=2)
    rho3 = Rho(set=set3,weight=0.2,id=3)

    mrho_nt = {
    "rho1" : Rho(*args),
    "rho2" : rho2,
    "rho3" : rho3
    }
    print(mrho_nt['rho1'].id, 'HEREEEEEEEEEEEEEEEEe')
    for r in mrho_nt.values():
        var = 'a'
        if var in r.set:
            print(r.weight, r.id)
    
    print('pruebas', len(mrho_nt.keys()))
    
    # mrho = dict()
    # for predicado in pred:
        
    #     args = [set1,0.5,1]
        
        
    #     for i,rho in enumerate(rhos):
    #         mrho['rho'+str(i)] = Rho(*args)