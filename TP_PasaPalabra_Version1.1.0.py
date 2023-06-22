import estado_juego
from interfaces.interfaz_usuarios import iniciar_interfaz
from interfaces.interfaz_salida import salida_inesperada
from operaciones.dinamica_1 import iniciar_juego


def main():
    """
    Controla la ejecución del programa dirigiendo las llamadas a otras funciones.
    Hecho por: Walter Britez
    Modificado por: Brian Duarte
    Corregido por:
    """
    estado_juego.verificar_archivos()

    continuar_juego = True
    while continuar_juego:
        nombres_jugadores = iniciar_interfaz()

        if not nombres_jugadores:
            continuar_juego = salida_inesperada()
        else:
            iniciar_juego(nombres_jugadores)
            continuar_juego = False


if __name__ == "__main__":
    main()