#Ejer1#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario 

def factorial_recur(num):#defino la funcion recursiva
    if num==0:
        return 1
    else:
        return num*factorial_recur(num-1) #calaculo factorial

#pido al usuario ingrese un numero#

num=int(input("Ingrese un número para calcular el factorial: "))

#ciclo para imprimir por cada resultado#

for i in range(1, num + 1):
    print(f"El factorial de {i} es: {factorial_recur(i)}")


#Ejer2#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique. 

def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
    
num=int(input("Ingrese un número para calcular su fibonacci:"))   
for i in range (num):
    print(f"La serie de Fibonacci es  {i} es: {fibonacci(i)}")


#Ejer3# Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
#algoritmo general. 

def potencia_recur(num, exp):
    if exp==0:
        return 1
    else:
         return num * potencia_recur(num, exp- 1)
    
num=int(input("Ingrese el numero para calcular la potencia: "))
exp=int(input("Ingrese el exponente : "))

resultado=potencia_recur(num,exp)
print(f"El número ingresado es {num} el exponente es {exp} y el resultado es: {resultado}")

#Ejer4#Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto. 

# Ejer4: Crear una función recursiva que reciba un número entero positivo en base decimal
# y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2) # Divide el número por 2
        #y descarta los decimales (división entera) y numero % 2 Calcula el resto de esa división (0 o 1). 
        # Ese resto es el último dígito binario.

# Programa principal
numero = input("Ingrese un número decimal: ")

if numero.isdigit():  # valida que sea un número entero positivo
    numero = int(numero)
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")
else:
    print("Error: Debe ingresar un número entero positivo.")

#Ejer5#  Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 

def es_palindromo(palabra):
    # si la palabra tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    else:
        # Compara primera y última letra
        if palabra[0] != palabra[-1]:
            return False
        else:
            # Llamada recursiva con la palabra sin primera y última letra
            return es_palindromo(palabra[1:-1])

# Programa principal
texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(texto):
    print(f"'{texto}' es un palíndromo.")
else:
    print(f" '{texto}' no es un palíndromo.")


#Ejer6#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
#número entero positivo y devuelva la suma de todos sus dígitos. 
 #    Restricciones: No se puede convertir el número a string. Usá operaciones matemáticas (%, //) y recursión.

def suma_digitos(num):
    if num==0:
        return 0
    else:
        resultado=suma_digitos(num // 10) + (num % 10)
        return resultado
    
numero = int(input("Ingrese un número para la suma: "))
result=suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {result}")

#Ejer7#Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#último nivel con un solo bloque.

def contar_bloques(num):
    if num==0:
       return 0
    else:
        bloques=num+contar_bloques(num -1) #suma le num ingresado y le resta 1 para la proxiam invocacion, hast llegara 0
        return bloques

num = int(input("Ingrese el número de bloques en el nivel más bajo: "))

total = contar_bloques(num)
print(f"Para construir una pirámide con {num} bloques en la base se necesitan {total} bloques en total.")

#Ejer8# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#aparece ese dígito dentro del número.

def contar_digito(num, dig):
    # Caso base: si el número llegó a 0, termina
    if num == 0:
        return 0
    else:
        # Si el último dígito es igual al buscado, sumo 1
        if num % 10 == dig:
            return 1 + contar_digito(num // 10, dig)
        else:
            return contar_digito(num // 10, dig)

# Programa principal
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito que desea contar (0-9): "))

resultado = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")


