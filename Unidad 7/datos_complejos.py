#Ejer1#
#Diccionario dado#

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
#garego frutas#
precios_frutas['Naranjas'] = 1200
precios_frutas['Manzanas'] = 1500
precios_frutas['Peras'] = 2300
#imprimo diccionario #
print(precios_frutas)

#Ejer2#
#actualizar los precios de las siguientes frutas#

precios_frutas['Banana'] = 1330
precios_frutas['Manzanas'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)
#Ejer3# crear una lista que contenga únicamente las frutas sin los precios.
#creo la lista frutas #
frutas = list(precios_frutas.keys())
#imprimo la lista#
print(frutas)

#Ejer4# Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
#creo diccionario#
agenda_contactos={}
#cargo 5 contactos#
for i in range(5):
    nombre=(input("Ingrese el nombre para el contacto:")).lower()
    numero=int(input("Ingrese el número de teléfono:"))
    agenda_contactos[nombre] = numero
    i+=1
contacto=input("Ingrese el nombre del contacto a buscar:").lower()
if contacto in agenda_contactos:
    print(f"El contacto: {contacto} tiene el número:{agenda_contactos[contacto]} ")
else:
    print("El contacto no existe")

#Ejer5#
# Solicitar una frase al usuario
frase = input("Ingrese una frase: ").lower()

# Separar la frase en palabras .split separa la frase en palabras#
palabras = frase.split()

# Encontrar  las palabras únicas usando un set 
palabras_unicas = set(palabras)

# Creo un diccionario vacio para contar las veces que esta cada palabra


cont_palabras = {}

#creo un ciclo for para contar #
for palabra in palabras:
    if palabra in cont_palabras:
        cont_palabras[palabra] += 1
    else:
        cont_palabras[palabra] = 1

# Imprime por pantalla  resultados#
print("\nPalabras únicas:")
print(palabras_unicas)

print("\nCantidad de veces que aparece cada palabra:")
print(cont_palabras)

#Ejer6#) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno.

# Crear un diccionario vacío para guardar alumnos y sus notas

alumnos = {}

# Cargar los nombres y notas
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    
    # Guardar las notas como una tupla
    alumnos[nombre] = (nota1, nota2, nota3)

# Mostrar el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {round(promedio, 2)}")



#Ejer7#Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

# Conjuntos (sets) de estudiantes que aprobaron cada parcial
parcial1 = {"Ana", "Luis", "Sofía", "Martín", "Pedro"}
parcial2 = {"Sofía", "Pedro", "María", "Lucía"}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

#  Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

# Estudiantes que aprobaron al menos un parcial (unión)
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)



# Ejer 8 #
# Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

stock_productos = {'banana': 1200, 'ananá': 2500, 'melón': 3000, 'uva': 1450}

# Consultar stock
prod_existente = input("Ingrese el nombre del producto a buscar: ").lower()# ingresa el ususrio el producto#
# si el producto esta en el stock entonces imprime el producto y su stock y sino imprieme no existe#
if prod_existente in stock_productos:
    print(f"El producto '{prod_existente}' tiene {stock_productos[prod_existente]} unidades en stock.")
else:
    print(f"El producto '{prod_existente}' no existe en el stock.")

# Agregar productos o unidades
print("\nDesea agregar unidades o productos nuevos al stock.")# pregunta si quiere agregar nuevos productos#
cant = int(input("¿Cuántos productos desea agregar?: "))# la cantidad

for i in range(cant): #ciclo de 1 hasta la cantidad ingresada"
    producto = input(f"Ingrese el nombre del producto {i + 1}: ").lower()# ingresa el nombre del producto#
    cantidad = int(input("Ingrese la cantidad del producto: "))#ingresa cantidad 

    # Si ya existe, se suman unidades; si no, se crea el producto nuevo
    if producto in stock_productos:
        stock_productos[producto] += cantidad
        print(f"Se agregaron {cantidad} unidades al producto '{producto}'.")
    else:
        stock_productos[producto] = cantidad
        print(f"Se agregó el nuevo producto '{producto}' con {cantidad} unidades.")

# Mostrar el stock actualizado
print("\nStock actualizado:")
print(stock_productos)

# Ejer 9 #
# Crear una agenda donde las claves sean tuplas (día, hora) y los valores sean eventos

#creo una  agenda con una tupla como clave y de valores los eventos#
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "14:30"): "Clase de programación",
    ("miércoles", "09:00"): "Consulta médica",
}

# Mostrar agenda inicial
print("Agenda actual:")
for clave, evento in agenda.items():
    print(f"{clave[0].capitalize()} a las {clave[1]} : {evento}")#aca imprime la clave en la posicion 0, a las calve posicion 1y evento#

# Permitir agregar un nuevo evento
dia = input("\nIngrese el día del nuevo evento: ").lower()
hora = input("Ingrese la hora del nuevo evento (por ejemplo 15:30): ")
evento = input("Ingrese el nombre del evento: ")

# Creo la tupla como clave
agenda[(dia, hora)] = evento

print("\nEvento agregado con éxito ")

# Mostrar agenda actualizada
print("\nAgenda actualizada:")
for clave, evento in agenda.items():
    print(f"{clave[0].capitalize()} a las {clave[1]} :{evento}")#aca se imprime 

# Ejer 10 #
# Diccionario original: países capitales, con clave los paises y valores las capitales#
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

print("Diccionario original (país: capital):")
print(paises_capitales)##imrime el diccionario original

# Crear nuevo diccionario (capital: país)
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}# aca se crea un nuevo diccionario con la capital: el for pais 
#desempaqueta la tupla pais y capital y capital :pais indica que el nuevo diccionario sera capital :pais#

print("\nDiccionario invertido (capital:  país):")
print(capitales_paises)#imprime el diccionario nuevo

