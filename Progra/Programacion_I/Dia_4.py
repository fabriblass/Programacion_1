sueldo= float(input("Ingrese el valor de su sueldo anual ...."))

if sueldo <= 10000:
    tipo_impositivo = 5
elif  10000 <= sueldo <= 20000:
    tipo_impositivo = 15
elif 20000 >= sueldo <= 35000:
    tipo_impositivo = 20
elif 35000 >= sueldo <=60000:
    tipo_impositivo = 30
else:
    tipo_impositivo = 40
print("Su suekdo suma el porcentaje improvisto es..." , tipo_impositivo , "%") 


















