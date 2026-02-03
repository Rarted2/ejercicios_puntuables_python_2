"""
Programa contador persistedo en un archivo de texto.
Permite incrementar o decrementar un valor almacenado en 'files/numero.txt'.
"""

import os

# Configuración de constantes
DIRECTORIO_FILES = "files"
NOMBRE_ARCHIVO = "numero.txt"
RUTA_ARCHIVO = os.path.join(DIRECTORIO_FILES, NOMBRE_ARCHIVO)

def inicializar_archivo():
    """Crea el directorio y el archivo inicial si no existen."""
    if not os.path.exists(DIRECTORIO_FILES):
        os.makedirs(DIRECTORIO_FILES)
        
    if not os.path.exists(RUTA_ARCHIVO):
        with open(RUTA_ARCHIVO, 'w', encoding='utf-8') as f:
            f.write("0")
        return True
    return False

def leer_valor():
    """Lee el valor actual del archivo. Devuelve 0 si hay error."""
    try:
        with open(RUTA_ARCHIVO, 'r', encoding='utf-8') as f:
            contenido = f.read().strip()
            return int(contenido) if contenido else 0
    except (FileNotFoundError, ValueError):
        return 0

def guardar_valor(valor):
    """Guarda el nuevo valor en el archivo."""
    with open(RUTA_ARCHIVO, 'w', encoding='utf-8') as f:
        f.write(str(valor))

def main():
    recien_creado = inicializar_archivo()
    
    print("=" * 40)
    print("GESTOR DE CONTADOR PERSISTENTE")
    print("=" * 40)
    print(f"Archivo: {RUTA_ARCHIVO}")
    if recien_creado:
        print("Aviso: El archivo no existía y ha sido inicializado en 0.")
    print("----------------------------------------")

    while True:
        print("\nOpciones: [I] Incrementar | [D] Decrementar | [F] Finalizar")
        opcion = input("Seleccione una opción: ").strip().upper()

        if opcion == 'F':
            break
        
        if opcion in ('I', 'D'):
            valor_actual = leer_valor()
            print(f"Valor en disco: {valor_actual}")
            
            if opcion == 'I':
                nuevo_valor = valor_actual + 1
                accion = "incrementado"
            else:
                nuevo_valor = valor_actual - 1
                accion = "decrementado"
            
            guardar_valor(nuevo_valor)
            print(f"Valor {accion} a: {nuevo_valor}")
            print(".....")
        else:
            print("(!) Opción no válida. Por favor, use I, D o F.")

    print("\n" + "=" * 40)
    print("Programa terminado correctamente.")
    print("=" * 40)

if __name__ == "__main__":
    main()