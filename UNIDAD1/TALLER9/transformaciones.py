"""
TALLER COMPUTACIÓN GRÁFICA
UNIDAD 1
TRANSFORMACIONES (IMAGENES)
ESTUDIANTE: DANIEL FELIPE BERMUDEZ F
CODIGO: 1055751031
"""

import numpy as np
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# 1) Ajustar el brillo de una imagen según un factor
def ejercicio1():
    print("\nEjercicio 1: Ajustar el brillo de una imagen")
    img_path = input("Ingrese la ruta de la imagen: ")
    factor = float(input("Ingrese el factor de ajuste de brillo (0-2, 1 es sin cambio): "))
    img = Image.open(img_path).convert('RGB')
    enhancer = ImageEnhance.Brightness(img)
    adjusted_img = enhancer.enhance(factor)
    plt.imshow(adjusted_img)
    plt.title(f'Imagen con Brillo Ajustado (Factor: {factor})')
    plt.show()

# 2) Ajustar el brillo de un canal específico según un factor
def ejercicio2():
    print("\nEjercicio 2: Ajustar el brillo de un canal específico")
    img_path = input("Ingrese la ruta de la imagen: ")
    canal = input("Ingrese el canal (R, G, B): ").upper()
    factor = float(input("Ingrese el factor de ajuste de brillo (0-2, 1 es sin cambio): "))
    img = Image.open(img_path).convert('RGB')
    img_array = np.array(img)
    if canal == 'R':
        img_array[:, :, 0] = np.clip(img_array[:, :, 0] * factor, 0, 255)
    elif canal == 'G':
        img_array[:, :, 1] = np.clip(img_array[:, :, 1] * factor, 0, 255)
    elif canal == 'B':
        img_array[:, :, 2] = np.clip(img_array[:, :, 2] * factor, 0, 255)
    else:
        print("Canal no válido. Use R, G o B.")
        return
    adjusted_img = Image.fromarray(img_array.astype(np.uint8))
    plt.imshow(adjusted_img)
    plt.title(f'Imagen con Brillo Ajustado en {canal} (Factor: {factor})')
    plt.show()

# 3) Ajustar el contraste de una imagen según un factor
def ejercicio3():
    print("\nEjercicio 3: Ajustar el contraste de una imagen")
    img_path = input("Ingrese la ruta de la imagen: ")
    factor = float(input("Ingrese el factor de contraste (0-2, 1 es sin cambio): "))
    img = Image.open(img_path).convert('RGB')
    enhancer = ImageEnhance.Contrast(img)
    adjusted_img = enhancer.enhance(factor)
    plt.imshow(adjusted_img)
    plt.title(f'Imagen con Contraste Ajustado (Factor: {factor})')
    plt.show()

# 4) Realizar zoom a una parte de la imagen
def ejercicio4():
    print("\nEjercicio 4: Realizar zoom a una parte de la imagen")
    img_path = input("Ingrese la ruta de la imagen: ")
    img = Image.open(img_path).convert('RGB')
    x, y = map(int, input("Ingrese las coordenadas (x, y) del centro del zoom: ").split())
    w, h = map(int, input("Ingrese el ancho y alto del área de zoom (w, h): ").split())
    cropped_img = img.crop((x - w//2, y - h//2, x + w//2, y + h//2))
    zoomed_img = cropped_img.resize((300, 300), Image.Resampling.BICUBIC)
    plt.imshow(zoomed_img)
    plt.title('Imagen con Zoom')
    plt.show()

# 5) Binarizar una imagen
def ejercicio5():
    print("\nEjercicio 5: Binarizar una imagen")
    img_path = input("Ingrese la ruta de la imagen: ")
    img = Image.open(img_path).convert('L')  # Convertir a escala de grises
    img_array = np.array(img)
    threshold = 128  # Umbral típico
    binary_img = (img_array > threshold).astype(np.uint8) * 255
    plt.imshow(binary_img, cmap='gray')
    plt.title('Imagen Binarizada')
    plt.show()

# 6) Rotar una imagen
def ejercicio6():
    print("\nEjercicio 6: Rotar una imagen")
    img_path = input("Ingrese la ruta de la imagen: ")
    angle = float(input("Ingrese el ángulo de rotación (en grados): "))
    img = Image.open(img_path).convert('RGB')
    rotated_img = img.rotate(angle, expand=True)
    plt.imshow(rotated_img)
    plt.title(f'Imagen Rotada {angle}°')
    plt.show()

# 7) Sacar el histograma de cada capa de una imagen
def ejercicio7():
    print("\nEjercicio 7: Histograma de cada capa de una imagen")
    img_path = input("Ingrese la ruta de la imagen: ")
    img = Image.open(img_path).convert('RGB')
    img_array = np.array(img)
    colors = ['red', 'green', 'blue']
    plt.figure(figsize=(10, 6))
    for i, color in enumerate(colors):
        hist, bins = np.histogram(img_array[:, :, i], bins=256, range=(0, 256))
        plt.plot(bins[:-1], hist, color=color, label=f'Capa {color}')
    plt.title('Histogramas de las Capas RGB')
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.grid(True)
    plt.show()

# Menú principal
def menuPrincipal():
    while True:
        print("\n=== Menú Principal - Taller de Transformaciones ===")
        print("1. Ajustar el brillo de una imagen")
        print("2. Ajustar el brillo de un canal específico")
        print("3. Ajustar el contraste de una imagen")
        print("4. Realizar zoom a una parte de la imagen")
        print("5. Binarizar una imagen")
        print("6. Rotar una imagen")
        print("7. Sacar el histograma de cada capa")
        print("0. Salir")

        opcion = int(input("Ingrese una opción (0 - 7): "))

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
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menuPrincipal()