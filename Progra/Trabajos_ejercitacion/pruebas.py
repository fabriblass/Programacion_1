def numero_primo_false(es_par):
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    if numero % 2 == 0:
        es_par= True
    else:
        es_par= False
        
        return es_par
    
resultado = numero_primo_false(1)
print(resultado)