import random

# Definición compacta de las caras del dado para impresión (índice 0 vacío para alinear 1-6)
dados_dibujo = [
    "", 
    "\n   \n * \n   \n", "\n*  \n   \n  *\n", "\n*  \n * \n  *\n", 
    "\n* *\n   \n* *\n", "\n* *\n * \n* *\n", "\n* *\n* *\n* *\n"
]
lista_dados = [] # Almacena números únicos que han salido

# Bucle principal hasta que el usuario decida salir con '0'
while True:
    try:
        if (n_lanzamientos := int(input("¿Cuántos dados lanzamos? (0 para salir): "))) == 0:
            # Al salir: ordenar, formatear y mostrar los valores únicos obtenidos
            print(f"Valores lanzados: {', '.join(map(str, sorted(lista_dados)))}\nFin del programa.")
            break
            
        for i in range(n_lanzamientos):
            # Generar número, dibujar dado y añadir a la lista si es nuevo
            val = random.randint(1, 6)
            print(f"El lanzamiento {i+1} ha generado un {val}:{dados_dibujo[val]}")
            if val not in lista_dados: lista_dados.append(val)
            
    except ValueError: print("Por favor, introduce un número entero válido.")