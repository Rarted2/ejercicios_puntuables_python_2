import os

# ==========================================
# 1. CONSTANTES Y CONFIGURACIÓN
# ==========================================
NOMBRE_CARPETA = "files"
NOMBRE_FICHERO = "numero.txt"
# Construimos la ruta completa (files/numero.txt) de forma compatible con cualquier SO
RUTA_COMPLETA = os.path.join(NOMBRE_CARPETA, NOMBRE_FICHERO)

# ==========================================
# 2. FUNCIONES DE GESTIÓN DE ARCHIVOS
# ==========================================

def verificar_entorno():
    mensaje_estado = ""

    # 1. Verificamos/Creamos la carpeta
    if not os.path.exists(NOMBRE_CARPETA):
        os.makedirs(NOMBRE_CARPETA)
    
    # 2. Verificamos/Creamos el fichero
    if os.path.exists(RUTA_COMPLETA):
        mensaje_estado = f"Iniciado el programa. El fichero {NOMBRE_FICHERO} se abrió correctamente."
    else:
        # Si no existe, lo creamos con el valor inicial '0'
        f = open(RUTA_COMPLETA, 'w', encoding='utf-8')
        f.write("0")
        f.close()
        mensaje_estado = f"Iniciado el programa. El fichero {NOMBRE_FICHERO} se abrió correctamente. (Hubo que crearlo.)"
    
    return mensaje_estado

def leer_valor_fichero():
    try:
        f = open(RUTA_COMPLETA, 'r', encoding='utf-8')
        contenido = f.readline().strip()
        f.close()
        
        if contenido == "":
            return 0 # Si está vacío, asumimos 0
        return int(contenido)
    except ValueError:
        print("Error: El contenido del fichero no es un número válido. Se reinicia a 0.")
        return 0

def escribir_valor_fichero(nuevo_valor):
    f = open(RUTA_COMPLETA, 'w', encoding='utf-8')
    f.write(str(nuevo_valor))
    f.close()

# ==========================================
# 3. FUNCIONES LÓGICAS (OPERACIONES)
# ==========================================


def procesar_incremento():
    # 1. Leer
    valor = leer_valor_fichero()
    # 2. Mostrar previo
    print(f"Valor encontrado: {valor}")
    # 3. Calcular
    valor += 1
    # 4. Mostrar nuevo
    print(f"Valor actual: {valor}")
    # 5. Guardar
    escribir_valor_fichero(valor)

def procesar_decremento():
    # 1. Leer
    valor = leer_valor_fichero()
    # 2. Mostrar previo
    print(f"Valor encontrado: {valor}")
    # 3. Calcular
    valor -= 1
    # 4. Mostrar nuevo
    print(f"Valor actual: {valor}")
    # 5. Guardar
    escribir_valor_fichero(valor)


# ==========================================
# 4. PROGRAMA PRINCIPAL
# ==========================================

def main():
    print("PROGRAMA CONTADOR/DESCONTADOR")
    
    # Paso 1: Inicialización y comprobación
    mensaje_inicio = verificar_entorno()
    print(mensaje_inicio)
    print() # Línea en blanco estética
    
    continuar = True
    
    # Diccionario para simular switch-case (como aprendimos antes)
    # Mapeamos letras (mayúsculas) a funciones
    acciones = {
        'I': procesar_incremento,
        'D': procesar_decremento
    }

    while continuar:
        # Solicitamos opción y convertimos a mayúsculas para ser tolerantes a minúsculas
        opcion = input("¿Quiere incrementar, decrementar o finalizar (I, D o F)? ").upper()
        
        if opcion == 'F':
            continuar = False
            print("\nPrograma terminado.")
        elif opcion in acciones:
            # Ejecutamos la función correspondiente del diccionario
            acciones[opcion]()
            print(".....\n") # Separador visual entre operaciones
        else:
            print("Opción no válida. Por favor use I, D o F.")
            print()

# Punto de entrada
if __name__ == "__main__":
    main()