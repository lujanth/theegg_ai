
"""
Realiza un programa que sume todos los números enteros impares desde el 0 hasta el 115.
"""

def sumaEnterosImpares_0_115():
    suma=0
    for i in range(1,116,2):
        suma += i
   
    print('Resultado de la suma = ', suma)

sumaEnterosImpares_0_115()