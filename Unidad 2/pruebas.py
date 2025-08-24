contrasenia=str(input("Ingrese un acontarseña de 8 a 14 caracteres: "))
longitud=len(contrasenia)
if longitud>=7 and longitud<=13:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

