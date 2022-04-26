# Autor: Jesus.0sorio
# Junio 2022

import itertools as it
from sympy.utilities.iterables import multiset_permutations

def variaciones(v,ele,r):
    if v == 1:
        res = list(it.permutations(ele, r))
        print("El listado de las variacion sin repeticiones son:\n" + str(res))
    else:
        res = list(it.product(ele, repeat=r))
        print("El listado de las variacion con repeticion son:\n" + str(res))

def permutaciones(p,ele,n):
    if p == 1:
        res = list(it.permutations(ele))
        print("El listado de las permutaciones sin repeticiones son:\n" + str(res))
    elif p == 2:
        while True:
            try:
                ele = []
                a = 1
                for h in range(n):           
                    p = input("Ingrese el elemento " + str(a) +": ")
                    a += 1
                    ele.append(p)
            except ValueError:
                continue
            else:
                break
        res = [ele[:1]+list(perm) for perm in it.permutations(ele[1:])]
        return res
    elif p == 3:
        res = list(it.product(ele, repeat=n))
        print("El listado de las permutaciones con repeticion son:\n" + str(res))
    else:
        res = []
        for i in multiset_permutations(ele):
            d = ''.join(i)
            res.append(d)
        print(res)

def combinaciones(c,ele,r):
    if c == 1:
        res = list(it.combinations(ele, r))
        print("El listado de las combinaciones sin repeticiones son:\n" + str(res))
    else:
        res = res = list(it.combinations(ele, r))
        print("El listado de las combinaciones con repeticion son:\n" + str(len(res)))