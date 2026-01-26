import os
import json

# ==========================================
# CONFIGURACIÓN E INICIALIZACIÓN
# ==========================================
RUTA_DIR = "files"
RUTA_FICHERO = os.path.join(RUTA_DIR, "inventario.json")

# Crear carpeta si no existe
os.makedirs(RUTA_DIR, exist_ok=True)

# Intentar cargar inventario existente
try:
    with open(RUTA_FICHERO, "r") as f:
        inventario = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    inventario = {}  # Inventario vacío si falla la carga

# ==========================================
# BUCLE PRINCIPAL
# ==========================================
while True:
    print("\n" + "="*30)
    print("      GESTIÓN INVENTARIO")
    print("="*30)
    print("1. Añadir / Actualizar Producto")
    print("2. Modificar Precio")
    print("3. Eliminar Producto")
    print("4. Valor Total del Inventario")
    print("5. Listar Stock")
    print("6. Guardar y Salir")
    
    opcion = input("\n> Elige una opción: ")

    # --------------------------------------------------
    # 1. Añadir o Actualizar producto
    # --------------------------------------------------
    if opcion == "1":
        print("\n--- NUEVO PRODUCTO ---")
        nombre = input("Nombre del producto: ")
        
        try:
            precio = float(input("Precio (€): "))
            cantidad = int(input("Cantidad: "))
            
            inventario[nombre] = {
                "precio": precio,
                "cantidad": cantidad
            }
            print(f"Producto '{nombre}' guardado correctamente.")
        except ValueError:
            print("Error: Debes introducir números válidos.")

    # --------------------------------------------------
    # 2. Modificar precio
    # --------------------------------------------------
    elif opcion == "2":
        print("\n--- MODIFICAR PRECIO ---")
        nombre = input("Nombre del producto: ")
        
        if nombre in inventario:
            try:
                nuevo_precio = float(input(f"Nuevo precio para '{nombre}': "))
                inventario[nombre]["precio"] = nuevo_precio
                print(f"Precio actualizado a {nuevo_precio:.2f}€.")
            except ValueError:
                print("Error: El precio debe ser un número.")
        else:
            print("Error: Producto no encontrado.")

    # --------------------------------------------------
    # 3. Eliminar producto
    # --------------------------------------------------
    elif opcion == "3":
        print("\n--- ELIMINAR PRODUCTO ---")
        nombre = input("Nombre del producto: ")
        
        if nombre in inventario:
            del inventario[nombre]
            print(f"Producto '{nombre}' eliminado del inventario.")
        else:
            print("Error: Producto no encontrado.")

    # --------------------------------------------------
    # 4. Calcular valor total
    # --------------------------------------------------
    elif opcion == "4":
        total = sum(item["precio"] * item["cantidad"] for item in inventario.values())
        print(f"\nValor total del inventario: {total:.2f}€")

    # --------------------------------------------------
    # 5. Listar stock
    # --------------------------------------------------
    elif opcion == "5":
        print("\n--- STOCK ACTUAL ---")
        if not inventario:
            print("(El inventario está vacío)")
        else:
            for nombre, datos in inventario.items():
                print(f"- {nombre}: {datos['cantidad']} u.  |  {datos['precio']:.2f}€")

    # --------------------------------------------------
    # 6. Guardar y Salir
    # --------------------------------------------------
    elif opcion == "6":
        with open(RUTA_FICHERO, "w") as f:
            json.dump(inventario, f, indent=4)
        print(f"\nCambios guardados en '{RUTA_FICHERO}'.")
        print("¡Adiós!")
        break

    # --------------------------------------------------
    # Opción no válida
    # --------------------------------------------------
    else:
        print("Opción no reconocida. Inténtalo de nuevo.")