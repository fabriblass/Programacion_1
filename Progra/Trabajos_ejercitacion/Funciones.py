def sumar_1():
    un_numero= input("ingrese un numero")
    un_numero=int(un_numero)
    otro_numero= input("Ingrese otro numero")
    otro_numero= int(otro_numero)

    suma= un_numero + otro_numero

    print(f"La suma es: " ,  {suma})

#MAIN- entry point

sumar_1()
print("Realizamos una suma: ")
sumar_1()

#---------------------------------------------------#
def sumar_2(un_numero , otro_numero):
    suma= un_numero + otro_numero
    print(f"La suma es: " ,  {suma})

un_numero= input("ingrese un numero")
un_numero=int(un_numero)
otro_numero= input("Ingrese otro numero")
otro_numero= int(otro_numero)

sumar_2(un_numero , otro_numero)
sumar_2(7, 9)

#---------------------------------------------------------#

def sumar_3():
    un_numero= input("ingrese un numero")
    un_numero=int(un_numero)
    otro_numero= input("Ingrese otro numero")
    otro_numero= int(otro_numero)

    suma= un_numero + otro_numero

    return suma
#MAIN

resultado= sumar_3() 
#-------------------------------------------------------#
def sumar_4(un_numero, otro_numero):
    suma= un_numero + otro_numero
    return suma

suma= sumar_4()
print(suma)

un_numero= input("ingrese un numero")
un_numero=int(un_numero)
otro_numero= input("Ingrese otro numero")
otro_numero= int(otro_numero)

resultado= sumar_4(un_numero, otro_numero)
print(resultado) 
#----------------------------------------------#

def sumar_4(un_numero, otro_numero, tercer_numero = 0):
    suma= un_numero + otro_numero + tercer_numero
    return suma
resultado= sumar_4(7,8,9)
print(resultado)

resultado= sumar_4(7,8,)
print(resultado) 
#--------------------------------------------------------#
def sumar_4(un_numero, otro_numero, mensaje ,tercer_numero = None):
    print(mensaje)

    suma= un_numero + otro_numero 
    if tercer_numero != None:
        suma+= tercer_numero

    return suma
resultado= sumar_4(7,8,"Estoy sumando")
print(resultado)

resultado= sumar_4(7,8,"Estoy sumando" , 9)
print(resultado)

#-------------------------------------------#
def sumar_4(un_numero: int):
    if un_numero % 2== 0:
        es_par= True
    else:
        es_par= False

resultado= sumar_4(7)
print(resultado)
#-----------------------------------------------#

def determinar_numero(numero:int)->bool:
    es_par= None

    if type(numero)== int:
         es_par= False
         
         if numero % 2== 0:
            es_par= True
       
            
    
    return es_par

resultado= determinar_numero(7)
print(resultado)

    





