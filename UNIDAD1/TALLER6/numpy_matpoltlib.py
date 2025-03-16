"""
TALLER COMPUTACIÓN GRÁFICA
UNIDAD 1
ANALISIS NÚMERICO Y VISUALIZACIÓN CON MATPLOTLIB
ESTUDIANTE: DANIEL FELIPE BERMUDEZ F
CODIGO: 1055751031
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1) Creación y Manipulación de Arrays
def ejercicio1():
    print("\nEjercicio 1: Creación y Manipulación de Arrays")
    global A  # Declarar A como global para usarlo en otros ejercicios
    A = np.array(range(1, 16))
    A = A.reshape(3, 5)
    print("Matriz A (3x5):\n", A)

# 2) Operaciones Básicas
def ejercicio2():
    print("\nEjercicio 2: Operaciones Básicas")
    if 'A' not in globals():
        ejercicio1()
    suma = np.sum(A)
    media = np.mean(A)
    producto = np.prod(A)
    print("Suma:", suma)
    print("Media:", media)
    print("Producto:", producto)

# 3) Acceso y Slicing
def ejercicio3():
    print("\nEjercicio 3: Acceso y Slicing")
    if 'A' not in globals():
        ejercicio1()
    elementos = A[1, 1:3]  # Segundo y tercer elemento de la segunda fila (índices 1 y 2)
    print("Segundo y tercer elemento de la segunda fila:", elementos)

# 4) Indexación Booleana
def ejercicio4():
    print("\nEjercicio 4: Indexación Booleana")
    if 'A' not in globals():
        ejercicio1()
    global B  # Declarar B como global
    B = A[A > 7]
    print("Array B (elementos mayores que 7):", B)

# 5) Álgebra Lineal
def ejercicio5():
    print("\nEjercicio 5: Álgebra Lineal")
    C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Matriz cuadrada 3x3
    determinante = np.linalg.det(C)
    inversa = np.linalg.inv(C)
    print("Matriz C:\n", C)
    print("Determinante:", determinante)
    print("Inversa:\n", inversa)

# 6) Estadísticas con NumPy
def ejercicio6():
    print("\nEjercicio 6: Estadísticas con NumPy")
    global D  # Declarar D como global
    D = np.random.random(100) * 100  # 100 números aleatorios entre 0 y 100
    max_val = np.max(D)
    min_val = np.min(D)
    media = np.mean(D)
    std_dev = np.std(D)
    print("Array D (100 números aleatorios):", D)
    print("Máximo:", max_val)
    print("Mínimo:", min_val)
    print("Media:", media)
    print("Desviación estándar:", std_dev)

# 7) Gráfico Básico
def ejercicio7():
    print("\nEjercicio 7: Gráfico Básico")
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    seno = np.sin(x)
    coseno = np.cos(x)
    plt.figure()
    plt.plot(x, seno, label='Seno')
    plt.plot(x, coseno, label='Coseno')
    plt.title('Seno y Coseno')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

# 8) Gráficos de Dispersión
def ejercicio8():
    print("\nEjercicio 8: Gráficos de Dispersión")
    if 'D' not in globals():
        ejercicio6()
    indices = np.arange(len(D))
    plt.figure()
    plt.scatter(indices, D, color='blue', alpha=0.5)
    plt.title('Gráfico de Dispersión de D')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.grid(True)
    plt.show()

# 9) Histogramas
def ejercicio9():
    print("\nEjercicio 9: Histogramas")
    if 'D' not in globals():
        ejercicio6()
    plt.figure()
    plt.hist(D, bins=10, edgecolor='black')
    plt.title('Histograma de D')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()

# 10) Manipulación de Imágenes
def ejercicio10():
    print("\nEjercicio 10: Manipulación de Imágenes")
    # Usar una imagen de ejemplo (asegúrate de tener una imagen llamada 'imagen.jpg' en el directorio)
    imagen = Image.open('imagen.jpg')  # Reemplaza 'imagen.jpg' con el nombre de tu imagen
    imagen_gris = imagen.convert('L')
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(imagen)
    plt.title('Imagen Original')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(imagen_gris, cmap='gray')
    plt.title('Imagen en Escala de Grises')
    plt.axis('off')
    plt.show()

# Menú principal
def menuPrincipal():
    while True:
        print("\n=== Menú Principal - Taller de Análisis Numérico y Visualización ===")
        print("1. Creación y Manipulación de Arrays")
        print("2. Operaciones Básicas")
        print("3. Acceso y Slicing")
        print("4. Indexación Booleana")
        print("5. Álgebra Lineal")
        print("6. Estadísticas con NumPy")
        print("7. Gráfico Básico")
        print("8. Gráficos de Dispersión")
        print("9. Histogramas")
        print("10. Manipulación de Imágenes")
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