# Diccionario global para almacenar el inventario.
# La estructura será: {'NombreProducto': {'cantidad': int, 'precio': float}}
# Este diccionario actúa como la base de datos en memoria del programa.
inventario = {}

def mostrar_menu():
    """
    Muestra el menú de opciones disponibles en el programa.
    No recibe parámetros ni devuelve nada, solo imprime por pantalla las opciones
    para que el usuario sepa qué números introducir.
    """
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

def anadir_producto(inventario):
    """
    Solicita los datos de un nuevo producto y lo añade al inventario.
    
    Argumentos:
        inventario (dict): El diccionario donde se almacenan los productos.
    """
    print("Añadir nuevo producto")
    print("="*50)
    # Solicitamos el nombre y lo capitalizamos para mantener consistencia (ej. "manzana" -> "Manzana")
    # Esto ayuda a evitar duplicados por diferencias de mayúsculas/minúsculas.
    nombre = input("Nombre: ").capitalize() 
    
    # Control de errores para asegurar que cantidad y precio sean numéricos
    # Utilizamos un bloque try-except para capturar errores de conversión de tipos.
    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio unitario: "))
        
        # Añadimos el nuevo producto al diccionario usando el nombre como clave
        # El valor es otro diccionario con la cantidad y el precio, creando una estructura anidada.
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
        
        print("Añadido al inventario")
        
    except ValueError:
        # Si el usuario introduce texto en lugar de números, capturamos el error
        # y mostramos un mensaje amigable en lugar de que el programa falle.
        print("¡Error! Debes introducir un número válido para la cantidad y el precio.")

def modificar_precio(inventario):
    """
    Modifica el precio de un producto existente en el inventario.
    
    Argumentos:
        inventario (dict): El diccionario donde se almacenan los productos.
    """
    print("Modificar producto concreto")
    print("="*50)
    nombre = input("Nombre: ").capitalize()
    
    # Verificamos si el producto existe antes de intentar modificarlo
    # Esto previene errores de clave no encontrada (KeyError).
    if nombre in inventario:
        try:
            nuevo_precio = float(input("Nuevo precio unitario: "))
            # Guardamos el precio antiguo para mostrarlo en el mensaje de confirmación
            # Accedemos al diccionario interno del producto para obtener el precio actual.
            precio_antiguo = inventario[nombre]['precio']
            
            # Actualizamos el precio en el diccionario con el nuevo valor.
            inventario[nombre]['precio'] = nuevo_precio
            print(f"Modificado producto {nombre} en el inventario. Antes {precio_antiguo}, ahora {nuevo_precio}")
        except ValueError:
            print("¡Error! El precio debe ser un valor numérico.")
    else:
        # Informamos al usuario si el producto no se encuentra en el inventario.
        print(f"El producto '{nombre}' no existe en el inventario.")

def eliminar_producto(inventario):
    """
    Elimina un producto del inventario si existe.
    
    Argumentos:
        inventario (dict): El diccionario donde se almacenan los productos.
    """
    print("Eliminar producto concreto")
    print("="*50)
    nombre = input("Nombre: ").capitalize()
    
    # Verificamos si el producto existe antes de intentar borrarlo.
    if nombre in inventario:
        # Usamos 'del' para eliminar la clave del diccionario y liberar memoria.
        del inventario[nombre]
        print(f"Eliminados los datos del producto {nombre} del inventario.")
    else:
        print(f"No se puede eliminar. El producto '{nombre}' no existe.")

def consultar_valor_total(inventario):
    """
    Calcula y muestra el valor total de todos los productos en el inventario.
    El valor se calcula como la suma de (cantidad * precio) de cada producto.
    
    Argumentos:
        inventario (dict): El diccionario donde se almacenan los productos.
    """
    print("Consultar valor inventario")
    print("="*50)
    valor_total = 0.0
    
    # Recorremos todos los productos (valores del diccionario principal).
    # Cada 'producto' es un diccionario con 'cantidad' y 'precio'.
    for producto in inventario.values():
        # Sumamos: cantidad * precio de cada producto al acumulador total.
        valor_total += producto['cantidad'] * producto['precio']
    
    # Mostramos el total formateado con 2 decimales para representar centavos.
    # len(inventario) nos da la cantidad de claves (productos distintos) en el diccionario.
    print(f"Los {len(inventario)} productos del inventario tienen un valor de {valor_total:.2f}€")

def listar_productos(inventario):
    """
    Muestra un listado formateado de todos los productos, sus cantidades y precios.
    Utiliza formato de cadenas para alinear las columnas.
    
    Argumentos:
        inventario (dict): El diccionario donde se almacenan los productos.
    """
    print("="*50)
    print("Listar productos inventario")
    print(""*50)
    # Imprimimos la cabecera de la tabla con alineación a la izquierda (<) y ancho fijo.
    print(f"{'Nombre':<15} {'Cantidad':<10} {'Precio':<10}")
    
    # Recorremos items() para obtener clave (nombre) y valor (datos) al mismo tiempo.
    for nombre, datos in inventario.items():
        # Imprimimos cada fila respetando el mismo ancho que la cabecera.
        print(f"{nombre:<15} {datos['cantidad']:<10} {datos['precio']:.2f}€")

def main():
    """
    Función principal que controla el flujo del programa.
    Contiene el bucle principal que mantiene el programa en ejecución hasta que el usuario decida salir.
    """
    while True:
        # Mostramos el menú en cada iteración para que el usuario vea las opciones.
        mostrar_menu()
        opcion = input("Opción: ")

        # Estructura condicional para derivar a la función correspondiente según la opción elegida.
        if opcion == "1":
            anadir_producto(inventario)
            
        elif opcion == "2":
            modificar_precio(inventario)
            
        elif opcion == "3":
            eliminar_producto(inventario)
            
        elif opcion == "4":
            consultar_valor_total(inventario)
            
        elif opcion == "5":
            listar_productos(inventario)
            
        elif opcion == "6":
            print("Saliendo del programa...")
            break # Rompe el bucle while y termina la ejecución de main(), finalizando el programa.
            
        else:
            # Manejo de opciones no válidas para dar feedback al usuario.
            print("Opción no válida. Por favor, elija entre 1 y 6.")

# Punto de entrada del script.
# Esto asegura que main() solo se ejecute si el archivo se ejecuta directamente,
# y no si se importa como módulo en otro script.
if __name__ == "__main__":
    main()