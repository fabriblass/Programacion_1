#   Enunciado:

# De los 3 Jugadores de un Reality Show, se registra:
# nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos
#Informar:
#a. nombre del candidato con más votos
#b. nombre y edad del candidato con menos votos
#c. el promedio de edades de los candidatos
#d. total de votos emitidos.
#Todos los datos se ingresan mediante input()
#Nombre: Mauro
#Apellido: Giuliani


VotosTotales= 0
MaxJugadores=3
contador= 1
candidato_mas_votado = 0
candidato_menos_votado = 0
Nombre_candidato_mas_votado= ""
Nombre_candidato_menos_votado= ""
edad_candidato_menos_votado = 0
promedioedades = 0


while contador<=MaxJugadores:
   
    nombre = input(f"Ingrese el nombre del jugador {contador}: ")
   
    while True:
        edad = int(input(f"Ingrese la edad de {nombre}: "))    
        if edad>25:
            break
        else:
            print ("Edad incorrecta, tiene que ser mayor a 25 años")

    votos = int(input(f"Ingrese la cantidad de votos recibidos por {nombre}: "))
    VotosTotales= VotosTotales + votos
    promedioedades= promedioedades + edad

   


    if votos < candidato_menos_votado or candidato_menos_votado== 0 :
        candidato_menos_votado = votos
        edad_candidato_menos_votado = edad
        Nombre_candidato_menos_votado = nombre

    if votos > candidato_mas_votado:
       
        candidato_mas_votado = votos  
        Nombre_candidato_mas_votado = nombre

     

    contador = contador +1

promedioedades = promedioedades/MaxJugadores

print (f"El candidato mas votado es {Nombre_candidato_mas_votado}")
print (f"El jugador {Nombre_candidato_menos_votado} fue el candidato menos votado con una edad  de {edad_candidato_menos_votado}")
print (f"El promedio de edades es de {promedioedades}")
print (f"El total de votos es {VotosTotales} ")










































