import TP_PasaPalabra_Parte_2 
import random 

def seleccionar_palabras(diccionario, letras):
    """ 
    Pre: Recibe un diccionario válido y la lista 'letras' tendrá al menos 10 elementos
    Post: Devuelve una lista ordenada alfabéticamente con palabras selectas al azar del diccionario
    Hecha por: Genesis Pinto
    Modificado por:
    """
    letras_seleccionadas = random.sample(letras, 10)
    letras_seleccionadas_ordenadas = sorted(letras_seleccionadas)
    # Imprimo las letras que se eligió para mi lista
    # print(letras_seleccionadas_ordenadas)
    
    palabras_seleccionadas=[]
    
    for letra in letras_seleccionadas_ordenadas:
        palabras_candidatas = []
        # Se encarga de seleccionar las palabras, según su índice, que coincidan con letras_seleccionadas_ordenadas 
        # y las agrega a palabras_candidatas en cada iteración
        for palabra in diccionario.keys():
            if palabra.startswith(letra):
                palabras_candidatas.append(palabra)
                
        if palabras_candidatas:
            palabra_elegida = random.choice(palabras_candidatas)
            palabras_seleccionadas.append(palabra_elegida)
    
    return palabras_seleccionadas

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Llamo a la función generar_diccionario_palabras() del archivo TP_PasaPalabra_Parte_2 para extraer el diccionario
# Requiere modificaciones al reemplazarlo al programa general para su uso:
# diccionario = generar_diccionario_palabras()
diccionario = TP_PasaPalabra_Parte_2.generar_diccionario_palabras()
seleccionar_palabras(diccionario, letras)

"""
# Itero mi función para observar los diferentes casos de resultado
for i in range(100):
    palabras_a_adivinar = seleccionar_palabras(diccionario, letras)
    print(palabras_a_adivinar)  
"""
