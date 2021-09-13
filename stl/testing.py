import numpy as np 
from random import randint

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
    cars = dict()
    for x in range(3):	
	    car[x] = dict()
        for y in range(5):	
		    car[x][y]= x-y
        


    # # test()
    # num_rob = 2
    # x = []
    # y = []
    # u = []
    # v = []
    # h = dict()
    # h[1] = 2
    # for i in range(num_rob):

    #     x.append([])
    #     y.append([])
    #     u.append([])
    #     v.append([])

    #     x[i] = dict()
    #     y[i] = dict()
    #     u[i] = dict()
    #     v[i] = dict()

    # x[0][1] = 1    
    # print(x[0][1], type(h), h[1])
   