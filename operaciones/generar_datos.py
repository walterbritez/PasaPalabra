import os
from operaciones.constantes_operaciones import *

RUTA_ARCHIVO = os.path.join(ARCHIVO_PY_CONFIG, ARCHIVO_CSV_CONFIG)

with open(RUTA_ARCHIVO, "r", encoding="utf-8") as configuracion_juego:
    contenido = configuracion_juego.read().splitlines()

listado = [linea.split(",") for linea in contenido]

MIN_LARGO_PALABRA = int(listado[IND_PALABRA][IND_DEFINICION])


def formar_archivo_csv():
    '''
    Esta función lee los archivos "palabras.txt" y "definiciones.txt" y los escribe en un archivo de formato CSV.
    Hecho por: Felipe Gazcon
    Modificado por: Brian Duarte / Walter Britez
    Corregido por: 
    '''

    with open(ARCHIVO_DEFINICIONES, "r", encoding="utf-8") as definiciones, open(ARCHIVO_PALABRAS, "r", encoding="utf-8") as palabras, open(ARCHIVO_DATOS, "w", encoding="utf-8", newline="") as datos:
        linea_palabra = palabras.readline().rstrip()
        linea_definicion = definiciones.readline().rstrip()

        while linea_palabra:
            if len(linea_palabra) >= MIN_LARGO_PALABRA and linea_palabra.isalpha():
                datos.write(f"{linea_palabra},{linea_definicion}\n")

            linea_palabra = palabras.readline().strip()
            linea_definicion = definiciones.readline().strip()

        print("Archivo 'nuevo_archivo.csv' generado correctamente.")
