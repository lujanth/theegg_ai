"""
Determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual a 5 y a su vez es menor que 10.
"""

def longitudDeUnTexto():
    try:
        texto = input( "Introduce un texto. Cualquier dato numérico será considerado texto")
        longitud = len( texto)
        if( longitud >= 5 and longitud < 10):
            print( "El texto introducido cumple las condiciones, su longitud está entre 5 y 10 caracteres")
        else:
            print( "El texto introducido no cumple las condiciones indicadas")
    except:
        print( "Se ha producido un error")

longitudDeUnTexto()