continuar = "si"
genero_m_delantero = 0
genero_f_delantero = 0
genero_otro_delantero = 0
genero_campo_delantero = " "
general_credito = 0
edades_general_credito = 0
platea_debito = 0
suma_entradas_totales = 0
total_descuento_credito = 0
entrada_general_debito_caro = 0
nombre_general_debito_caro = " "
edad_general_debito_caro = 0
cantidad_platea_edadprimo = 0
total_recaudado_platea_debito_x6 = 0
precio_entrada = 0
entrada_descuento = 0
total_personas = 0

while continuar == "si":
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    if edad < 16:
        print("Debe ser mayor que 16 para comprar entradas")
        continuar = input("Ingresar otra compra? (INGRESAR SOLO si/no) ")
        if continuar != "si":
            break

    elif edad >= 16: 
        genero = input("Género: ")
        while genero != "masculino" and genero != "femenino" and genero != "otro":
            print("Escribir una opción válida (masculino,femenino,otro)")
            genero = input("Género: ")

        tipo_entrada = input("Tipo de entrada (general,campo delantero,platea): ")
        while tipo_entrada != "general" and tipo_entrada != "campo delantero" and tipo_entrada != "platea":
            print("Ingrese un tipo de entrada válido")
            tipo_entrada = input("Tipo de entrada (general,campo delantero,platea): ")
        
        medio_de_pago = input("Medio de pago (credito,efectivo,debito): ")
        while medio_de_pago != "credito" and medio_de_pago != "efectivo" and medio_de_pago != "debito":
            print("Ingrese un medio de pago valido")
            medio_de_pago = input("Medio de pago (credito,efectivo,debito): ")
    
        cantidad = int(input("Cantidad de entradas: "))
        while cantidad < 1:
            print("Ingrese un numero mayor a 0")
            cantidad = int(input("Cantidad de entradas: "))
       
        if tipo_entrada == "general":
            precio_entrada = 16000
        elif tipo_entrada == "campo delantero":
            precio_entrada = 25000
        else:
            precio_entrada = 30000
         
        if medio_de_pago == "credito":
            entrada_descuento = precio_entrada * 0.2
            total_descuento_credito += entrada_descuento
        elif medio_de_pago == "debito":
            entrada_descuento = precio_entrada * 0.15
    
        total_entrada = (precio_entrada - entrada_descuento) * cantidad
    
        if tipo_entrada == "campo delantero" and genero == "femenino":
            genero_f_delantero += 1
        elif tipo_entrada == "campo delantero" and genero == "masculino":
            genero_m_delantero += 1
        elif tipo_entrada == "campo delantero" and genero == "otro":
            genero_otro_delantero += 1

        if tipo_entrada == "general" and medio_de_pago == "credito":
            general_credito += 1
            edades_general_credito += edad
        if tipo_entrada == "platea" and medio_de_pago == "debito":
            platea_debito += 1

        if medio_de_pago == "debito" and tipo_entrada == "general" and total_entrada > entrada_general_debito_caro:
            entrada_general_debito_caro = total_entrada
            nombre_general_debito_caro = nombre
            edad_general_debito_caro = edad
        
        if tipo_entrada == "platea" and edad % 2 != 0 and edad % 3 != 0 and edad % 5 != 0:
            cantidad_platea_edadprimo += 1
        
        if tipo_entrada == "platea" and medio_de_pago == "debito" and edad % 6 == 0:
            total_recaudado_platea_debito_x6 += total_entrada
    
        total_personas += 1
    
        continuar = input("Ingresar otra compra? (si/no) ")
        while continuar != "si" and continuar != "no":
            continuar = input("Ingresar otra compra? (INGRESAR SOLO si/no) ")


if genero_f_delantero >= genero_m_delantero and genero_f_delantero >= genero_otro_delantero:
    genero_campo_delantero = "Femenino"
elif genero_m_delantero >= genero_f_delantero and genero_m_delantero >= genero_otro_delantero:
    genero_campo_delantero = "Masculino"
else:
    genero_campo_delantero = "Otro"
        

if total_personas > 0:
    if genero_f_delantero != 0 or genero_m_delantero != 0 or genero_otro_delantero != 0:
        print("Género más frecuente en compra de entradas de campo delantero:", genero_campo_delantero)
    else:
        print("No se compraron entradas en el campo delantero")

    if general_credito > 0:
        print("Cantidad de personas que compraron entradas general pagando con crédito:", general_credito)
        print("Y el promedio de sus edades es:", round(edades_general_credito / general_credito, 1))
    else:
        print("No se compraron entradas general pagando con crédito")

    print("El porcentaje de personas que compraron platea y pagaron con débito:", round(platea_debito / total_personas * 100, 2), "%")
    
    print("Total de descuentos aplicados por pagos con crédito:", total_descuento_credito, "$")
    
    if nombre_general_debito_caro != " ":
        print("Nombre de la persona que más pagó por entradas general y su pago fue con débito:", nombre_general_debito_caro)
        print("Y su edad fue de", edad_general_debito_caro, "años")
    else:
        print("No se compraron entradas en general")
    
    print("Cantidad de personas que compraron entradas de Platea y cuya edad es un número primo:", cantidad_platea_edadprimo)
    
    print("Recaudado por ventas de platea pagadas con débito por personas con edad múltiplo de 6:", total_recaudado_platea_debito_x6, "$")
else:
    print("No se compraron entradas")
    