#Ejer2#Leer y mostrar productos: Crear un programa que abra articulos.txt, lea cada 
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Abrir el archivo en modo lectura


import os 
#creo una función para mostar productos, primero pregunto si existe el archivo#
def mostrar_prod():
    if not os.path.exists("productos.txt"):
        print("productos.txt no existe")
        return
    #si el archivo existe lo abro, y creo la variable local archivo que va a contener todos los datos de txt#
    with open("productos.txt", "r", encoding="utf-8") as archivo:
        # Leer línea por línea
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            
            # Mostrar los datos
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

mostrar_prod()

#Ejer3#Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

def agregar_prod():
    nombre = input("Ingrese el producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad del producto: ")
    with open("productos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad} \n")
    print("Producto agregado")

print("Quiere usted agregar productos al archivo?:")
opcion = input("Elija la opcion: 1 para agregar y 0 para no agregar: ")
if opcion == "1":
    agregar_prod()
else:
    print("usted eligió no agregar")


#"Ejer4#"Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
#una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad. 

def cargar_prod_en_lista():
    productos=[]  #creo lista vacia
    #verifico que la lista no este vacia
    if not os.path.exists("productos.txt"):
        print("productos.txt no existe")
        return[]
    with open("productos.txt","r",encoding= "utf-8") as archivo:#abro archivo apra lectura
        for linea in archivo:#recorro linea por linea y voy a separa el nombre, precio y cantidad
            nombre, precio, cantidad=linea.strip().split(",")
            #creo un diccionario, con clave,valor
            producto={
                "nombre":nombre,#toma el valor de la linea del txt nombre
                "precio":precio,#toma el valor de la linea del txt precio
                "cantidad":cantidad#toma el valor de la linea del txt cantidad

            }
            #una vez que ya agrego los datos de la primera linea del txt, lo agrego a productos
            productos.append(producto)#agrego
       
        print("Productos agregados correctamente")
        
        return productos
    
diccionario=cargar_prod_en_lista()
print(diccionario)
#Ejer5#Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
#no existe, mostrar un mensaje de error. 
def buscar_prod(productos):
    if len(productos)==0:
        print("No hay productos en la lista debe carlos primero")
        return
    
    nombre_buscado=input("Ingrese el nombre del producto a buscar: ")
    encontrado=False

    for producto in productos:
        if producto['nombre'].lower()==nombre_buscado.lower():
             print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
             encontrado=True
             break
        
    if not encontrado:
        print("Producto no encontrado")   

buscar_prod(diccionario)

#Ejer6#Guardar los productos actualizados: Después de haber leído, buscado o agregado 
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
#productos actualizados desde la lista. 
def guardar_productos(productos):
    # Verifico si la lista tiene elementos
    if len(productos) == 0:
        print("No hay productos para guardar.")
        return
    
    # Abro el archivo en modo escritura para sobrescribir su contenido
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    
    print("Archivo actualizado correctamente.")
