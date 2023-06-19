import csv
import os

RUTA_ARCHIVO = os.path.join("Etapa_10", "configuracion.csv")
with open(RUTA_ARCHIVO, "r", encoding="utf-8") as configuracion_juego:
    lector = csv.reader(configuracion_juego, delimiter=",")
    listado = list(lector)
MIN_LARGO_PALABRA = int(listado[0][1])

def formar_archivo_csv():
    '''
    Esta función lee los archivos "palabras.txt" y "definiciones.txt" y los escribe en un archivo de formato CSV.
    Hecho por: Felipe Gazcon
    Modificado por: Brian Duarte
    Corregido por: 
    '''

    # Obtiene la ruta del archivo de script actual
    ruta_actual = os.path.dirname(__file__)

    # Construir las rutas relativas a partir de la ubicación actual
    ruta_palabras = os.path.join(ruta_actual, "palabras.txt")
    ruta_definiciones = os.path.join(ruta_actual, "definiciones.txt")
    ruta_nuevo_archivo = os.path.join(ruta_actual, "nuevo_archivo.csv")

    with open(ruta_palabras, "r", encoding="utf-8") as palabras, open(ruta_definiciones, "r", encoding="utf-8") as definiciones, open(ruta_nuevo_archivo, "w", encoding="utf-8", newline="") as nuevo_archivo:
        escritor = csv.writer(nuevo_archivo, delimiter=',')

        linea_palabra = palabras.readline().strip()
        linea_definicion = definiciones.readline().strip()

        while linea_palabra:
            if len(linea_palabra) >= MIN_LARGO_PALABRA and linea_palabra.isalpha():
                escritor.writerow([linea_palabra, linea_definicion])

            linea_palabra = palabras.readline().strip()
            linea_definicion = definiciones.readline().strip()

        print("Archivo 'nuevo_archivo.csv' generado correctamente.")

formar_archivo_csv()