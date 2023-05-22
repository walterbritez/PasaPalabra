from datos import obtener_lista_definiciones
import os
limpiar_pantalla=lambda: os.system("cls")
ERRORES=1
ACIERTOS=2
LETRAS=3
RESULTADOS=4
PALABRA=5
RESPUESTA=6
CORRECTO="a"
INCORRECTO="e"

#Mostrar por pantalla
#Falta mostrar las palabras a adivinar
def mostrar(datos,turno):
    '''
    Muestra por pantalla los datos cargados en el diccionario
    Hecho por: Walter Britez
    Modificado por:
    '''
    print(datos[LETRAS])
    print(datos[RESULTADOS])
    print(f"Aciertos {datos[ACIERTOS]}")
    print(f"Erroes {datos[ERRORES]}")
    print(f"Turno de la letra {datos[LETRAS][turno]} - Palabra de len(datos[PALABRA][TURNO]) letras") #Acá en la etapa 2 con esa estructura cargada
    print(f"Definicion: datos[PALABRA][turno]") #Acá en la etapa 2 con esa estructura cargada

def validar_respuesta(respuesta):
    '''
    Pre: Recibe una cadena de caracteres
    Post: Devuelve una validación, VERDADERO si la cadena está formada sólo por letras caso contrario devuelve FALSO
    Hecho por: Walter Britez
    Modificado por: 
    '''
    valida=True
    indice=0
    while valida==True and indice<len(respuesta):
        if not respuesta[indice].isalpha() or respuesta[indice].isspace():
            valida=False
        indice+=1
    return valida

def ingresar_respuesta():
    '''
    Permite la entrada de datos al usuario por teclado
    Hecho por: Walter Britez 
    '''
    valido=False
    respuesta=""
    while valido==False:
        respuesta=(input("Ingrese palabra: "))
        valido=validar_respuesta(respuesta)
        if valido==False:
            print("Palabra no valida (solo letras sin espacios)")
    return respuesta

#Procesar
def procesar_respuesta(datos,resp_usuario,turno):
    '''
    Pre: Recibe la estructura y la respuesta del usuario
    Post: Valida la respuesta y la carga en la estrucura la valudación junto con la respuesta
    Hecho por: Walter Britez
    Modificado por:
    '''  
    if resp_usuario==datos[PALABRA][turno]:
        datos[ACIERTOS]+=1
        datos[RESULTADOS][turno]=[CORRECTO] #verificar que esto funcione
        datos[RESPUESTA][turno]=resp_usuario
    else:
        datos[ERRORES]+=1
        datos[RESULTADOS][turno]=[INCORRECTO] #verificar que esto funcione
        datos[RESPUESTA][turno]=resp_usuario
    return datos
    
#Resumen
def resumen(datos):
    for i in range(0,len(datos[LETRAS])-1):
        if datos[RESULTADOS][i]==CORRECTO:
            print(f"Turno de la letra {datos[LETRAS][i]}-Palabra de {len(datos[PALABRA][i])} letras -{datos[PALABRA][i]}-acierto")
        else:
            print(f"Turno de la letra {datos[LETRAS][i]}-Palabra de {len(datos[PALABRA][i])} letras-{datos[RESPUESTA][i]}-error-Palabra Correcta: {datos[PALABRA][i]}")
    print(f"puntaje final: {datos[ACIERTOS]}")

def generar_letras(datos):
    #Falta Generar las definiciones
    '''
    Genera las letras del rosco y la estuctura de la tabla de aciertos.
    Hecho por Walter Britez:
    Modificado Por:
    '''
    letras=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
'X', 'Y', 'Z']
    letras_rosco=[]
    resultados=[]
    respuestas=[]
    for letra in range(0,len(letras)-1,2):
        letras_rosco.append([letras[letra]])
        resultados.append([" "])
        respuestas.append([" "])

    datos[LETRAS]=letras_rosco
    datos[RESULTADOS]=resultados
    datos[RESPUESTA]=respuestas
    datos[PALABRA]=resultados
    
    return datos
           
def generar_estructura():
    '''
    Genera una estrucura de datos adecuada, en este caso un diccionario
    Hecho por Walter Britez:
    Modificado por:
    '''
    datos={}
    datos[ERRORES]=0
    datos[ACIERTOS]=0
    generar_letras(datos)
    return datos    

def main():
    """
    controla la ejecución del programa dirigiendo las llamadas a otras funciones.
    Hecho por: Walter Britez
    Modificado por:
    """
    datos=generar_estructura()
    turno=0
    while turno<len(datos[LETRAS]):
        mostrar(datos,turno)
        resp_usuario=ingresar_respuesta()
        print(resp_usuario)
        datos=procesar_respuesta(datos, resp_usuario,turno) #esta es la parte más importante
        limpiar_pantalla()
        turno+=1
    resumen(datos)
main()