import os
from tkinter import messagebox
ARCHIVO_USUARIOS="./archivos/usarios.csv"
IMG_ENTRAR_JUGAR="./imagenes/Entrar_jugar.png"
IMG_REGISTRAR="./imagenes/registrar.png"
IMG_CONTINUAR="./imagenes/Continuar.png"
CAMPO_1="usuario"
CAMPO_2="clave"

def verificar_archivo_usuarios():
    '''
    Verifica que el archivo usario exista... en caso contrario creará un archivo .csv
    Hecho por: Walter Britez
    Modificado por:
    Corregido por:
    '''
    try:
        archivo=open(ARCHIVO_USUARIOS)
        archivo.close()
    except FileNotFoundError:
        archivo=open(ARCHIVO_USUARIOS,"w")
        archivo.write(f"{CAMPO_1},{CAMPO_2}")
        archivo.close()

def verificar_archivos():
    '''
    Verifica que los archivos usados existan en la misma direccion relativa que el main
    Hecho por: Walter Britez
    Modificado por:
    Corregido por:
    '''
    verificar_archivo_usuarios()

def verificar_fotos():
    if not os.path.isfile(IMG_ENTRAR_JUGAR):
        ruta=os.getcwd()
        messagebox.showwarning('Error', f"No se ha encontrado el archivo 'Entrar_jugar.png'\n\nEn: {ruta}/imagenes/?")
        raise FileExistsError("No se encuentra el archivo 'Entrar_jugar.png'")
    elif not os.path.isfile(IMG_REGISTRAR):
        ruta=os.getcwd()
        messagebox.showwarning('Error', f"No se ha encontrado el archivo 'Registrar.png'\n\nEn {ruta}/imagenes/?")
        raise FileExistsError("No se encuentra el archivo 'Registrar.png'")
    elif not os.path.isfile(IMG_CONTINUAR):
        ruta=os.getcwd()
        messagebox.showwarning('Error', f"No se ha encontrado el archivo 'Continuar.png'\n\nEn {ruta}/imagenes/?")
        raise FileExistsError("No se encuentra el archivo 'Continuar.png'")