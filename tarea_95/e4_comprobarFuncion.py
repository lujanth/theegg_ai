"""
El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. 
¿Eres capaz de identificar el problema y solucionarlo?
"""

def funcionDada():
    numero_1 = 9
    numero_2 = 3
    numero_3 = 6

    media = numero_1 + numero_2 + numero_3 / 3
    print( "La nota media es ", media)


def funcionCorregida():
    numero_1 = 9
    numero_2 = 3
    numero_3 = 6

    # Correcion => Debemos englobar la suma entre parentesis, para calcular la media
    # Esto es debido a las prioridades de los operadores
    media = ( numero_1 + numero_2 + numero_3) / 3
    print( "La nota media es ", media)

#funcionDada()
funcionCorregida()