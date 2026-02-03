"""
Programa que simula el lanzamiento de dados.
Muestra una representación visual del dado y guarda los valores únicos obtenidos.
"""

import random

# Representación visual de las caras del dado
DADOS_DIBUJO = {
    1: "+-------+\n|       |\n|   *   |\n|       |\n+-------+",
    2: "+-------+\n| *     |\n|       |\n|     * |\n+-------+",
    3: "+-------+\n| *     |\n|   *   |\n|     * |\n+-------+",
    4: "+-------+\n| *   * |\n|       |\n| *   * |\n+-------+",
    5: "+-------+\n| *   * |\n|   *   |\n| *   * |\n+-------+",
    6: "+-------+\n| *   * |\n| *   * |\n| *   * |\n+-------+"
}

def lanzar_dados(cantidad, valores_unicos):
    """Lanza la cantidad especificada de dados y actualiza el conjunto de valores únicos."""
    for i in range(1, cantidad + 1):
        valor = random.randint(1, 6)
        print(f"\nLanzamiento nº {i}:")
        print(f"Ha salido un {valor}:")
        print(DADOS_DIBUJO[valor])
        
        if valor not in valores_unicos:
            valores_unicos.add(valor)

def main():
    valores_obtenidos = set() # Usamos un set para valores únicos automáticamente
    
    print("=" * 40)
    print("SIMULADOR DE LANZAMIENTO DE DADOS")
    print("=" * 40)

    while True:
        try:
            linea_entrada = input("\n¿Cuántos dados quieres lanzar? (0 para salir): ").strip()
            
            if not linea_entrada:
                continue
                
            n_lanzamientos = int(linea_entrada)

            if n_lanzamientos == 0:
                print("\n" + "=" * 40)
                if valores_obtenidos:
                    lista_ordenada = sorted(list(valores_obtenidos))
                    print(f"Valores únicos que han salido: {', '.join(map(str, lista_ordenada))}")
                else:
                    print("No se ha lanzado ningún dado.")
                print("Fin del programa. ¡Adiós!")
                print("=" * 40)
                break
                
            if n_lanzamientos < 0:
                print("Error: El número de lanzamientos debe ser positivo.")
                continue

            lanzar_dados(n_lanzamientos, valores_obtenidos)
            
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")

if __name__ == "__main__":
    main()