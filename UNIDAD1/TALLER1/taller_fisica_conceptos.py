"""
TALLER COMPUTACIÓN GRÁFICA
UNIDAD 1
FÍSICA DE CONCEPTOS
ESTUDIANTE: DANIEL FELIPE BERMUDEZ F
CODIGO: 1055751031
"""


""""
Cálculo de la Caída Libre:
Escribe un programa en Python que calcule y muestre el tiempo que tarda un objeto en caer desde una altura determinada sin resistencia del aire. Utiliza la fórmula t = sqrt(2h/g), donde h es la altura en metros y g es la aceleración de la gravedad (9.8 m/s^2). El programa debe solicitar al usuario la altura en metros y mostrar el tiempo en segundos.
"""

import math

def tiempoCaida(h):
    g = 9.8
    t = math.sqrt(2*h/g)
    t = round(t, 2)
    return "El tiempo que tarda en caer el objeto es de: " + str(t) + " segundos"


"""
Conversión de unidades de velocidad:
Crear una función que convierta la velocidad de km/h a m/s y viceversa.La función debe tomar como argumento el valor de la velocidad y el tipo de conversión.
"""

def conversionKM_M(valor):
    m_s = (valor/3.6)
    return m_s

def conversionM_KM(valor):
    km_h = (valor * 3.6)
    return km_h


"""
Calculo del desplazamiento:
Función que calcule el desplazamiento de un objeto en movimiento rectilíneo uniformemente acelerado, dados la velocidad inicial, la aceleración y el tiempo
"""

def desplazamientoRUA(velocidadInicial, aceleracion, tiempo):
    s = (velocidadInicial*tiempo)+ 0.5*(aceleracion*(tiempo**2))
    return s


"""
Suma de vectores:
una función que tome dos vectores representados como listas y devuelva su suma vectorial
"""

def stringToInteger(vectorString):
    """
    Esta función es para convertir cada elemento de una lista (vector introducido por usuario y separado por ",")
    a enteros para poder operar con sus elementos
    """
    for i in vectorString:
        vectorString[i] = int(vectorString[i])

def sumaVectores(vector1, vector2):
    if len(vector1) == len(vector2):
        vectorResultante = []
        for i in range(len(vector1)):
            vectorResultante.append(vector1[i] + vector2[i])
        return vectorResultante
    else:
        return "Valores incorrectos o vectores de tamaño distinto."


"""
Producto escalar de vectores:
Programa que calcule el producto escalar entre dos vectores y determine el ángulo entre ellos, utilizando la formula del coseno del ángulo
"""

def moduloVector(vector):
    componentesCuadrado = []
    modulo = 0
    for i in range(len(vector)):
        componentesCuadrado.append(vector[i] ** 2)
    for i in componentesCuadrado:
        modulo += i
    return math.sqrt(modulo)
        
        
def productoEscalar(vector1, vector2):
    if len(vector1) == len(vector2):
        total = 0
        vectorResultante = []
        for i in range(len(vector1)):
            vectorResultante.append(vector1[i] * vector2[i])
        for i in vectorResultante:
            total += i
        return total
    
def anguloEntreVectores(vector1, vector2):
    """
    Función para hallar el ángulo entre dos vectores
    """
    productoPunto = productoEscalar(vector1, vector2)
    multiplicacionModulo = moduloVector(vector1) * moduloVector(vector2)
    angulo = math.degrees(math.acos(productoPunto/multiplicacionModulo))
    return round(angulo)



"""
Lanzamiento de proyectil
Script para calcular el alcane máximo (R) y la altura máxima (H) alcanzada por un proyectil lanzado con una velocidad inicial (Vi) (debe estar en m/s) a un ángulo (ang) (debe estar en degrees) con la horizontal. Ignora la resistencia del aire 
"""

def alcanceMaximo(Vi, ang):
    gravedad = 9.8
    angulo_radianes = math.radians(ang)
    R = ((Vi ** 2) * (math.sin(angulo_radianes * 2)))/gravedad
    return round(R)

def alturaMaxima(Vi, ang):
    gravedad = 9.8
    angulo_radianes = math.radians(ang)
    H = ((Vi ** 2) * (math.sin(angulo_radianes) **2))/(2* gravedad)
    return round(H)

#Vi = 21.0
#ang = 75.0
#R = alcanceMaximo(Vi, ang)
#H = alturaMaxima(Vi, ang)
#print("alcance maximo: ", R, "m")
#print("Altura máxima: ", H, "m")

"""
Menú interactivo -----------------------------------------------------------------------------------------
"""

def menu ():
    print("------------------------------")
    print("FISICA COMPUTACIONAL EN PYTHON")
    print("------------------------------")
    print("MENÚ DE OPCIONES:")
    print("1. CÁLCULO DE CAIDA LIBRE")
    print("2. CONVERSIÓN DE UNIDADES DE VELOCIDAD")
    print("3. CÁLCULO DEL DESPLAZAMIENTO")
    print("4. SUMA DE VECTORES")
    print("5. PRODUCTO ESCALAR DE VECTORES")
    print("6. LANZAMIENTO DE PROYECTIL")
    print("7. SALIR")
    opcion = int(input("QUE DESEA CÁLCULAR: "))
    if opcion == 1:
        print("Para cálcular cuanto tiempo tarda un objeto en caida libre es necesario conocer su altura")
        h = int(input("Ingrese el valor de la altura: "))
        print("El tiempo en que tarda en caer un objeto desde ", h, "es de: ", tiempoCaida(h))
    elif opcion == 2:
        print("1. CONVERSIÓN DE KM/H A M/S")
        print("2. CONVERSIÓN DE M/S A KM/H")
        conversion = int(input("QUE CONVERSIÓN DESEA REALIZAR: "))
        if conversion == 1:
            valor = int(input("Ingrese la velocidad en km/h: "))
            print(valor, "km/h es igual a ", conversionKM_M(valor), "m/s")
        if conversion == 2:
            valor = int(input("Ingrese la velocidad en m/s: "))
            print(valor, "m/s es igual a ", conversionM_KM(valor), "km/h")
    elif opcion == 3:
            print("Para calcular el desplazamiento de un objeto en MRUA necesitamos: ")
            velocidadInicial = int(input("Velocidad inicial: "))
            aceleracion = int(input("Aceleración (m/s²): "))
            tiempo = int(input("Tiempo total del desplazamiento (segundos): "))
            print("El desplazamiento realizado fue de: ", desplazamientoRUA(velocidadInicial, aceleracion, tiempo), "metros")
    elif opcion == 4:
            print("Recuerda que para la suma de dos vectores, estos deben ser siempre del mismo tamaño")
            valores1 = input("Ingresa los valores del vector 1 a sumar, separados por (,): ")
            vector1 = valores1.split(",")
            stringToInteger(vector1)
            valores2 = input("Ingresa los valores del vector 1 a sumar, separados por (,): ")
            vector2 = valores2.split(",")
            stringToInteger(vector2)
            print(vector1, "+", vector2) 
            print(sumaVectores(vector1, vector2))
            
            
    
    
menu()

