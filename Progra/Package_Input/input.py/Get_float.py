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