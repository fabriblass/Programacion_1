fin_bucle = "si"
edad_casado_joven = float("inf")
nombre_casado_joven = " "
edad_pasajero_viejo = 0
sexo_pasajero_viejo = " "
nombre_pasajero_viejo = " "
cantidad_casadas = 0
cantidad_viudas = 0
suma_edad_mujeres = 0
suma_mujeres = 0
promedio_edad_mujeres = 0
suma_edad_solteros = 0
suma_solteros = 0
promedio_edad_solteros = 0


while fin_bucle == "si":
    nombre = input("Nombre del pasajero/a: ")
    sexo = input("Ingrese el sexo del pasajero/a (f/m): ").lower()
    while sexo != "f" and sexo != "m":
        sexo = input("Ingrese correctamente el sexo del pasajero/a (f/m): ")
    edad = int(input("Edad del pasajero/a: "))
    if edad < 18:
        print("El pasajero no puede ser menor de edad")
    else:
        estado_civil = input("Ingrese su estado civil (soltero/casado/viudo): ")
        while estado_civil != "soltero" and estado_civil != "viudo" and estado_civil != "casado":
            print("Ingrese correctamente el estado civil")
            estado_civil = input("Ingrese su estado civil (soltero/casado/viudo): ")

        if sexo == "m" and estado_civil == "casado":
            if edad < edad_casado_joven:
                nombre_casado_joven = nombre
                edad_casado_joven = edad
        if sexo == "m" and edad > edad_pasajero_viejo:
            sexo_pasajero_viejo = sexo
            nombre_pasajero_viejo = nombre
            edad_pasajero_viejo = edad
        if sexo == "f" and estado_civil == "casado":
            cantidad_casadas += 1
        if sexo == "f" and estado_civil == "viudo":
            cantidad_viudas += 1
        if sexo == "f":
            suma_edad_mujeres += edad
            suma_mujeres += 1
        if sexo == "m" and estado_civil == "soltero":
            suma_edad_solteros += edad
            suma_solteros += 1
        
        fin_bucle = input("Ingresar otro pasajero? (si/no): ").lower()
        while fin_bucle != "si" and fin_bucle != "no":
            fin_bucle = input("Ingresar otro pasajero? (si/no): )").lower()

promedio_edad_mujeres = suma_edad_mujeres / suma_mujeres
promedio_edad_solteros = suma_edad_solteros / suma_solteros

if nombre_casado_joven != " ":
    print("El nombre del hombre casado mas joven es: " , nombre_casado_joven)
else: print("No hay hombres casados")

print("El nombre del pasajero mas viejo es: " , nombre_pasajero_viejo , " y su sexo es: " , sexo_pasajero_viejo)
print("En el crucero habrá " , cantidad_casadas , " mujeres casadas")
print("En el crucero habrá " , cantidad_viudas , " mujeres viudas")
print("El promedio de edad de las mujeres es de: " , promedio_edad_mujeres , " (si es 0 es que no hay mujeres)")
print("El promedio de edad de los hombres solteros es de: " , promedio_edad_solteros , " (si es 0 es que no hay hombres solteros)")