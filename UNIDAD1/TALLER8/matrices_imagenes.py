"""
TALLER COMPUTACIÓN GRÁFICA
UNIDAD 1
MATRICES Y MANEJO DE IMAGENES
ESTUDIANTE: DANIEL FELIPE BERMUDEZ F
CODIGO: 1055751031
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 1) Diseñar una matriz
def ejercicio1():
    print("\nEjercicio 1: Diseñar una matriz")
    matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Matriz diseñada:\n", matriz)
    plt.imshow(matriz, cmap='gray')
    plt.title('Matriz como Imagen')
    plt.colorbar()
    plt.show()

# 2) Diseñar una imagen a través de una matriz
def ejercicio2():
    print("\nEjercicio 2: Diseñar una imagen a través de una matriz")
    # Ejemplo: Matriz 5x5 que simula una imagen en escala de grises
    imagen_matriz = np.array([
        [255, 0, 0, 0, 255],
        [0, 255, 0, 255, 0],
        [0, 0, 255, 0, 0],
        [255, 255, 0, 255, 255],
        [0, 255, 255, 0, 0]
    ], dtype=np.uint8)
    img = Image.fromarray(imagen_matriz)
    plt.imshow(img, cmap='gray')
    plt.title('Imagen Diseñada desde Matriz')
    plt.show()

# 3) Invertir los colores de una imagen
def ejercicio3():
    print("\nEjercicio 3: Invertir los colores de una imagen")
    img_path = input("Ingrese la ruta de la imagen: ")
    img = Image.open(img_path).convert('RGB')
    img_array = np.array(img)
    inverted_img = 255 - img_array
    img_inverted = Image.fromarray(inverted_img)
    plt.imshow(img_inverted)
    plt.title('Imagen con Colores Invertidos')
    plt.show()

# 5) Retornar la capa Verde de una imagen
def ejercicio5():
    print("\nEjercicio 5: Retornar la capa Verde")
    img_path = input("Ingrese la ruta de la imagen: ")
    img = Image.open(img_path).convert('RGB')
    img_array = np.array(img)
    green_layer = img_array[:, :, 1]  # Capa Verde (índice 1)
    plt.imshow(green_layer, cmap='gray')
    plt.title('Capa Verde')
    plt.show()

# 6) Retornar la capa Azul de una imagen
def ejercicio6():
    print("\nEjercicio 6: Retornar la capa Azul")
    img_path = input("Ingrese la ruta de la imagen: ")
    img = Image.open(img_path).convert('RGB')
    img_array = np.array(img)
    blue_layer = img_array[:, :, 2]  # Capa Azul (índice 2)
    plt.imshow(blue_layer, cmap='gray')
    plt.title('Capa Azul')
    plt.show()

# 7) Retornar la imagen en Magenta
def ejercicio7():
    print("\nEjercicio 7: Retornar imagen en Magenta")
    img_path = input("Ingrese la ruta de la imagen: ")
    img = Image.open(img_path).convert('RGB')
    img_array = np.array(img)
    magenta_img = np.zeros_like(img_array)
    magenta_img[:, :, 0] = img_array[:, :, 2]  # Rojo = Azul
    magenta_img[:, :, 2] = img_array[:, :, 0]  # Azul = Rojo
    plt.imshow(Image.fromarray(magenta_img.astype(np.uint8)))
    plt.title('Imagen en Magenta')
    plt.show()

# 8) Retornar la imagen en Cyan
def ejercicio8():
    print("\nEjercicio 8: Retornar imagen en Cyan")
    img_path = input("Ingrese la ruta de la imagen: ")
    img = Image.open(img_path).convert('RGB')
    img_array = np.array(img)
    cyan_img = np.zeros_like(img_array)
    cyan_img[:, :, 1] = img_array[:, :, 1]  # Verde = Verde
    cyan_img[:, :, 2] = img_array[:, :, 2]  # Azul = Azul
    plt.imshow(Image.fromarray(cyan_img.astype(np.uint8)))
    plt.title('Imagen en Cyan')
    plt.show()

# 9) Retornar la imagen en Amarillo
def ejercicio9():
    print("\nEjercicio 9: Retornar imagen en Amarillo")
    img_path = input("Ingrese la ruta de la imagen: ")
    img = Image.open(img_path).convert('RGB')
    img_array = np.array(img)
    yellow_img = np.zeros_like(img_array)
    yellow_img[:, :, 0] = img_array[:, :, 0]  # Rojo = Rojo
    yellow_img[:, :, 1] = img_array[:, :, 1]  # Verde = Verde
    plt.imshow(Image.fromarray(yellow_img.astype(np.uint8)))
    plt.title('Imagen en Amarillo')
    plt.show()

# 10) Reconstruir imagen con capas RGB separadas
def ejercicio10():
    print("\nEjercicio 10: Reconstruir imagen con capas RGB")
    img_path = input("Ingrese la ruta de la imagen: ")
    img = Image.open(img_path).convert('RGB')
    img_array = np.array(img)
    r_layer = img_array[:, :, 0]
    g_layer = img_array[:, :, 1]
    b_layer = img_array[:, :, 2]
    reconstructed = np.dstack((r_layer, g_layer, b_layer)).astype(np.uint8)
    plt.imshow(Image.fromarray(reconstructed))
    plt.title('Imagen Reconstruida')
    plt.show()

# 11) Fusión de dos imágenes sin ecualizar
def ejercicio11():
    print("\nEjercicio 11: Fusión de dos imágenes sin ecualizar")
    img1_path = input("Ingrese la ruta de la primera imagen: ")
    img2_path = input("Ingrese la ruta de la segunda imagen: ")
    img1 = Image.open(img1_path).convert('RGB')
    img2 = Image.open(img2_path).convert('RGB')
    img1_array = np.array(img1)
    img2_array = np.array(img2)
    fused_img = (img1_array + img2_array) // 2
    plt.imshow(Image.fromarray(fused_img.astype(np.uint8)))
    plt.title('Fusión sin Ecualizar')
    plt.show()

# 12) Fusión de dos imágenes ecualizadas
def ejercicio12():
    print("\nEjercicio 12: Fusión de dos imágenes ecualizadas")
    img1_path = input("Ingrese la ruta de la primera imagen: ")
    img2_path = input("Ingrese la ruta de la segunda imagen: ")
    img1 = Image.open(img1_path).convert('RGB')
    img2 = Image.open(img2_path).convert('RGB')
    img1_array = np.array(img1)
    img2_array = np.array(img2)
    # Ecualización simple (normalización a [0, 255])
    img1_eq = (img1_array - np.min(img1_array)) / (np.max(img1_array) - np.min(img1_array)) * 255
    img2_eq = (img2_array - np.min(img2_array)) / (np.max(img2_array) - np.min(img2_array)) * 255
    fused_img = (img1_eq + img2_eq) // 2
    plt.imshow(Image.fromarray(fused_img.astype(np.uint8)))
    plt.title('Fusión Ecualizada')
    plt.show()

# 13) Imagen ecualizada según un factor
def ejercicio13():
    print("\nEjercicio 13: Imagen ecualizada según un factor")
    img_path = input("Ingrese la ruta de la imagen: ")
    factor = float(input("Ingrese el factor de ecualización (0-1): "))
    img = Image.open(img_path).convert('RGB')
    img_array = np.array(img)
    eq_img = img_array * factor
    eq_img = np.clip(eq_img, 0, 255).astype(np.uint8)
    plt.imshow(Image.fromarray(eq_img))
    plt.title('Imagen Ecualizada')
    plt.show()

# 14) Imagen con Técnica de Promedio (Average)
def ejercicio14():
    print("\nEjercicio 14: Imagen con Técnica de Promedio")
    img_path = input("Ingrese la ruta de la imagen: ")
    img = Image.open(img_path).convert('RGB')
    img_array = np.array(img)
    avg_img = np.mean(img_array, axis=2).astype(np.uint8)
    avg_img_3d = np.stack([avg_img] * 3, axis=-1)
    plt.imshow(Image.fromarray(avg_img_3d))
    plt.title('Técnica de Promedio')
    plt.show()

# 15) Escala de grises con Técnica de Promedio
def ejercicio15():
    print("\nEjercicio 15: Escala de grises con Técnica de Promedio")
    img_path = input("Ingrese la ruta de la imagen: ")
    img = Image.open(img_path).convert('RGB')
    img_array = np.array(img)
    gray_img = np.mean(img_array, axis=2).astype(np.uint8)
    plt.imshow(gray_img, cmap='gray')
    plt.title('Escala de Grises - Promedio')
    plt.show()

# 16) Escala de grises con Técnica de Luminosidad
def ejercicio16():
    print("\nEjercicio 16: Escala de grises con Técnica de Luminosidad")
    img_path = input("Ingrese la ruta de la imagen: ")
    img = Image.open(img_path).convert('RGB')
    img_array = np.array(img)
    luminosity = 0.299 * img_array[:, :, 0] + 0.587 * img_array[:, :, 1] + 0.114 * img_array[:, :, 2]
    gray_img = luminosity.astype(np.uint8)
    plt.imshow(gray_img, cmap='gray')
    plt.title('Escala de Grises - Luminosidad')
    plt.show()

# 17) Escala de grises con Técnica de Tonalidad (Midgray)
def ejercicio17():
    print("\nEjercicio 17: Escala de grises con Técnica de Tonalidad (Midgray)")
    img_path = input("Ingrese la ruta de la imagen: ")
    img = Image.open(img_path).convert('RGB')
    img_array = np.array(img)
    midgray = (img_array[:, :, 0] + img_array[:, :, 1] + img_array[:, :, 2]) / 3 + 128
    gray_img = np.clip(midgray, 0, 255).astype(np.uint8)
    plt.imshow(gray_img, cmap='gray')
    plt.title('Escala de Grises - Tonalidad (Midgray)')
    plt.show()

# Menú principal
def menuPrincipal():
    while True:
        print("\n=== Menú Principal - Taller de Matrices y Procesamiento de Imágenes ===")
        print("1. Diseñar una matriz")
        print("2. Diseñar una imagen a través de una matriz")
        print("3. Invertir los colores de una imagen")
        print("5. Retornar la capa Verde")
        print("6. Retornar la capa Azul")
        print("7. Retornar imagen en Magenta")
        print("8. Retornar imagen en Cyan")
        print("9. Retornar imagen en Amarillo")
        print("10. Reconstruir imagen con capas RGB")
        print("11. Fusión de dos imágenes sin ecualizar")
        print("12. Fusión de dos imágenes ecualizadas")
        print("13. Imagen ecualizada según un factor")
        print("14. Imagen con Técnica de Promedio")
        print("15. Escala de grises con Técnica de Promedio")
        print("16. Escala de grises con Técnica de Luminosidad")
        print("17. Escala de grises con Técnica de Tonalidad (Midgray)")
        print("0. Salir")

        opcion = int(input("Ingrese una opción (0 - 17): "))

        if opcion == 0:
            print("¡Hasta luego!")
            break
        elif opcion == 1:
            ejercicio1()
        elif opcion == 2:
            ejercicio2()
        elif opcion == 3:
            ejercicio3()
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
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menuPrincipal()