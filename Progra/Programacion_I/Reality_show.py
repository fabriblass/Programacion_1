jugador1 = input("Ingrese su nombre jugador numero 1...")
jugador2 = input("Ingrese su nombre jugador numero 2...")
jugador3 = input("Ingrese su nombre jugador numero 3...")

edad1=int(input("Ingrese su edad..." + jugador1 ))
while edad1 <= 25:
    edad1=int(input("Ingrese su edad sabiendo que debe sser mayor de 25 años..."))

edad2=int(input("Ingrese su edad..." + jugador2 ))
while edad2 <= 25:
    edad2=int(input("Ingrese su edad sabiendo que debe sser mayor de 25 años..."))

edad3=int(input("Ingrese su edad..." + jugador3 ))
while edad3 <= 25:
    edad3=int(input("Ingrese su edad sabiendo que debe sser mayor de 25 años..."))

promedio= edad1 + edad2 + edad3 / 3

votos1=int(input("Ingrese su cantidad de votos..." + jugador1 ))
while votos1 <0:
    votos1=int(input("Ingrese nuevamente su cantidad de votos ssabiendo que no puede ser menor a 0"))

votos2=int(input("Ingrese su cantidad de votos..." + jugador2 ))
while votos2 <0:
    votos2=int(input("Ingrese nuevamente su cantidad de votos ssabiendo que no puede ser menor a 0"))

votos3=int(input("Ingrese su cantidad de votos..." + jugador3 ))
while votos3 <0:
    votos3=int(input("Ingrese nuevamente su cantidad de votos ssabiendo que no puede ser menor a 0"))

suma= votos1 + votos2 + votos3

if votos1 > (votos2 and votos3):
    print("El jugador con mas votos es el jugador..." + jugador1)
elif votos2 > (votos1 and votos3):
    print("El jugador con mas votos es el jugador..." + jugador2)
elif votos3 > (votos1 and votos2):
    print("El jugador con mas votos es el jugador..." + jugador3)

print("El promedio de edad es de..." , promedio ) 

print("El total de la cantidad de votos es de..." , suma )
