mes=int(input("Ingrese el mes siendo del 1 al 8..."))
while mes > 8 or mes < 0:
    print("FECHA INCORRENCTA...")
    mes=int(input("Ingrese el mes correcto sabiendo que es solo del 1 al 8..."))
if mes >= 1 or mes <=3:
    print("Usted esta en el curso de ingreso...")
elif mes >=4 or mes <=6:
    print("Usted esta en mes de cursada...")
elif mes==7:
    print("Ustes esta en etapa de parcial...")
elif mes == 8:
    print("Se encuenra en mes de finales...")
print("Muchas gracias...")













