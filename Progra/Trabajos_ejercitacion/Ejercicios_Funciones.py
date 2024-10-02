# """ Escribir una función que calcule el área de un rectángulo. 
# La función recibe la base y la altura y retorna el área.  """

# def calcular_area_rectangulo(base, altura):
#     base =input("Ingrese la base del rectangulo: ")
#     base =int(base)

#     altura =input("Ingrese la altura del rectangulo: ")
#     altura =int(altura)
    
#     area= base * altura

#     return area

# resultado= calcular_area_rectangulo(5, 12)
# print("el area del rectangulos es: " , resultado) 

# #----------------------------------------------------------------#
# """ Escribe una función que calcule el área de un círculo.
# La función debe recibir el radio como parámetro y devolver el área. """

# def calcular_area_circulo(radio):
#     radio =input("Ingrese el radio de su circulo: ")
#     radio =float(radio)

#     perimetro= radio * radio
#     area= perimetro * 3.1416

#     return area

# resultado= calcular_area_circulo()
# print(resultado)

#----------------------------------------------------------#
# """ Crea una función que verifique si un número dado es par o impar. 
# La función debe imprimir un mensaje indicando si el número es par o impar. """

# def numeros_primos(numero):
#     numero= input("Ingrese un numero: ")
#     numero= int(numero)
#     if numero % 2 == 0:
#         print("Tu numero " , {numero} , "no es primo")
#     else:
#         print("Tu numero " , {numero}, "es primo")
        
#         return numero
    
# resultado= numeros_primos(17)
# print(resultado)

#------------------------------------------------------------#
# """ Crea una función que verifique si un número dado es par o impar. 
# La función retorna True si el número es par, False en caso contrario. """

# def numero_primo_false(es_par):
#     numero = input("Ingrese un numero: ")
#     numero = int(numero)
#     if numero % 2 == 0:
#         es_par= True
#     else:
#         es_par= False
        
#     return es_par
    
# resultado = numero_primo_false(1)
# print(resultado)

# ---------------------------------------------------------#

# """ Define una función que encuentre el máximo de tres números. 
# La función debe aceptar tres argumentos y devolver el número más grande. """

# def numero_mayor(numero_mayor):
#     numero_mayor = 0

#     numero_1= input("Ingrese un numero: ")
#     numero_1= int(numero_1)

#     numero_2= input("Ingrese un numero: ")
#     numero_2= int(numero_2)

#     numero_3= input("Ingrese un numero: ")
#     numero_3= int(numero_3)

#     numero_mayor = numero_1
   
#     if numero_2 > numero_mayor:
#         numero_mayor = numero_2
#     if numero_3 > numero_mayor:
#         numero_mayor = numero_3

#     return numero_mayor

# resultado= numero_mayor(1) 
# print("El numero mayor es ", resultado)

#----------------------------------------------#
# """ Diseña una función que calcule la potencia de un número. 
# La función debe recibir la base y el exponente como argumentos y devolver el resultado. """

# def potencia_de_numero(potencia):

#     base=input("Ingrese la base de tu numero: ")
#     base=int(base)

#     potenciador=input("Ingrse por que numero quiere que sea la pontecia: ")
#     potenciador=int(potenciador)

#     potencia = base ** potenciador 
#     return potencia


# resultado= potencia_de_numero(1)
# print(resultado)

#---------------------------------------------------------------------#
# """ Crear una función que reciba un número y retorne True 
# si el número es primo, False en caso contrario. """
# def primo_2 (numero):
#     numero= input("Ingrese un numero: ")
#     numero= int(numero)
#     if numero % 2 == 0:
#         print(True)
#     else:
#         print(False)
        
#         return numero
    
# resultado= primo_2(17)
# print(resultado)

#---------------------------------------------------------------------#
""" Crear una función que (utilizando la función del punto 11), 
muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. 
La función retorna la cantidad de números primos encontrados."""







        
    







