# Construye un código en lenguaje Python que llama a una función tras haberle suministrado una
# palabra. Dicha función, de nombre es_palindromo(), recibirá la palabra tecleada por el usuario y
# averiguará si ésta es o no un palíndromo. Un palíndromo es una palabra que se lee igual del
# derecho que del revés, por ejemplo RADAR. La función devolverá True si es un palíndromo o
# False si no lo es. Dicho resultado será debidamente adecuado para el entendimiento del usuario
# con un mensaje.
# El número de palabras puede ser indeterminado y el programa finalizará cuando se escriba la
# palabra FIN.
# 
# Nota Final: El nombre del fichero a entregar será Py2T_2_Iniciales de nombre y apellidos
# (por ejemplo, Py2T_2_ATG.py). Utiliza comentarios para documentar el código con objeto de
# aspirar a la máxima nota del ejercicio.
# 
# PROGRAMA PALÍNDROMO
# 
# Introduzca la palabra o FIN: radar
# La palabra radar es un palíndromo
# Introduzca la palabra o FIN: arosa
# La palabra arosa no es un palíndromo
# .........
# Introduzca la palabra o FIN: FIN
# oooOOO Fin del programa OOOooo




# Función que comprueba si una palabra es un palíndromo
def es_palindromo(palabra):
    """
    Verifica si una palabra es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
    
    Argumentos:
        palabra (str): La palabra a verificar.
        
    Retorna:
        bool: True si es palíndromo, False en caso contrario.
    """
    # Comparamos la palabra original con su inversa (slicing [::-1])
    return palabra == palabra[::-1]

def obtener_entrada():
    """
    Solicita al usuario que introduzca una palabra.
    
    Retorna:
        str: La palabra introducida por el usuario, convertida a minúsculas para facilitar la comparación.
    """
    print("="*50)
    # Convertimos a minúsculas (.lower()) para que 'Ana' sea igual a 'ana'
    return input("Introduce una palabra: ").lower()

def mostrar_resultado(palabra):
    """
    Muestra por pantalla si la palabra es un palíndromo o no.
    
    Argumentos:
        palabra (str): La palabra a evaluar y mostrar.
    """
    if es_palindromo(palabra):
        print(f"La palabra '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo.")

def main():
    """
    Función principal que controla el bucle de ejecución del programa.
    """
    while True:
        # Obtenemos la entrada del usuario
        palabra = obtener_entrada()
        
        # Condición de salida: si el usuario escribe "fin", terminamos el bucle.
        if palabra == "fin":
            print("oooOOO Fin del programa OOOooo")
            break # Rompe el bucle while

        # Si no es el comando de salida, procesamos y mostramos el resultado
        mostrar_resultado(palabra)

# Punto de entrada del script.
if __name__ == "__main__":
    main()