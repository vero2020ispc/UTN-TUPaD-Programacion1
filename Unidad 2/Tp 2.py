#Ej1#
#Pido a al usuario que ingrese su edad#
edad_usuario=int(input("Ingresa tu edad: "))
#Aquí evalua si el número ingresado es mayor a 18#
if edad_usuario > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")  
#Ej2#
#Solicito al usuario ingrese una nota#
nota=float(input("Ingrese su nota:"))
#Comparo la nota#
if nota >=6:
    print("Aprobado")
else:
    print("Desaprobado")    
#Ej3#
num1=int(input("Ingrese el primer número par: "))
if num1%2==0:
    print("Ha ingresado un número par:")
else:
    print("Por favor, ingrese un número par")
#Ej4#
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.#
edad_usuario=int(input("Ingresa tu edad: "))
#Aquí evalua si el número ingresado es menor  a 12 #
if edad_usuario < 12:
    print("Usted pertenece a la categoria Niño/a")
elif edad_usuario<18 :
    print("Usted pertenece a la categoria Adolescente")
elif edad_usuario<30 :
    print("Usted pertenece a la categoria Adulto/a joven") 
else:
    print("Usted pertenece a la categoria Adulto/a ")       
   