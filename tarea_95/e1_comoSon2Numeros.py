"""
Realiza un programa que lea 2 números por teclado y determine:
    Si los dos números son iguales
    Si los dos números son diferentes
    Si el primero es mayor que el segundo
    Si el segundo es mayor o igual que el primero
"""

def comoSon2Numeros():
    try:
        num1 = float( input( "Introduce el primer número:"))
        num2 = float( input( "Introduce el segundo número:"))

        if ( num1 == num2):
            print( "Los números introducidos son iguales")
        else:
            print( "Los números introducidos son distintos")
            if (num1 < num2):
                print( "El primer numero (", num1, ") es menor que el segundo (", num2, ")")
            else:
                print( "El primer numero (", num1, ") es mayor que el segundo (", num2, ")")
        
    except ValueError:
            print("Debes introducir un dato numérico")           

comoSon2Numeros()

