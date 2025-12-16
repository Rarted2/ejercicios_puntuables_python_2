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
    # Comparamos la palabra original con su inversa (slicing [::-1])
    return palabra == palabra[::-1]

def main():
    while True:
        # Obtenemos la entrada del usuario
        palabra = input("Introduzca la palabra o FIN: ").lower()
        
        # Condición de salida: si el usuario escribe "fin", terminamos el bucle.
        if palabra == "fin":
            print("oooOOO Fin del programa OOOooo")
            break # Rompe el bucle while

        # Si no es el comando de salida, procesamos y mostramos el resultado
        if es_palindromo(palabra):
            print(f"La palabra {palabra} es un palíndromo")
        else:
            print(f"La palabra {palabra} no es un palíndromo")

# Punto de entrada del script.
if __name__ == "__main__":
    main()