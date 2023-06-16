"""
Parte con el proposito de leer los archvos de texto (definiciones.txt) y (palabras.txt) para reescribir su 
contenido en un .wsv
"""
import csv

def formar_archivo_csv(min_largo_palabra):
    with open("textos/palabras.txt", "r", encoding="utf-8") as palabras, open("textos/definiciones.txt", "r", encoding="utf-8") as definiciones, open("textos/nuevo_archivo.csv", "w", encoding="utf-8", newline="") as nuevo_archivo:
        escritor = csv.writer(nuevo_archivo, delimiter=',')
        
        linea_palabra = palabras.readline().strip()
        linea_definicion = definiciones.readline().strip()
        
        while linea_palabra:
            if len(linea_palabra) >= min_largo_palabra and linea_palabra.isalpha():
                escritor.writerow([linea_palabra, linea_definicion])
            
            linea_palabra = palabras.readline().strip()
            linea_definicion = definiciones.readline().strip()
        
        print("Archivo 'nuevo_archivo.csv' generado correctamente.")

formar_archivo_csv(5)



