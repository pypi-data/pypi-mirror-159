import numpy as np 

def Saludar():
    print("Hola, te saludo desde la funcion Saludar() desde el mudulo saludos.py")

def prueba():
    print("Esto es una nueva prueba de la nueva versión 0.6")

def generar_array(numeros):
    return np.arange(numeros)

class Saludo():
    def __init__(self):
        print("Hola, te saludo desde '__init__' de la clase Saludo de saludos.py")

if __name__ == '__main__':
    print(generar_array(5))