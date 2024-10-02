""" TEMA A:
UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva
franquicia que se insertará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
Se ingresa de cada encuestado:
● nombre
● edad (no menor a 18)
● está empleado (si-no)
● género (Masculino - Femenino - Otro)
● voto (APPLE, DUNKIN, IKEA)
Se necesita saber:
1. Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA,
cuya edad esté entre 25 y 50 años inclusive.
2. Nombre y voto del encuestado de género Masculino con menor edad.
3. Porcentaje de votos de cada género. 
4. Promedio de edad de los encuestados de género Femenino que votaron
IKEA.
5. Determinar cuál fue el género que tuvo más encuestados. """

""" Nombre: Fabrizo Fernandez
DNI.47101170
DIV.:102 """

nombre= ""
edad= 0
empleado_estado=""
genero= ""
voto=""
cantidad_de_votantes= 8
encuestados_desempleados= 0
 
porcentaje_masculino= 0
porcentaje_femenino= 0
porcentaje_otro= 0
votos_masculinos= 0
votos_femeninas= 0
votos_otros= 0
cantidad_votos= 0

nombre_menor_masculino= ""
voto_menor_masculino= ""
edad_menor_masculino= 0

promedio_edad_femenino= 0
edad_femeninos_suma= 0
voto_femenino_ikea= 0


while cantidad_de_votantes >0:
    edad=int(input("Ingrese su edad:" ))
    if edad < 18:
        print("No puede votar es menor de 18 años.")
    else:

     nombre=input("Ingrese su nombre: ")

     empleado_estado=input("Usted tiene empleo? (SOLO si o no): ")

     genero=input("Ingrese su genero(masculinio-femenino-otro): ")

     voto=input("Ingrese su voto (apple- dunkin- ikea)")
    
     

     if (voto == "dunkin" or voto== "ikea") and (edad >=25 and edad <= 50):
        if empleado_estado == "no":
           encuestados_desempleados+=1
     
     if (edad < edad_menor_masculino or edad_menor_masculino== 0) and (genero== "masculino"):
        nombre_menor_masculino= nombre
        edad_menor_masculino= edad
        voto_menor_masculino= voto

     if genero == "masculino":
        votos_masculinos+=1 
        cantidad_votos+=1
     
     if genero == "femenino":
        votos_femeninas+=1 
        cantidad_votos+=1
        if voto == "ikea":
           edad_femeninos_suma+= edad
           voto_femenino_ikea+=1
     
     if genero == "otro":
        votos_otros+=1 
        cantidad_votos+=1

     cantidad_de_votantes-=1


if votos_masculinos > votos_femeninas and  votos_masculinos > votos_otros:
   print("El genero con mas votos es el masculino.")
elif votos_femeninas > votos_masculinos and votos_femeninas > votos_otros:
   print("El genero con mas votos es el femenino.")
elif votos_otros > votos_masculinos and votos_otros > votos_femeninas:
   print("El genero con mas votos es el otro.")
else:
   print("Todos los generos tuvieron los mismos votos.")
   
   

     


promedio_edad_femenino= edad_femeninos_suma / (voto_femenino_ikea or 1)
porcentaje_masculino= (votos_masculinos / cantidad_votos) * 100
porcentaje_femenino= (votos_femeninas / cantidad_votos) * 100
porcentaje_otro= (votos_otros / cantidad_votos) * 100


print("El promedio de edad de las femeninas que votaron a ikea es de: " , promedio_edad_femenino)

print("El porcentaje de votos de cada genero femenino es: " , porcentaje_femenino )

print("El porcentaje de votos de cada genero otro es: " , porcentaje_otro)

print("El porcentaje de votos de cada genero masculino es: " ,  porcentaje_masculino)

print("Cantidad de encuentados sin empleo es: " , encuestados_desempleados)

print("El nombre, el voto del votante de menor edad es :" , nombre_menor_masculino , voto_menor_masculino )     
    













