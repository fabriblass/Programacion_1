""" Mostrar los números ascendentes desde el 1 al 10 """

""" for i in list(range(1, 11)):
    print(i)   """
#---------------------------------------------------------#

""" Mostrar los números descendentes desde el 10 al 1 """

""" for i in list(range(10, 0, -1)):
    print(i)  """

#-----------------------------------------------------------------#

""" Ingresar un número. Mostrar los números desde 0 hasta el número ingresado. """
""" numero= 0
numero= input("Ingrese un numero: ")
numero= int(numero)

for i in list(range(0,numero)):
    print(i) """

#-----------------------------------------------------------#

""" Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

	5 x 0 = 0
	5 x 1  = 5
	5 x 2 = 10
	5 x 3  = 15 … """

""" numero= int(input("Ingrese un numero: "))

for i in list(range(0, 11)):
    resultado = i * numero
    print(numero, "X" ,  i , "=" , resultado)
 """
#-----------------------------------------------------------------#

""" Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0.
Mostrar la suma y el promedio de todos los números. """

""" numero = 0
for i in list(range(10)):
    numero= int(input("Ingrese un numero: "))
    if numero == 0:
        break
    print(numero) """

#---------------------#
""" Imprimir los números múltiplos de 3 entre el 1 y el 10 (*) """
""" divisores= 0
for i in list(range(1, 11)):
    if i % 3 == 0:
        divisores= i
        print(divisores)  """

#---------------------------#
""" Mostrar los números pares que hay desde la unidad hasta el número 50 (*) """
""" multiplos= 0
for i in list(range(0, 50)):
    if i % 2 == 0:
        multiplos= i
        print(multiplos) 
 """
#--------------------------------#

""" Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, 
la salida del programa será la siguiente: """


""" numero = int(input("Ingresa un número: "))

for i in range(1, numero + 1):
    for j in range(1, i + 1):
            print(j, end='')
    print()   """
#------------------------------------#
""" Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. 
Mostrar la cantidad de divisores encontrados. """

""" numero= print("introduzca el numero")
numero = int(input()) #aquí se lee el número entero
contador = 0
print("los divisores de ",numero)
for divisor in range(1,numero+1):
    if (numero % divisor) == 0 :
        print(divisor,"es divisor")
        contador += 1
print("el numero ",numero," tiene ",contador," divisores") """

#-----------------------------------------------------------------------#

""" Ingresar un número. Determinar si el número es primo o no. """

numero= int(input("Ingrese un numero: "))
for i in list(range(1)):
    if numero % 2 == 0:
        print("El numero", numero , "no es un numero primo, es divisor")
        break
    print(numero , "Es numero primo") 

#--------------------------------------------------------------------------#

""" Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. 
Informar cuántos números primos se encontraron. """

# primo= 0
# contador_primos= 0
# cantidad= 0
# numero= int(input("Ingrese un numero: "))
# es_primo=  True

# for x in range(2, numero + 1):
#     es_primo= True
#     for i in range(2, x):
#        if x % i == 0:
#         es_primo= False
#         break

#     if es_primo == True:
#       print(f"{x} Es primo")
#       contador_primos+=1
# print(f"se encontraron , {contador_primos}, numeros primos.")



        




  


    
        
       
      


    









