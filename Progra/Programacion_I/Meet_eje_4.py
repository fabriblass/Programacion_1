#Ejercicio 5
#Para tributar un determinado impuesto se debe ser mayor de 16 años
#y tener unos ingresos iguales o superiores a 1000 € mensuales. 
#Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre
#por pantalla si el usuario tiene que tributar o no.

edad = 16
ingresos = 1000
edad1=int(input("Ingrese su edad..."))
ingresos1= float(input("Ingrese sus ingresos mensuales..."))
if edad1 >=edad:
    print("Puede tributar si su ingreso es correcto...")
elif edad1 < edad:
    print("no puede tributar es menor de 16 años... ")
if ingresos1 >= ingresos:
    print("Debe tributar su ingreso mensual...")
elif ingresos1 < ingresos:
    print("No puede tributar su ingreso mensual...")

