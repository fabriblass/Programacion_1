edad=int(input("Ingrese su numero de edad..."))
if edad<10:
    print("Usted es un niño/a")
if edad >=10:
    if edad>13:
        print("Usted paso la edad limite de pre/adolescente")
    else:
        print("Usted es pre/adolescente")  
if edad>=13:
    if edad>17:
        print("Usted no es mas adolescente")
    else:
        print("Usted es adolescente")
print("Adioosss...")
