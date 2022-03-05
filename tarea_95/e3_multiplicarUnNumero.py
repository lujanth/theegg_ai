"""
Realiza un programa que haga la tabla de multiplicación de un número introducido de valor entre 0 y 99:
    Guarda en una variable el número introducido por el usuario
    Añade un filtro que asegure que el número sea entre 0 y 99
    Escribe la tabla multiplicando el valor introducido por valores entre 1 y 10
"""
def multiplicarUnNumero():
    try:
        numero = float( input ("Introduce un valor numérico entre 0 y 99"))
        if (numero >= 0 and numero <= 99):
            for i in range(1,10):
                print (str(numero), ' * ', str(i), ' = ', str(numero*i))
        else:
            print( "El numero debe ser un valor entre 0 y 99 ambos incluidos")

    except ValueError:
        print( "Debes introducir un dato numérico") 

multiplicarUnNumero()