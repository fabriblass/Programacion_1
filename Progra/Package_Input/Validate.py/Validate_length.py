def validate_length(input_value, minimo_length=0, maximo_length=None):
    length = len(input_value)
    
    if maximo_length is not None:
        if length < minimo_length or length > maximo_length:
            return False
    else:
        if length < minimo_length:
            return False
    
    return True


text = input("Introduce un texto(mayor a 5 caracteres y menor a 10): ")
minimo_len = 5
maximo_len = 10

if validate_length(text, minimo_len, maximo_len):
    print(f"El texto tiene una longitud válida (entre {minimo_len} y {maximo_len} caracteres).")
else:
    print(f"El texto no cumple con la longitud requerida (mínimo {minimo_len} y máximo {maximo_len} caracteres).")