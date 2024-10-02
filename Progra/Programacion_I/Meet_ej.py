#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#  calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla
#  la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal
#  calculado redondeado con dos decimales.

#Ejercicio 8
#Escribir un programa que pregunte al usuario una cantidad a invertir,
#  el interés anual y el número de años, y muestre por pantalla el capital
#  obtenido en la inversión

cantidad_invertir = float(input("ingrese la cantidad a invertir: "))
interes_anual = float(input("ingrese el interes anual: "))
años_inversion = int(input("Cantidad de años a invertir: "))

interes_anual = interes_anual / 100

total_dinero = cantidad_invertir * interes_anual * años_inversion

print("El dinero a recibir es de: " , total_dinero + cantidad_invertir)