# Autor: Jesus.0sorio
# Abril 2022

import itertools as it

from funciones import *
from prints import *

m = inicio()

if m == 1:
    v = opcion1()
    if v == 1:
        n = numero()
        ele = elementos(n)
        r = repeticion1(n)
        res = factorial(n)/factorial((n-r))
        print("La cantidad de variaciones sin repeticiones que hay son: " + str(res))
        l = lista()
        if l == "SI": 
            variaciones(v,ele,r)
    else:
        n = numero()
        ele = elementos(n)
        r = repeticion2(n)
        res = n**r
        print("La cantidad de variaciones con repeticiones que hay son: " + str(res))
        l = lista()
        if l == "SI":
            variaciones(v,ele,r)

elif m == 2:
    p = opcion2()
    if p == 1:
        n = numero()
        ele = elementos(n)
        print("La cantidad de permutaciones lineales que hay son: " + str(factorial(n)))
        l = lista()
        if l == "SI":
            permutaciones(p,ele,n)
    elif p == 2:
        n = numero()
        res = permutaciones(p,None,n)
        print("La cantidad de permutaciones circulares que hay son:\n" + str(len(list(res))))
        l = lista()
        if l == "SI":
            print("El listado de las permutaciones circulares son:\n" + str(res))    
    elif p == 3:
        n = numero()
        ele = elementos(n)
        print("La cantidad de permutaciones con repeticiones que hay son: " + str(n**n))
        l = lista()
        if l == "SI":
            permutaciones(p,ele,n)
    else:
        n = numero()
        ele = elements(n)
        print(len(list(multiset_permutations(ele))))
        l = lista()
        if l == "SI":
            permutaciones(p,ele,n)
        
else:
    c = opcion3()
    if c == 1:
        n = numero()
        ele = elementos(n)
        r = repeticion1(n)
        res = int(factorial(n)/(factorial(n-r)*factorial(r)))
        print("La cantidad de combinaciones sin repeticiones que hay son: " + str(res))
        l = lista()        
        if l == "SI": 
            combinaciones(c,ele,r)
    else:
        n = numero()
        ele = elementos(n)
        r = combinacionR()
        res = list((it.combinations_with_replacement(ele, r)))
        print("La cantidad de combinaciones con repeticiones que hay son: " + str(len(res)))
        l = lista()
        if l == "SI":
            combinaciones(c,ele,r)