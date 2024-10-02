#Desarrolle un algoritmo para determinar si un año leído por teclado es o no bisiesto.
#para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100,
#excepto que también sea divisible por 400.

año_elegido = int(input("Elija un año para ver si es bisiesto o no: "))

if año_elegido % 4 == 0 and (año_elegido % 100 != 0 or año_elegido % 400 == 0) :
    print("El año " , año_elegido , " es bisiesto")
else:
    print("El año " , año_elegido , " no es bisiesto")