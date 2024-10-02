#Diana Rodriguez
#En el ingreso a un viaje en crucero nos solicitan 
#nombre , 
#edad(mayores de 18), 
#sexo("f" o "m") y 
#estado civil("soltero", "casado" o "viudo");
#Se debe Informar al usuario lo siguiente:
#a)El nombre del hombre casado más joven.OKK
#b)El sexo y nombre del pasajero/a más viejo.OKK
#c)La cantidad de mujeres que hay casadas o viudas.OKK
#d)El promedio de edad entre las mujeres. OKKK
#e)El promedio de edad entre los hombres solteros. OKKK
pasajeros= 3
contador = 0
nombre= " "
edad= 0
sexo= " "
estado_civil= " "

suma_edad_mujeres = 0
suma_mujeres = 0
promedio_edad_mujeres = 0
suma_edad_solteros = 0
suma_solteros = 0
promedio_edad_solteros = 0
edad_casado= 0
edad_viejo= 0
nombre_pasajero_viejo= " "
cantidad_mujeres_casadas_viudas= 0
sexo_pasajero_viejo= " "
nombre_pasajero_mas_joven= " "


while contador < pasajeros:
    edad=int(input("Ingrese su edad..."))
    if edad <18:
        print("Usted es menor de edad no puede continuar...")
    else:
     nombre=input("Ingrese su nombre...")
     sexo=input("Introduzca su sexo (F o M)...").upper()
     estado_civil=input("Ingrese si usted esta casado, soltero o es viudo..." ).lower()
     
     if sexo == "F":
        suma_edad_mujeres += edad 
        suma_mujeres += 1
    
     if sexo== "M" and estado_civil == "soltero":
       suma_edad_solteros += edad
       suma_solteros +=1

     if sexo == "F" and (estado_civil == "casado" or estado_civil == "viudo"):
        cantidad_mujeres_casadas_viudas +=1

     if sexo == "F" or sexo == "M" and edad > edad_viejo:
          sexo_pasajero_viejo= sexo
          edad_viejo = edad
          nombre_pasajero_viejo= nombre

     if sexo == "M" and estado_civil == "casado":
         
        if edad < edad_casado or edad_casado == 0:
         nombre_pasajero_mas_joven= nombre
         edad_casado = edad

          
          


     contador += 1
 


promedio_edad_mujeres = suma_edad_mujeres / (suma_mujeres or 1)
promedio_edad_solteros= suma_edad_solteros / (suma_solteros or 1)

print("El promedio de la edad de mujeres es..." , promedio_edad_mujeres)
print("El promedio de la edad de los solteros es..." , promedio_edad_solteros)
print("El pasajero mas viejo es ..." + nombre_pasajero_viejo + "  " +   sexo_pasajero_viejo + "  "  , edad_viejo)
print("El nombre del pasajero mas joves es..." + nombre_pasajero_mas_joven + " " , edad_casado)
print("Cntadidad de mujeres viudad o casadas es de..." ,  cantidad_mujeres_casadas_viudas)


    










   #"""  if nombre_casado_joven != " ":
    #print("El nombre del hombre casado mas joven es: " , nombre_casado_joven)
#else: print("No hay hombres casados")

#print("El nombre del pasajero mas viejo es: " , nombre_pasajero_viejo , " y su sexo es: " , sexo_pasajero_viejo)
#print("En el crucero habrá " , cantidad_casadas , " mujeres casadas")
#print("En el crucero habrá " , cantidad_viudas , " mujeres viudas")
#print("El promedio de edad de las mujeres es de: " , promedio_edad_mujeres , " (si es 0 es que no hay mujeres)")
#print("El promedio de edad de los hombres solteros es de: " , promedio_edad_solteros , " (si es 0 es que no hay hombres solteros)") """
