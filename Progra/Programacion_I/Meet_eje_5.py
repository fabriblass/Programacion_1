#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
#El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre
#posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo,
#y muestre por pantalla el grupo que le corresponde.

GrupoA= "a" and"b"and "c"and "d"and "e"and "f"and "g" and "h" and "i" and "j" and "k" and "l" and "m"
GruopoB = "n"and "ñ"and "o"and "p"and "q"and "r"and "s" and "t"and "u"and "v"and "w"and "x"and "y"and "z"
nombre=input("Ingrese su nombre...")
sexo=input("Cual es tu sexo (F/M)...")
if sexo  == "M":
    if nombre <= "m":
        GrupoA
    else:
        GruopoB
else:
    if nombre >"n":
        GrupoA
    else:
        GruopoB
print("Tu grupo es..." + GrupoA or GruopoB ) 

    
        

