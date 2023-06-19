import csv
import os

RUTA_ARCHIVO = os.path.join("Etapa_10", "configuracion.csv")
VALORES_ORIGINALES = [
    ["LONGITUD_PALABRA_MINIMA","4"],
    ["CANTIDAD_LETRAS_ROSCO","10"],
    ["MAXIMMO_PARTIDAS","5"],
    ["PUNTAJE_ACIERTO","10"],
    ["PUNTAJE_DESACIERTO","3"]
]
NOMBRE_CONFIGURACION = 0
VALOR_CONFIGURACION = 1

def reseteo_archivo_config():
    '''
    Funcion para devolver el .csv a sus valores originales
    '''
    with open(RUTA_ARCHIVO, "w", encoding="utf-8", newline="") as escritura_config:

        escritor = csv.writer(escritura_config, delimiter=",")
        escritor.writerows(VALORES_ORIGINALES)

def nuevo_valor_config(valor_inicial):
    '''
    Funcion para decidir si cambiar las configuraciones y poder cambiar cada valor de la 
    configuracion preexistente.
    '''
    devolucion = valor_inicial
    quiere_cambiar_valor = input("Si quiere cambiar el valor de esta configuracion, introduzca el valor deseado. \nDe no ser asi, introduzca 'n'. ")
    if quiere_cambiar_valor.isnumeric():
        devolucion = quiere_cambiar_valor
    elif quiere_cambiar_valor != "n":
        devolucion = nuevo_valor_config(valor_inicial)
    return devolucion

def establecer_configuracion():
    '''
    Primero usamos la función para resetear la configuración, luego leemos la configuración como está y armamos
    una lista, preguntando si quiere mantener ese valor o modificandolo. Luego, un writer sobreescribe los nuevos
    valores.
    Hecho por: Felipe Gazcon
    Modificado por: 
    '''
    reseteo_archivo_config()
    filas_nuevas = []
    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as lectura_config:

        lector = csv.reader(lectura_config, delimiter=',')
        lineas_configuracion = list(lector)
        for i in lineas_configuracion:
            print(f"{i[NOMBRE_CONFIGURACION]}:{i[VALOR_CONFIGURACION]}.")
            valor = nuevo_valor_config(i[VALOR_CONFIGURACION])
            filas_nuevas.append([i[NOMBRE_CONFIGURACION], valor])
    
    with open(RUTA_ARCHIVO, "w", encoding="utf-8", newline="") as escritura_config:

        escritor = csv.writer(escritura_config, delimiter=",")
        escritor.writerows(filas_nuevas)

