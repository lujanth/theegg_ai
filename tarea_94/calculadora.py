
## Funcion de SUMA de 2 números
def suma2( num1, num2):
    return( num1 + num2 )

## Funcion de RESTA de 2 números
def resta2( num1, num2):
    return( num1 - num2 )

## Funcion de MULTIPLICACION de 2 números
def multiplica2( num1, num2):
    return( num1 * num2 )
    
## Funcion de DIVISION de 2 números    
def divide2( num1, num2):
    try:
        return( num1 / num2 )
    
    except ZeroDivisionError:
        print("División por cero")
        



