import csv
import random
import os


def limpiar_consola():
    """
    Limpia la consola según el sistema operativo (Windows, Linux, macOS).
    """
    # Hecho por: Brian Duarte
    # Modificado por:
    # Corregido por:

    # Comando para limpiar la consola en Windows
    if os.name == 'nt':
        os.system('cls')
    # Comando para limpiar la consola en Linux y macOS
    else:
        os.system('clear')


def leer_archivo_csv(nombre_archivo):
    """
    Lee un archivo CSV y retorna una lista con los datos leídos.
    """
    # Hecho por: Brian Duarte
    # Modificado por:
    # Corregido por:

    ruta_archivo_csv = os.path.join(os.path.dirname(__file__), "Etapa_8", nombre_archivo)
    with open(ruta_archivo_csv, "r", encoding="utf-8") as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter=',')
        palabras = list(lector)
    return palabras


def iniciar_juego(num_rondas):
    """
    Inicia el juego del pasapalabra con el número de rondas especificado.
    """
    # Hecho por: Brian Duarte
    # Modificado por:
    # Corregido por:

    palabras = leer_archivo_csv("nuevo_archivo.csv")
    participantes = {
        1: {"nombre": "Pedro", "aciertos": 0, "errores": 0, "puntos": 0},
        2: {"nombre": "Juan", "aciertos": 0, "errores": 0, "puntos": 0},
        3: {"nombre": "Maria", "aciertos": 0, "errores": 0, "puntos": 0}
    }
    turno_actual = 1
    rondas = 0
    continuar_juego = True

    print("Jugadores:")
    for jugador in participantes.values():
        print(f"{jugador['nombre']} - Aciertos: {jugador['aciertos']} - Errores: {jugador['errores']}")

    resultado_partida = []

    while rondas < num_rondas and continuar_juego:
        rosco = random.choice(palabras)
        print(f"\nRonda {rondas + 1} - Turno {turno_actual} - Letra: {rosco[0][0]} - Jugador: {participantes[turno_actual]['nombre']} - Palabra de {len(rosco[0])} letras - Definición: {rosco[1]}")

        saltar_ronda = False
        respuesta = input("Ingrese la palabra correspondiente (presione P para Pasapalabra): ")

        if respuesta.lower() == "p":
            turno_actual = siguiente_turno(turno_actual, participantes)  # Siguiente turno si se pasa

        elif respuesta.lower() == rosco[0].lower():
            print("La palabra es correcta.")
            participantes[turno_actual]["aciertos"] += 1
            participantes[turno_actual]["puntos"] += 10
            resultado_partida.append(
                f"Ronda {rondas + 1} - Turno {turno_actual} - Letra: {rosco[0][0]} - Jugador: {participantes[turno_actual]['nombre']} - Palabra de {len(rosco[0])} letras - {rosco[0]} - Acierto"
            )
            turno_actual = siguiente_turno(turno_actual, participantes)  # Siguiente turno normal

        elif respuesta == "":
            print("Debe ingresar una palabra por favor.")
            saltar_ronda = True

        else:
            participantes[turno_actual]["errores"] += 1
            participantes[turno_actual]["puntos"] -= 5  # Restar 5 puntos por cada error

            resultado_partida.append(
                f"Ronda {rondas + 1} - Turno {turno_actual} - Letra: {rosco[0][0]} - Jugador: {participantes[turno_actual]['nombre']} - Palabra de {len(rosco[0])} letras - {respuesta} - Error - Palabra correcta: {rosco[0]}"
            )
            turno_actual = siguiente_turno(turno_actual, participantes)  # Siguiente turno normal

        if not saltar_ronda:
            if turno_actual == 1:
                rondas += 1
                if rondas < num_rondas:
                    mostrar_puntaje_parcial(participantes)  # Mostrar puntaje parcial
                    continuar = input("\n¿Desea continuar a la siguiente ronda? (S/N): ")
                    if continuar.lower() == "n":
                        continuar_juego = False
                    limpiar_consola()  # Limpia la consola antes de cada ronda
                    print("\nJugadores:")
                    for jugador in participantes.values():
                        print(f"{jugador['nombre']} - Aciertos: {jugador['aciertos']} - Errores: {jugador['errores']}")

    print("\nResultado de partida:")
    for resultado in resultado_partida:
        print(resultado)

    print("\nPuntaje de la partida:")
    for jugador in participantes.values():
        print(f"{jugador['nombre']} - Puntos: {jugador['puntos']}")

    print("\nPuntaje Parcial:")
    for jugador in participantes.values():
        puntaje_parcial = jugador['puntos']
        print(f"{jugador['nombre']} - {puntaje_parcial} puntos")

    print("\nReporte final del juego:")
    print("Reporte Final: Partidas jugadas:", rondas)
    puntajes_finales = sorted(participantes.items(), key=lambda x: x[1]['puntos'], reverse=True)
    print("Puntaje Final:")
    for i, jugador in enumerate(puntajes_finales):
        print(f"{i + 1}. {jugador[1]['nombre']} - {jugador[1]['puntos']} puntos")


def siguiente_turno(turno_actual, participantes):
    """
    Calcula el siguiente turno en base al turno actual y la cantidad de jugadores.
    """
    # Hecho por: Brian Duarte
    # Modificado por:
    # Corregido por:

    num_jugadores = len(participantes)
    siguiente_turno = turno_actual + 1
    if siguiente_turno > num_jugadores:
        siguiente_turno = 1
    return siguiente_turno


def mostrar_puntaje_parcial(participantes):
    """
    Muestra el puntaje parcial de cada jugador.
    """
    # Hecho por: Brian Duarte
    # Modificado por:
    # Corregido por:

    print("\nPuntaje Parcial:")
    for jugador in participantes.values():
        puntaje_parcial = jugador['puntos']
        print(f"{jugador['nombre']} - {puntaje_parcial} puntos")


# Llama a la función para iniciar el juego con 10 rondas
iniciar_juego(10)
