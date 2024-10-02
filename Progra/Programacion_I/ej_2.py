'''
Su tarea es crear el código teniendo en cuenta los siguientes puntos:

pedirá al usuario que ingrese un número entero;
utilizará un bucle while;
comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago.
Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje 
"¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente.
Si el número ingresado por el usuario coincide con el número escogido por el mago,
el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras:
"¡Bien hecho, Junior! Eres libre ahora."
'''
numero_mago = 4

while numero_mago:
 val1=int(input("Ingrese un numero entero..."))
 if val1 == 4:
    print("¡Bien hecho, Junior! Eres libre ahora. El numero era el 4 ")
 else:
    print("¡Ja, ja! ¡Estas atrapado en mi bucle!...")


















