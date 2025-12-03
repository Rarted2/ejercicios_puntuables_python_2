# Función que comprueba si una palabra es un palíndromo
def esPalindromo(palabra):
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
    if esPalindromo(palabra):
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
            print("Fin del programa.")
            break # Rompe el bucle while

        # Si no es el comando de salida, procesamos y mostramos el resultado
        mostrar_resultado(palabra)

# Punto de entrada del script.
if __name__ == "__main__":
    main()