contador = 0
producto = ""
precio = 0
unidades_totales = 0

barbijo_precio = 0
barbijo_caro = 0
barbijo_fabricante = ""
barbijo_unidades = 0

fabricante_unidades = ""

jabon_total = 0

while contador < 6:
    producto = input("Ingrese el producto para prevención de contagio (barbijo, alchol, jabon, etc): ")
    precio = int(input("Ingrese el precio del producto: "))
    while precio < 100 or precio > 300:
        precio = int(input("Ingrese un precio valido"))     
    unidades = int(input("Ingrese la cantidad de unidades: "))
    while unidades <= 0 or unidades > 1000:
        unidades = int(input("Ingrese un numero valido de unidades (Mayor a 0 y menor a 1000): ")) 
    fabricante = input("Ingrese el nombre del fabricante del producto: ")
    if 100 > precio > 300: 
        precio= int(input("El precio esta fuera de los limites porfavor ingrese un precio valido: "))

    if producto == "barbijo":
        barbijo_precio = precio
        if barbijo_precio > barbijo_caro:  
            barbijo_caro = barbijo_precio
            barbijo_fabricante = fabricante
            barbijo_unidades = unidades
    
    if unidades > unidades_totales:
        unidades_totales = unidades
        fabricante_unidades = fabricante

    if producto == "jabon":
        jabon_total += unidades

    contador += 1

print("De los barbijos caros se pidieron",barbijo_unidades,"del fabricante",barbijo_fabricante)
print("Se pidieron una cantidad de unidades de:",unidades_totales,"del fabricante",fabricante_unidades)
print("Unidades de jabones totales:",jabon_total)


