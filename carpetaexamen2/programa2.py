import csv
import os

NOMBRE_ARCHIVO = "producto.csv"

def obtener_productos():
    productos = []


    if not os.path.exists(NOMBRE_ARCHIVO):# pregunto si el archivo existe y si no existe ingresa aca#
        print("Archivo no existe")
        #abro el archivo en modo escritura con el w
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            #escribo dentro el csv. con el escritor, le mando el archivo con los encabezados, nombre y precio#
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
            #aca escribo los encabezados
            escritor.writeheader()
        return productos

    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:#abro archivo producto.csv; el newline hace que no agregue
        #un enter despues de cada linea, el encoding utf-8 es el más comun#
        #lector(.dictreader empieza a leer el archivo que se envia, devuelve un iterador uqe lee cada una de las lineas
        #un diccionario (nombre,precio)
        lector = csv.DictReader(archivo)

        #con el for recorro cada uno de los items de lector#
        for fila in lector:
            #agrego un diccionario, como clave nombre, y de valor precio se convierte aflotante porque era un string y 
            #por último muestro con el return.
            productos.append({"nombre": fila["nombre"], "precio": float(fila["precio"])})
    return productos    
#defino la funcion agregar producto#
def agregar_productos(producto):
    with open(NOMBRE_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:#abro el archivo para agregar con a, #
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])#abro para escritura con los encabezados#
        escritor.writerow(producto)#guardo una columna
#
def existe_producto(nombre):
    productos = obtener_productos()
    #recorro productos para ver si el producto ya existe#
    for producto in productos:
        if producto["nombre"].lower() == nombre.strip().lower():#pregunto si ese producto esta, pongo todo en minuscula, y si existe
           #si esta escribe true y sino false
            return True
    return False
#la función valida que el precio sea n°positivo #
def validar_numero_positivo(precio):
    if precio.count(".") > 1:
        return False
    if not precio.replace(".", "").isdigit():#reemplaza los puntos por nada, isdigit si todos no son digitos retorna un false
        return False
    return True

def mostrar_productos():
    print("---Listado de productos---")
    productos = obtener_productos()
    if not productos:
        print("No hay productos para mostrar")
        return
    print("Nombre      Precio")
    #aca hago un for para que recorra mostrar productos y sus precios#
    for producto in productos:
        print(f"{producto['nombre']} - ${producto['precio']}")
#pido el nombre del producto, saco los espacios adelante y final, voy validando
def agregar_producto():
    print("---Agregar nuevo producto---")
    nombre = input("Ingrese nombre: ").strip()

    if existe_producto(nombre):
        print("El producto ya existe")
        return
    
    precio = input("Ingrese precio: ").strip()

    if not validar_numero_positivo(precio):
        print("El precio no es válido")
        return
    
    precio = float(precio)
    agregar_productos({"nombre": nombre, "precio": precio})
    print("Se agregó correctamente")

def guardar_productos(productos):
    with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:#aca abrimos el archivo para ecsritura con w
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
        escritor.writeheader()#escribe los encabezados
        escritor.writerows(productos)#crea varias columnas
#defino la funcion para editar
def editar_producto():
    nombre = input("Ingrese el nombre a modificar: ").strip()#solicito el nombre a modificar y strip saca espacios#
    if not nombre:#si no cargaron ningun nombre #
        print("El nombre no puede ser vacío")
        return

    productos = obtener_productos()
    encontrado = False# bandera falsa que cambiara de valor#
    #recorro los productos#
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():#si el producto en el indice nombre es igual al nombre del producto
            precio = input("Ingrese nuevo precio: ").strip()#ingresa el nuevo precio
            if not validar_numero_positivo(precio):#si el precio no es positivo#
                print("El precio no es válido")
                return
            producto["precio"] = float(precio)#se cambia el precio
            guardar_productos(productos) #guardo 
            encontrado = True #aca la bandera cambio de valor ya que el producto fue encontardo
            print("Producto modificado correctamente")
            break

    if not encontrado:#aca la bandera quedo en false e imprime #
        print("No se encuentra el producto en el archivo")

#defino la funcion eliminar#
def eliminar_producto():
    nombre = input("Ingrese el nombre a eliminar: ").strip()#pido el nombre del producto y pregunto si esta vacio
    if not nombre:
        print("El nombre no puede ser vacío")
        return

    productos = obtener_productos()#llamo a al función obtener productos
    productos_filtrados = [] #creo una tupla

    #recorro lista de productos
    for producto in productos:
        if nombre.lower() != producto["nombre"].lower():#si producto es distinto a producto
            productos_filtrados.append(producto)# 

    if len(productos_filtrados) == len(productos):# si es 
        print("El producto no se encuentra en el archivo")
        return

    guardar_productos(productos_filtrados)# 
    print("El producto ha sido eliminado")

def mostrar_menu():
    while True:
        print("*" * 40)
        print("1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Editar precio de producto")
        print("4. Eliminar producto")
        print("5. Salir")
        print("*" * 40)
        opcion = input("Ingrese opción: ").strip()

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            editar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("Usted eligió la opción salir")
            break
        else:
            print("Opción ingresada no válida")

mostrar_menu()
