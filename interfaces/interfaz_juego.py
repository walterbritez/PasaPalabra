from operaciones.constantes_operaciones import*

def mostar_participantes(participantes):
    print("Jugadores:")
    for jugador in participantes.values():
        print(f"{jugador[JUGADOR]} - Aciertos: {jugador[ACIERTOS]} - Errores: {jugador[ERRORES]}")

def mostrar_datos(rondas,turno_actual,turno_jugador,participantes,rosco):
    print(f"\nRonda {rondas + 1} - Turno {turno_actual} - Letra: {rosco[0][0]} - Jugador: {participantes[turno_jugador][JUGADOR]} - Palabra de {len(rosco[0])} letras - Definición: {rosco[1]}")

def mostrar_puntaje_partida(participantes):
    print("\nPuntaje de la partida:")
    for jugador in participantes.values():
        print(f"{jugador[JUGADOR]} - Puntos: {jugador[PUNTOS]}")

def mostrar_puntaje_parcial(participantes):
    """
    Muestra el puntaje parcial de cada jugador.
    """
    # Hecho por: Brian Duarte
    # Modificado por:
    # Corregido por:

    print("\nPuntaje Parcial:")
    for jugador in participantes.values():
        puntaje_parcial = jugador[PUNT_PARCIALES]
        print(f"{jugador[JUGADOR]} - {puntaje_parcial} puntos")

def mostrar_resultado(resultado_partida,participantes,rondas):
    print("\nResultado de partida:")
    for resultado in resultado_partida:
        print(resultado)

    print("\nPuntaje de la partida:")
    for jugador in participantes.values():
        print(f"{jugador[JUGADOR]} - Puntos: {jugador[PUNTOS]}")
    '''
    print("\nPuntaje Parcial:")
    for jugador in participantes.values():
        puntaje_parcial = jugador[PUNTOS]
        print(f"{jugador[JUGADOR]} - {puntaje_parcial} puntos")
    '''

    print("\nReporte final del juego:")
    print("Reporte Final: Partidas jugadas:", rondas)
    puntajes_finales = sorted(participantes.items(), key=lambda x: x[1][PUNT_PARCIALES], reverse=True)
    print("Puntaje Final:")
    for i, jugador in enumerate(puntajes_finales):
        print(f"{i + 1}. {jugador[1][JUGADOR]} - {jugador[1][PUNT_PARCIALES]} puntos")