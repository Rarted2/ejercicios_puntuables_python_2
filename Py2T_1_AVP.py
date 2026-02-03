"""
Programa de gestión de inventario.
Permite añadir, modificar, eliminar, listar y calcular el valor total de los productos.
"""

# Diccionario para el inventario: {nombre: [cantidad, precio]}
inventario = {}

def mostrar_menu():
    print("=" * 50)
    print("PROGRAMA INVENTARIO")
    print("=" * 50)
    print("1) Añadir")
    print("2) Modificar precio")
    print("3) Eliminar")
    print("4) Valor total")
    print("5) Listar")
    print("6) Salir")
    print("=" * 50)

def añadir_producto():
    try:
        nombre = input("Nombre: ").strip().capitalize()
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio unitario: "))
        inventario[nombre] = [cantidad, precio]
        print(f"Producto '{nombre}' añadido al inventario.")
    except ValueError:
        print("¡Error! Debes introducir números válidos para cantidad y precio.")

def modificar_precio():
    nombre = input("Nombre del producto a modificar: ").strip().capitalize()
    if nombre in inventario:
        try:
            nuevo_precio = float(input("Nuevo precio: "))
            precio_anterior = inventario[nombre][1]
            inventario[nombre][1] = nuevo_precio
            print(f"Modificado {nombre}. Antes: {precio_anterior:.2f}€, ahora: {nuevo_precio:.2f}€")
        except ValueError:
            print("Error: Precio inválido.")
    else:
        print(f"El producto '{nombre}' no existe.")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ").strip().capitalize()
    if nombre in inventario:
        inventario.pop(nombre)
        print(f"Producto '{nombre}' eliminado correctamente.")
    else:
        print(f"El producto '{nombre}' no existe.")

def calcular_valor_total():
    if not inventario:
        print("El inventario está vacío.")
        return

    total = sum(datos[0] * datos[1] for datos in inventario.values())
    print(f"Los {len(inventario)} productos valen un total de {total:.2f}€")

def listar_productos():
    if not inventario:
        print("El inventario está vacío.")
        return

    print(f"\n{'Nombre':<15} {'Cantidad':<10} {'Precio':<10}")
    print("-" * 35)
    for nombre, datos in inventario.items():
        cantidad, precio = datos
        print(f"{nombre:<15} {cantidad:<10} {precio:>8.2f}€")

def main():
    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            añadir_producto()
        elif opcion == "2":
            modificar_precio()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            calcular_valor_total()
        elif opcion == "5":
            listar_productos()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()