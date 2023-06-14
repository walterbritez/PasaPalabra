import os
from tkinter import messagebox
ARCHIVO_USUARIOS='usuarios.csv'
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
    '''
    Verfica que las fotos usadas existan en la misma direccion relativa que el main
    Hecho por: Walter Britez
    Modificado por:
    Corregido por:
    '''
    if not os.path.isfile("Entrar_jugar.png"):
        messagebox.showwarning('Error', "No se ha encontrado el archivo 'Entrar_jugar.png' ")
        raise FileExistsError("No se encuentra el archivo 'Entrar_jugar.png'")
    elif not os.path.isfile("Registrar.png"):
        messagebox.showwarning('Error', "No se ha encontrado el archivo 'Registrar.png' ")
        raise FileExistsError("No se encuentra el archivo 'Registrar.png'")
    