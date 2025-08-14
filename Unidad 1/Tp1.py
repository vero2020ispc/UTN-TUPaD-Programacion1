#Ejercicio 1#
print( "Hola mundo!")

#Ejercicio 2#
nombre=input("Por favor escribe tu nombre: ")
print(f"Hola {nombre} " )

#Ejercicio 3#
print("Ingrese los datos solicitados a medida que se lo solicite")
nombre=input ("Ingrese su nombre y apellido: ")
edad=input("Ingrese su edad: ")
lugar=input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre}, tengo {edad} años y vivo en {lugar}" )

#Ejercicio 4#
print("Vamos a calcular el área y perímetro de un circulo")
radio=float(input("Ingrese el radio: "))
area=float(3.14*(radio**2))
perimetro=float(2*3.14*radio)
print(f"El área de el circulo es:{area} y el perimetro es: {perimetro}")

#ejercicio 5#
print("Vamos a calcular la cantidad de horas que son los segundos que va a ingresar")
segundos=float(input("Ingrese los segundos: "))
horas=float((segundos// 60) // 60)
print(f"La cantidad de horas son: {horas}")

#Ejercicio 6#
print("Vamos a realizar la tabla de multiplicar de un número")
numero=int(input("Ingrese el número: "))
var1=numero*1
var2=numero*2
var3=numero*3
var4=numero*4
var5=numero*5
var6=numero*6
var7=numero*7
var8=numero*8
var9=numero*9
var10=numero*10
print(f"La tabla de {numero} es: {var1}, {var2}, {var3}, {var4}, {var5}, {var6}, {var7}, {var8}, {var9}, {var10}")

#Ejercicio 7#
print("Ingrese dos números enteros distinto de cero")
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
suma= int(num1+num2)
resta=float(num1-num2)
multiplicacion= int(num1*num2)
division= float(num1/num2)
print(f"La suma es: {suma}, la resta es: {resta},la multiplicación es: {multiplicacion}, la división: es {division}")

#Ejercicio 8#
print("Vamos a calcular su índice de masa corporal")
peso=float(input("Ingrese su peso: "))
altura=float(input("Ingrese su altura: "))
aux=float(altura*altura)
imc= peso/aux
print(f"Su IMC es: {imc}")

#Ejercicio 9#
celsuis=float(input("Ingrese los  grados Celsuis: "))
farenheit=float((celsuis*1.8)+32)
print(f"Los grados Farenheit son:  {farenheit}")

#Ejercicio 10#
print("Vamos a calcular el promedio de  tres números ")
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
num3=float(input("Ingrese el tercer número: "))
promedio= float((num1+num2+num3)/3)
print(f"El promedio es:{promedio}")