# Segmento con el proposito de crear un diccionario con las palabras 
# y sus definiciones, ademas de la cantidad por letra y en general.
# Para esto, se nos dara una funcion que retorna una lista con los 
# datos requeridos
# Hecho por: Felipe Gazcon
# Modificado por:

from datos import obtener_lista_definiciones

def generar_diccionario_palabras():
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

    diccionario_vocales_acento = {
        "á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u"
    }
    for palabra_definicion in obtener_lista_definiciones():
    # Este fragmento es para evitar la errores por las tildes y sumar la
    # cantidad de palabras por letra de manera correcta
        if palabra_definicion[0][0] in diccionario_vocales_acento:
            letra = diccionario_vocales_acento[palabra_definicion[0][0]]
        else:
            letra = palabra_definicion[0][0]

        if len(palabra_definicion[1]) >= 5:
            diccionario_palabras_candidatas[palabra_definicion[0]] = palabra_definicion[1]
            diccionario_cantidad_por_letra[letra] += 1
            cantidad_de_palabras += 1

    # Estas tres lineas son las encargadas de imprimir la cantidad de palabras
    # por letra y las palabras en general
    for i, n in diccionario_cantidad_por_letra.items():
        print(f" Hay {n} palabras que empiezan con {i}.")
    print(f" La cantidad de palabras total es de {cantidad_de_palabras}.")
    
    return diccionario_palabras_candidatas

generar_diccionario_palabras()

    

