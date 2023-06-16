import estado_juego 
from interfaces.interfaz_usuarios import iniciar_interfaz

def main():
    """
    controla la ejecución del programa dirigiendo las llamadas a otras funciones.
    Hecho por: Walter Britez
    Modificado por:
    Corregido por: 
    """
    estado_juego.verificar_archivos()
    estado_juego.verificar_fotos()
    nom_jugadores=iniciar_interfaz()
    
    '''
    ESTA PARTE SE COMENTO. SE IMPLEMENTARÁ MODIFICANDOLO PARA LAS SIGUIENTES ETAPAS 

    continuar="s"                          
    puntaje_total=0
    while continuar=="s":
        puntaje_partida=operaciones.iniciar_partida()
        puntaje_total+=puntaje_partida
        continuar=operaciones.estado_juego(puntaje_total)
    '''
main()