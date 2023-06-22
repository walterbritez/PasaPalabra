import os
from operaciones.constantes_operaciones import *

RUTA_ARCHIVO = os.path.join(ARCHIVO_PY_CONFIG, ARCHIVO_CSV_CONFIG)

def formar_archivo_csv():
    '''
    Esta función lee los archivos "palabras.txt" y "definiciones.txt" y los escribe en un archivo de formato CSV.
    Hecho por: Felipe Gazcon
    Modificado por: Brian Duarte / Walter Britez
    Corregido por: 
    '''
    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as configuracion_juego:
        listado = [line.split(",") for line in configuracion_juego]
        MIN_LARGO_PALABRA = int(listado[0][1])
        
    with open(ARCHIVO_DEFINICIONES, "r", encoding="utf-8") as definiciones, open(ARCHIVO_PALABRAS, "r", encoding="utf-8") as palabras, open(ARCHIVO_DATOS, "w", encoding="utf-8", newline="") as datos:
        linea_palabra = palabras.readline().rstrip()
        linea_definicion = definiciones.readline().rstrip()

        while linea_palabra:
            if len(linea_palabra) > MIN_LARGO_PALABRA and linea_palabra.isalpha():
                datos.write(f"{linea_palabra},{linea_definicion}\n")

            linea_palabra = palabras.readline().strip()
            linea_definicion = definiciones.readline().strip()

        print("Archivo 'nuevo_archivo.csv' generado correctamente.")
