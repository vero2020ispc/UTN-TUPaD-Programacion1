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
#Solicito al usuario que ingrese una contraseña, aquí a lo que ingrese lo convierto en string para que luego pueda contar la cantidad de caracteres#
contrasenia=str(input("Ingrese una contraseña de 8 a 14 caracteres: "))
#calculo la longitud#
longitud=len(contrasenia)
#comparo ese valor de longitud#
if longitud>=7 and longitud<=13:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
#Ejer7#
#Solicito al usuario ingrese una palabra o frase#
frase = str(input("Ingrese un palabra o frase:"))
#Aquí se la longitud de la frase o palabra#
longitud=len(frase)
#Acá consigo la última letra de la frase o palabra#
ultima_letra = frase[longitud-1]
#comparo la ultima letra con vocales, si es vocal le agrega el !, sino lo escribe como la ingreso#
if ultima_letra=="a" or ultima_letra=="e" or ultima_letra=="i" or ultima_letra=="o" or ultima_letra=="u":
   print("La frase ingresada es:", frase +"!")
else:
    print("La frase ingresada es:", frase)         