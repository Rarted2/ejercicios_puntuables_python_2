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
    """
    Verifica que exista la carpeta y el fichero necesarios.
    Si no existen, los crea e inicializa.
    Devuelve un mensaje de estado para mostrar al inicio.
    """
    mensaje_estado = ""

    # 1. Verificamos/Creamos la carpeta
    if not os.path.exists(NOMBRE_CARPETA):
        os.makedirs(NOMBRE_CARPETA)
    
    # 2. Verificamos/Creamos el fichero
    if os.path.exists(RUTA_COMPLETA):
        mensaje_estado = f"Iniciado el programa. El fichero {NOMBRE_FICHERO} se abrió correctamente."
    else:
        # Si no existe, lo creamos con el valor inicial '0'
        with open(RUTA_COMPLETA, 'w', encoding='utf-8') as f:
            f.write("0")
        mensaje_estado = f"Iniciado el programa. El fichero {NOMBRE_FICHERO} se abrió correctamente. (Hubo que crearlo.)"
    
    return mensaje_estado

def leer_valor_fichero():
    """
    Abre el fichero en modo lectura, recupera el número y lo devuelve como entero.
    Gestiona errores si el fichero está vacío o corrupto.
    """
    try:
        with open(RUTA_COMPLETA, 'r', encoding='utf-8') as f:
            contenido = f.read().strip() # Quitamos posibles saltos de línea
            if contenido == "":
                return 0 # Si está vacío, asumimos 0
            return int(contenido)
    except ValueError:
        print("Error: El contenido del fichero no es un número válido. Se reinicia a 0.")
        return 0

def escribir_valor_fichero(nuevo_valor):
    """
    Sobrescribe el fichero con el nuevo valor calculado.
    """
    with open(RUTA_COMPLETA, 'w', encoding='utf-8') as f:
        f.write(str(nuevo_valor))

# ==========================================
# 3. FUNCIONES LÓGICAS (OPERACIONES)
# ==========================================

def mostrar_estado_actual(valor_leido):
    """Muestra el valor encontrado antes de operar."""
    print(f"Valor encontrado: {valor_leido}")

def mostrar_nuevo_estado(valor_nuevo):
    """Muestra el valor resultante después de operar."""
    print(f"Valor actual: {valor_nuevo}")

def procesar_incremento():
    """
    Orquesta la operación de sumar 1: Lee -> Muestra -> Calcula -> Muestra -> Guarda
    """
    # 1. Leer
    valor = leer_valor_fichero()
    # 2. Mostrar previo
    mostrar_estado_actual(valor)
    # 3. Calcular
    valor += 1
    # 4. Mostrar nuevo
    mostrar_nuevo_estado(valor)
    # 5. Guardar
    escribir_valor_fichero(valor)

def procesar_decremento():
    """
    Orquesta la operación de restar 1: Lee -> Muestra -> Calcula -> Muestra -> Guarda
    """
    # 1. Leer
    valor = leer_valor_fichero()
    # 2. Mostrar previo
    mostrar_estado_actual(valor)
    # 3. Calcular
    valor -= 1
    # 4. Mostrar nuevo
    mostrar_nuevo_estado(valor)
    # 5. Guardar
    escribir_valor_fichero(valor)

def opcion_no_reconocida():
    """Informa al usuario si teclea una letra incorrecta."""
    print("Opción no válida. Por favor use I, D o F.")

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
            opcion_no_reconocida()
            print()

# Punto de entrada
if __name__ == "__main__":
    main()