import os

# Configuración de rutas
NOMBRE_FICHERO = "numero.txt"
RUTA_CARPETA = "files"
os.makedirs(RUTA_CARPETA, exist_ok=True)
RUTA_COMPLETA = os.path.join(RUTA_CARPETA, NOMBRE_FICHERO)

def verificar_entorno():
    mensaje_estado = ""
    if os.path.exists(RUTA_COMPLETA):
        mensaje_estado = f"Iniciado el programa. El fichero {NOMBRE_FICHERO} se abrió correctamente."
    else:
        # Creamos el fichero con valor inicial 0 si no existe
        f = open(RUTA_COMPLETA, 'w')
        f.write("0")
        f.close()
        mensaje_estado = f"Iniciado el programa. El fichero {NOMBRE_FICHERO} se abrió correctamente. (Hubo que crearlo.)"
    return mensaje_estado

def leer_valor_fichero():
    try:
        f = open(RUTA_COMPLETA, 'r')
        contenido = f.readline().strip()
        f.close()
        return int(contenido) if contenido != "" else 0
    except ValueError:
        print("Error: Contenido no numérico. Reiniciando a 0.")
        return 0

def escribir_valor_fichero(nuevo_valor):
    f = open(RUTA_COMPLETA, 'w')
    f.write(str(nuevo_valor))
    f.close()

def procesar_incremento():
    valor = leer_valor_fichero()
    print(f"Valor encontrado: {valor}")
    valor += 1
    print(f"Valor actual: {valor}")
    escribir_valor_fichero(valor)

def procesar_decremento():
    valor = leer_valor_fichero()
    print(f"Valor encontrado: {valor}")
    valor -= 1
    print(f"Valor actual: {valor}")
    escribir_valor_fichero(valor)

def main():
    print("PROGRAMA CONTADOR/DESCONTADOR")
    print(verificar_entorno())
    print() 
    
    continuar = True
    while continuar:
        opcion = input("¿Quiere incrementar, decrementar o finalizar (I, D o F)? ").upper()
        if opcion == 'F':
            continuar = False
            print("\nPrograma terminado.")
        elif opcion == 'I':
            procesar_incremento()
            print(".....")
        elif opcion == 'D':
            procesar_decremento()
            print(".....")
        else:
            print("Opción no válida.\n")

if __name__ == "__main__":
    main()