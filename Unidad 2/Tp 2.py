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
#solicito al usuario ingrese un número par #
num1=int(input("Ingrese un número par: "))
#Divido por dos, si el resto es cero: es par#
if num1%2==0:
    print("Ha ingresado un número par:")
else:
    print("Por favor, ingrese un número par")
#Ej4#
#Solicito al usuario que ingrese su edad#
edad_usuario=int(input("Ingresa tu edad: "))
#Aquí evalua si el número ingresado es menor  a 12 #
if edad_usuario < 12:
    print("Usted pertenece a la categoria Niño/a")
#Aquí evalua si el número ingresado es menor  a 18 #
elif edad_usuario<18 :
    print("Usted pertenece a la categoria Adolescente")
 #Aquí evalua si el número ingresado es menor  a 30 #
elif edad_usuario<30 :
    print("Usted pertenece a la categoria Adulto/a joven") 
else:
    print("Usted pertenece a la categoria Adulto/a ")       
#Ej5#
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string.#
contrasenia=str(input("Ingrese un acontarseña de 8 a 14 caracteres: "))
longitud=len(contrasenia)
if longitud>=7 and longitud<=13:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
