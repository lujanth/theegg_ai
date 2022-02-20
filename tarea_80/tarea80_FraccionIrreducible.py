
#%%
""" 
Funcion que comprueba si el dato introducido es un número 
y está dentro del rango permitido 0.0001 - 0.9999
    Parametro de entrada: numerador
    Parametros de salida: Mensaje, vbleComprobarNumero(booleana)
"""
def comprorbarNumero( numero):
    vbleComprobarNumero = True
    mensajeComprobarNumero = ""

    if (numero<0.0001 or numero>0.9999):
        vbleComprobarNumero = False
        mensajeComprobarNumero="El número indicado no es correcto, introduzca un valor comprendido entre 0.0001 y 0.9999"
    
    return vbleComprobarNumero, mensajeComprobarNumero

"""
Funcion que va comprobando si numerador y denominador son divisibles.
Saca mensaje por pantalla indicando las fracciones intermedias.
Cuando detecta que ya no son divisibles, marca a true la vlble que controla el fin del bucle
    Parametros de entrada: numeradorCalc, denominadorCalc
    Parametro de salida: True, False
"""

def buscarFraccionIrreducible(numeradorCalc, denominadorCalc):
    esFraccionIrreducible = False
    while not esFraccionIrreducible:
        if ( (numeradorCalc % 2 == 0) and (denominadorCalc % 2 == 0)):
            numeradorCalc = numeradorCalc/2
            denominadorCalc = denominadorCalc/2
            print('Fracción intermedia: ' + str(int(numeradorCalc)) + '/' + str(int(denominadorCalc)))
        elif ( (numeradorCalc % 5 == 0) and (denominadorCalc % 5 == 0)):
            numeradorCalc = numeradorCalc/5
            denominadorCalc = denominadorCalc/5
            print('Fracción intermedia: ' + str(int(numeradorCalc)) + '/' + str(int(denominadorCalc)))
        else:
            esFraccionIrreducible = True
    return int(numeradorCalc), int(denominadorCalc)
            

"""
Funcion principal que calcula la fraccion irreducible del numero indicado e indica al usuario su fraccion irreducible
    Parametro de entrada: numero
"""

def calcularFraccionIrreducible():

    try:
        numero = float( input( "Indica un número comprendido entre 0.0001 y 0.9999: "))
        vbleComprobarNumero, mensajeComprobarNumero = comprorbarNumero(numero)
        if (vbleComprobarNumero):
            # Pasamos el numero a string y obtenemos su parte entera y decimal
            numeroEnForm = str(numero).split(".");
            # metemos en una variable, la parte entera del numero del form y en otra la parte decimal
            parteEntera = numeroEnForm[0];
            parteDecimal = numeroEnForm[1];
            
            # Pasamos a numero la parte decimal, que será el numerador inicial de la fraccion
            numerador=int(parteDecimal);
            
            # Calculamos el denominador de la fraccion en base a la longitud de la parte decimal
            longitudDenominador = len(parteDecimal);
            # Damos al demonimador el valor correspondiente
            if longitudDenominador == 1:
                denominador = 10
            elif longitudDenominador == 2:
                denominador = 100
            elif longitudDenominador == 3:
                denominador = 1000
            # damos por hecho que si no se trata de los casos anteriores es de long=4, porque hemos hecho la comprobacion previa del numero
            else: 
                denominador = 10000

            #Llamamos a la funcion que buscara la fraccion irreducible
            numeradorFrac, denominadorFrac = buscarFraccionIrreducible(numerador, denominador)
            print('La fraccion IRREDUCIBLE calculada para ' + str(numero) + ' es: ' + str(numeradorFrac) + '/' + str(denominadorFrac))
            
        else:
            print(mensajeComprobarNumero)

            
    except ValueError:
        print("Debes introducir un dato numérico comprendido entre 0.0001 y 0.9999")


calcularFraccionIrreducible()

