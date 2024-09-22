import tkinter.messagebox as mbox

def salida_inesperada():
    continuar = True
    ans=mbox.askyesno("Salir","Estás seguro que desea salir")
    if ans:
        continuar = False    
    return continuar

def es_salir():
    continuar = True
    '''
    ans=mbox.askyesno("Salir","Juego terminado!\ndesea continuar")
    if ans:
        continuar = False    
    '''
    mensaje="JUEGO TERMINADO"
    print(f"{mensaje:-^70}")
    continuar_jugando=input("Desea CONTINUAR? presione 'S'\nDesea SALIR? presiones 'N'\nRespuesta: ")
    if continuar_jugando.lower() =="n":
        continuar = False
    return continuar


    