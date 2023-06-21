import estado_juego 
from interfaces.interfaz_usuarios import iniciar_interfaz_usuarios
from interfaces.interfaz_salida import salida_inesperada
from operaciones.dinamica_1 import iniciar_juego

def main():
    """
    controla la ejecución del programa dirigiendo las llamadas a otras funciones.
    Hecho por: Walter Britez
    Modificado por:
    Corregido por: 
    """
    estado_juego.verificar_archivos()
    continuar = True
    while continuar:
        nom_jugadores=iniciar_interfaz_usuarios()
        if not nom_jugadores:
            continuar=salida_inesperada()
        else:
            iniciar_juego(nom_jugadores)
            continuar=False
main()