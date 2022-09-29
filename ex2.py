#Ejercicio de arreglos desde 1 hasta n desde consola, teniendo ese arreglo vamos a saber cuáles números son primos
from pickle import TRUE
def practica1():
  print("Introduce valor")
  X = int(input())
  lst = list(range(1, X+1))
  print("Lista de números generada:")
  print(lst)
  def f(n):
    return all([not n%x==0 for x in range (2,n)])
  for i in range(1,X+1):
    i,f(i)
    primos = []
    for lNum in range(1, X+1):
        if (f(lNum)):
          primos.append(lNum)
  print("Lista de números primos:")
  print(primos)

practica1()