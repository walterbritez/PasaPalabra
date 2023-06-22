import os

RUTA_ARCHIVO = os.path.join("Etapa_10", "configuracion.csv")
with open(RUTA_ARCHIVO, "r", encoding="utf-8") as configuracion_juego:
    listado = [line.split(",") for line in configuracion_juego]
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
    ruta_diccionario = os.path.join(ruta_actual, "diccionario.csv")

    with open(ruta_palabras, "r", encoding="utf-8") as palabras, open(ruta_definiciones, "r", encoding="utf-8") as definiciones, open(ruta_diccionario, "w", encoding="utf-8", newline="") as diccionario:
        linea_palabra = palabras.readline().strip()
        linea_definicion = definiciones.readline().strip()

        while linea_palabra:
            if len(linea_palabra) >= MIN_LARGO_PALABRA and linea_palabra.isalpha():
                diccionario.write(f"{linea_palabra},'{linea_definicion}'\n")

            linea_palabra = palabras.readline().strip()
            linea_definicion = definiciones.readline().strip()

        print("Archivo 'nuevo_archivo.csv' generado correctamente.")

formar_archivo_csv()
