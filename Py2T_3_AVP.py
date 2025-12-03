import random

def lanzar_dado():
    # Genera un número entero aleatorio incluyendo el 1 y el 6
    return random.randint(1, 6)

def dibujar_dado(numero):
    if numero == 1:
        print()
        print("   ")
        print(" * ")
        print("   ")
        print()
    elif numero == 2:
        print()
        print("* ")
        print("   ")
        print("  *")
        print()
    elif numero == 3:
        print()
        print("* ")
        print(" * ")
        print("  *")
        print()
    elif numero == 4:
        print()
        print("* *")
        print("   ")
        print("* *")
        print()
    elif numero == 5:
        print()
        print("* *")
        print(" * ")
        print("* *")
        print()
    elif numero == 6:
        print()
        print("* *")
        print("* *")
        print("* *")
        print()
    else:
        print("Número incorrecto (no es un dado estándar)")


def main():
    # Lista para almacenar los valores de los dados
    lista_dados = []
    while True:
        numero = int(input("¿Cuántos dados lanzamos?: "))
        # Salimos del bucle
        if numero == 0:
            # Ordenamos la lista y la convertimos a string, separado por comas
            lista_dados.sort()
            texto_lista = ", ".join(str(dado) for dado in lista_dados)
            # Mostramos la lista
            print("Los valores lanzados son:", texto_lista)
            print("Fin del programa.")
            break

        # Lanzamos los dados
        for i in range(numero):
            print(f"el número {i+1} ha generado aleatoriamente un: ")
            numero_dado = lanzar_dado()
            dibujar_dado(numero_dado)
            
            # Solo añadimos si NO está ya dentro
            if numero_dado not in lista_dados:
                lista_dados.append(numero_dado)

if __name__ == "__main__":
    main()


    