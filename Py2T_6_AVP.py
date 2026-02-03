"""
Programa de procesamiento de ventas (Versión 2).
Lee datos desde un CSV en 'files/' y guarda el análisis detallado en 'files/ventasestad.json'.
"""

import csv
import json
import os
import time

# --- Configuración de Rutas ---
CARPETA_DATOS = "files"
FICHERO_ENTRADA = "ventasprod.csv"
FICHERO_SALIDA = "ventasestad.json"

RUTA_ENTRADA = os.path.join(CARPETA_DATOS, FICHERO_ENTRADA)
RUTA_SALIDA = os.path.join(CARPETA_DATOS, FICHERO_SALIDA)

def cargar_ventas(ruta):
    datos_validados = []
    try:
        if not os.path.exists(ruta):
            print(f"Error: No se localiza el archivo en {ruta}")
            return None

        with open(ruta, mode='r', encoding='utf-8', newline='') as f:
            lector = csv.DictReader(f)
            for num_fila, fila in enumerate(lector, 1):
                try:
                    fila['cantidad_vendida'] = int(fila['cantidad_vendida'])
                    fila['precio_unitario'] = float(fila['precio_unitario'])
                    fila['devueltos'] = int(fila['devueltos'])
                    datos_validados.append(fila)
                except (ValueError, KeyError) as e:
                    print(f"Aviso: Error en fila {num_fila} ({e}). Saltando...")
        return datos_validados

    except Exception as e:
        print(f"Error crítico al leer datos: {e}")
        return None

def generar_informe(ventas):
    if not ventas:
        return {}

    total_ingresos = 0.0
    total_unidades = 0
    top_producto = {"nombre": None, "cantidad": -1}

    for v in ventas:
        ingreso = v['cantidad_vendida'] * v['precio_unitario']
        total_ingresos += ingreso
        total_unidades += v['cantidad_vendida']

        if v['cantidad_vendida'] > top_producto["cantidad"]:
            top_producto = {
                "nombre": v['producto'],
                "cantidad": v['cantidad_vendida'],
                "ingreso_generado": f"{ingreso:.2f}€"
            }

    return {
        "metadata": {
            "registros_procesados": len(ventas),
            "fecha_proceso": time.strftime("%Y-%m-%d %H:%M:%S")
        },
        "metricas_globales": {
            "ingresos_totales": f"{total_ingresos:.2f}€",
            "unidades_totales": total_unidades
        },
        "producto_lider": top_producto
    }

def exportar_json(datos, ruta):
    try:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al exportar JSON: {e}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("ANÁLISIS DE VENTAS - VERSIÓN 2.0")
    print("=" * 60)
    time.sleep(1)

    # 1. Lectura
    print(f"-> Cargando: {RUTA_ENTRADA}")
    ventas = cargar_ventas(RUTA_ENTRADA)
    
    if ventas is None:
        print("Error al cargar los datos.")
        exit()
    print(f"-> Éxito: {len(ventas)} registros cargados.")
    time.sleep(0.5)

    # 2. Análisis
    print("-> Ejecutando algoritmos de análisis...")
    informe = generar_informe(ventas)
    time.sleep(0.5)

    print("\nRESUMEN EJECUTIVO:")
    print(json.dumps(informe["metricas_globales"], indent=4, ensure_ascii=False))
        
    # 3. Guardado
    print(f"\n-> Exportando informe a: {RUTA_SALIDA}")
    if exportar_json(informe, RUTA_SALIDA):
        print("-> Exportación completada con éxito.")
        
    time.sleep(1)
    print("\n" + "=" * 60)
    print("FIN DEL TRATAMIENTO DE DATOS")
    print("=" * 60)