"""
TALLER COMPUTACIÓN GRÁFICA
UNIDAD 1
OPERACIONES BÁSICAS CON NUMPY
ESTUDIANTE: DANIEL FELIPE BERMUDEZ F
CODIGO: 1055751031
"""

import numpy as np

# 1) Crear un Array Unidimensional
def ejercicio1():
    print("\nEjercicio 1: Crear un Array Unidimensional")
    array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("Array unidimensional:", array_1d)

# 2) Crear un Array Multidimensional
def ejercicio2():
    print("\nEjercicio 2: Crear un Array Multidimensional")
    array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Matriz 2D:\n", array_2d)

# 3) Operaciones Básicas con Arrays
def ejercicio3():
    print("\nEjercicio 3: Operaciones Básicas con Arrays")
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([1, 2, 3, 4, 5])
    resultado = array1 + array2
    print("Array 1:", array1)
    print("Array 2:", array2)
    print("Suma de los arrays:", resultado)

# 4) Funciones Matemáticas
def ejercicio4():
    print("\nEjercicio 4: Funciones Matemáticas")
    array = np.array([1, 2, 3, 4, 5])
    resultado = np.exp(array)
    print("Array original:", array)
    print("Exponencial de cada elemento:", resultado)

# 5) Indexación y Segmentación
def ejercicio5():
    print("\nEjercicio 5: Indexación y Segmentación")
    array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    pares = array[array % 2 == 0]
    print("Array original:", array)
    print("Elementos pares:", pares)

# 6) Generación de Datos Aleatorios
def ejercicio6():
    print("\nEjercicio 6: Generación de Datos Aleatorios")
    array_random = np.random.random(10)
    print("Array de 10 números aleatorios entre 0 y 1:", array_random)

# 7) Funciones de Agregación
def ejercicio7():
    print("\nEjercicio 7: Funciones de Agregación")
    array = np.array([1, 2, 3, 4, 5])
    media = np.mean(array)
    print("Array original:", array)
    print("Media de los elementos:", media)

# 8) Creación de Arrays con Funciones de Fábrica
def ejercicio8():
    print("\nEjercicio 8: Creación de Arrays con Funciones de Fábrica")
    array = np.full(5, 7)
    print("Array de 5 elementos inicializados con 7:", array)

# 9) Operaciones de Alineación y Broadcasting
def ejercicio9():
    print("\nEjercicio 9: Operaciones de Alineación y Broadcasting")
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])
    resultado = array1 + array2
    print("Array 1:", array1)
    print("Array 2:", array2)
    print("Suma con broadcasting:", resultado)

# 10) Funciones de Transformación y Redimensionamiento
def ejercicio10():
    print("\nEjercicio 10: Funciones de Transformación y Redimensionamiento")
    array = np.array([1, 2, 3, 4, 5, 6])
    array_reshaped = array.reshape(2, 3)
    print("Array original:", array)
    print("Matriz 2x3:\n", array_reshaped)

# Menú principal
def menuPrincipal():
    while True:
        print("\n=== Menú Principal - Taller de NumPy ===")
        print("1. Crear un Array Unidimensional")
        print("2. Crear un Array Multidimensional")
        print("3. Operaciones Básicas con Arrays")
        print("4. Funciones Matemáticas")
        print("5. Indexación y Segmentación")
        print("6. Generación de Datos Aleatorios")
        print("7. Funciones de Agregación")
        print("8. Creación de Arrays con Funciones de Fábrica")
        print("9. Operaciones de Alineación y Broadcasting")
        print("10. Funciones de Transformación y Redimensionamiento")
        print("0. Salir")

        opcion = int(input("Ingrese una opción (0 - 10): "))

        if opcion == 0:
            print("¡Hasta luego!")
            break
        elif opcion == 1:
            ejercicio1()
        elif opcion == 2:
            ejercicio2()
        elif opcion == 3:
            ejercicio3()
        elif opcion == 4:
            ejercicio4()
        elif opcion == 5:
            ejercicio5()
        elif opcion == 6:
            ejercicio6()
        elif opcion == 7:
            ejercicio7()
        elif opcion == 8:
            ejercicio8()
        elif opcion == 9:
            ejercicio9()
        elif opcion == 10:
            ejercicio10()
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menuPrincipal()