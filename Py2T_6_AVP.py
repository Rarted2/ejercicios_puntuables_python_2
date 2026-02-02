# Nombre del fichero a entregar: Py2T_6_TuNombre_TuApellido.py
import csv
import json

# --- Definición de Funciones ---

def carga_datos_csv(nombre_fichero):
    """
    Tarea 1: Carga datos de un fichero CSV a una lista de diccionarios.
    Lee el fichero, convierte los campos numéricos de cadena a sus tipos
    correspondientes (int o float) y devuelve la lista de registros.
    """
    lista_ventas = []
    try:
        # Se abre el fichero en modo lectura ('r') con codificación utf-8
        with open(nombre_fichero, mode='r', newline='', encoding='utf-8') as fichero:
            reader = csv.DictReader(fichero)
            for row in reader:
                # Es CRUCIAL convertir los datos numéricos que vienen como texto del CSV
                # a tipos numéricos reales para poder operar con ellos después.
                try:
                    row['cantidad_vendida'] = int(row['cantidad_vendida'])
                    row['precio_unitario'] = float(row['precio_unitario'])
                    row['devueltos'] = int(row['devueltos'])
                    lista_ventas.append(row)
                except ValueError as e:
                     print(f"Error de conversión de tipos en una fila: {e}")
                     # Opcional: decidir si saltar la fila o detener el programa
                     continue

    except FileNotFoundError:
        print(f"Error: No se encontró el fichero {nombre_fichero}")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado leyendo el CSV: {e}")
        return None

    return lista_ventas

def procesa_datos_ventas(lista_datos):
    """
    Tarea 2: Procesa la lista de datos para obtener estadísticas.
    Calcula el producto más vendido, totales monetarios y de unidades,
    y el número de referencias. Devuelve un diccionario formateado.
    """
    if not lista_datos:
        return {}

    suma_total_euros = 0.0
    suma_total_unidades = 0
    max_unidades_vendidas = -1
    producto_estrella_info = {}

    # Iteramos sobre cada venta para realizar los cálculos
    for venta in lista_datos:
        nombre = venta['producto']
        cantidad = venta['cantidad_vendida']
        precio = venta['precio_unitario']
        ingreso_producto = cantidad * precio

        # Acumuladores totales
        suma_total_euros += ingreso_producto
        suma_total_unidades += cantidad

        # Lógica para encontrar el producto estrella (basado en cantidad vendida)
        if cantidad > max_unidades_vendidas:
            max_unidades_vendidas = cantidad
            # Guardamos los datos del producto estrella.
            # Nota: El ingreso aquí se formatea como cadena con '€' según la imagen de salida.
            producto_estrella_info = {
                "nombre": nombre,
                "cantidad": cantidad,
                "ingreso": f"{ingreso_producto:.2f}€"
            }

    # Número total de referencias (filas en el CSV original)
    num_productos = len(lista_datos)

    # Construcción del diccionario de estadísticas final.
    # Se formatean los valores monetarios como cadenas añadiendo '€' para coincidir con el ejemplo.
    estadisticas = {
        "producto_estrella": producto_estrella_info,
        "total_vendido": f"{suma_total_euros:.2f}€",
        "total_unidades_vendidas": suma_total_unidades,
        "numero_de_productos": num_productos
    }

    return estadisticas

def guardar_estadisticas_json(nombre_fichero, datos_stats):
    """
    Tarea 3: Almacenamiento de los resultados en un fichero JSON.
    (Nota: El enunciado tiene una errata pidiendo llamar a esta función también
    'procesa_datos_ventas'. Se ha usado un nombre distinto para claridad funcional).
    """
    try:
        # Se abre el fichero en modo escritura ('w')
        # 'indent=4' sirve para que el JSON se guarde "bonito" y legible.
        with open(nombre_fichero, 'w', encoding='utf-8') as fichero_json:
            json.dump(datos_stats, fichero_json, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar el fichero JSON: {e}")
        return False

# --- Programa Principal ---

if __name__ == "__main__":
    # Definición de nombres de ficheros
    nombre_csv = "ventasprod.csv"
    nombre_json = "ventasestad.json"

    print("\nPROGRAMA VENTAS")
    print("-" * 20)

    # 1. Carga
    print(f"Iniciando carga de datos desde el fichero {nombre_csv}...")
    datos_ventas = carga_datos_csv(nombre_csv)

    # Verificamos si la carga fue exitosa antes de continuar
    if datos_ventas is not None:
        print(f"Se cargaron {len(datos_ventas)} filas de datos.")

        # 2. Procesamiento
        print("\nProcesando los datos...")
        estadisticas_finales = procesa_datos_ventas(datos_ventas)

        print("\nEstadísticas de Ventas:")
        # Usamos json.dumps solo para imprimir en pantalla con indentación bonita
        # y que se parezca a la captura del enunciado.
        print(json.dumps(estadisticas_finales, indent=4, ensure_ascii=False))

        # 3. Almacenamiento
        print(f"\nAlmacenando en fichero {nombre_json}...")
        if guardar_estadisticas_json(nombre_json, estadisticas_finales):
            print("Fichero guardado correctamente.")
        else:
            print("Hubo un problema al guardar el fichero.")
    else:
        print("No se pudo continuar debido a errores en la carga de datos.")

    print("\n--- Fin del programa ---")