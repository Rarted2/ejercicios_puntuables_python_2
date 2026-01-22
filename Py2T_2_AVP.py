# Bucle principal: se ejecuta hasta que el usuario escriba 'FIN'
while (palabra := input("Introduzca la palabra o FIN: ").lower()) != "fin":
    
    # Verificamos si es palíndromo comparando la palabra con su versión invertida
    es_palindromo = palabra == palabra[::-1]
    
    # Mostramos el resultado adecuado según la verificación
    print(f"La palabra {palabra} {'es' if es_palindromo else 'no es'} un palíndromo")

print("oooOOO Fin del programa OOOooo")