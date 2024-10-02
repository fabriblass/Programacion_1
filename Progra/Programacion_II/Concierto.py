""" Se nos ha solicitado desarrollar una aplicación para llevar el registro de las entradas vendidas en el Estadio River Plate para el concierto de Asspera. 
El sistema debe solicitar al usuario la siguiente información al momento de comprar cada entrada: 
 Al comenzar el programa, se deberán ingresar los siguientes datos hasta que el usuario decida detenerse: 
Datos a Solicitar para las Ventas: (VALIDAR TODOS LOS DATOS) 
● Nombre del comprador 
● Edad (no menor a 16) 
● Género (Masculino, Femenino, Otro)
Descuentos: 
● Entradas adquiridas con tarjeta de crédito: 20% de descuento sobre el precio de la entrada. OK
● Entradas adquiridas con tarjeta de débito: 15% de descuento sobre el precio de la entrada. OK
Informes Finales: Al finalizar la carga de datos, el programa deberá mostrar los siguientes informes: 
1. Género más frecuente entre los compradores de entradas de tipo "Campo delantero". OK
2. Cantidad de personas que compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio
Lista de Precios: 
● General: $16000 
● Campo delantero: $25000 
● Platea: $30000
3. Porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito respecto al total de personas en la lista. OK
4. Total de descuentos en pesos aplicados por la empresa para pagos con tarjeta de crédito.
 5. Nombre y edad de la persona que pagó el precio más alto por entradas de tipo "General" y su pagó fue con tarjeta de débito. OK
 6. Cantidad de personas que compraron entradas de tipo "Platea" y cuya edad es un número primo. OK
 7. Monto total recaudado por la venta de entradas. de tipo "Platea" pagadas con tarjeta de débito por personas cuyas edades son múltiplos de 6.
Datos a Solicitar para las Ventas: (VALIDAR TODOS LOS DATOS) 
● Nombre del comprador
 ● Edad (no menor a 16)
 ● Género (Masculino, Femenino, Otro) 
● Tipo de entrada (General, Campo delantero, Platea)
 ● Medio de pago (Crédito, Efectivo, Débito) 
● Cantidad de entradas """

nombre= " "
edad= 0
genero= "F" or "M" or "otro"
Metedo_de_pago= "Debito" or "Credito"
general= 16000
campo= 25000
platea= 30000
tipo_de_entrada= "campo" or "general" or "platea"
cantidad_de_entradas= 0
entrada_descuento= 0
valor_de_entrada= 0
precio_total= 0
platea_debito= 0
total_descuento=0
entrada_mas_cara= 0
nombre_entrada_mas_cara= " "
edad_entrada_mas_cara= 0
genero_campodelantero_masculino= 0
genero_campodelantero_femenino= 0
genero_campodelantero_otro= 0
cantidad_platea_edadprimo= 0
contador= 0
contador_general= 0
fin_de_bucle= "si"

while fin_de_bucle == "si":
    print("Bienvenido al la venta online de entradas de el Concierto en River Campus!!")

    nombre=input("Ingrese su nombre para seguir con la compra...")
    edad=int(input("Ingrese su edad para seguir con la compra..."))
    if edad < 16:
        print("Usted es menor de edad no puede continuar con la compra... ")
        fin_de_bucle=input("¿Desea realizar devuelta la compra?(Responder solo con (si/no)).")
        if fin_de_bucle != "si":
            break


    elif edad> 16:
        genero=input("Ingrese su genero (F/M/OTRO) ... ").upper()
        tipo_de_entrada=input("Eliga la ubicacion para ver el show (campo/general/platea)... ").lower()

        Metedo_de_pago=(input("Eliga el medio de pago el caul va realizar la compra (Debito/Credito)..." )).lower()
        if Metedo_de_pago != "debito" or Metedo_de_pago != "credito":
            print("Ingrese el dato correcto")
            Metedo_de_pago=(input("Usted va a abonar con debito/credito?"))

        cantidad_de_entradas=int(input("Ingrese la cantidad de entradas que desea comprar. "))
        if cantidad_de_entradas< 1:
            print("Cantidad invalida, ingrese un valor mayor a 0." )
            cantidad_de_entradas=int(input("Ingrese la cantidad de entradas que desea comprar." ))


        if tipo_de_entrada == "campo":
            valor_de_entrada = campo

        elif tipo_de_entrada== "general":
            valor_de_entrada= general

        elif tipo_de_entrada== "platea":
            valor_de_entrada= platea
        
        if Metedo_de_pago == "debito":
         entrada_descuento= valor_de_entrada * 0.20
        elif Metedo_de_pago== "credito":
          entrada_descuento= valor_de_entrada * 0.15

        if tipo_de_entrada == "campo" and genero == "M":
            genero_campodelantero_masculino+=1
        elif tipo_de_entrada == "campo" and genero == "F":
            genero_campodelantero_femenino+=1
        elif tipo_de_entrada == "campo" and genero == "OTRO":
            genero_campodelantero_otro+=1
        
        if tipo_de_entrada == "platea" and Metedo_de_pago== "debito":
            platea_debito +=1 
        if tipo_de_entrada== "general" and Metedo_de_pago== "debito" and total_entrada > entrada_mas_cara:
            entrada_mas_cara= total_entrada
            nombre_entrada_mas_cara = nombre
            edad_entrada_mas_cara= edad

        if tipo_de_entrada == "platea" and edad % 2 != 0 and edad % 3 != 0 and edad % 5 != 0:
            cantidad_platea_edadprimo += 1
        
        


        


    total_entrada = (valor_de_entrada - entrada_descuento) * cantidad_de_entradas
         

        
   
        


    


    






















