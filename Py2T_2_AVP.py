"""
Programa para comprobar si una palabra es un palíndromo.
Un palíndromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda.
"""

def es_palindromo(texto):
    # Eliminamos espacios y convertimos a minúsculas para una comprobación precisa
    limpio = texto.replace(" ", "").lower()
    return limpio == limpio[::-1]

def main():
    print("=" * 40)
    print("DETECTOR DE PALÍNDROMOS")
    print("=" * 40)
    print("Instrucciones: Escriba palabras para comprobar si son palíndromos.")
    print("Escriba 'FIN' para salir del programa.\n")

    while True:
        entrada = input("Introduzca una palabra o frase: ").strip()
        
        if entrada.upper() == "FIN":
            break
            
        if not entrada:
            print("Por favor, introduzca algo de texto.")
            continue

        if es_palindromo(entrada):
            print(f"-> '{entrada}' SÍ es un palíndromo.")
        else:
            print(f"-> '{entrada}' NO es un palíndromo.")
            
    print("\n" + "=" * 40)
    print("Fin del programa. ¡Hasta pronto!")
    print("=" * 40)

if __name__ == "__main__":
    main()