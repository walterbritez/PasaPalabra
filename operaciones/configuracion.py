import os
from operaciones.constantes_operaciones import*

RUTA_ARCHIVO = os.path.join(ARCHIVO_PY_CONFIG, ARCHIVO_CSV_CONFIG)
VALORES_ORIGINALES = [
    ["LONGITUD_PALABRA_MINIMA","4"],
    ["CANTIDAD_LETRAS_ROSCO","10"],
    ["MAXIMO_PARTIDAS","5"],
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
        for i in VALORES_ORIGINALES:
            escritura_config.write(f"{i[0]},{i[1]}\n")

def nuevo_valor_config(valor_inicial):
    '''
    Funcion para que el usuario decida si cambiar la configuracion presentada, y a que valor cambiarla.
    '''
    devolucion = valor_inicial
    quiere_cambiar_valor = input("Si quiere cambiar el valor de esta configuracion, introduzca el valor deseado. \nDe no ser asi, introduzca 'n'. ")
    if quiere_cambiar_valor.isnumeric():
        devolucion = quiere_cambiar_valor
    elif quiere_cambiar_valor != "n":
        devolucion = nuevo_valor_config(valor_inicial)
    return devolucion

def lectura_configuracion():
    '''
    Funcion para leer el csv con los valores ACTUALES y retornarlos en formato de lista, para hacer mas facil la utilizacionde estos
    '''
    configuracion_actual = []
    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as configuracion:
        valores = configuracion.readlines()
        for i in valores:
            configuracion_actual.append(i.strip().split(","))
    return configuracion_actual

def establecer_configuracion():
    '''
    Primero usamos la función para resetear la configuración, luego leemos la configuración como está y armamos
    una lista, preguntando si quiere mantener ese valor o modificandolo. Luego, se sobreescriben los nuevos
    valores.
    Hecho por: Felipe Gazcon
    Modificado por: 
    '''
    reseteo_archivo_config()
    configuracion_actual = lectura_configuracion()
    futura_configuracion = []
    for i in configuracion_actual:
        print(f"El valor actual de {i[0]} es: {i[1]}")
        nuevo_valor = nuevo_valor_config(i[1])
        futura_configuracion.append([i[0], nuevo_valor])

    with open(RUTA_ARCHIVO, "w", encoding="utf-8", newline="") as escritura_csv:
        for i in futura_configuracion:
            escritura_csv.write(f"{i[0]}, {i[1]}\n")

