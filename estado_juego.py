import os
from tkinter import messagebox
from archivos.constantes_archivos import*
from operaciones.constantes_operaciones import*
from interfaces.constantes_interfaces import*

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

def verificar_archivos_constantes():
    if not os.path.isfile(ARCHIVO_CONSTANTES):
        ruta=os.getcwd()
        messagebox.showwarning('Error', f"No se ha encontrado el archivo 'constantes_archivos'\n\nEn: {ruta}/imagenes/?")
        raise FileExistsError("No se encuentra el archivo 'constantes.py'")
    elif not os.path.isfile(AR_CONST_OPERACIONES):
        ruta=os.getcwd()
        messagebox.showwarning('Error', f"No se ha encontrado el archivo 'constantes_operaciones'\n\nEn: {ruta}/imagenes/?")
        raise FileExistsError("No se encuentra el archivo 'constantes_operaciones.py'")
    elif not os.path.isfile(AR_CONST_INTERFACES):
        ruta=os.getcwd()
        messagebox.showwarning('Error', f"No se ha encontrado el archivo 'constantes_operaciones'\n\nEn: {ruta}/imagenes/?")
        raise FileExistsError("No se encuentra el archivo 'constantes_operaciones'")
        
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
    
def verificar_archivos_txt():
    if not os.path.isfile(ARCHIVO_PALABRAS):
        ruta=os.getcwd()
        messagebox.showwarning('Error', f"No se ha encontrado el archivo 'palabras.txt'\n\nEn: {ruta}/imagenes/?")
        raise FileExistsError("No se encuentra el archivo 'palabras.txt'")
    elif not os.path.isfile(ARCHIVO_DEFINICIONES):
        ruta=os.getcwd()
        messagebox.showwarning('Error', f"No se ha encontrado el archivo 'constantes_archivos'\n\nEn: {ruta}/imagenes/?")
        raise FileExistsError("No se encuentra el archivo 'definiciones.txt'")

def verificar_archivos():
    '''
    Verifica que los archivos usados existan en la misma direccion relativa que el main
    Hecho por: Walter Britez
    Modificado por:
    Corregido por:
    '''
    verificar_archivo_usuarios()
    verificar_archivos_constantes()
    verificar_archivos_txt()
    verificar_archivos_constantes()