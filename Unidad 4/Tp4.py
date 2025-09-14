#Ejer1# 1) Crear una lista con las notas de 10 estudiantes. 
#• Mostrar la lista completa. 
#• Calcular y mostrar el promedio. 
#• Indicar la nota más alta y la más baja.
#crear lista de notas#
notas=[7,8,5,9,9,6,2,8,9,7]
#mostrar lista#
print("Notas: ")
for n in notas:
    print(n, end=" ")

print()
#calculo promedio y lo muestro
prom= sum(notas)/len(notas)
print("Promedio :", prom)
#Calculo nota más alta y baja
print("La nota más alta es: ", max(notas))
print("La nota más baja es:", min(notas))

#Ejer2# Pedir al usuario que cargue 5 productos en una lista. 
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
# Preguntar al usuario qué producto desea eliminar y actualizar la lista. 
#pedimos al usuario que cargue 5 productos
productos=[]
for i in range(5):
    item=input(f"Ingrese el producto {i+1}:")
    productos.append(item)

print("\nLista de productos original:")
print(productos)

print("\nLista ordenada alfabeticamente:")
print(sorted(productos))

eliminar=input("\nIngrese el producto que desee eliminar:")

if eliminar in productos:
    productos.remove(eliminar)
else:
    print(f"El producto {eliminar} no existe:")
    
print("La lista actualizada es:",productos)    

#Ejer3#Generar una lista con 15 números enteros al azar entre 1 y 100. 
#• Crear una lista con los pares y otra con los impares. 
# # Mostrar cuántos números tiene cada lista.
import random
numeros=[]
#genero lista con 15 números aleatorios entre 1 y 100
for i in range(15):
    #genero un número entero de 1 a 100 y se guarda en la variable num_aleatorio#
    num_aleatorio=random.randint(1,100)
    #agrego a la lista numero el número aleatorio con append#
    numeros.append(num_aleatorio)
    #Imprimo la lista
print("La lista original es:", numeros)
#separar los pares de los impares genero dos listas #
pares=[]
impares=[]
for numero in numeros:
    if numero%2==0:
        pares.append(numero)
    else:
        impares.append(numero)
print("Los numeros pares son:",pares)
print("La cantidad de números pares son:",len(pares))        
print("Los numeros impares son:",impares)
print("La cantidad de números impares son:",len(impares))   

#Ejer4#Dada una lista con valores repetidos: 
# Crear una nueva lista sin elementos repetidos. 
# Mostrar el resultado.
datos=[1,3,5,3,7,1,9,3]
sin_duplicados=[]
for d in datos:
    if d not in sin_duplicados:
        sin_duplicados.append(d)
print("La lista original es:")
for d in datos:
    print(d, end=" ")
print()
for d in sin_duplicados:
    print(d, end=" ")
print()

#Ejer5#Crear una lista con los nombres de 8 estudiantes presentes en clase. 
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# Mostrar la lista final actualizada.

estudiantes=["Juan","Pedro","Jorge","Luis","Hugo","José","María","Lulu"]
#Muestro lista
for i in estudiantes:
 print(i)

 #Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
opcion=input("Elige (A) para agregar un estudiante y (B)si quieres eliminar").upper()

if opcion=="A":
    nuevo=input("Ingrese el nombre a agregar")
    estudiantes.append(nuevo)
elif opcion=="B":
    eliminar=input("Ingrese el nombre a eliminar")
    if eliminar in estudiantes:
     estudiantes.remove(eliminar)
else:
    print("El estudiante ingresado no existe en la lista:")

print("Lista final:")
for i in estudiantes:
    print(i)

#Ejer6# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#último pasa a ser el primero).
lista=[1,2,3,4,5,6,7]
print("Lista original:",lista)
#acá consigo el ultimo numero de la lista#
ultimo=lista[-1]
#aca consigo todos los numeros menos el ultimo#
resto=lista[:-1]
#lista rotada#
lista_rotada=[ultimo] + resto

print("Lista rotada:",lista_rotada)

#Ejer7#Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
#semana. 
# Calcular el promedio de las mínimas y el de las máximas. 
#Mostrar en qué día se registró la mayor amplitud térmica. 
temperatura=[
    [10,20],
    [12,22],
     [8,10],
    [15,25],
    [11,29],
     [9,17],
    [11,23]
]
# Calcular el promedio de las mínimas y el de las máximas. 

minima = [fila[0] for fila in temperatura]  
maxima = [fila[1] for fila in temperatura]  

#muestro las minimas y maximas#
print(minima)
print(maxima)
#calculo los promedios de minimas y maximas#

prom_minima= sum(minima)/len(minima)
prom_maxima= sum(maxima)/len(maxima)
#Mostrar en qué día se registró la mayor amplitud térmica. 
# aca lo que hago recorrer el arreglo temperatura y  es restar la fila 1 menos la 0 y conseguir la diferencia de temperatura del dia#
# creo un nuevo arreglo con esa diferencia#
amplitudes=[fila[1]-fila[0] for fila in temperatura]
#aca creo una variable que guardara la mayor amplitud de el arreglo amplitudes, .index lo que hace es recorrer el arreglo
#amplitudes y max consigue el mayor valor de ese arrgelo, le agrego mas 1 porque el index recorre  desde la posicion 0 
# y querermos que recorra hasta la posicion 7  ya que despues se va am ostrar por pantalla el día
dia_mayor_amplitud=amplitudes.index(max(amplitudes))+1
print("El día de mayor amplitud es:",dia_mayor_amplitud)

#Ejer8# Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#• Mostrar el promedio de cada estudiante. 
#• Mostrar el promedio de cada materia. 
notas=[
    [7,8,9],
    [5,6,7],
    [9,9,7],
    [10,5,6],
    [2,6,7]
]
print("Notas de estudiantes:")
for fila in notas:
    for nota in fila:
        print(nota,end=" ")
    print()  

#• Mostrar el promedio de cada estudiante. 
print("Promedio de cada estudiante")

for i in range(5):
 suma=0
 for j in range(3):
  suma+=notas[i][j]
 promedio=suma/3
 #aca imprime la posicion del estudiante con el promedio con hasta 2 decimales
 print(f"Estudiante en la posicion { i+1} : {promedio: .2f}")

#• Mostrar el promedio de cada materia. 

for j in range(3):
 suma=0
 for i in range(5):
   suma+=notas[i][j]
 promedio=suma/5
 #aca imprime la posicion del estudiante con el promedio con hasta 2 decimales
 print(f"Promedio por materia {j+1}:{promedio: .2f}")

#Ejer9#Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#• Inicializarlo con guiones "-" representando casillas vacías. 
# •# Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#Mostrar el tablero después de cada jugada. 

#creo tablero de Ta-Te-Ti como una lista de listas (3x3).
 tablero=[]
for i in  range(3):
   fila=[]
   for j in range (3):
      fila.append("-")
   tablero.append(fila)

for fila in tablero:
   for celda in fila:
      print(celda, end=" ")
   print() 

#inicializo variables de control
jugador="X"
jugadas=0
# bucle de 9  jugadas#
while jugadas<9:
   print(f"\nTurno de jugador {jugador}")

   fila=int(input("Ingrese la fila (0-2) :"))
   columna=int(input("Ingrese la columna (0-2) :"))

   if fila<0 or fila>2 or columna<0 or columna>2:
      print("Posición fuera de rango, intente de nuevo:")
      continue
   
   if tablero [fila][columna] =="-":
      tablero [fila][columna]=jugador
      jugadas+=1
   else:
      print("casilla ocupada, intente de nuevo:")
      continue
   for fila in tablero:
      for celda in fila:
         print(celda, end=" ")
      print()

   if jugador=="X":
      jugador="O"
   else:
      jugador="X"
      
  #Ejer10#Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
# Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana.  
#creo matriz de 4 x7#
ventas=[
   [2,3,4,5,6,7,8],
   [9,2,3,6,7,9,1],
   [2,4,6,8,9,2,3],
   [9,3,5,6,7,8,4]
]
#creo una lista con los totales de los productos#
total_productos=[]
for i in range(4):
   total_producto=0
   for j in range(7):
      total_producto=ventas[i][j]
   total_productos.append(total_producto)
   print(f" productos {i +1}: {total_producto}")
# Mostrar el día con mayores ventas totales. 
mayor_ventas=0
dia_mayor=0
for j in range(7):
   total_dia=0
   for i in range(4):
      total_dia=ventas[i][j]
   print(f"Total día {j +1}: {total_dia}")
   if total_dia>dia_mayor:
         mayor_ventas=total_dia
         dia_mayor=j
print(f"El día con mayor ventas es {dia_mayor+1}, con {mayor_ventas} ventas.")
#Indicar cuál fue el producto más vendido en la semana. 

mayor_producto=0
mayor_indice=0

for i in range(4):
   if total_productos[i]> mayor_producto:
      mayor_producto= total_productos[i]
      mayor_indice=i

print(f"El producto más vendido es {mayor_indice+1}, con {mayor_producto} ventas en la semana.")


