from operaciones.constantes_operaciones import*

def mostar_participantes(participantes,rosco):
    """
    Muestra el puntaje parcial de cada jugador.
    """
    # Hecho por: Walter Britez / Brian Duarte
    # Modificado por:
    # Corregido por:
    mensaje="ROSCO"
    mensaje2="RESULTADOS POR LETRA"
    mensaje3="TURNOS"
    rosco_letras=str(rosco[IND_LETRA])
    resultado_rosco=str(rosco['resultado_rosco'])
    turno_rosco=str(rosco['turno_rosco'])
    print(f"{mensaje:-^70}")
    print(f"{rosco_letras:-^70}\n\n{mensaje2:-^70}\n{resultado_rosco:-^70}\n\n{mensaje3:-^70}\n{turno_rosco:-^70}")
    print("\nJugadores:")
    for jugador in participantes.values():
        print(f"{jugador[JUGADOR]}"+" - Aciertos:"+"\033[1;32m"+f" {jugador[ACIERTOS]}"+"\033[0m"+" - Errores:"+"\033[1;31m"+f" {jugador[ERRORES]}"+"\033[0m")

def mostrar_datos(rondas,turno_actual,turno_jugador,participantes,rosco):
    print(f"\nRonda {rondas + 1} - Turno {turno_actual} - Letra: {rosco[IND_LETRA][turno_actual-1]} - Jugador: {participantes[turno_jugador][JUGADOR]} - Palabra de {len(rosco[IND_PAL_DEF][turno_actual-1][IND_PALABRA])} letras")
    print("\n\nDefinición:"+"\033[1;36m"+f" {rosco[IND_PAL_DEF][turno_actual-1][IND_DEFINICION]}"+"\033[0m")

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

    print("\nReporte final del juego:")
    print("Reporte Final: Partidas jugadas:", rondas)
    puntajes_finales = sorted(participantes.items(), key=lambda x: x[1][PUNT_PARCIALES], reverse=True)
    print("Puntaje Final:")
    for i, jugador in enumerate(puntajes_finales):
        print(f"{i + 1}. {jugador[1][JUGADOR]} - {(jugador[1][PUNT_PARCIALES])+(participantes[1][PUNTOS])} puntos")
