import os
import json

# Rutas de almacenamiento
FICH_TITULOS = os.path.join("files", "mensajes.txt")
FICH_OPCIONES = os.path.join("files", "mensajes.json")
FICH_DATOS = os.path.join("files", "abonados.json")

def configurar_sistema():
    os.makedirs("files", exist_ok=True)
    if not os.path.exists(FICH_TITULOS) or not os.path.exists(FICH_OPCIONES):
        print("AVISO: Ficheros de configuración no encontrados. Iniciando configuración...\n")
        crear_ficheros_configuracion()

def crear_ficheros_configuracion():
    print("--- Configuración de Títulos ---")
    titulo_principal = input("Introduce el Título Principal: ")
    subtitulo = input("Introduce el Subtítulo: ")
    
    f = open(FICH_TITULOS, "w")
    f.write(titulo_principal + "\n")
    f.write(subtitulo + "\n")
    f.close()

    print("\n--- Configuración de Opciones ---")
    opciones = {}
    textos_default = [
        "Alta de nuevos abonados",
        "Modificación del valor de la factura de un abonado",
        "Consulta del dato de facturación de un abonado",
        "Consulta del dato de facturación total de la compañía",
        "Eliminar el fichero de datos",
        "Salir"
    ]
    
    for i, texto_defecto in enumerate(textos_default, 1):
        entrada = input(f"Introduce texto para opción {i} [{texto_defecto}]: ")
        opciones[str(i)] = entrada if entrada.strip() else texto_defecto
    
    f = open(FICH_OPCIONES, "w")
    json.dump(opciones, f, indent=4)
    f.close()

def mostrar_menu():
    print()
    if os.path.exists(FICH_TITULOS):
        f = open(FICH_TITULOS, "r")
        print(f.readline().strip())
        print(f.readline().strip())
        f.close()
        print("=" * 20)
    
    if os.path.exists(FICH_OPCIONES):
        f = open(FICH_OPCIONES, "r")
        opciones = json.load(f)
        f.close()
        for k, v in opciones.items():
            print(f"{k}) {v}")

def cargar_datos():
    if not os.path.exists(FICH_DATOS):
        return {}
    try:
        f = open(FICH_DATOS, "r")
        datos = json.load(f)
        f.close()
        return datos
    except json.JSONDecodeError:
        return {}

def guardar_datos(datos):
    f = open(FICH_DATOS, "w")
    json.dump(datos, f, indent=4)
    f.close()

def alta_abonado():
    datos = cargar_datos()
    nombre = input("\nNombre del nuevo abonado: ").strip().title()
    if nombre in datos:
        print("¡Error! Ese abonado ya existe.")
    else:
        try:
            factura = float(input("Valor de la factura (€): "))
            datos[nombre] = factura
            guardar_datos(datos)
            print(f"Abonado '{nombre}' dado de alta.")
        except ValueError:
            print("Error: Valor numérico requerido.")

def modificar_factura():
    datos = cargar_datos()
    nombre = input("\nNombre del abonado a modificar: ").strip().title()
    if nombre not in datos:
        print("Error: No encontrado.")
    else:
        try:
            nueva_factura = float(input(f"Factura actual ({datos[nombre]}€). Nuevo valor: "))
            datos[nombre] = nueva_factura
            guardar_datos(datos)
            print("Factura actualizada.")
        except ValueError:
            print("Error: Valor incorrecto.")

def consultar_abonado():
    datos = cargar_datos()
    nombre = input("\nNombre del abonado a consultar: ").strip().title()
    if nombre in datos:
        print(f"La factura de '{nombre}' asciende a: {datos[nombre]}€")
    else:
        print("No encontrado.")

def consultar_total():
    datos = cargar_datos()
    if not datos:
        print("\nNo hay datos de facturación.")
    else:
        total = sum(datos.values())
        print(f"\nFacturación Total: {total:.2f}€ ({len(datos)} abonados)")

def eliminar_fichero_datos():
    if os.path.exists(FICH_DATOS):
        if input("\n¿Seguro que quieres borrar todos los datos? (s/n): ").lower() == 's':
            os.remove(FICH_DATOS)
            print("Fichero eliminado.")
    else:
        print("\nNo existe fichero de datos.")

def main():
    configurar_sistema()
    while True:
        mostrar_menu()
        opcion = input("\nOpción: ")
        if opcion == "1": alta_abonado()
        elif opcion == "2": modificar_factura()
        elif opcion == "3": consultar_abonado()
        elif opcion == "4": consultar_total()
        elif opcion == "5": eliminar_fichero_datos()
        elif opcion == "6": break
        else: print("Opción no válida.")

if __name__ == "__main__":
    main()