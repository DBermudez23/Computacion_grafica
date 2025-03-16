"""
TALLER COMPUTACIÓN GRÁFICA
UNIDAD 1
SERIES DE TAYLOR
ESTUDIANTE: DANIEL FELIPE BERMUDEZ F
CODIGO: 1055751031
"""

import numpy as np
import matplotlib.pyplot as plt

# Función para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Serie de Taylor para e^x
def taylor_exp(x, n_terms=10):
    result = 0
    for n in range(n_terms):
        result += (x ** n) / factorial(n)
    return result

# Serie de Taylor para sin(x)
def taylor_sin(x, n_terms=10):
    result = 0
    for n in range(n_terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        result += term
    return result

# Serie de Taylor para cos(x)
def taylor_cos(x, n_terms=10):
    result = 0
    for n in range(n_terms):
        term = ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
        result += term
    return result

# Serie de Taylor para ln(1+x), válida para |x| < 1
def taylor_ln(x, n_terms=10):
    if abs(x) >= 1:
        raise ValueError("ln(1+x) solo es válida para |x| < 1")
    result = 0
    for n in range(1, n_terms + 1):
        term = ((-1) ** (n + 1)) * (x ** n) / n
        result += term
    return result

# Serie de Taylor para tan^-1(x), válida para |x| < 1
def taylor_arctan(x, n_terms=10):
    if abs(x) > 1:
        raise ValueError("tan^-1(x) solo es válida para |x| <= 1")
    result = 0
    for n in range(n_terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
        result += term
    return result

# 1) Calcular e^x usando la Serie de Taylor
def ejercicio1():
    print("\nEjercicio 1: Aproximación de e^x usando Serie de Taylor")
    x = float(input("Ingrese un valor para x: "))
    approx = taylor_exp(x)
    real = np.exp