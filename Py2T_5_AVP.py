import os
import json

# --- CONSTANTES: Nombres de los ficheros ---
# Definimos las rutas de los archivos de forma centralizada para facilitar cambios futuros.
# os.path.join asegura que la ruta sea correcta independientemente del sistema operativo (Windows/Linux/Mac).
FICH_TITULOS = os.path.join("files", "mensajes.txt")
FICH_OPCIONES = os.path.join("files", "mensajes.json")
FICH_DATOS = os.path.join("files", "abonados.json")

# ==========================================
# BLOQUE 1: GESTIÓN DE FICHEROS DE CONFIGURACIÓN
# ==========================================

def configurar_sistema():
    """
    Verifica si existen los ficheros de configuración del menú.
    Si no existen, solicita al usuario que los cree (rellenado por teclado).
    """
    # Crea el directorio 'files' si no existe. exist_ok=True evita error si ya existe.
    os.makedirs("files", exist_ok=True)
    
    # Comprobamos si faltan los archivos de configuración.
    if not os.path.exists(FICH_TITULOS) or not os.path.exists(FICH_OPCIONES):
        print("AVISO: Ficheros de configuración no encontrados. Iniciando configuración inicial...\n")
        crear_ficheros_configuracion()
    else:
        # Opcional: Podríamos cargar silenciosamente, pero no es necesario imprimir nada si todo está bien.
        pass

def crear_ficheros_configuracion():
    """
    Pide al usuario los títulos y las opciones del menú y genera los ficheros
    mensajes.txt y mensajes.json.
    """
    print("--- Configuración de Títulos (mensajes.txt) ---")
    titulo_principal = input("Introduce el Título Principal (ej. PROGRAMA GESTIÓN COMPAÑÍA): ")
    subtitulo = input("Introduce el Subtítulo (ej. Menú de Opciones): ")
    
    # Guardamos los títulos en texto plano en el archivo mensajes.txt
    with open(FICH_TITULOS, "w", encoding="utf-8") as f:
        f.write(titulo_principal + "\n")
        f.write(subtitulo + "\n")
    print(f"-> {FICH_TITULOS} generado correctamente.\n")

    print("--- Configuración de Opciones (mensajes.json) ---")
    opciones = {}
    # Sabemos que son 6 opciones fijas según el enunciado
    textos_default = [
        "Alta de nuevos abonados",
        "Modificación del valor de la factura de un abonado",
        "Consulta del dato de facturación de un abonado",
        "Consulta del dato de facturación total de la compañía",
        "Eliminar el fichero de datos",
        "Salir"
    ]
    
    # Iteramos para pedir el texto de cada opción, ofreciendo un valor por defecto.
    for i, texto_defecto in enumerate(textos_default, 1):
        # Le mostramos una sugerencia al usuario, pero le dejamos escribir lo que quiera
        entrada = input(f"Introduce texto para opción {i} [{texto_defecto}]: ")
        # Si pulsa enter sin escribir, usamos el texto por defecto
        opciones[str(i)] = entrada if entrada.strip() else texto_defecto
    
    # Guardamos las opciones en formato JSON para preservar la estructura diccionario.
    with open(FICH_OPCIONES, "w", encoding="utf-8") as f:
        json.dump(opciones, f, indent=4)
    print(f"-> {FICH_OPCIONES} generado correctamente.\n")


def mostrar_menu():
    """
    Lee los ficheros de configuración y muestra el menú por pantalla.
    """
    print()
    # 1. Mostrar títulos desde .txt
    if os.path.exists(FICH_TITULOS):
        with open(FICH_TITULOS, "r", encoding="utf-8") as f:
            print(f.read().strip())
        print("=" * 20)
    
    # 2. Mostrar opciones desde .json
    if os.path.exists(FICH_OPCIONES):
        with open(FICH_OPCIONES, "r", encoding="utf-8") as f:
            opciones = json.load(f)
            # Iteramos sobre las opciones cargadas para imprimirlas ordenadamente.
            for k, v in opciones.items():
                print(f"{k}) {v}")


# ==========================================
# BLOQUE 2: GESTIÓN DE DATOS (ABONADOS)
# ==========================================

def cargar_datos():
    """
    Recupera el diccionario de abonados del fichero JSON.
    
    Retorna:
        dict: Diccionario con los datos cargados, o vacío si no existe el fichero o hay error.
    """
    if not os.path.exists(FICH_DATOS):
        return {}
    try:
        with open(FICH_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Si el archivo está corrupto o vacío, devolvemos un diccionario vacío para evitar crash.
        return {}

def guardar_datos(datos):
    """
    Guarda el diccionario de abonados en el fichero JSON.
    
    Argumentos:
        datos (dict): El diccionario de abonados a persistir.
    """
    with open(FICH_DATOS, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

# ==========================================
# BLOQUE 3: LÓGICA DE LAS OPCIONES
# ==========================================

def alta_abonado():
    """Añade un nuevo abonado al diccionario y lo guarda en el fichero JSON."""
    datos = cargar_datos()
    nombre = input("\nNombre del nuevo abonado: ").strip().title()
    
    # Verificamos duplicados
    if nombre in datos:
        print("¡Error! Ese abonado ya existe.")
    else:
        try:
            factura = float(input("Valor de la factura (€): "))
            datos[nombre] = factura
            # Guardamos inmediatamente para persistir el cambio
            guardar_datos(datos)
            print(f"Abonado '{nombre}' dado de alta con {factura}€.")
        except ValueError:
            print("Error: El valor de la factura debe ser numérico.")

def modificar_factura():
    """Modifica el valor de la factura de un abonado existente."""
    datos = cargar_datos()
    nombre = input("\nNombre del abonado a modificar: ").strip().title()
    
    if nombre not in datos:
        print("Error: Abonado no encontrado.")
    else:
        try:
            nueva_factura = float(input(f"Factura actual ({datos[nombre]}€). Nuevo valor: "))
            datos[nombre] = nueva_factura
            guardar_datos(datos)
            print("Factura actualizada correctamente.")
        except ValueError:
            print("Error: Valor incorrecto.")

def consultar_abonado():
    """Consulta el valor de la factura de un abonado existente."""
    datos = cargar_datos()
    nombre = input("\nNombre del abonado a consultar: ").strip().title()
    
    if nombre in datos:
        print(f"La factura de '{nombre}' asciende a: {datos[nombre]}€")
    else:
        print("Abonado no encontrado en la base de datos.")

def consultar_total():
    """Consulta el valor total de la facturación de la compañía."""
    datos = cargar_datos()
    if not datos:
        print("\nNo hay datos de facturación registrados.")
    else:
        # Sumamos todos los valores (facturas) del diccionario
        total = sum(datos.values())
        num_clientes = len(datos)
        print(f"\nFacturación Total de la Compañía: {total:.2f}€ ({num_clientes} abonados)")

def eliminar_fichero_datos():
    """Elimina el fichero de datos si existe, reseteando el sistema."""
    if os.path.exists(FICH_DATOS):
        confirmacion = input("\n¿Seguro que quieres BORRAR TODOS los datos de abonados? (s/n): ").lower()
        if confirmacion == 's':
            os.remove(FICH_DATOS)
            print("Fichero de datos eliminado. Se ha reiniciado el sistema.")
        else:
            print("Operación cancelada.")
    else:
        print("\nNo existe fichero de datos para eliminar.")

# ==========================================
# BLOQUE 4: FLUJO PRINCIPAL
# ==========================================

def main():
    """
    Función principal que orquesta el flujo del programa.
    """
    # Paso 0: Asegurar que existen los ficheros de menú antes de empezar
    configurar_sistema()
    
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("\nOpción: ")
        
        # Dispatcher de opciones
        if opcion == "1":
            alta_abonado()
        elif opcion == "2":
            modificar_factura()
        elif opcion == "3":
            consultar_abonado()
        elif opcion == "4":
            consultar_total()
        elif opcion == "5":
            eliminar_fichero_datos()
        elif opcion == "6":
            print("Saliendo del programa...")
            continuar = False
        else:
            print("Opción no válida. Por favor, elija entre 1 y 6.")

if __name__ == "__main__":
    main()