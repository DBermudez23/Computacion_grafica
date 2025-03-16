"""
TALLER COMPUTACIÓN GRÁFICA
UNIDAD 1
PROGRAMACIÓ NUMÉRICA CON NUMPY
ESTUDIANTE: DANIEL FELIPE BERMUDEZ F
CODIGO: 1055751031
"""

import numpy as np

# Función para ordenar tuplas (del requerimiento anterior)
def ordenarTuplas(lista):
    return sorted(lista, key=lambda x: (x[1], x[0]))  # Ordenamos primero por edad y luego por nombre

# Ejercicio 1: Creación y Propiedades de Arrays
def ejercicio1():
    print("\nEjercicio 1: Creación y Propiedades de Arrays")
    array = np.array(range(1, 11))
    print("Array original:", array)
    array_reshaped = array.reshape(2, 5)
    print("Array con nueva forma (2, 5):", array_reshaped)
    print("Forma:", array_reshaped.shape)
    print("Tamaño:", array_reshaped.size)
    print("Dimensiones:", array_reshaped.ndim)

# Ejercicio 2: Operaciones Básicas
def ejercicio2():
    print("\nEjercicio 2: Operaciones Básicas")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("Array a:", a)
    print("Array b:", b)
    print("Suma (a + b):", a + b)
    print("Resta (a - b):", a - b)
    print("Producto elemento a elemento (a * b):", a * b)
    print("Suma de todos los elementos de a:", np.sum(a))

# Ejercicio 3: Indexación y Slicing
def ejercicio3():
    print("\nEjercicio 3: Indexación y Slicing")
    data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print("Array original:", data)
    print("Quinto elemento (data[4]):", data[4])
    print("Subsección (data[2:7]):", data[2:7])

# Ejercicio 4: Broadcasting y Funciones Universales
def ejercicio4():
    print("\nEjercicio 4: Broadcasting y Funciones Universales")
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Matriz A:\n", A)
    print("Suma de un escalar (A + 10):\n", A + 10)
    print("Raíz cuadrada de A (np.sqrt(A)):\n", np.sqrt(A))

# Ejercicio 5: Manipulación de Formas y Álgebra Lineal
def ejercicio5():
    print("\nEjercicio 5: Manipulación de Formas y Álgebra Lineal")
    M = np.array([1, 2, 3, 4, 5, 6])
    print("Array original M:", M)
    M_reshaped = M.reshape(3, 2)
    print("M con nueva forma (3, 2):\n", M_reshaped)
    print("Transpuesta de M (M.T):\n", M_reshaped.T)
    print("Producto punto de M y su transpuesta:\n", np.dot(M_reshaped, M_reshaped.T))

# Ejercicio 6: Trabajo con Datos Faltantes
def ejercicio6():
    print("\nEjercicio 6: Trabajo con Datos Faltantes")
    data = np.array([1, 2, np.nan, 4, 5, np.nan, 7])
    print("Array con datos faltantes:", data)
    data_cleaned = np.nan_to_num(data, nan=0)
    print("Array después de reemplazar NaN por 0:", data_cleaned)
    print("Media del array limpio:", np.mean(data_cleaned))

# Ejercicio 7: Guardar y Cargar Arrays
def ejercicio7():
    print("\nEjercicio 7: Guardar y Cargar Arrays")
    data = np.array([10, 20, 30, 40, 50])
    np.save('mi_array.npy', data)
    print("Array guardado:", data)
    loaded_data = np.load('mi_array.npy')
    print("Array cargado desde el archivo:", loaded_data)

# Función para ordenar tuplas (integrada como opción adicional)
def ejercicio8():
    print("\nEjercicio 8: Ordenar Lista de Tuplas por Edad y Nombre")
    lista_tuplas = eval(input("Ingrese una lista de tuplas (nombre, edad) separadas por comas, ej: [('Ana', 25), ('Juan', 22)]: "))
    lista_ordenada = ordenarTuplas(lista_tuplas)
    print("Lista ordenada:", lista_ordenada)

# Menú principal
def menuPrincipal():
    while True:
        print("\n=== Menú Principal - Taller de NumPy ===")
        print("1. Creación y Propiedades de Arrays")
        print("2. Operaciones Básicas")
        print("3. Indexación y Slicing")
        print("4. Broadcasting y Funciones Universales")
        print("5. Manipulación de Formas y Álgebra Lineal")
        print("6. Trabajo con Datos Faltantes")
        print("7. Guardar y Cargar Arrays")
        print("8. Ordenar Lista de Tuplas por Edad y Nombre")  # Nueva opción
        print("0. Salir")

        opcion = int(input("Ingrese una opción (0 - 8): "))

        if opcion == 0:
            print("¡Hasta luego!")
            break
        elif opcion == 1:
            ejercicio1()
            pass
        elif opcion == 2:
            ejercicio2()
            pass
        elif opcion == 3:
            ejercicio3()
            pass
        elif opcion == 4:
            ejercicio4()
            pass
        elif opcion == 5:
            ejercicio5()
            pass
        elif opcion == 6:
            ejercicio6()
            pass
        elif opcion == 7:
            ejercicio7()
            pass
        elif opcion == 8:
            ejercicio8()
            pass
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menuPrincipal()