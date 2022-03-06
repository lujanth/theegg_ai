import calculadora as calc

def calculos():
    try:
        num1 = float( input( "Indica el primer numero: "))
        num2 = float( input( "Indica el segundo numero: "))

        print ("El resultado de la suma es: ", calc.suma2( num1, num2 ))
        print ("El resultado de la resta es: ", calc.resta2( num1, num2 ))
        print ("El resultado de la multiplicación es: ", calc.multiplica2( num1, num2 ))
        division = calc.divide2( num1, num2 )
        if (division !=None):
            print ("El resultado de la división es: ", division)
        

    except ValueError:
            print("Debes introducir un dato numérico")           

calculos()

