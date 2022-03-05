"""
Realiza un programa que lea un número impar por teclado. 
Si el usuario no introduce un número impar el proceso debe repetirse hasta que lo introduzca correctamente.
"""

def solicitarNumeroImpar():
    datoIncorrecto = True
    while (datoIncorrecto):
        try:
            numero = float(input( "Introduce un numero impar:"))
            if( (numero % 2) != 0):
                datoIncorrecto = False
                print("Dato correcto, has terminado!")
        
        except ValueError:
            datoIncorrecto = True


solicitarNumeroImpar()