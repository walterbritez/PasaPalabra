import random
import os
from operaciones.constantes_operaciones import *
from operaciones.generar_datos import formar_archivo_csv
from operaciones.configuracion import establecer_configuracion
from interfaces.interfaz_salida import es_salir
from interfaces.interfaz_juego import *


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


def leer_archivo_csv():
    """
    Lee un archivo CSV y retorna una lista con los datos leídos.
    """
    # Hecho por: Brian Duarte
    # Modificado por: Walter Britez
    # Corregido por:

    palabras = []
    with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo_csv:
        for linea in archivo_csv:
            palabra = linea.strip().split(',')
            palabras.append(palabra)
    return palabras


def siguiente_turno(turno_actual, participantes):
    """
    Calcula el siguiente turno en base al turno actual y la cantidad de jugadores.
    """
    # Hecho por: Brian Duarte
    # Modificado por: Walter Britez
    # Corregido por:

    num_jugadores = len(participantes)
    siguiente_turno = turno_actual + 1
    if siguiente_turno > num_jugadores:
        siguiente_turno = 1
    return siguiente_turno


def es_continuar():
    """
    Verifica si el jugador desea continuar a la siguiente ronda del juego.
    """
    # Hecho por: Brian Duarte
    # Modificado por:Walter Britez
    # Corregido por:
    
    continuar = input("\n¿Desea continuar a la siguiente ronda? (S/N): ")
    if continuar.lower() == "n":
        continuar = False
    else:
        continuar = True
    limpiar_consola()  # Limpia la consola antes de cada ronda
    return continuar


def obtener_puntaje_parcial(participantes):
    """
    Calcula y actualiza el puntaje parcial de cada jugador en base a su puntaje acumulado.
    """
    # Hecho por: Brian Duarte
    # Modificado por: Walter Britez
    # Corregido por:
    
    parcial = 0
    for jugador in participantes.values():
        parcial = jugador[PUNTOS]
        jugador[PUNT_PARCIALES] += parcial
        print(f"\nPrueba de que parciales se está sumando {jugador[PUNT_PARCIALES]}")
        jugador[PUNTOS] = 0


def procesar_respuesta(turno_actual, turno_jugador, participantes, configuracion, resultado_partida, rosco, rondas):
    """
    Procesa la respuesta ingresada por el jugador y actualiza los datos correspondientes.
    """
    # Hecho por: Brian Duarte
    # Modificado por: Walter Britez/Brian Duarte
    # Corregido por:
    
    repetir_pregunta = True
    while repetir_pregunta:
        respuesta = input("Ingrese la palabra correspondiente (presione P para Pasapalabra): ")
        if respuesta.lower() == "":
            limpiar_consola()
            mostrar_datos(rondas, turno_actual, turno_jugador, participantes, rosco)  # Mostrar los datos nuevamente
            print("No ingresó ninguna palabra. ¡Inténtelo nuevamente!")
        elif respuesta.lower() == "p":
            turno_jugador = siguiente_turno(turno_actual, participantes)  # Siguiente turno si se pasa
            repetir_pregunta = False
        else:
            repetir_pregunta = False

    limpiar_consola()  # Limpia la consola después de ingresar una palabra
    if respuesta.lower() == rosco[0].lower():
        print("La palabra es correcta.")
        participantes[turno_jugador][ACIERTOS] += 1
        participantes[turno_jugador][PUNTOS] += int(configuracion[PTOS_ACIERTOS])
        resultado_partida.append(
            f"Ronda {rondas + 1} - Turno {turno_jugador} - Letra: {rosco[0][0]} - Jugador: {participantes[turno_jugador][JUGADOR]} - Palabra de {len(rosco[0])} letras - {rosco[0]} - Acierto"
        )
    elif respuesta.lower() == "p":
        print("Pasaste al siguiente turno sin ingresar una palabra.")
        turno_jugador = siguiente_turno(turno_actual, participantes)  # Siguiente turno si se pasa
    else:
        print("La palabra es incorrecta.")
        participantes[turno_jugador][ERRORES] += 1
        participantes[turno_jugador][PUNTOS] -= int(configuracion[PTOS_ERRORES])
        resultado_partida.append(
            f"Ronda {rondas + 1} - Turno {turno_jugador} - Letra: {rosco[0][0]} - Jugador: {participantes[turno_jugador][JUGADOR]} - Palabra de {len(rosco[0])} letras - {respuesta} - Error - Palabra correcta: {rosco[0]}"
        )
    
    turno_jugador = siguiente_turno(turno_actual, participantes)  # Siguiente turno


def jugar(participantes, configuracion):
    """
    Inicia el juego del pasapalabra con el número de rondas especificado.
    """
    # Hecho por: Brian Duarte
    # Modificado por: Walter Britez
    # Corregido por:
    palabras = leer_archivo_csv()
    turno_actual = 1
    turno_jugador = 1
    rondas = 0
    continuar_juego = True
    resultado_partida = []
    while rondas <= int(configuracion[MAX_PARTIDAS]) and continuar_juego:
        turno_actual = 1
        while turno_actual <= int(configuracion[CANT_TURNO]):
            mostar_participantes(participantes)
            rosco = random.choice(palabras)
            mostrar_datos(rondas, turno_actual, turno_jugador, participantes, rosco)
            procesar_respuesta(turno_actual, turno_jugador, participantes, configuracion, resultado_partida, rosco,
                               rondas)
            turno_jugador = siguiente_turno(turno_jugador, participantes)  # Siguiente turno si se pasa
            turno_actual += 1
            limpiar_consola()
        if rondas < int(configuracion[MAX_PARTIDAS]) and continuar_juego:
            mostrar_puntaje_partida(participantes)  # Mostrar puntaje parcial
            obtener_puntaje_parcial(participantes)
            mostrar_puntaje_parcial(participantes)
            continuar_juego = es_continuar()
        rondas += 1
    obtener_puntaje_parcial(participantes)
    mostrar_resultado(resultado_partida, participantes, rondas)


def obtener_configuracion():
    """
    Lee el archivo de configuración y retorna un diccionario con los valores de configuración.
    """
    # Hecho por: Felipe Gazcon
    # Modificado por:
    # Corregido por:
    dicc = {}
    archivo = open(ARCHIVO_CSV_CONFIG_2, "r")
    for linea in archivo:
        linea = linea.rstrip("\n").split(",")
        dicc[linea[NOMBRE_CONFIGURACION]] = linea[VALOR_CONFIGURACION]
    return dicc


def obtener_datos_jugadores(nom_jug):
    """
    Crea un diccionario con los datos de los jugadores a partir de una lista de nombres.
    """
    # Hecho por: Walter Britez
    # Modificado por:
    # Corregido por:
    dicc = {}
    indice = 1
    for i in range(len(nom_jug)):
        dicc[indice] = [nom_jug[i], 0, 0, 0, 0]
        indice += 1
    return dicc


def iniciar_juego(nom_jugadores):
    """
    Inicia el juego del pasapalabra con los nombres de los jugadores proporcionados.
    """
    # Hecho por: Walter Britez
    # Modificado por: 
    # Corregido por:
    continuar_jugando = True
    while continuar_jugando:
        establecer_configuracion()
        configuracion = obtener_configuracion()
        participantes = obtener_datos_jugadores(nom_jugadores)
        formar_archivo_csv()
        limpiar_consola()
        jugar(participantes, configuracion)
        continuar_jugando = es_salir()



