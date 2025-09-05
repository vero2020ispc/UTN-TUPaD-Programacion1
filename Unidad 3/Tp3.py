#Ejer1#  Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# aquí hago un ciclo for para imprimir los numeros desde 0 hasta 100#
for cont in range (0,101):
    print(cont)

#Ejer2# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.

#Solicito al usuario ingrese un número#
print("Ingrese un número entero:") 
#asigno a la variable num el valor entero ingresado por teclado#
num=str(int(input()))
#transformo ese entero en una cadena de caracteres para contar los dígitos y luego imprimo el resultado#
digito=len(num)
print(f"El número ingresado es {num}, tiene {digito} dígitos")

#Ejer3# Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.
#solicito al usuario dos valores enteros#
print("Ingrese dos números enteros")
num1=int(input("Ingrese el primer número entero: "))
num2=int(input("Ingrese el segundo número entero: "))
#busco el mayor y el menor#
if num1>num2:
    mayor=num1
    menor=num2
else:
    mayor=num2
    menor=num1
suma=0
 # excluye los extremos#
for i in range(menor+1, mayor): 
    suma += i
print(f"La suma de los enteros entre {num1} y {num2} es: {suma}")

#Ejer4# 
#solicito al usuario ingrese numeros#
print("Ingrese los números que desea sumar e ingrese 0 cuando termine de ingresar los números")
num=int(input())
suma=0
while num !=0:
     suma+=num
     num = int(input())

print(f"La suma total es: {suma}")

#Ejer5# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

#llamo  a la funcion ramdom para crear numeros aleatorios#
import random
print("Introduzca un número entre 0 y 9 y acierte el número alaetorio generado ")
num=int(input())
i=0
#aca la variable numero aleatorio va a tomar un valor entre 0 y 9#
numero_aleatorio = random.randint(0, 9)
#aca verifica que este entre 0 y 9, si es verdadero entonces compara#
while num>=0 and num<=9:
 if num==numero_aleatorio:
    i=i+1
    print(f"Usted ha acertado el número aleatorio {numero_aleatorio} en el intento:{i}  ")
    break
 else:
      print("Usted no ha acertado el número aleatorio")
      num = int(input("Ingrese otro número (entre 0 y 9): "))
      i+=1

#Ejer6#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente. 


for i in range (100,-1,-1):
    if i % 2 == 0:
        print(i)
   
#Ejer7# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.
 
# Inicializo la variable suma como acumulador#   
suma=0
print("Ingrese un número entero:")
num=int(input())
#inicializo la variable j para que me guarde el numero ingresado por el usuario y le sumo 1 para que lo incluya al numero#
j=num+1
for i in range (0,j,1):
    suma=suma+i
    
print("La suma es:",suma)        

#Ejer8#
#  Escribe un programa que permita al usuario ingresar 10 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Inicializo variables en 0#   
par=0
impar=0
positivos=0
negativos=0
i=0
#Mientras i sea menor a 100, va a solicitar un número al usuario#
while i<=100 :
    num=int(input("Ingrese un número :"))
    #verifica si el número es par, sino es impar y lo suma según corresponda a su contador#
    if num % 2 == 0:
        par=par+1
        
    else:
        impar=impar+1
    #verifica si es positivo o negativo y lo suma según corresponda a su contador#      
    if num>0:
        positivos=positivos+1
    else:
        negativos=negativos+1
    i=i+1
print("Cantidad de números pares es:", par)
print("Cantidad de números impares es:", impar)
print("Cantidad de números positivos es:", positivos)
print("Cantidad de números negativos es:", negativos)

#Ejer9# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).
#  
#llamo a la función para usar mean#
from statistics import mode, median, mean 
#inicializo variables#
media=0
i=1
#creo una lista para guardar los numeros#
numeros=[]
while i<=5 :
    num=int(input("Ingrese un número :"))
    #acá guardo la lista de números#
    numeros.append(num)
    #incremento i#
    i=i+1
#Calculo la media#    
media=mean(numeros)
print("La media es :",media)

#Ejer10#
#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

