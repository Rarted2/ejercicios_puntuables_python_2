# Función que comprueba si una palabra es un palíndromo
def esPalindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False

def main():
    while(True):
        print("="*50)
        palabra = input("Introduce una palabra: ").lower()
        # Final del programa
        if palabra == "FIN":
            print("Fin del programa.")
            break

        # Comprobamos si es palíndromo
        if esPalindromo(palabra):
            print(f"La palabra '{palabra}' es un palíndromo.")
        else:
            print(f"La palabra '{palabra}' no es un palíndromo.")


if __name__ == "__main__":
    main()