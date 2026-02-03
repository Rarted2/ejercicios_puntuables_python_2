import csv
import json
import os
import time

# --- Configuración de Rutas ---
# Nota: Si tus archivos están en la raíz junto al script, cambia "files" por "."
CARPETA_DATOS = "files" 
FICHERO_ENTRADA = "ventasprod.csv"
FICHERO_SALIDA = "ventasestad.json"

RUTA_ENTRADA = os.path.join(CARPETA_DATOS, FICHERO_ENTRADA)
RUTA_SALIDA = os.path.join(CARPETA_DATOS, FICHERO_SALIDA)

def carga_datos_csv(ruta):
    datos_validados = []
    try:
        if not os.path.exists(ruta):
            print(f"Error: No se localiza el archivo en {ruta}")
            return None

        with open(ruta, mode='r', encoding='utf-8', newline='') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    # Convertimos los tipos de datos según sea necesario para operar después
                    fila['cantidad_vendida'] = int(fila['cantidad_vendida'])
                    fila['precio_unitario'] = float(fila['precio_unitario'])
                    fila['devueltos'] = int(fila['devueltos'])
                    datos_validados.append(fila)
                except (ValueError, KeyError):
                    # Si hay un dato corrupto, lo ignoramos (según lógica estándar)
                    continue
        return datos_validados

    except Exception as e:
        print(f"Error crítico al leer datos: {e}")
        return None

def procesa_datos_ventas(ventas):
    if not ventas:
        return {}

    total_vendido_acumulado = 0.0
    total_unidades_acumulado = 0
    productos_unicos = set() # Usamos un set para contar referencias únicas
    
    # Variables para calcular el producto estrella
    max_cantidad = -1
    prod_estrella = {}

    for v in ventas:
        nombre_prod = v['producto']
        cantidad = v['cantidad_vendida']
        precio = v['precio_unitario']
        
        ingreso_linea = cantidad * precio
        
        # Acumuladores globales
        total_vendido_acumulado += ingreso_linea
        total_unidades_acumulado += cantidad
        productos_unicos.add(nombre_prod)

        # Lógica de producto estrella (mayor cantidad vendida)
        if cantidad > max_cantidad:
            max_cantidad = cantidad
            prod_estrella = {
                "nombre": nombre_prod,
                "cantidad": cantidad,
                "ingreso": f"{ingreso_linea:.2f}€" # Formato exacto de la imagen
            }

    # Construcción del diccionario plano según la imagen del enunciado
    estadisticas = {
        "producto_estrella": prod_estrella,
        "total_vendido": f"{total_vendido_acumulado:.2f}€",
        "total_unidades_vendidas": total_unidades_acumulado,
        "numero_de_productos": len(productos_unicos)
    }

    return estadisticas

def guardar_json(datos, ruta):
    try:
        # Aseguramos que exista la carpeta
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        
        with open(ruta, 'w', encoding='utf-8') as f:
            # ensure_ascii=False para que se vean bien los acentos y el símbolo €
            json.dump(datos, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al exportar JSON: {e}")
        return False

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    
    # Cabecera simple como en la imagen
    print("\n" + "PROGRAMA VENTAS".center(40, "_"))
    print()

    # 1. Carga
    print(f"Iniciando carga de datos desde el fichero {FICHERO_ENTRADA}...")
    # Simulamos un pequeño tiempo de espera
    time.sleep(1)
    
    datos = carga_datos_csv(RUTA_ENTRADA)
    
    if datos is None:
        print("No se pudieron cargar los datos. Fin del programa.")
        exit()

    print(f"\nSe cargaron {len(datos)} filas de datos.")
    print("\nProcesando los datos...")
    time.sleep(1)

    # 2. Procesamiento
    resultados = procesa_datos_ventas(datos)

    # Mostrar en pantalla con formato JSON
    print("\nEstadísticas de Ventas:")
    print(json.dumps(resultados, indent=4, ensure_ascii=False))

    # 3. Almacenamiento
    print(f"\nAlmacenando en fichero {FICHERO_SALIDA}...")
    if guardar_json(resultados, RUTA_SALIDA):
        # En la imagen no sale mensaje de "éxito", así que lo dejamos limpio
        pass
    
    print("\n" + "_"*40)