import csv, json, os

os.makedirs("files", exist_ok=True)
F_CSV, F_JSON = os.path.join("files", "ventasprod.csv"), os.path.join("files", "ventasestad.json")

# Generar archivo CSV de prueba si no existe
if not os.path.exists(F_CSV):
    with open(F_CSV, "w", newline="") as f:
        csv.writer(f).writerows([["Producto", "Cantidad", "PrecioUnitario"], ["Ratón", "700", "20.00"], ["Teclado", "300", "45.50"], ["Monitor", "150", "120.00"], ["Cable HDMI", "500", "5.50"], ["Impresora", "50", "200.00"], ["USB 32GB", "400", "10.00"], ["Webcam", "150", "35.00"]])
    print(f"AVISO: Se ha creado el fichero de prueba '{F_CSV}'.\n")

# Proceso principal: Leer CSV -> Procesar -> Guardar JSON
try:
    with open(F_CSV, mode="r", newline="") as f:
        # Convertimos filas a diccionario con tipos correctos, ignorando errores
        ventas = []
        for r in csv.DictReader(f):
            try: ventas.append({"nombre": r["Producto"], "cant": int(r["Cantidad"]), "precio": float(r["PrecioUnitario"]), "ingreso": int(r["Cantidad"]) * float(r["PrecioUnitario"])})
            except ValueError: pass # Ignorar filas con datos corruptos
    
    if ventas:
        # Calcular estadísticas usando funciones 'max' y 'sum' para eficiencia
        estrella = max(ventas, key=lambda x: x["ingreso"])
        stats = {
            "producto_estrella": {"nombre": estrella["nombre"], "cantidad": estrella["cant"], "ingreso": f"{estrella['ingreso']:.2f}€"},
            "total_vendido": f"{sum(x['ingreso'] for x in ventas):.2f}€",
            "total_unidades": sum(x["cant"] for x in ventas),
            "cant_productos": len(ventas)
        }
        
        print(f"Estadísticas:\n{json.dumps(stats, indent=4, ensure_ascii=False)}")
        try: json.dump(stats, open(F_JSON, "w"), indent=4, ensure_ascii=False); print(f"Guardado en {F_JSON}")
        except OSError: print("Error guardando JSON.")
    else: print("No se encontraron datos válidos en el CSV.")

except Exception as e: print(f"Error procesando datos: {e}")