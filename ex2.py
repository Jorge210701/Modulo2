#Ejercicio de arreglos desde 1 hasta n desde consola, teniendo ese arreglo vamos a saber cuáles números son primos
import sys
import numpy as np
def arreglo_1(sys.argv[1]):
    print("Introduce tu numero")
    x = int(input())
    y = np.arange(1,x+1)
    print(y)
    return