import csv
import json
import os

# Rutas de archivos
FICH_CSV = os.path.join("files", "ventasprod.csv")
FICH_JSON = os.path.join("files", "ventasestad.json")

def generar_csv_prueba():
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
            f = open(FICH_CSV, "w", newline="")
            writer = csv.writer(f)
            writer.writerows(datos)
            f.close()
            print(f"AVISO: Se ha creado un fichero '{FICH_CSV}' de prueba.\n")
        except OSError as e:
            print(f"Error creando fichero de prueba: {e}")

def carga_datos_csv(nombre_fichero):
    lista_productos = []
    try:
        f = open(nombre_fichero, mode="r", newline="")
        reader = csv.DictReader(f)
        for fila in reader:
            try:
                producto = {
                    "nombre": fila["Producto"],
                    "cantidad": int(fila["Cantidad"]),
                    "precio": float(fila["PrecioUnitario"])
                }
                lista_productos.append(producto)
            except ValueError:
                print(f"Línea ignorada: {fila}")
        f.close()
        return lista_productos
    except Exception as e:
        print(f"Error leyendo CSV: {e}")
        return []

def procesa_datos_ventas(lista_ventas):
    if not lista_ventas: return None

    total_euros = 0.0
    total_unidades = 0
    estrella = None
    max_ingreso = -1.0

    for item in lista_ventas:
        ingreso = item["cantidad"] * item["precio"]
        total_euros += ingreso
        total_unidades += item["cantidad"]
        
        if ingreso > max_ingreso:
            max_ingreso = ingreso
            estrella = {
                "nombre": item["nombre"],
                "cantidad": item["cantidad"],
                "ingreso": f"{ingreso:.2f}€"
            }

    return {
        "producto_estrella": estrella,
        "total_vendido": f"{total_euros:.2f}€",
        "total_unidades_vendidas": total_unidades,
        "numero_de_productos": len(lista_ventas)
    }

def guardar_estadisticas_json(datos, nombre_fichero):
    try:
        f = open(nombre_fichero, "w")
        json.dump(datos, f, indent=4, ensure_ascii=False)
        f.close()
        print(f"Guardando en {nombre_fichero}...")
    except OSError as e:
        print(f"Error guardando JSON: {e}")

if __name__ == "__main__":
    generar_csv_prueba()
    datos_ventas = carga_datos_csv(FICH_CSV)
    
    if not datos_ventas:
        print("No hay datos para procesar.")
        return

    stats = procesa_datos_ventas(datos_ventas)
    print("Estadísticas de Ventas:")
    print(json.dumps(stats, indent=4, ensure_ascii=False))
    guardar_estadisticas_json(stats, FICH_JSON)