# Este es un modulo con funcions que saludan
import numpy as np # Esto es un modulo externo, es una dependencia que tendrá nuestro paquete

def Saludar():
    print("Hola, te saludo desde la funcion Saludar() desde el mudulo saludos.py")

# Función que usa un modulo externo
def generar_array(numeros):
    # Hacer antes un: pip install numpy
    return np.arange(numeros)

class Saludo():
    def __init__(self):
        print("Hola, te saludo desde '__init__' de la clase Saludo de saludos.py")

if __name__ == '__main__':
    print(generar_array(5))