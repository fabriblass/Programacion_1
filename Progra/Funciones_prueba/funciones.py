def get_int(mensaje: str, mensaje_error: str, num_minmo: int, num_max: int, reitentos: int) -> int| None:
    

    contador_reintentos = 0
    numero = None
    if num_minmo > num_max:
        auxiliar = num_max
        num_max = num_minmo
        num_minmo = auxiliar
       
    while contador_reintentos < reitentos:
            contador_reintentos+=1
            try:
                numero = int(input(mensaje))
                if numero < num_minmo or numero > num_max:
                    numero= None
                    print(mensaje_error)
                else:
                    break
            except ValueError:
                print(mensaje_error)
    return numero
                  
                        
print(get_int("Ingrese un numero mayor a 1 y menor a 20: ", "Invalido, Ingrese nuevamente el numero: " , 1 , 20, 3))

#---------------------------------------------------------------------------------------------------------------------#
def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int)->float|None:
    print(mensaje)
    numero = float(input("• "))
    reintentos -= 2    

    for reintentos in range(reintentos, -1 , -1):
        if numero >= minimo and numero <= maximo:
            return numero
            break
        numero = float(input(mensaje_error))
    if numero >= minimo and numero <= maximo:
        return numero
    return None

resultado= get_float("-Ingrese su altura: ","-La altura no es correcta, vuelva a intentar: ",1.00, 5.00, 3)
print(resultado)


#----------------------------------------------------#

def get_string (mensaje: str, mensaje_error: str, longitud: int, reitentos: int) -> str|None:

    contador_reitentos= 0
    cadena= input(mensaje)
    
    while len(cadena) > longitud:
        cadena= input(mensaje_error)
        contador_reitentos+=1
        print(f"Intento numero: {contador_reitentos}")
        if contador_reitentos >= reitentos:
            print("Se terminaron los intentos.")
            return None
    return cadena

resultado  = get_string("-Ingrese su nombre: ", "-Incorrecto, intente  nuevamente: ", 10,1)
print(resultado)









   





