from datos import obtener_lista_definiciones
import os
import random 
limpiar_pantalla=lambda: os.system("cls")
ERRORES=1
ACIERTOS=2
LETRAS=3
RESULTADOS=4
PALABRA=5
RESPUESTA=6
PAL_SELECIONADAS=7
LETRAS_SELECIONADAS=8
CORRECTO='a'
INCORRECTO='e'

def mostrar(datos,turno):
    '''
    Muestra por pantalla los datos cargados en el diccionario
    Hecho por: Walter Britez
    Modificado por:
    '''
    print(datos[LETRAS])
    print(datos[RESULTADOS])
    print("Aciertos "+"\033[1;32m"+f"{datos[ACIERTOS]}"+ "\033[0m")
    print("Errores "+"\033[1;31m"+f"{datos[ERRORES]}"+"\033[0m") 
    print("Turno de la letra "+"\033[1;34m"+f"{datos[LETRAS][turno]} " + "\033[0m" + f"- Palabra de {len(datos[PALABRA][turno][0])} letras") 
    print("\033[1;36m"+f"Definicion: {datos[PALABRA][turno][1]}"+"\033[0;m") 

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

def procesar_respuesta(datos,resp_usuario,turno):
    '''
    Pre: Recibe la estructura y la respuesta del usuario
    Post: Valida la respuesta y la carga en la estrucura la valudación junto con la respuesta
    Hecho por: Walter Britez
    Modificado por:
    '''  
    if resp_usuario==datos[PALABRA][turno][0]:
        datos[ACIERTOS]+=1
        datos[RESULTADOS][turno]=[CORRECTO] #verificar que esto funcione
        datos[RESPUESTA][turno]=resp_usuario
    else:
        datos[ERRORES]+=1
        datos[RESULTADOS][turno]=[INCORRECTO] #verificar que esto funcione
        datos[RESPUESTA][turno]=resp_usuario
    return datos
    
def resumen(datos):
    for i in range(0,len(datos[LETRAS])):
        if datos[RESULTADOS][i][0]==CORRECTO:
            print(f"Turno de la letra {datos[LETRAS][i]} - Palabra de {len(datos[PALABRA][i][0])} letras - {datos[PALABRA][i][0]} - acierto")
        else:
            print(f"Turno de la letra {datos[LETRAS][i]} - Palabra de {len(datos[PALABRA][i][0])} letras - {datos[RESPUESTA][i]} - error - Palabra Correcta: {datos[PALABRA][i][0]}")
    print(f"puntaje final: {datos[ACIERTOS]}")

def generar_letras_palabras(datos,palabras_definiciones):
    '''
    Genera las letras del rosco y la estuctura de la tabla de aciertos.
    Hecho por Walter Britez:
    Modificado Por: Brian Duarte
    '''
    resultado=[]
    respuesta=[]
    letras_rosco=[]
    for i in range(len(palabras_definiciones[LETRAS_SELECIONADAS])):
        resultado.append([" "])
        respuesta.append([" "])
        letras_rosco.append([palabras_definiciones[LETRAS_SELECIONADAS][i]])
    datos[LETRAS]=letras_rosco
    datos[PALABRA]=palabras_definiciones[PAL_SELECIONADAS]
    datos[RESULTADOS]=resultado
    datos[RESPUESTA]=respuesta
    return datos
           
def generar_estructura(palabras_definiciones):
    '''
    Genera una estrucura de datos adecuada, en este caso un diccionario
    Hecho por Walter Britez:
    Modificado por:
    '''
    datos={}
    datos[ERRORES]=0
    datos[ACIERTOS]=0
    generar_letras_palabras(datos,palabras_definiciones)
    return datos    

def generar_diccionario_palabras():
    # Segmento con el proposito de crear un diccionario con las palabras 
    # y sus definiciones, ademas de la cantidad por letra y en general.
    # Para esto, se nos dara una funcion que retorna una lista con los 
    # datos requeridos
    # Hecho por: Felipe Gazcon
    # Modificado por: Brian Duarte / Walter Britez 

    diccionario_palabras_candidatas = {}
    diccionario_cantidad_por_letra = {}
    cantidad_de_palabras = 0
    conjunto_letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                       "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    # Con este bloque, armamos un diccionarios con valores en 0 
    # para cada letra posible. La idea es facilitar luego la suma cada vez 
    # que aparezca una letra nueva.
    for i in conjunto_letras:
        diccionario_cantidad_por_letra[i] = 0

    # Este bloque itera por cada fragmento de la lista recibida de los 
    # datos, filtra segun si la palabra, i[0], tiene mas de 5 letras y si 
    # es asi, hace tres cosas: agrega la el conjunto palabra-definicion al
    # diccionario pedido, aumenta en 1 el contador de cantidad de palabras,
    # y aumenta en 1 el contador de palabras por letra.
    for palabra_definicion in obtener_lista_definiciones():

    # Este fragmento es para evitar la errores por las tildes y sumar la
    # cantidad de palabras por letra de manera correcta
        if palabra_definicion[0][0] == "á":
            letra = "a"
        elif palabra_definicion[0][0] == "é":
            letra = "e"
        elif palabra_definicion[0][0] == "í":
            letra = "i"
        elif palabra_definicion[0][0] == "ó":
            letra = "o"
        elif palabra_definicion[0][0] == "ú":
            letra = "u"
        else:
            letra = palabra_definicion[0][0]

    # Este bloque 
        if len(palabra_definicion[1]) >= 5:
            diccionario_palabras_candidatas[palabra_definicion[0]] = palabra_definicion[1]
            diccionario_cantidad_por_letra[letra] += 1
            cantidad_de_palabras += 1
    return diccionario_palabras_candidatas

def seleccionar_palabras(diccionario, letras):
    """ 
    Pre: Recibe un diccionario válido y la lista 'letras' tendrá al menos 10 elementos
    Post: Devuelve una lista ordenada alfabéticamente con palabras selectas al azar del diccionario
    Hecha por: Genesis Pinto
    Modificado por: Brian Duarte/Walter Britez
    """
    letras_seleccionadas = random.sample(letras, 10)
    letras_seleccionadas_ordenadas = sorted(letras_seleccionadas)
    # Imprimo las letras que se eligió para mi lista
    # print(letras_seleccionadas_ordenadas)
    
    palabras_seleccionadas=[]
    palabras_definiciones={}
    
    for letra in letras_seleccionadas_ordenadas:
        palabras_candidatas = []
        # Se encarga de seleccionar las palabras, según su índice, que coincidan con letras_seleccionadas_ordenadas 
        # y las agrega a palabras_candidatas en cada iteración
        for palabra in diccionario.keys():
            if palabra.startswith(letra):
                palabras_candidatas.append(palabra)
                
        if palabras_candidatas:
            palabra_elegida = random.choice(palabras_candidatas)
            palabras_seleccionadas.append([palabra_elegida,diccionario[palabra_elegida]])
    palabras_definiciones[PAL_SELECIONADAS]=palabras_seleccionadas
    palabras_definiciones[LETRAS_SELECIONADAS]=letras_seleccionadas_ordenadas
    return palabras_definiciones

def main():
    """
    controla la ejecución del programa dirigiendo las llamadas a otras funciones.
    Hecho por: Walter Britez
    Modificado por: Brian Duarte / Walter Britez
    """
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    diccionario_palabra=generar_diccionario_palabras()
    palabras_definiciones=seleccionar_palabras(diccionario_palabra,letras)
    datos=generar_estructura(palabras_definiciones)
    turno=0
    while turno<len(datos[LETRAS]):
        mostrar(datos,turno)
        resp_usuario=ingresar_respuesta()
        datos=procesar_respuesta(datos, resp_usuario,turno)
        limpiar_pantalla()
        turno+=1
    resumen(datos)
main()