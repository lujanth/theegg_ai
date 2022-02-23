
"""
Creamos la clase personaje con sus valores de vida y ataque
"""
class Personaje:
    def __init__(self, vida, ataque):
        self.vida = vida
        self.ataque = ataque


"""
Función que solicita por pantalla los datos de vida y ataque para Pikachu y Jiggly
Si los datos no son numericos (entero o float), saca un mensaje de aviso y vuelve a pedirlos hasta que sean correctos
"""
def solicitarDatosJugadores():
    tengoDatos = False
    tengo_P_vida = False
    tengo_P_ataque = False
    tengo_J_vida = False
    tengo_J_ataque = False

    while not tengoDatos:
        try:
            while not tengo_P_vida:
                P_vida = float( input( "Indica el valor de la VIDA de PIKACHU: "))
                tengo_P_vida = True   
            while not tengo_P_ataque:
                P_ataque = float( input( "Indica el valor del ATAQUE de PIKACHU: "))
                tengo_P_ataque = True 
            while not tengo_J_vida:
                J_vida = float( input( "Indica el valor de la VIDA de JIGGLYPUFF: "))
                tengo_J_vida = True 
            while not tengo_J_ataque:
                J_ataque = float( input( "Indica el valor del ATAQUE de JIGGLYPUFF: "))
                tengo_J_ataque = True 
        except ValueError:
            print("Debes introducir un dato numérico entero o decimal")
        if( tengo_P_vida == True and tengo_P_ataque == True and tengo_J_vida == True and tengo_J_ataque == True):
            tengoDatos = True
    return float(P_vida), float(P_ataque), float(J_vida), float(J_ataque)


"""
Función que solicita por pantalla a quien le va a corresponder el primer turno
    j o J para Jiggly
    p o P para Pikachu
Si el dato del turno no es correcto, da un mensaje y lo vuelva a solicitar
"""
def solicitarDatoTurno():
    tengoTurno = False
    try:
        while not tengoTurno:
            turno = str( input( "Indica a quien daras el turno: P (PIKACHU) o J (JIGGLYPUFF): "))
            if not isinstance(turno, str) or (turno.upper() != "P" and turno.upper() != "J"):
                print("El turno debe ser P o J")
            else:
                tengoTurno = True
        return turno.upper()

    except ValueError:
        print("Debe indicar el turno con una letra")


"""
Funcion con la logica del juego y que devulve un mensaje indicando el pokemos ganador
"""
def jugarPokemons(Pikachu, JigglyPuff, turno):
    
    # Mientras algun de los dos tenga vida, jugamos
    while (Pikachu.vida > 0 and JigglyPuff.vida >0):
        if (turno.upper() == "P"):
            JigglyPuff.vida = JigglyPuff.vida - Pikachu.ataque
            turno="J"
        else:
            Pikachu.vida = Pikachu.vida - JigglyPuff.ataque
            turno="P"
    
    # Alguno de los dos ha perdido la vida. Comprobamos quien esta vivo y generamos el mensaje con el nombre del ganador
    if Pikachu.vida > JigglyPuff.vida:
        ganador = "Pikachu"
    else:
        ganador = "JigglyPuff"
        
    mensajeJuego = ganador + " ha ganado."
    return mensajeJuego


def iniciarJuegoPikachu():
    
    # Le pedimos al usuario que nos de los valores de vida y fuerza de ataque
    P_vida, P_ataque, J_vida, J_ataque = solicitarDatosJugadores()
    # Le pedimos al usuario que indique a quien da el turno
    turno = solicitarDatoTurno()

    # Creamos a Pikachu y Jiggly con los datos del usuario 
    Pikachu = Personaje(P_vida, P_ataque)
    JigglyPuff = Personaje(J_vida, J_ataque)
    
    # Los ponemos a jugar
    mensaje = jugarPokemons(Pikachu, JigglyPuff, turno)
    
    # Por ultimo mostramos el mensaje sobre el ganador
    print(mensaje)
    



iniciarJuegoPikachu()