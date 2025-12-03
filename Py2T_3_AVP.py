import random

def lanzar_dado():
    """
    Simula el lanzamiento de un dado de 6 caras.
    
    Retorna:
        int: Un número entero aleatorio entre 1 y 6 (ambos inclusive).
    """
    # random.randint(a, b) devuelve un entero N tal que a <= N <= b.
    return random.randint(1, 6)

def dibujar_dado(numero):
    """
    Dibuja en la consola una representación ASCII de la cara del dado.
    
    Argumentos:
        numero (int): El número obtenido en el lanzamiento (1-6).
    """
    # Utilizamos una estructura if-elif-else para determinar qué dibujo mostrar
    # basándonos en el número recibido.
    if numero == 1:
        print()
        print("   ")
        print(" * ") # Punto central
        print("   ")
        print()
    elif numero == 2:
        print()
        print("* ") # Superior izquierda
        print("   ")
        print("  *") # Inferior derecha
        print()
    elif numero == 3:
        print()
        print("* ") # Superior izquierda
        print(" * ") # Centro
        print("  *") # Inferior derecha
        print()
    elif numero == 4:
        print()
        print("* *") # Superiores
        print("   ")
        print("* *") # Inferiores
        print()
    elif numero == 5:
        print()
        print("* *") # Superiores
        print(" * ") # Centro
        print("* *") # Inferiores
        print()
    elif numero == 6:
        print()
        print("* *") # Superiores
        print("* *") # Medios
        print("* *") # Inferiores
        print()
    else:
        # Caso de error por si se pasa un número fuera del rango 1-6
        print("Número incorrecto (no es un dado estándar)")


def main():
    """
    Función principal que gestiona la interacción con el usuario y la lógica del juego.
    """
    # Lista para almacenar los valores únicos de los dados que van saliendo.
    lista_dados = []
    
    while True:
        # Solicitamos al usuario cuántos dados quiere lanzar en esta tirada.
        try:
            numero = int(input("¿Cuántos dados lanzamos?: "))
        except ValueError:
            print("Por favor, introduce un número entero válido.")
            continue

        # Condición de salida: si el usuario introduce 0.
        if numero == 0:
            # Ordenamos la lista de números obtenidos de menor a mayor.
            lista_dados.sort()
            
            # Convertimos la lista de enteros a una cadena de texto separada por comas
            # para mostrarla de forma legible.
            texto_lista = ", ".join(str(dado) for dado in lista_dados)
            
            # Mostramos el resumen final de todos los valores únicos obtenidos.
            print("Los valores lanzados son:", texto_lista)
            print("Fin del programa.")
            break # Terminamos el bucle y el programa.

        # Bucle para realizar el número de lanzamientos solicitados.
        for i in range(numero):
            print(f"el número {i+1} ha generado aleatoriamente un: ")
            
            # Generamos el valor aleatorio
            numero_dado = lanzar_dado()
            
            # Dibujamos el dado por pantalla
            dibujar_dado(numero_dado)
            
            # Lógica de almacenamiento: Solo añadimos si NO está ya dentro de la lista.
            # Esto asegura que la lista final contenga solo valores únicos.
            if numero_dado not in lista_dados:
                lista_dados.append(numero_dado)

# Punto de entrada del script.
if __name__ == "__main__":
    main()