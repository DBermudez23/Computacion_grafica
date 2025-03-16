"""
TALLER COMPUTACIÓN GRÁFICA
UNIDAD 1
SUBRUTINAS, ESTRUCTURAS DE CONTROL, ARREGLOS Y LISTAS
ESTUDIANTE: DANIEL FELIPE BERMUDEZ F
CODIGO: 1055751031
"""

"""
Crea una función para cada operación básica (suma, resta,
multiplicación, división) que acepte dos argumentos y devuelva el resultado.
Implementa una función principal que solicite al usuario números y la operación a
realizar, utilizando las funciones creadas.
"""

import math

class Calculadora:
    """
    Clase que implementa una calculadora con operaciones básicas.
    Incluye suma, resta, multiplicación, división, potencia y raíz cuadrada.
    """
    
    def __init__(self):
        pass

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b


    
    def menuCalculadora(self):
        print("\n=== Calculadora Básica ===")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione una operación (1-5): ").strip()

        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))

                if opcion == "1":
                    resultado = self.suma(num1, num2)
                    print(f"Resultado de la suma: {resultado}")
                elif opcion == "2":
                    resultado = self.resta(num1, num2)
                    print(f"Resultado de la resta: {resultado}")
                elif opcion == "3":
                    resultado = self.multiplicacion(num1, num2)
                    print(f"Resultado de la multiplicación: {resultado}")
                elif opcion == "4":
                    if num2 == 0:
                        print("Error: No se puede dividir por cero")
                    else:
                        resultado = self.division(num1, num2)
                        print(f"Resultado de la división: {resultado}")
            except ValueError:
                print("Error: Por favor ingrese números válidos")
        elif opcion == "5":
            print("Regresando al Menú Principal...")
            menuMain()
        else:
            print("Opción inválida. Por favor seleccione una opción entre 1 y 5.")
    

"""
Desarrolla una función que reciba una lista de números y devuelva 
solo aquellos que sean pares. Utiliza un bucle y condicionales dentro de la función. 
"""

def convertirALista(string):
    lista = string.split(",")
    listaInt = []
    for i in lista:
        listaInt.append(int(i))
    return listaInt


def numerosPares(lista):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            pass
    return "Los números pares son: {pares}"


"""
Escribe un script que utilice map y una 
función lambda para convertir todas las temperaturas de una lista de grados Celsius 
a Fahrenheit. La fórmula de conversión es: F = (9/5) * C + 32.
"""

def celsiusToFahrenheit(lista):
    fahrenheit = list(map(lambda c: (9/5) * c + 32, lista))
    return "los grados de la lista {lista} en fahreheit son: {fahrenheit}"


"""
Implementa  una  función  que  reciba  una  lista  de 
calificaciones numéricas y devuelva una lista con las calificaciones convertidas a 
letras (A, B, C, D, F) según el rango en el que se encuentren.
"""

def calificacionesLetras(lista):
    if len(lista) == 0:
        return "No hay calificaciones para evaluar."
    else:
        calificaciones = []
        for i in lista:
            if i >= 4.0:
                calificaciones.append("A")
            elif i >= 3.0:
                calificaciones.append("B")
            elif i >= 2.0:
                calificaciones.append("C")
            elif i >= 1.0:
                calificaciones.append("D")
            else:
                calificaciones.append("F")
        return "Las calificaciones {lista} en letras es: {calificaciones}" 


"""
Crea una función que reciba una cadena de texto y retorne un 
diccionario con el conteo de cuántas veces aparece cada palabra. Considera ignorar 
mayúsculas y signos de puntuación. 
"""
import re #Trabajaremos con expresiones regulares para optimización

def conteoPalabras(texto):
    textoMinusculas = texto.lower()
    palabras = re.split(r'\W+', textoMinusculas) #'\W+' expresión regular que eliminara cualquier caracter que no sea alfanumérico
    frecuencia = {}
    for palabra in palabras:
        if palabra not in frecuencia:
            frecuencia[palabra] = 1
        else:
            frecuencia[palabra] += 1
    return "La frecuencia de cada palabra en el texto: {frecuencia} "


"""
Desarrolla una función que busque un elemento dado dentro 
de una lista y devuelva su índice si lo encuentra o -1 si no está presente. No utilices 
métodos predefinidos como .index(). Desarrolla una función que busque un elemento dado dentro 
de una lista y devuelva su índice si lo encuentra o -1 si no está presente. No utilices 
métodos predefinidos como .index(). 
"""

def busquedaElemento(lista, elemento):
    for i in range(len(lista)): #Recorremos la lista
        if lista[i] == elemento:
            return i
    return -1   


"""
Escribe  una  función  que  tome  una  cadena  de  solo 
paréntesis ( y ) y determine si la secuencia es válida (cada paréntesis abierto tiene un 
correspondiente paréntesis cerrado). 
"""

def secuenciaValida(secuencia):
    pila = []
    for i in secuencia:
        if i == "(":
            pila.append(i)
        elif i == ")":
            if len(pila) == 0:
                return False #En caso de que se cierre un paréntesis sin haber abierto uno
            pila.pop()
    return len(pila) == 0


"""
Implementa una función que ordene una lista de 
tuplas (nombre, edad) primero por edad y luego por nombre (ambos en orden 
ascendente). Puedes usar la función sort o sorted con parámetros personalizados.
"""

def ordenarTuplas(lista):
    return sorted(lista, key = lambda x: (x[1], x[0])) #Ordenamos primero por edad y luego por nombre


#lista_tuplas = [("Ana", 25), ("Juan", 22), ("Pedro", 25), ("Lucía", 22)]
#lista_ordenada = ordenarTuplas(lista_tuplas)

#print(lista_ordenada)


"""
Crea una función que genere una contraseña aleatoria 
que consista en una combinación de letras mayúsculas, minúsculas, números y 
símbolos. La longitud de la contraseña debe ser un parámetro de la función.
"""

import random
import string

def contraseñaAleatoria(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation #Caracteres posibles
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return "La contraseña generada aleatoriamente es: {contraseña}"

#print(contraseñaAleatoria(10)) 


"""
Desarrolla un programa que utilice funciones para 
permitir al usuario agregar, buscar, eliminar y mostrar todos los contactos de una 
agenda telefónica almacenada en un diccionario. 
"""

class AgendaTelefonica:
    def __init__(self):
        """Inicializa la agenda con un diccionario vacío"""
        self.contactos = {}

    def agregar_contacto(self):
        """Método para agregar un nuevo contacto a la agenda"""
        nombre = input("Ingrese el nombre del contacto: ").strip()
        if nombre in self.contactos:
            print("¡Este contacto ya existe!")
            return
        
        telefono = input("Ingrese el número de teléfono: ").strip()
        self.contactos[nombre] = telefono
        print(f"Contacto '{nombre}' agregado exitosamente!")

    def buscar_contacto(self):
        """Método para buscar un contacto en la agenda"""
        nombre = input("Ingrese el nombre del contacto a buscar: ").strip()
        if nombre in self.contactos:
            print(f"Nombre: {nombre} - Teléfono: {self.contactos[nombre]}")
        else:
            print("Contacto no encontrado!")

    def eliminar_contacto(self):
        """Método para eliminar un contacto de la agenda"""
        nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"Contacto '{nombre}' eliminado exitosamente!")
        else:
            print("Contacto no encontrado!")

    def mostrar_todos(self):
        """Método para mostrar todos los contactos de la agenda"""
        if not self.contactos:
            print("La agenda está vacía!")
        else:
            print("\n=== Lista de Contactos ===")
            for nombre, telefono in self.contactos.items():
                print(f"Nombre: {nombre} - Teléfono: {telefono}")
            print("======================")

    def menu(self):
        """Método principal que muestra el menú y maneja las opciones"""
        while True:
            print("\n=== Agenda Telefónica ===")
            print("1. Agregar contacto")
            print("2. Buscar contacto")
            print("3. Eliminar contacto")
            print("4. Mostrar todos los contactos")
            print("5. Salir")
            
            opcion = input("Seleccione una opción (1-5): ").strip()
            
            if opcion == "1":
                self.agregar_contacto()
                pass
            elif opcion == "2":
                self.buscar_contacto()
                pass
            elif opcion == "3":
                self.eliminar_contacto()
                pass
            elif opcion == "4":
                self.mostrar_todos()
                pass
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción entre 1 y 5.")
                


def menuMain():
    calculadora = Calculadora()
    agenda = AgendaTelefonica()
    """Función principal que muestra el menú y maneja las opciones"""
    while True:
        print("\n=== Menú Interactivo ===")
        print("1. Operaciones Básicas (Calculadora)")
        print("2. Filtrado de Lista por Números Pares")
        print("3. Conversión de Temperaturas de Celsius a Fahrenheit")
        print("4. Sistema de Calificaciones a Letras")
        print("5. Conteo de Palabras en una Cadena")
        print("6. Búsqueda de Elemento en Lista")
        print("7. Validación de Secuencia de Paréntesis")
        print("8. Ordenamiento Personalizado de Lista de Tuplas")
        print("9. Generador de Contraseñas Aleatorias")
        print("10. Gestión de Agenda Telefónica")
        print("11. Salir del Programa")

        opcion = input("Seleccione una opción (1-11): ").strip()

        if opcion == "1":
            calculadora()
            pass
        elif opcion == "2":
            lista = input("Ingrese la lista de numeros separados por una (,)")
            listaEnteros = convertirALista(lista)
            numerosPares(listaEnteros)
            pass
        elif opcion == "3":
            listaCelcius = input("Ingrese la lista de valores de grados celcius separados por (,)")
            listaCelInt = convertirALista(listaCelcius)
            celsiusToFahrenheit(listaCelInt)
            pass
        elif opcion == "4":
            notas = input("Ingrese calificaciones (0.0 - 5.0) para la lista separados por (,) :")
            notasInt = convertirALista(notas)
            calificacionesLetras(notasInt)
            pass
        elif opcion == "5":
            frase = input("Ingrese la frase para conocer la frecuencia de las palabras")
            conteoPalabras(frase)
            pass
        elif opcion == "6":
            lista = input("Ingrese los elementos de la lista separados por(,)")
            lista = list(lista) 
            pass
        elif opcion == "7":
            secuencia = input("Ingrese un texto para comprobar que se cierran todos los parentesis: ")
            secuenciaValida(secuencia)
            pass
        elif opcion == "8":
            lista_tuplas = eval(input("Ingrese una lista de tuplas (nombre, edad) separadas por comas, ej: [('Ana', 25), ('Juan', 22)]: "))
            listaOrdenada = ordenarTuplas(lista_tuplas)
            print("La lista ordenada: ", listaOrdenada)
            pass
        elif opcion == "9":
            contraseñaAleatoria()
            pass
        elif opcion == "10":
            agenda.menu()
        elif opcion == "11":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción entre 1 y 11.")

# Iniciar el programa
if __name__ == "__main__":
    menuMain()
   
    