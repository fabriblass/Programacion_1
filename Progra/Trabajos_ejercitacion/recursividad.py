# # Realizar una función recursiva que calcule la suma de los primeros números naturales

# def sumar_naturales(numero:int)-> int:
#     if numero == 1:
#         return 1
#     else:
#         resultado= numero + sumar_naturales(numero - 1)
#     return resultado

# suma_naturales= sumar_naturales(5)
# print(suma_naturales)

#------------------------------------------------------------#
# # Realizar una función recursiva que calcule la potencia de un número
# def potencia_numero(base, exponente):
#     if exponente != 0:
#         resultado= base * potencia_numero(base, exponente - 1)
#         return resultado
#     else:
#         return 1

# potencias= potencia_numero(2, 3)
# print(potencias)

#------------------------------------------------------------#
# Realizar una función recursiva que permita realizar la suma de los dígitos de un número
def suma_digitos(numero):
    if numero==0:
        if numero == 0:
            return 0
        else:
            resultado= numero % 10 + suma_digitos(numero / 10) 
        return resultado
    
digitos= suma_digitos(222)
print(digitos)
