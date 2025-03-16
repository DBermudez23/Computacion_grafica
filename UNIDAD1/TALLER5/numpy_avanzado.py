"""
TALLER COMPUTACIÓN GRÁFICA
UNIDAD 1
NUMPY AVANZADO
ESTUDIANTE: DANIEL FELIPE BERMUDEZ F
CODIGO: 1055751031
"""

import numpy as np
from scipy import stats

# 1) Cree el siguiente vector A = [2, 3, 5, 1, 4, 79, 8, 6, 10]
def ejercicio1():
    print("\nEjercicio 1: Crear vector A")
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    print("Vector A:", A)

# 2) Cree un vector B que contenga los elementos desde el 11 hasta el 20
def ejercicio2():
    print("\nEjercicio 2: Crear vector B")
    B = np.array(range(11, 21))
    print("Vector B:", B)

# 3) Componer un vector C formado por los vectores A y B en la misma fila
def ejercicio3():
    print("\nEjercicio 3: Crear vector C")
    global C  # Declarar C como global para usarlo en otros ejercicios
    A = np.array([2, 3, 5, 1, 4, 79, 8, 6, 10])
    B = np.array(range(11, 21))
    C = np.concatenate((A, B))
    print("Vector C:", C)

# 4) Encuentre el valor mínimo en el vector C
def ejercicio4():
    print("\nEjercicio 4: Valor mínimo en el vector C")
    if 'C' not in globals():
        ejercicio3()  # Asegura que C esté definido
    min_val = np.min(C)
    print("Valor mínimo:", min_val)

# 5) Encuentre el valor máximo en el vector C
def ejercicio5():
    print("\nEjercicio 5: Valor máximo en el vector C")
    if 'C' not in globals():
        ejercicio3()
    max_val = np.max(C)
    print("Valor máximo:", max_val)

# 6) Encuentre la longitud en el vector C
def ejercicio6():
    print("\nEjercicio 6: Longitud del vector C")
    if 'C' not in globals():
        ejercicio3()
    length = len(C)
    print("Longitud:", length)

# 7) Encuentre el promedio de los elementos en el vector C usando suma y división
def ejercicio7():
    print("\nEjercicio 7: Promedio de C usando suma y división")
    if 'C' not in globals():
        ejercicio3()
    promedio = np.sum(C) / len(C)
    print("Promedio:", promedio)

# 8) Encuentre el promedio en el vector C usando la función propia de NumPy
def ejercicio8():
    print("\nEjercicio 8: Promedio de C usando np.mean")
    if 'C' not in globals():
        ejercicio3()
    promedio = np.mean(C)
    print("Promedio:", promedio)

# 9) Encuentre la media en el vector C usando la función propia de NumPy
def ejercicio9():
    print("\nEjercicio 9: Media de C usando np.mean")
    if 'C' not in globals():
        ejercicio3()
    media = np.mean(C)
    print("Media:", media)

# 10) Encuentre la suma en el vector C usando la función propia de NumPy
def ejercicio10():
    print("\nEjercicio 10: Suma de C usando np.sum")
    if 'C' not in globals():
        ejercicio3()
    suma = np.sum(C)
    print("Suma:", suma)

# 11) Cree un vector D a partir del vector C con los elementos mayores que 5
def ejercicio11():
    print("\nEjercicio 11: Vector D con elementos mayores que 5")
    if 'C' not in globals():
        ejercicio3()
    D = C[C > 5]
    print("Vector D:", D)

# 12) Cree un vector E a partir del vector C con los elementos mayores que 5 y menores que 15
def ejercicio12():
    print("\nEjercicio 12: Vector E con elementos mayores que 5 y menores que 15")
    if 'C' not in globals():
        ejercicio3()
    E = C[(C > 5) & (C < 15)]
    print("Vector E:", E)

# 13) Cambie los elementos 5 y 15 elemento del vector C por 7
def ejercicio13():
    print("\nEjercicio 13: Cambiar elementos 5 y 15 de C por 7")
    if 'C' not in globals():
        ejercicio3()
    C[4] = 7  # 5to elemento (índice 4)
    C[14] = 7  # 15to elemento (índice 14)
    print("Vector C modificado:", C)

# 14) Determine la moda del vector C
def ejercicio14():
    print("\nEjercicio 14: Moda del vector C")
    if 'C' not in globals():
        ejercicio3()
    moda = stats.mode(C)[0][0]  # Usamos scipy.stats.mode para calcular la moda
    print("Moda:", moda)

# 15) Ordene el vector C de menor a mayor
def ejercicio15():
    print("\nEjercicio 15: Ordenar vector C de menor a mayor")
    if 'C' not in globals():
        ejercicio3()
    C_ordenado = np.sort(C)
    print("Vector C ordenado:", C_ordenado)

# 16) Multiplique el vector C por 10
def ejercicio16():
    print("\nEjercicio 16: Multiplicar vector C por 10")
    if 'C' not in globals():
        ejercicio3()
    C_multiplicado = C * 10
    print("Vector C multiplicado por 10:", C_multiplicado)

# 17) Cambie los elementos del 6 al 8 de la matriz C por 60, 70 y 80
def ejercicio17():
    print("\nEjercicio 17: Cambiar elementos 6 al 8 de C por 60, 70 y 80")
    if 'C' not in globals():
        ejercicio3()
    C[5] = 60  # 6to elemento
    C[6] = 70  # 7mo elemento
    C[7] = 80  # 8vo elemento
    print("Vector C modificado:", C)

# 18) Cambie los elementos del 14 al 16 de la matriz C por 140, 150 y 160
def ejercicio18():
    print("\nEjercicio 18: Cambiar elementos 14 al 16 de C por 140, 150 y 160")
    if 'C' not in globals():
        ejercicio3()
    C[13] = 140  # 14to elemento
    C[14] = 150  # 15to elemento
    C[15] = 160  # 16to elemento
    print("Vector C modificado:", C)

# Menú principal
def menuPrincipal():
    while True:
        print("\n=== Menú Principal - Taller de Manipulación Avanzada de Arrays ===")
        print("1. Crear vector A")
        print("2. Crear vector B")
        print("3. Crear vector C")
        print("4. Encontrar valor mínimo en C")
        print("5. Encontrar valor máximo en C")
        print("6. Encontrar longitud de C")
        print("7. Promedio de C (suma y división)")
        print("8. Promedio de C (np.mean)")
        print("9. Media de C (np.mean)")
        print("10. Suma de C (np.sum)")
        print("11. Crear vector D (mayores que 5)")
        print("12. Crear vector E (mayores que 5 y menores que 15)")
        print("13. Cambiar elementos 5 y 15 de C por 7")
        print("14. Determinar la moda de C")
        print("15. Ordenar vector C")
        print("16. Multiplicar C por 10")
        print("17. Cambiar elementos 6 al 8 de C por 60, 70, 80")
        print("18. Cambiar elementos 14 al 16 de C por 140, 150, 160")
        print("0. Salir")

        opcion = int(input("Ingrese una opción (0 - 18): "))

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
        elif opcion == 11:
            ejercicio11()
        elif opcion == 12:
            ejercicio12()
        elif opcion == 13:
            ejercicio13()
        elif opcion == 14:
            ejercicio14()
        elif opcion == 15:
            ejercicio15()
        elif opcion == 16:
            ejercicio16()
        elif opcion == 17:
            ejercicio17()
        elif opcion == 18:
            ejercicio18()
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menuPrincipal()