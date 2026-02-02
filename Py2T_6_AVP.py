# Nombre del fichero a entregar: Py2T_6_TuNombre_TuApellido.py
import csv
import json
import os  # Importamos os para manejar rutas de manera más robusta (opcional, pero recomendado)

# --- Definición de Funciones ---

def carga_datos_csv(nombre_fichero):
    lista_ventas = []
    try:
        # Se abre el fichero en modo lectura.
        with open(nombre_fichero, mode='r', newline='', encoding='utf-8') as fichero:
            reader = csv.DictReader(fichero) # Lee el fichero y lo convierte en una lista de diccionarios
            for row in reader:
                try:
                    # Conversión de tipos
                    row['cantidad_vendida'] = int(row['cantidad_vendida'])
                    row['precio_unitario'] = float(row['precio_unitario'])
                    row['devueltos'] = int(row['devueltos'])
                    lista_ventas.append(row)
                except ValueError as e:
                     print(f"Error de conversión de tipos en una fila: {e}")
                     continue

    except FileNotFoundError:
        print(f"Error: No se encontró el fichero en la ruta: {nombre_fichero}")
        print("Asegúrate de que la carpeta 'files' existe y el archivo está dentro.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado leyendo el CSV: {e}")
        return None

    return lista_ventas

def procesa_datos_ventas(lista_datos):
    if not lista_datos:
        return {}

    suma_total_euros = 0.0
    suma_total_unidades = 0
    max_unidades_vendidas = -1
    producto_estrella_info = {}

    for venta in lista_datos:
        nombre = venta['producto']
        cantidad = venta['cantidad_vendida']
        precio = venta['precio_unitario']
        ingreso_producto = cantidad * precio

        suma_total_euros += ingreso_producto
        suma_total_unidades += cantidad

        if cantidad > max_unidades_vendidas:
            max_unidades_vendidas = cantidad
            producto_estrella_info = {
                "nombre": nombre,
                "cantidad": cantidad,
                "ingreso": f"{ingreso_producto:.2f}€"
            }

    num_productos = len(lista_datos)

    estadisticas = {
        "producto_estrella": producto_estrella_info,
        "total_vendido": f"{suma_total_euros:.2f}€",
        "total_unidades_vendidas": suma_total_unidades,
        "numero_de_productos": num_productos
    }

    return estadisticas

def guardar_estadisticas_json(nombre_fichero, datos_stats):
    try:
        with open(nombre_fichero, 'w', encoding='utf-8') as fichero_json:
            json.dump(datos_stats, fichero_json, indent=4, ensure_ascii=False) # Guarda los datos en un fichero JSON
        return True
    except Exception as e:
        print(f"Error al guardar el fichero JSON: {e}")
        return False

# --- Programa Principal ---

if __name__ == "__main__":
    # ACTUALIZACIÓN: Ruta relativa incluyendo la carpeta 'files'
    # Esto busca 'ventasprod.csv' dentro de una carpeta llamada 'files'
    # que debe estar en el mismo lugar donde ejecutes este script.
    nombre_csv = "files/ventasprod.csv"
    
    # El JSON de salida se guardará en la carpeta raíz (donde está el script)
    nombre_json = "files/ventasestad.json"

    print("\nPROGRAMA VENTAS")
    print("-" * 20)

    # 1. Carga
    print(f"Iniciando carga de datos desde el fichero {nombre_csv}...")
    datos_ventas = carga_datos_csv(nombre_csv)

    # Verificamos si la carga fue exitosa
    if datos_ventas is not None:
        print(f"Se cargaron {len(datos_ventas)} filas de datos.")

        # 2. Procesamiento
        print("Procesando los datos...")
        estadisticas_finales = procesa_datos_ventas(datos_ventas)

        print("\nEstadísticas de Ventas:")
        print(json.dumps(estadisticas_finales, indent=4, ensure_ascii=False))

        # 3. Almacenamiento
        print(f"\nAlmacenando en fichero {nombre_json}...")
        if guardar_estadisticas_json(nombre_json, estadisticas_finales):
            print("Fichero guardado correctamente.") # Mensaje genérico de éxito
        else:
            print("Hubo un problema al guardar el fichero.")
    else:
        print("No se pudo continuar debido a errores en la carga de datos.")

    print("\n--- Fin del programa ---")