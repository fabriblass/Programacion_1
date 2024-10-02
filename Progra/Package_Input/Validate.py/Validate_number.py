def validate_number(input_value):
    try:
        
        float(input_value)
        return True
    except ValueError:
        return False


numero = input("Introduce un número: ")
if validate_number(numero):
    print(f"{numero} es un número válido.")
else:
    print(f"{numero} no es un número válido.")
