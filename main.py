# Autor: Jesus.0sorio
# Junio 2022

import itertools as it
from funciones import *

m = inicio()

if m == 1:
    v = opcion1()
    if v == 1:
        n = numero()
        ele = elementos(n)
        r = repeticion1(n)
        res = factorial(n)/factorial((n-r))
        print("La cantidad de variaciones que hay sin repeticiones es: " + str(res))
        l = lista()
        
        if l == "SI": 
            res = list(it.permutations(ele, r))
            print(res)
    else:
        n = numero()
        ele = elementos(n)
        r = repeticion2()
        res = n**r
        print("La cantidad de variaciones que hay con repeticiones es: " + str(res))
        l = lista()
        print(ele)
        if l == "SI":
            res = list(it.product(ele, repeat=r))
            print(res)

elif m == 2:
    p = opcion2()
    if p == 1:
        n = numero()
        ele = elementos(n)
        print(factorial(n))
        l = lista()
        if l == "SI":
            res = list(it.permutations(ele))
            print(res)
    elif p == 2:
        None
    
    elif p == 3:
        n = numero()
        ele = elementos(n)
        print(n**n)
        l = lista()
        if l == "SI":
            res = list(it.product(ele, repeat=n))
            print(res)
        
else:
    c = opcion3()
    if c == 1:
        n = numero()
        ele = elementos(n)
        r = repeticion1(n)
        res = int(factorial(n)/(factorial(n-r)*factorial(r)))
        print("La cantidad de combinaciones que hay sin repeticiones es: " + str(res))
        l = lista()        
        if l == "SI": 
            res = list(it.combinations(ele, r))
            print(res)
    else:
        n = numero()
        ele = elementos(n)
        r = repeticion2()
        res = list((it.combinations_with_replacement(ele, r)))
        print("La cantidad de combinaciones que hay con repeticiones es: " + str(len(res)))
        l = lista()
        if l == "SI":
            print(res)
