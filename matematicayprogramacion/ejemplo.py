print("=== Conversión de Números ===")
print("1. Decimal a Binario")
print("2. Binario a Decimal")
print("3. Salir")

opcion = input("Elija una opción (1-3): ")

if opcion == "1":
    numero = input("Ingrese un número decimal: ")
    if numero.isdigit():   # valida que sea un número entero positivo
        numero = int(numero)
        binario = bin(numero)[2:]  # conversión sin '0b'
        print(f"El número {numero} en binario es: {binario}")
    else:
        print("Error: Debe ingresar un número entero positivo.")

elif opcion == "2":
    cadena = input("Ingrese un número binario: ")
    if all(caracter in "01" for caracter in cadena):  # valida que solo tenga 0 y 1
        decimal = int(cadena, 2)
        print(f"El binario {cadena} en decimal es: {decimal}")
    else:
        print(" Error: El valor ingresado no es un número binario válido.")

elif opcion == "3":
    print("Programa finalizado.")

else:
    print(" Error: Opción no válida. Intente nuevamente.")
