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