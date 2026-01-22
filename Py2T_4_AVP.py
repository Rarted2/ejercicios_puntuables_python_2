import os

# Asegurar que el directorio existe y definir la ruta del archivo
os.makedirs("files", exist_ok=True)
ruta = os.path.join("files", "numero.txt")

# Verificar si el archivo existe; si no, crearlo con el valor inicial "0"
creado = False
if not os.path.exists(ruta):
    open(ruta, 'w').write("0")
    creado = True

# Mostrar mensaje de inicio indicando si se creó el archivo
print(f"PROGRAMA CONTADOR/DESCONTADOR\nIniciado el programa. El fichero numero.txt se abrió correctamente.{' (Hubo que crearlo.)' if creado else ''}\n")

# Bucle principal: pide la opción y continúa hasta que sea 'F'
# Se utiliza el operador 'walrus' (:=) para asignar y comparar en una línea
while (opcion := input("¿Quiere incrementar, decrementar o finalizar (I, D o F)? ").upper()) != 'F':
    if opcion in "ID":
        try:
            # Intentar leer el número del archivo; si está vacío o falla, usar 0
            valor = int(open(ruta).read().strip() or 0)
        except ValueError:
            valor = 0
            print("Error: Contenido no numérico. Reiniciando a 0.")

        print(f"Valor encontrado: {valor}")
        
        # Incrementar o decrementar el valor según la opción elegida
        valor += 1 if opcion == 'I' else -1
        
        print(f"Valor actual: {valor}\n.....")
        
        # Guardar el nuevo valor en el archivo
        open(ruta, 'w').write(str(valor))
    else:
        print("Opción no válida.\n")

print("\nPrograma terminado.")