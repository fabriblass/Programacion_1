# Fecha:26/08/2024
# UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, 
# que promete revolucionar el mercado.

# Las posibles aplicaciones son las siguientes:
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA),
# Internet de las cosas (IOT)

# Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

# A) Los datos a ingresar por cada empleado encuestado son:
# nombre del empleado
# edad (no menor a 18)
# género (Masculino - Femenino - Otro)
# tecnologia (IA, RV/RA, IOT)  
# B) Cargar por terminal 10 encuestas.
# C) Determinar:
# 1)Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
# 2)Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
# 3)Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.

encuestados = 0
i = True
while encuestados < 10 and i == True:
    encuestados += 1

    #ingración de datos ↓
    nombre = input("• Ingrese su nombre: ") #Nombre

    edad = int(input("• Ingrese su edad: "))  #Edad ↓
    while edad < 18:
        edad = int(input("Error, vuelva a intentar: "))
    
    genero = input("• Ingrese su genero ( Masculino / Femenino / Otro ): ") #Género ↓
    while genero != "Masculino" and genero != "Femenino" and genero !="Otro":
        genero = input("• Error, vuelva a intantar: ")
    
    tecnologia = input("• Ingrese la tecnologia ( IA / RV / IOT ): ") #Género ↓
    while tecnologia != "IA" and tecnologia != "RV" and tecnologia !="IOT":
        tecnologia = input("• Error, vuelva a intantar: ")
    
    #Filtros ↓
    
    cantidad_empledos_preguta1 = 0
    if genero == "Masculino":
        if tecnologia == "IOT" or tecnologia == "IA":
            if edad >= 25 or edad <=50:
                cantidad_empledos_preguta1 += 1

    cantidad_empledos_pregunta2 = 0
    if genero != "Femenino":
        if tecnologia != "IA":
            if edad >= 33 or edad <= 40:
                cantidad_empledos_pregunta2 += 1

    i = input("desa continuar?: ")
    if i == "si":
        i = True
    else:
        i = False
    print("•---------------------------------•\n")

# 1)Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.


mensage = f"Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive es de {cantidad_empledos_preguta1}"
print(mensage)

# 2)Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.

ptj = 0
if cantidad_empledos_pregunta2 > 0:
    ptj = cantidad_empledos_pregunta2 * 100 / encuestados

mensage = f"porcentaje empleados pregunta 2 es de : {round(ptj,2)}%"
print(mensage)