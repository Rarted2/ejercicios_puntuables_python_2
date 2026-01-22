# Diccionario para el inventario: {nombre: [cantidad, precio]}
inventario = {}

# Bucle principal que muestra el menú y gestiona las opciones hasta que el usuario elija Salir (6)
while True:
    print("="*50 + "\nPROGRAMA INVENTARIO\n" + "="*50 + "\n1) Añadir\n2) Modificar precio\n3) Eliminar\n4) Valor total\n5) Listar\n6) Salir\n" + "="*50)
    opcion = input("Opción: ")

    if opcion == "1": # Añadir producto
        try:
            nombre = input("Nombre: ").capitalize()
            # Se añaden cantidad y precio como una lista al diccionario
            inventario[nombre] = [int(input("Cantidad: ")), float(input("Precio unitario: "))]
            print("Añadido al inventario")
        except ValueError: print("¡Error! Debes introducir números válidos.")

    elif opcion == "2": # Modificar precio
        nombre = input("Nombre: ").capitalize()
        # Se verifica existencia y se actualiza el precio (índice 1 de la lista)
        if nombre in inventario:
            try:
                nuevo = float(input("Nuevo precio: "))
                print(f"Modificado {nombre}. Antes {inventario[nombre][1]}, ahora {nuevo}")
                inventario[nombre][1] = nuevo
            except ValueError: print("Error: Precio inválido.")
        else: print(f"El producto '{nombre}' no existe.")

    elif opcion == "3": # Eliminar producto
        # Si existe, se elimina la clave del diccionario; si no, se avisa
        print(f"Eliminado {input('Nombre: ').capitalize()}" if input('Nombre: ').capitalize() in inventario and not inventario.pop(input('Nombre: ').capitalize(), None) else "No existe.")

    elif opcion == "4": # Consultar valor total
        # Suma de (cantidad * precio) para todos los items
        print(f"Los {len(inventario)} productos valen {sum(d[0]*d[1] for d in inventario.values()):.2f}€")

    elif opcion == "5": # Listar productos
        print(f"{'Nombre':<15} {'Cantidad':<10} {'Precio':<10}")
        # Se recorre y muestra cada producto formateado
        for n, d in inventario.items(): print(f"{n:<15} {d[0]:<10} {d[1]:.2f}€")

    elif opcion == "6": # Salir
        print("Saliendo..."); break

    else: print("Opción no válida.")