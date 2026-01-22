import os, json

# Rutas de ficheros
os.makedirs("files", exist_ok=True)
R_TIT, R_OPC, R_DAT = os.path.join("files", "mensajes.txt"), os.path.join("files", "mensajes.json"), os.path.join("files", "abonados.json")

# Configurar ficheros si no existen
if not os.path.exists(R_TIT) or not os.path.exists(R_OPC):
    print("AVISO: Configuración no encontrada. Iniciando...\n--- Configuración ---")
    open(R_TIT, "w").write(f"{input('Título Principal: ')}\n{input('Subtítulo: ')}\n")
    # Crear diccionario de opciones pidiendo input o usando defecto
    texto = ["Alta", "Modificación", "Consulta abonado", "Consulta total", "Eliminar fichero", "Salir"]
    json.dump({str(i): (input(f"Texto opción {i} [{t}]: ").strip() or t) for i, t in enumerate(texto, 1)}, open(R_OPC, "w"), indent=4)

# Bucle principal
while True:
    # Mostrar título y menú cargado desde ficheros
    print(f"\n{open(R_TIT).read().strip()}\n" + "="*20)
    opciones = json.load(open(R_OPC))
    for k, v in opciones.items(): print(f"{k}) {v}")

    op = input("\nOpción: ")
    datos = json.load(open(R_DAT)) if os.path.exists(R_DAT) else {} # Cargar datos

    if op == "1": # Alta
        if (nom := input("Nombre: ").title()) in datos: print("¡Error! Ya existe.")
        else:
            try: datos[nom] = float(input("Factura (€): ")); json.dump(datos, open(R_DAT, "w"), indent=4); print(f"Abonado '{nom}' añadido.")
            except ValueError: print("Error: Valor numérico requerido.")

    elif op == "2": # Modificar
        if (nom := input("Nombre: ").title()) in datos:
            try: datos[nom] = float(input(f"Factura actual ({datos[nom]}€). Nueva: ")); json.dump(datos, open(R_DAT, "w"), indent=4); print("Actualizado.")
            except ValueError: print("Error numérico.")
        else: print("No encontrado.")

    elif op == "3": # Consultar uno
        print(f"Factura: {datos[input('Nombre: ').title()]}€" if (nom := input("Nombre: ").title()) in datos else "No encontrado.") 

    elif op == "4": # Consultar total
        print(f"Facturación Total: {sum(datos.values()):.2f}€ ({len(datos)} abonados)" if datos else "Sin datos.")

    elif op == "5": # Eliminar fichero
        if os.path.exists(R_DAT) and input("¿Borrar todo? (s/n): ").lower() == 's': os.remove(R_DAT); print("Eliminado.")
    
    elif op == "6": break # Salir
    else: print("Opción no válida.")