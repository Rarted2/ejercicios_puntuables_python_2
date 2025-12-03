import csv
import json
import os

# --- CONSTANTES ---
# Definimos las rutas de los archivos de entrada (CSV) y salida (JSON).
FICH_CSV = os.path.join("files", "ventasprod.csv")
FICH_JSON = os.path.join("files", "ventasestad.json")

# ==========================================
# 0. FUNCIÓN AUXILIAR (PARA CREAR DATOS DE PRUEBA)
# ==========================================
def generar_csv_prueba():
    """
    Crea el fichero ventasprod.csv con datos ficticios si no existe,
    para que el alumno pueda probar el ejercicio inmediatamente sin necesidad de crear el archivo manualmente.
    """
    os.makedirs("files", exist_ok=True)
    if not os.path.exists(FICH_CSV):
        datos = [
            ["Producto", "Cantidad", "PrecioUnitario"],
            ["Ratón", "700", "20.00"],
            ["Teclado", "300", "45.50"],
            ["Monitor", "150", "120.00"],
            ["Cable HDMI", "500", "5.50"],
            ["Impresora", "50", "200.00"],
            ["USB 32GB", "400", "10.00"],
            ["Webcam", "150", "35.00"]
        ]
        try:
            # newline="" es importante en Windows para evitar líneas en blanco extra en CSV
            with open(FICH_CSV, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(datos)
            print(f"AVISO: Se ha creado un fichero '{FICH_CSV}' de prueba con datos ficticios.\n")
        except OSError as e:
            print(f"Error creando fichero de prueba: {e}")

# ==========================================
# 1. CARGA DE DATOS (CSV)
# ==========================================
def carga_datos_csv(nombre_fichero):
    """
    Lee el fichero CSV y devuelve una lista de diccionarios.
    Convierte las cantidades y precios a tipos numéricos para poder operar con ellos.
    
    Argumentos:
        nombre_fichero (str): Ruta al archivo CSV.
        
    Retorna:
        list: Lista de diccionarios, donde cada diccionario representa una fila del CSV.
    """
    lista_productos = []
    try:
        with open(nombre_fichero, mode="r", newline="", encoding="utf-8") as f:
            # Usamos DictReader para que convierta cada fila en un diccionario {'Columna': Valor}
            # Esto hace que el código sea más legible que usar índices numéricos.
            reader = csv.DictReader(f)
            
            for fila in reader:
                # Es importante convertir los textos a números (int/float) para poder calcular después.
                # Usamos try-except interno por si una fila viene con datos corruptos, para no detener todo el proceso.
                try:
                    producto = {
                        "nombre": fila["Producto"],
                        "cantidad": int(fila["Cantidad"]),
                        "precio": float(fila["PrecioUnitario"])
                    }
                    lista_productos.append(producto)
                except ValueError:
                    print(f"Advertencia: Fila ignorada por datos no numéricos: {fila}")
                    
        return lista_productos

    except FileNotFoundError:
        print(f"Error: El fichero {nombre_fichero} no existe.")
        return []
    except Exception as e:
        print(f"Error inesperado leyendo CSV: {e}")
        return []

# ==========================================
# 2. PROCESAMIENTO (LÓGICA DE NEGOCIO)
# ==========================================
def procesa_datos_ventas(lista_ventas):
    """
    Recibe la lista de ventas y calcula las estadísticas requeridas.
    Devuelve un diccionario con la estructura lista para guardar en JSON.
    
    Argumentos:
        lista_ventas (list): Lista de diccionarios con los datos de ventas.
        
    Retorna:
        dict: Diccionario con las estadísticas calculadas (producto estrella, totales, etc.).
    """
    if not lista_ventas:
        return None

    total_euros_vendido = 0.0
    total_unidades = 0
    
    # Variables para rastrear al producto estrella (el que más ingresos generó)
    producto_estrella = None
    max_ingreso = -1.0

    for item in lista_ventas:
        # Cálculos por producto
        ingreso_actual = item["cantidad"] * item["precio"]
        
        # Acumuladores globales
        total_euros_vendido += ingreso_actual
        total_unidades += item["cantidad"]
        
        # Comprobar si es el producto estrella (mayor ingreso generado)
        if ingreso_actual > max_ingreso:
            max_ingreso = ingreso_actual
            producto_estrella = {
                "nombre": item["nombre"],
                "cantidad": item["cantidad"],
                "ingreso": f"{ingreso_actual:.2f}€" # Formato texto para la salida
            }

    # Construimos el diccionario final con la estructura pedida
    estadisticas = {
        "producto_estrella": producto_estrella,
        "total_vendido": f"{total_euros_vendido:.2f}€",
        "total_unidades_vendidas": total_unidades,
        "numero_de_productos": len(lista_ventas)
    }
    
    return estadisticas

# ==========================================
# 3. ALMACENAMIENTO (JSON)
# ==========================================
def guardar_estadisticas_json(datos, nombre_fichero):
    """
    Guarda el diccionario de estadísticas en un fichero JSON.
    
    Argumentos:
        datos (dict): Las estadísticas a guardar.
        nombre_fichero (str): Ruta del archivo de destino.
    """
    try:
        with open(nombre_fichero, "w", encoding="utf-8") as f:
            # indent=4 para que quede bonito y legible (pretty print).
            # ensure_ascii=False permite que se guarden caracteres especiales (tildes, ñ, €) correctamente.
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print(f"Almacenando en fichero {nombre_fichero}...")
    except OSError as e:
        print(f"Error guardando el fichero JSON: {e}")

# ==========================================
# 4. PROGRAMA PRINCIPAL
# ==========================================
def main():
    """
    Función principal que coordina la carga, procesamiento y guardado de datos.
    """
    # Paso 0: Generar CSV si no existe (para que puedas probarlo)
    generar_csv_prueba()

    print(f"Iniciando carga de datos desde el fichero {FICH_CSV}...")
    
    # Paso 1: Carga
    datos_ventas = carga_datos_csv(FICH_CSV)
    
    # Verificación de carga
    if not datos_ventas:
        print("No se pudieron cargar datos o el fichero está vacío.")
        return

    print(f"Se cargaron {len(datos_ventas)} filas de datos.")

    # Paso 2: Procesamiento
    print("Procesando los datos...")
    resultado_estadisticas = procesa_datos_ventas(datos_ventas)

    # Paso 3: Mostrar por pantalla (Requisito Nota 2 y 3)
    print("Estadísticas de Ventas:")
    # Usamos json.dumps solo para imprimirlo bonito por pantalla igual que la imagen
    print(json.dumps(resultado_estadisticas, indent=4, ensure_ascii=False))

    # Paso 4: Guardar en JSON
    guardar_estadisticas_json(resultado_estadisticas, FICH_JSON)

if __name__ == "__main__":
    main()