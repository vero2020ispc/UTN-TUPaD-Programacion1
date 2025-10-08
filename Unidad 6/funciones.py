#Ejer1#
# Crear una función llamada imprimir_hola_mundo que imprima por
 #pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo() 


#Ejer2#
# Crear una función llamada saludar_usuario(nombre) que reciba  como parámetro un nombre y devuelva un saludo personalizado.
 #Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de volver: “Hola Marcos!”. Llamar a esta función desde el programa
 #principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print("Hola", nombre,"!")

usuario=str(input("Ingrese su nombre:")) #solicito al ususario ingrese su nombre3
saludar_usuario(usuario) #llamo a la funcion y le mando el  argumentos#

#Ejer3#
# Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 #[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores in
#ingresados


def informacion_personal(nombre, apellido, edad, residencia):
    print("Soy", nombre, apellido, "tengo", edad, "años y vivo en", residencia)

print("Ingrese sus datos personales:") ##solicito al ususario ingrese sus datos personales#

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia) #llamo a la funcion y le mando los argumentos#

#Ejer4#
#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):    #funcion para calcular el area#
    area=float(3.14*(radio**2))
    print("El área del radio ingresado es:",area)

def calcular_perimetro_circulo(radio):    #funcion para calcular perimetro#
    perimetro=float(2*3.14*radio)
    print("El perimetro del radio ingresado es:",perimetro)

radio=(float(input("Ingrese el radio del circulo:")))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#Ejer5#
## Crear una función llamada segundos_a_horas(segundos) que reciba  #una cantidad de segundos como parámetro y devuelva la cantidad
 #de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#funcion para calcular las horas #
def segundos_a_horas(segundos):
    horas=int ((segundos/3600)*100)/100
    print("Los segundos ingresados", segundos , "son", horas, "horas")


seg=float(input("Ingrese los segundos a calcular:")) #usuario ingresa los segundos#

segundos_a_horas(seg)  #llamo a la funcion y le envio el argumento#

#Ejer6#
#Crear una función llamada tabla_multiplicar(numero) que reciba un  número como parámetro y imprima la tabla de multiplicar de ese
 #número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):  #funcion para las tablas #
   for i in range (1,11):
       resultado=numero*i
       print(numero,"x",i, "=",resultado)
       i+=1

num=(int(input("Ingrese el número para obtener la tabla:"))) #solicito al usuario el numero de la tabla#

tabla_multiplicar(num)  #llamo a la funcion#

#Ejer7#
#Crear una función llamada operaciones_basicas(a, b) que reciba  dos números como parámetros y devuelva una 
# tupla con el resulta do de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara

def operaciones_basicas(a, b):   #funcion par calculat las oparciones básicas#
    suma= a+b
    if a>b:
     resta= a-b
    else:
         resta=b-a
    
    multiplicacion=a*b

    if a!=0 and b!=0:
        if a>b:
         division=a/b
        else:
            division=b/a

    operaciones=[suma, resta, multiplicacion, division]
    return operaciones


#solicito al usario dos numeros#
num1=int(input("Ingrese el primer número:"))
num2=int(input("Ingrese el segundo número:"))

resultados=operaciones_basicas(num1,num2)  #llamo a la funcion y envio argumentos)
print(resultados)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#Ejer8#
#Crear una función llamada calcular_imc(peso, altura) que reciba el  peso en kilogramos y la altura en metros, 
# y devuelva el índice de  masa corporal (IMC). Solicitar al usuario los datos y 
# llamar a la función para mostrar el resultado con dos decimales

def calcular_imc(peso,altura):  #funcion para calcular el imc#
    aux=float(altura*altura)
    imc= peso/aux
    print(f"Su IMC es: {imc}")

print("Vamos a calcular su índice de masa corporal")
peso=float(input("Ingrese su peso: "))
altura=float(input("Ingrese su altura: "))

calcular_imc(peso,altura)  #llamo a la función#

#Ejer9#
#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba  una temperatura en grados Celsius y 
# devuelva su equivalente en  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el  resultado usando la función.

def celsius_a_fahrenheit(celsius):  #funcion pra calcular los grados farenheit#
    
    farenheit=float((celsius*1.8)+32)
    print(f"Los grados Farenheit son:  {farenheit}")

grados_celsuis=float(input("Ingrese los  grados Celsuis: ")) #solicito al usuario los grados celsius#
celsius_a_fahrenheit(grados_celsuis)  #llamo a la funcion#

#Ejer10#
#Crear una función llamada calcular_promedio(a, b, c) que reciba  tres números como parámetros y
#  devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a,b,c):   #funcion para calcular promedio#
    promedio= float((num1+num2+num3)/3)
    print(f"El promedio es:{promedio}")

print("Vamos a calcular el promedio de  tres números ")  #solicito al usuario tres nuemros#
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
num3=float(input("Ingrese el tercer número: "))
calcular_promedio(num1,num2,num3)  #llamo a la funcion y envio tres numeros#