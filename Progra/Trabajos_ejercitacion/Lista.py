# # 1) Escribir una función que reciba una lista de enteros, 
# # la misma calculará y devolverá el promedio de todos los números.

# notas= [7, 6, 6]

# def promedios_de_lista(mi_lista:list)-> float:
#     acumulador = 0
#     lista_cantidad = len(mi_lista)

#     for i in range(len(mi_lista)):
#         acumulador+= mi_lista[i]
    
#     if acumulador > 0:
#         promedio = acumulador / lista_cantidad
#     else:
#         promedio= 0

#     return promedio

# resultado = promedios_de_lista(notas)
# print(resultado)


#---------------------------------------------------#
# 2) Escribir una función parecida a la anterior, 
# pero la misma deberá calcular y devolver el promedio de los números positivos.

# notas= [-2, 7, 7, 7]

# def promedios_de_lista(mi_lista:list)-> float:
#     acumulador = 0
#     contador= 0
#     lista_cantidad = len(mi_lista)

#     for i in range(len(mi_lista)):
#         if mi_lista[i] < 1:
#             print("No hay numeros positivos.")
#         else:
#             contador+=1
#             acumulador+= mi_lista[i]
    
#     if acumulador > 0:
#         promedio = acumulador / contador
#     else:
#         promedio= 0

#     return promedio

# resultado = promedios_de_lista(notas)
# print(resultado)
#------------------------------------------------#
# 3)Escribir una función que calcule y retorne el 
# producto de todos los elementos de la lista que recibe como parámetro.

# def calcular_producto(mi_lista: list)->int:
#     acumulador = 1
    
#     lista_cantidad = len(mi_lista)

#     for i in range(len(mi_lista)):
#        acumulador*= mi_lista[i]

#     return acumulador

# lista=[2, 3, 4]
# producto= calcular_producto(lista)
# print(f"El producto de todos los elementos de la lista es: {producto}")

#-----------------------------------------------------------#
# 4) Escribir una función que reciba como parámetros una lista de enteros y 
# retorne la posición del valor máximo encontrado

# def posicion_maximo(mi_lista: list)-> int:
     
#     bandera_maximo = True
#     maximo = 0
#     posicion = -1
    
#     for i in range (len(mi_lista)):
#         if mi_lista[i] > maximo or bandera_maximo == True:
#             maximo = mi_lista[i]
#             posicion = i
#             bandera_maximo = False
    
#     return posicion

# lista_prueba=[2, 6, 8]
# resultado= posicion_maximo(lista_prueba) + 1
# print(resultado)

#---------------------------------------------#
# 5) Escribir una función que reciba como parámetros una lista de enteros y 
# muestre la/las posiciones en donde se encuentra el valor máximo hallado




#----------------------------------------------------------#
# 6) Escribir una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, 
# un nombre a reemplazar y su correspondiente reemplazo. 
# La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista 
# con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados.

def reemplazar_nombre(lista: list, nombre_original: str, nombre_remplazo: str)-> int:
    pass

    contador = 0

    for i in range (len(lista)):
        if lista[i] == nombre_original:
            lista[i] = nombre_remplazo
            contador+=1
        return contador
    
    
lista_nombres= ["Milan", "Venecia", "Mora", "Fabrizio", "Milan",  "Erica", "Benicio", "Baltazar", "Pablo", "Venecia"]

cantidad_de_remplazos= reemplazar_nombre(lista_nombres, "Milan", "Rojo")
print(f"Cantidad de reemplazos: {cantidad_de_remplazos}")

for j in range (len(lista_nombres)):
    print(lista_nombres[j], end=",")











        
        




