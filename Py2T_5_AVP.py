"""
Programa de procesamiento de ventas.
Lee datos desde un CSV, calcula estadísticas básicas y guarda el resultado en un JSON.
"""

import csv
import json
import os
import time

# --- Constantes de Configuración ---
RUTA_CSV = os.path.join("files", "ventasprod.csv")
RUTA_JSON_SALIDA = "ventasestad.json"

def cargar_datos_csv(ruta_fichero):
    """
    Lee el fichero CSV y devuelve una lista de diccionarios con los tipos corregidos.
    """
    ventas = []
    try:
        if not os.path.exists(ruta_fichero):
            print(f"Error: No se encontró el fichero '{ruta_fichero}'.")
            return None

        with open(ruta_fichero, mode='r', newline='', encoding='utf-8') as fichero:
            lector = csv.DictReader(fichero)
            for fila in lector:
                try:
                    # Conversión de tipos de datos
                    fila['cantidad_vendida'] = int(fila['cantidad_vendida'])
                    fila['precio_unitario'] = float(fila['precio_unitario'])
                    fila['devueltos'] = int(fila['devueltos'])
                    ventas.append(fila)
                except ValueError as e:
                    print(f"(!) Ignorando fila malformada: {e}")
                    continue
        return ventas

    except Exception as e:
        print(f"Error inesperado al leer el CSV: {e}")
        return None

def procesar_estadisticas(lista_ventas):
    """
    Calcula el total vendido, unidades totales y el producto con más ventas.
    """
    if not lista_ventas:
        return {}

    total_euros = 0.0
    total_unidades = 0
    max_unidades = -1
    producto_estrella = {}

    for item in lista_ventas:
        nombre = item['producto']
        cantidad = item['cantidad_vendida']
        precio = item['precio_unitario']
        ingresos = cantidad * precio

        total_euros += ingresos
        total_unidades += cantidad

        if cantidad > max_unidades:
            max_unidades = cantidad
            producto_estrella = {
                "nombre": nombre,
                "cantidad": cantidad,
                "ingresos": f"{ingresos:.2f}€"
            }

    return {
        "resumen": {
            "total_ingresos": f"{total_euros:.2f}€",
            "total_unidades_vendidas": total_unidades,
            "total_distintos_productos": len(lista_ventas)
        },
        "producto_destacado": producto_estrella
    }

def guardar_json(datos, ruta_salida):
    """Guarda el diccionario de datos en formato JSON."""
    try:
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")
        return False

def main():
    print("=" * 50)
    print("SISTEMA DE ANÁLISIS DE VENTAS")
    print("=" * 50)
    time.sleep(1)

    # 1. Fase de Carga
    print(f"[*] Cargando datos desde: {RUTA_CSV}...")
    datos = cargar_datos_csv(RUTA_CSV)
    
    if datos is None:
        print("Finalizando programa por error en la carga.")
        return

    print(f"[OK] Se han procesado {len(datos)} registros.")
    time.sleep(0.5)

    # 2. Fase de Procesamiento
    print("[*] Generando estadísticas...")
    stats = procesar_estadisticas(datos)
    time.sleep(0.5)

    print("\nRESULTADOS DEL ANÁLISIS:")
    print("-" * 30)
    print(json.dumps(stats, indent=4, ensure_ascii=False))
    print("-" * 30)

    # 3. Fase de Almacenamiento
    print(f"\n[*] Guardando resultados en: {RUTA_JSON_SALIDA}...")
    if guardar_json(stats, RUTA_JSON_SALIDA):
        print("[OK] El archivo se ha generado correctamente.")
    
    time.sleep(1)
    print("\n" + "=" * 50)
    print("PROCESO FINALIZADO")
    print("=" * 50)

if __name__ == "__main__":
    main()