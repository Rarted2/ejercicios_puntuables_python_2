import os

# Constante para el nombre del fichero
NOMBRE_FICHERO = "numero.txt"

def inicializar_fichero(nombre_fich):
    """
    Comprueba si el fichero existe. Si no existe, lo crea con valor 0.
    """
    if os.path.exists(nombre_fich):
        print(f"Iniciado el programa. El fichero {nombre_fich} se abrió correctamente.")
    else:
        # Si no existe, usamos la función de escritura para crearlo con 0
        escribir_nuevo_valor(nombre_fich, 0)
        print(f"Iniciado el programa. El fichero {nombre_fich} se abrió correctamente. (Hubo que crearlo.)")

def leer_valor_actual(nombre_fich):
    """
    Lee el fichero y devuelve el número entero que contiene.
    Si hay error (fichero vacío o texto no numérico), devuelve 0.
    """
    try:
        with open(nombre_fich, "r") as f:
            contenido = f.read()
            # Si tiene contenido lo convierte, si no devuelve 0
            if contenido.strip():
                return int(contenido)
            return 0
    except ValueError:
        print("Aviso: El fichero contenía datos corruptos. Se usará valor 0.")
        return 0

def escribir_nuevo_valor(nombre_fich, valor):
    """
    Recibe un número entero y lo escribe en el fichero (sobrescribiendo).
    """
    with open(nombre_fich, "w") as f:
        f.write(str(valor))

def calcular_operacion(valor_actual, opcion):
    """
    Recibe el valor actual y la opción (I o D) y devuelve el valor calculado.
    """
    if opcion == "I":
        return valor_actual + 1
    elif opcion == "D":
        return valor_actual - 1
    return valor_actual # Por seguridad

def solicitar_opcion_usuario():
    """
    Se encarga únicamente de pedir el dato al usuario y devolverlo limpio (mayúsculas).
    """
    print() # Salto de línea estético
    return input("¿Quiere incrementar, decrementar o finalizar (I, D o F)? ").upper()

def main():
    """
    Función principal: Orquesta el flujo del programa llamando a las otras funciones.
    """
    # 1. Fase de Inicio
    inicializar_fichero(NOMBRE_FICHERO)

    # 2. Bucle principal
    ejecutando = True
    
    while ejecutando:
        opcion = solicitar_opcion_usuario()

        if opcion == "F":
            print("Programa terminado.")
            ejecutando = False
            
        elif opcion == "I" or opcion == "D":
            # Paso A: Leer
            valor_antiguo = leer_valor_actual(NOMBRE_FICHERO)
            print(f"Valor encontrado: {valor_antiguo}")

            # Paso B: Calcular
            valor_nuevo = calcular_operacion(valor_antiguo, opcion)

            # Paso C: Escribir
            escribir_nuevo_valor(NOMBRE_FICHERO, valor_nuevo)
            print(f"Valor actual: {valor_nuevo}")
            
        else:
            print("Opción no válida. Inténtelo de nuevo.")

# Punto de entrada del script
if __name__ == "__main__":
    main()