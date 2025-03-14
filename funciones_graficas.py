import numpy as np
import matplotlib.pyplot as plt

# "Objetivo: Ajusta el brillo de una imagen"
def AjusteBrillo(Img, B):
    """
    Parámetros:
    Img: Imagen en formato numpy array
    B: Valor de ajuste de brillo
    
    Retorna:
    Imagen con brillo ajustado
    """
    # Ejemplo de uso:
    # ImgBrillo = AjusteBrillo(MiImagen, 0.5)
    
    return Img + B

# "Objetivo: Ajusta el brillo de un canal de una imagen"
def AjusteCanal(Img, capa):
    """
    Parámetros:
    Img: Imagen en formato numpy array
    capa: Canal a ajustar de brillo
    
    Retorna:
    Imagen con brillo ajustado en un canal
    """
    # Ejemplo de uso:
    # ImgCanal = AjusteCanal(MiImagen, 0.7, 0)
    ImgCanal = np.copy(Img)
    ImgCanal[:, :, capa] = Img[:, :, capa] + 0.7  # Ajuste de brillo en el canal especificado
    return ImgCanal

# "Objetivo: Ajusta el contraste de una imagen"
def AjusteContraste(Img, K, Tipo):
    """
    Parámetros:
    Img: Imagen en formato numpy array
    K: Valor de ajuste de contraste
    Tipo: Tipo de ajuste de contraste (0: Oscuro, 1: Claro)
    
    Retorna:
    Imagen con contraste ajustado
    """
    # Ejemplo de uso:
    # ImgContraste = AjusteContraste(MiImagen, 0.8, 0)
    if (Tipo == 0):  # Si es oscuro
        ImgContraste = K * np.log(1 + Img)
    else:  # Si es claro
        ImgContraste = K * np.exp(Img - 1)
    return ImgContraste

# "Objetivo: Extrae una capa de una imagen"
def CapImagen(Img, capa):
    """
    Parámetros:
    Img: Imagen en formato numpy array
    capa: Capa (canal) a extraer
    
    Retorna:
    Imagen con una capa extraída
    """
    # Ejemplo de uso:
    # ImgCapa = CapImagen(MiImagen, 0)
    Fila, Columna, Canal = Img.shape
    ImgCanal = np.zeros((Fila, Columna, 3))
    ImgCanal[:, :, capa] = Img[:, :, capa]
    return ImgCanal
