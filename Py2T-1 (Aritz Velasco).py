import sys

# Diccionario global para almacenar el inventario.
# La estructura será: {'NombreProducto': {'cantidad': int, 'precio': float}}
inventario = {}

def mostrar_menu():
    print("="*50)
    print("PROGRAMA INVENTARIO")
    print("Menú de Opciones")
    print("="*50)
    print("1) Añadir un nuevo producto")
    print("2) Modificar el precio de un producto concreto")
    print("3) Eliminar un producto concreto")
    print("4) Consultar el valor actual del inventario")
    print("5) Presentar un listado de nombre de producto y su cantidad en stock")
    print("6) Salir")
    print("="*50)

def main():
    while True:
        mostrar_menu()
        # Solicitamos la opción al usuario
        opcion = input("Opción: ")

        # OPCIÓN 1: AÑADIR PRODUCTO
        if opcion == "1":
            print("="*50)
            print("Añadir nuevo producto")
            print("="*50)
            nombre = input("Nombre: ").capitalize() # Guardamos con la primera mayúscula por estética
            
            # Control de errores (Excepción al canto) para datos numéricos 
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio unitario: "))
                
                # Añadimos al diccionario usando el nombre como clave
                inventario[nombre] = {"cantidad": cantidad, "precio": precio}
                
                print("="*50)
                print("Añadido al inventario")
                print("="*50)
                
            except ValueError:
                print("¡Error! Debes introducir un número válido para la cantidad y el precio.")

        # OPCIÓN 2: MODIFICAR PRECIO
        elif opcion == "2":
            print("="*50)
            print("Modificar producto concreto")
            print("="*50)
            nombre = input("Nombre: ").capitalize()
            
            if nombre in inventario:
                try:
                    nuevo_precio = float(input("Nuevo precio unitario: "))
                    precio_antiguo = inventario[nombre]['precio']
                    
                    # Actualizamos el precio
                    inventario[nombre]['precio'] = nuevo_precio
                    print(f"Modificado producto {nombre} en el inventario. Antes {precio_antiguo}, ahora {nuevo_precio}") # 
                except ValueError:
                    print("¡Error! El precio debe ser un valor numérico.")
            else:
                print(f"El producto '{nombre}' no existe en el inventario.")

        # OPCIÓN 3: ELIMINAR PRODUCTO
        elif opcion == "3":
            print("="*50)
            print("Eliminar producto concreto")
            print("="*50)
            nombre = input("Nombre: ").capitalize()
            
            if nombre in inventario:
                del inventario[nombre]
                print(f"Eliminados los datos del producto {nombre} del inventario.")
            else:
                print(f"No se puede eliminar. El producto '{nombre}' no existe.")

        # OPCIÓN 4: CONSULTAR VALOR TOTAL
        elif opcion == "4":
            print("="*50)
            print("Consultar valor inventario")
            print("="*50)
            valor_total = 0.0
            
            # Recorremos el diccionario para calcular: cantidad * precio
            for producto in inventario.values():
                valor_total += producto['cantidad'] * producto['precio']
            
            # len(inventario) nos da el número de claves (productos distintos)
            print(f"Los {len(inventario)} productos del inventario tienen un valor de {valor_total:.2f}€")

        # OPCIÓN 5: LISTAR PRODUCTOS
        elif opcion == "5":
            print("="*50)
            print("Listar productos inventario")
            print(""*50)
            # Usamos f-strings con espaciado para alinear columnas (similar a la imagen del PDF)
            print(f"{'Nombre':<15} {'Cantidad':<10} {'Precio':<10}")
            
            for nombre, datos in inventario.items():
                print(f"{nombre:<15} {datos['cantidad']:<10} {datos['precio']:.2f}€")

        # OPCIÓN 6: SALIR
        elif opcion == "6":
            print("="*50)
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción no válida. Por favor, elija entre 1 y 6.")

if __name__ == "__main__":
    main()