# Autor: Jesus.0sorio
# Junio 2022

def numero():
    while True:
        try:
            n = int(input("Ingrese la cantidad de elementos siendo un entero mayor a 0: "))
        except ValueError:
            print("Digite un numero entero")
            continue

        if n <= 0:
            print("Digite un numero mayor a 0")
            continue
        else:
            break
    return n

def repeticion1(n):
    while True:
        try:
            i = int(input("Ingrese el numero de elementos que quiere tomar a la vez: "))
        except ValueError:
            print("Digite un numero entero")
            continue

        if n < i:
            print("Digite un numero menor o igual a la cantidad de datos que hay")
            continue
        else:
            break
    return i

def repeticion2():
    while True:
        try:
            i = int(input("Ingrese el numero de elementos que quiere tomar a la vez: "))
        except ValueError:
            print("Digite un numero entero")
            continue
        if i > 0:
            break            
        else:
            print("Ingrese un numero entero mayor a 0 ")
            continue
            
    return i

def inicio():
    while True:
        try:
            n = int(input(menu))
        except ValueError:
            print("Digite una de las opciones")
            continue

        if n <= 0 or n > 3:
            print("Digite una de las 3 opciones")
            continue
        else:
            break
    return n

def opcion1():
    while True:
        try:
            n = int(input(variacion))
        except ValueError:
            print("Digite una de las opciones")
            continue

        if n <= 0 or n > 2:
            print("Digite una de las 2 opciones")
            continue
        else:
            break
    return n

def opcion2():
    while True:
        try:
            n = int(input(permutacion))
        except ValueError:
            print("Digite una de las opciones")
            continue

        if n <= 0 or n > 4:
            print("Digite una de las 4 opciones")
            continue
        else:
            break
    return n

def opcion3():
    while True:
        try:
            n = int(input(combinacion))
        except ValueError:
            print("Digite una de las opciones")
            continue

        if n <= 0 or n > 2:
            print("Digite una de las 2 opciones")
            continue
        else:
            break
    return n

def lista():
    while True:
        try:
            n = input("""¿Desea generar el listado de los resultados?
            SI o NO  :  """).upper()
        except ValueError:
            print("Digite una de las opciones")
            continue

        if n == "SI" or n == "NO":
            break
        else:
            print("Debe ingresar SI o NO")
            continue
    return n

def elements(n):
    while True:
        try:
            i = input("Ingrese los elementos: ")
        except ValueError:
            continue

        if n < len(i) or n > len(i):
            print("Ingrese el mismo numero de elementos que al que se le va hacer el calculo")
            continue
        else:
            break
    return i
def elementos(n):   
    while True:
        try:
            o = int(input("""Desea escribir palabras o caracteres individuales unidos
            1 - Palabras
            2 - Caracteres
            Eliga una opcion: """))
        except ValueError:
            print("\nIngrese una de las dos opciones")
            continue
        if o == 1:
            ele = []
            a = 1
            for h in range(n):           
                p = input("Ingrese la " + str(a)+ " palabra: ")
                a += 1
                ele.append(p)
            break
        elif o == 2:
            ele = elements(n)    
            break
        else:
            print("\nIngrese una de las dos opciones")
            continue
    return ele

def factorial(num): 
    if num < 0: 
        print("No exite factorial negativo")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

menu = """
Que operacion desea realizar

1 - Variacion
2 - Permutacion
3 - Combinacion

Elige una opción: """

variacion =  """
Que tipo de variacion desea realizar

1 - Variacion sin repeticion
2 - Variacion con repeticion

Elige una opcion: """

permutacion =  """
Que tipo de permutacion desea realizar

1 - Permutacion lineal
2 - Permutacion circulares
3 - Permutacion con repeticion
4 - Permutacion con multiconjuntos

Elige una opcion: """

combinacion =  """
Que tipo de permutacion desea realizar

1 - Combinacion sin repeticiones
2 - Combinacion con repeticiones

Elige una opcion: """
