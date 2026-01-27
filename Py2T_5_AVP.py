import os
import time
import json

# === RUTAS DE LOS ARCHIVOS ===
# Definimos dónde guardamos las cosas
carpeta = "files"
# Creamos la carpeta al principio si no existe
if not os.path.exists(carpeta):
    os.makedirs(carpeta)

ruta_txt = os.path.join(carpeta, "mensajes.txt")
ruta_opciones = os.path.join(carpeta, "mensajes.json")
ruta_datos = os.path.join(carpeta, "abonados.json")

# ========================================================
# PARTE 1: CREAR ARCHIVOS SI NO EXISTEN (CONFIGURACIÓN)
# ========================================================
# Comprobamos si falta alguno de los archivos obligatorios
if not os.path.exists(ruta_txt) or not os.path.exists(ruta_opciones):
    print("Faltan archivos de configuración. Vamos a crearlos.")
    
    # 1. PREGUNTAR TEXTOS (TITULOS)
    titulo = input("Dime el TÍTULO PRINCIPAL: ")
    subtitulo = input("Dime el SUBTÍTULO DEL MENÚ: ")
    texto_opcion = input("Dime el texto Para pedir OPCIÓN: ")

    # 2. GUARDAR EN TXT
    with open(ruta_txt, "w", encoding="utf-8") as fichero:
        fichero.write(f"{titulo}\n")
        fichero.write(f"{subtitulo}\n")
        fichero.write(texto_opcion)

    # 3. PREGUNTAR OPCIONES DEL MENU
    print("Ahora vamos a configurar las opciones del menú (1 al 6):")
    
    # Creamos un diccionario vacío
    mi_menu = {}

    mi_menu["1"] = input("Texto para Opción 1 [Alta]: ")
    mi_menu["2"] = input("Texto para Opción 2 [Modificar]: ")
    mi_menu["3"] = input("Texto para Opción 3 [Consulta]: ")
    mi_menu["4"] = input("Texto para Opción 4 [Total]: ")
    mi_menu["5"] = input("Texto para Opción 5 [Eliminar]: ")
    mi_menu["6"] = input("Texto para Opción 6 [Salir]: ")

    # 4. GUARDAR EN JSON
    with open(ruta_opciones, "w", encoding="utf-8") as fichero_json:
        json.dump(mi_menu, fichero_json, indent=4)
    
    print("Archivos creados correctamente.\n")
    time.sleep(2)

# ========================================================
# PARTE 2: CARGAR LOS DATOS PARA EMPEZAR
# ========================================================

# LEEMOS EL TXT
with open(ruta_txt, "r", encoding="utf-8") as fichero:
    # .read().splitlines() lee todo y quita los saltos de línea
    lineas = fichero.read().splitlines()

titulo = lineas[0]
subtitulo = lineas[1]
# La tercera linea puede no existir si el archivo es viejo, pero en tu caso existirá.
# Para hacerlo básico asumimos que siempre está bien creado.
texto_opcion = lineas[2]

# LEEMOS EL MENU (JSON)
with open(ruta_opciones, "r", encoding="utf-8") as fichero_json:
    menu_opciones = json.load(fichero_json)

# LEEMOS LOS ABONADOS (JSON)
# Si el archivo NO existe, empezamos con diccionario vacío
if os.path.exists(ruta_datos):
    with open(ruta_datos, "r", encoding="utf-8") as f_datos:
        abonados = json.load(f_datos)
else:
    abonados = {}


# ========================================================
# PARTE 3: BUCLE PRINCIPAL DEL PROGRAMA
# ========================================================
while True:
    # Mostramos titulos
    print("\n-------------------------")
    print(titulo)
    print("-------------------------")
    print(subtitulo)
    print("=========================")

    # Mostramos las opciones (1 al 6)
    print(f"1) {menu_opciones['1']}")
    print(f"2) {menu_opciones['2']}")
    print(f"3) {menu_opciones['3']}")
    print(f"4) {menu_opciones['4']}")
    print(f"5) {menu_opciones['5']}")
    print(f"6) {menu_opciones['6']}")
    print("=========================")

    # Pedimos la opción
    opcion_elegida = input(texto_opcion)

    # -----------------------------------------------
    # OPCIÓN 1: ALTA
    if opcion_elegida == "1":
        print("--- NUEVO ABONADO ---")
        nombre = input("Nombre: ").title() # .title() pone mayúscula inicial
        
        # Verificamos si ya existe
        if nombre in abonados:
            print("Ese nombre YA EXISTE.")
        else:
            dinero = float(input("Factura (€): "))
            abonados[nombre] = dinero
            
            # Guardamos cada vez que cambiamos algo
            with open(ruta_datos, "w", encoding="utf-8") as f:
                json.dump(abonados, f)
            print("Guardado.")

    # -----------------------------------------------
    # OPCIÓN 2: MODIFICAR
    elif opcion_elegida == "2":
        print("--- MODIFICAR ---")
        nombre = input("Nombre a buscar: ").title()

        if nombre in abonados:
            print(f"Factura actual: {abonados[nombre]}")
            nueva_factura = float(input("Nueva factura: "))
            abonados[nombre] = nueva_factura
            
            # Guardar
            with open(ruta_datos, "w", encoding="utf-8") as f:
                json.dump(abonados, f)
            print("Modificado correctamente.")
        else:
            print("No encuentro a ese abonado.")

    # -----------------------------------------------
    # OPCIÓN 3: CONSULTAR UNO
    elif opcion_elegida == "3":
        print("--- CONSULTA ---")
        nombre = input("Nombre a buscar: ").title()

        if nombre in abonados:
            # Mostramos el nombre y su valor
            print(f"Abonado: {nombre}")
            print(f"Factura: {abonados[nombre]} euros")
        else:
            print("No existe.")

    # -----------------------------------------------
    # OPCIÓN 4: TOTAL
    elif opcion_elegida == "4":
        print("--- TOTAL COMPAÑÍA ---")
        # .values() devuelve solo los números (las facturas)
        lista_facturas = abonados.values()
        suma_total = sum(lista_facturas)
        
        print(f"Dinero total: {suma_total} euros")
        print(f"Clientes: {len(abonados)}")

    # -----------------------------------------------
    # OPCIÓN 5: BORRAR FICHERO
    elif opcion_elegida == "5":
        seguro = input("¿Borrar fichero de datos? (s/n): ")
        if seguro == "s":
            if os.path.exists(ruta_datos):
                os.remove(ruta_datos)
                abonados = {} # Vaciamos la memoria también
                print("Archivo borrado.")
            else:
                print("No existía archivo para borrar.")

    # -----------------------------------------------
    # OPCIÓN 6: SALIR
    elif opcion_elegida == "6":
        print("¡Adiós!")
        time.sleep(2)
        break # Esto hace que el while se termine

    # -----------------------------------------------
    else:
        print("Opción incorrecta.")
    
    time.sleep(2)