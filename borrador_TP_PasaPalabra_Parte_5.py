
def calcular_puntaje(palabras):
    """
    La funcion se encarga de analizar el resultado del juego,y asignar sus valores,dependiendo
  del resultado y devolver los puntos acumulados en la jugada.
  Ademas, pregunta al usuario si desea jugar de nuevo.
  Autor Nahuel Cabrera
  
    """
    
    puntaje = 0
    for palabra in palabras:
        respuesta = input(f"Ingrese su respuesta para '{palabra}': ")
        if respuesta == palabra:
            puntaje += 10
        else:
            puntaje -= 3
    return puntaje

puntaje_total = 0


while True:
    print("¡Nuevo juego!")
    puntaje_partida = calcular_puntaje()
    puntaje_total += puntaje_partida
    print(f"Puntaje de la partida: {puntaje_partida}")
    print(f"Puntaje total: {puntaje_total}")
    
    respuesta = input("¿Quiere jugar otra partida? (s/n): ")
    if respuesta.lower() == "n":
    

print("¡Ronda Terminada!")
