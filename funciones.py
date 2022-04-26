# Autor: Jesus.0sorio
# Abril 2022

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

        if n < i and i == 0:
            print("Digite un numero menor al numero de elementos que hay y mayor a 0")
            continue
        else:
            break
    return i

def repeticion2(n):
    while True:
        try:
            i = int(input("Ingrese el numero de elementos que quiere tomar a la vez: "))
        except ValueError:
            print("Digite un numero entero")
            continue
        if i > 0 and i != n:
            break            
        else:
            print("Ingrese un numero entero mayor a 0 y diferente a la cantidad de elementos ingresados ")
            continue            
    return i

def combinacionR():
    while True:
        try:
            i = int(input("Ingrese el numero de elementos que quiere tomar a la vez: "))
        except ValueError:
            print("Digite un numero entero")
            continue
        if i == 0 and i < 0:
            print("Ingrese un numero entero mayor a 0")
            continue
        else:
            break
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
            i = input("Ingrese la palabra o cifras(unidas sin comas): ")
        except ValueError:
            continue

        if n < len(i) or n > len(i):
            print("Ingrese una palabra que tenga el mismo tamaño de n")
            continue
        else:
            break
    return i
def elementos(n):   
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

1 - Variacion ordinarias
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