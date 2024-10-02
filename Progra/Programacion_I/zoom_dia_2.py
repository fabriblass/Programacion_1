#Ejercicio 5
#Crear un programa que permita al usuario elegir un candidato por el cual votar.
#Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde,
#candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir
#el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
#Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

voto_usu=str(input("Debe votar entre los candidatos, A, B, o C; Por favor vote..."))

if voto_usu == "A":
    print("Usted a votado al partido ROJO!!!...")
elif voto_usu == "B":
    print("Usted a elegido al partido VERDE!!!... ")
elif voto_usu == "C":
    print("Usted a votado al partido AZUL!!!...")
else:
    print("NOO, OPCION ERRONEA... Intente de nuevo ")

#d.rodriguez@sistemas-utnfra.com.ar