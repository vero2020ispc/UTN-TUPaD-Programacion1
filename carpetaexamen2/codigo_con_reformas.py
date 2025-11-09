import csv
import os

NOMBRE_ARCHIVO = "producto.csv"

# Obtener productos desde el archivo CSV
def obtener_productos():
    productos = []

    if not os.path.exists(NOMBRE_ARCHIVO):
        print("Archivo no existe. Se creará uno nuevo.")
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
            escritor.writeheader()
        return productos

    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            productos.append({"nombre": fila["nombre"], "precio": float(fila["precio"])})
    return productos

# Agregar un producto al CSV
def agregar_productos(producto):
    with open(NOMBRE_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
        escritor.writerow(producto)

# Verificar si un producto ya existe
def existe_producto(nombre):
    productos = obtener_productos()
    for producto in productos:
        if producto["nombre"].lower() == nombre.strip().lower():
            return True
    return False

# Validar que el precio sea un número positivo
def validar_numero_positivo(precio):
    if precio.count(".") > 1:
        return False
    if not precio.replace(".", "").isdigit():
        return False
    return True

# Mostrar todos los productos
def mostrar_productos():
    print("---Listado de productos---")
    productos = obtener_productos()
    if not productos:
        print("No hay productos para mostrar")
        return
    print("Nombre      Precio")
    for producto in productos:
        print(f"{producto['nombre']} - ${producto['precio']}")

# Función para agregar un nuevo producto
def agregar_producto():
    print("---Agregar nuevo producto---")
    while True:
        nombre = input("Ingrese nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
        elif existe_producto(nombre):
            print("El producto ya existe.")
        else:
            break

    while True:
        precio = input("Ingrese precio: ").strip()
        if not validar_numero_positivo(precio):
            print("El precio no es válido. Debe ser un número positivo.")
        else:
            precio = float(precio)
            break

    agregar_productos({"nombre": nombre, "precio": precio})
    print("Se agregó correctamente.")

# Guardar productos completos en el CSV
def guardar_productos(productos):
    with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
        escritor.writeheader()
        escritor.writerows(productos)

# Editar un producto existente
def editar_producto():
    productos = obtener_productos()
    if not productos:
        print("No hay productos para editar.")
        return

    nombre = input("Ingrese el nombre a modificar: ").strip()
    if not nombre:
        print("El nombre no puede ser vacío")
        return

    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            while True:
                precio = input("Ingrese nuevo precio: ").strip()
                if not validar_numero_positivo(precio):
                    print("El precio no es válido. Debe ser un número positivo.")
                else:
                    producto["precio"] = float(precio)
                    break
            guardar_productos(productos)
            print("Producto modificado correctamente")
            encontrado = True
            break

    if not encontrado:
        print("No se encuentra el producto en el archivo")

# Eliminar un producto existente
def eliminar_producto():
    productos = obtener_productos()
    if not productos:
        print("No hay productos para eliminar.")
        return

    nombre = input("Ingrese el nombre a eliminar: ").strip()
    if not nombre:
        print("El nombre no puede ser vacío")
        return

    productos_filtrados = [p for p in productos if p["nombre"].lower() != nombre.lower()]

    if len(productos_filtrados) == len(productos):
        print("El producto no se encuentra en el archivo")
        return

    guardar_productos(productos_filtrados)
    print("El producto ha sido eliminado")

# Menú principal con match y loop bloqueante
def mostrar_menu():
    while True:
        print("*" * 40)
        print("1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Editar precio de producto")
        print("4. Eliminar producto")
        print("5. Salir")
        print("*" * 40)

        # Loop bloqueante para validar opción
        opcion = None
        while opcion not in {"1", "2", "3", "4", "5"}:
            opcion = input("Ingrese opción (1-5): ").strip()
            if opcion not in {"1", "2", "3", "4", "5"}:
                print("Opción inválida. Intente nuevamente.")

        match opcion:
            case "1":
                mostrar_productos()
            case "2":
                agregar_producto()
            case "3":
                editar_producto()
            case "4":
                eliminar_producto()
            case "5":
                print("Usted eligió la opción salir")
                break

# Ejecutar el programa
mostrar_menu()
