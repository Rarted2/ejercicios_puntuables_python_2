import os, json

# --- CONFIGURACIÓN E INICIALIZACIÓN ---
RUTA_DIR = "files"
RUTA_FICHERO = os.path.join(RUTA_DIR, "inventario.json")

# Crear carpeta si no existe y cargar datos
os.makedirs(RUTA_DIR, exist_ok=True)
try:
    with open(RUTA_FICHERO, "r") as f: inventario = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    inventario = {}  # Inventario vacío si falla la carga

# --- BUCLE PRINCIPAL ---
while True:
    print("\n--- GESTIÓN INVENTARIO ---\n1. Añadir\n2. Modificar Precio\n3. Eliminar\n4. Valor Inventario\n5. Listar Stock\n6. Salir")
    opcion = input("Opción: ")

    if opcion == "1":  # Añadir/Actualizar producto
        nombre = input("Nombre del producto: ")
        inventario[nombre] = {"precio": float(input("Precio: ")), "cantidad": int(input("Cantidad: "))}
        print(f"Producto '{nombre}' añadido/actualizado.")

    elif opcion == "2":  # Modificar precio
        nombre = input("Nombre del producto a modificar: ")
        if nombre in inventario:
            inventario[nombre]["precio"] = float(input(f"Nuevo precio para {nombre}: "))
        else: print("Error: Producto no encontrado.")

    elif opcion == "3":  # Eliminar producto
        nombre = input("Nombre del producto a eliminar: ")
        if nombre in inventario: 
            del inventario[nombre]
            print("Producto eliminado.")
        else: print("Error: Producto no encontrado.")

    elif opcion == "4":  # Calcular valor total del inventario
        total = sum(item["precio"] * item["cantidad"] for item in inventario.values())
        print(f"Valor total del inventario: {total:.2f}€")

    elif opcion == "5":  # Listar stock actual
        print("\n--- STOCK ACTUAL ---")
        for nombre, datos in inventario.items():
            print(f"- {nombre}: {datos['cantidad']} unidades")

    elif opcion == "6":  # Guardar y Salir
        with open(RUTA_FICHERO, "w") as f:
            json.dump(inventario, f, indent=4)
        print(f"Cambios guardados en '{RUTA_FICHERO}'. ¡Adiós!")
        break

    else: print("Opción no válida.")