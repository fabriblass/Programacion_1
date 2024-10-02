numeros_pares = 0
numeros_impares = 0
numero = int(input("Introduce un número o escribe 0 para detener: "))
 
while numero != 0:
     if numero % 2 == 1:
        numeros_impares += 1
     else:
         numeros_pares += 1
     numero = int(input("Introduce un número o escribe 0 para detener: "))
print("Conteo de números impares:", numeros_impares)
print("Conteo de números pares:", numeros_pares)
