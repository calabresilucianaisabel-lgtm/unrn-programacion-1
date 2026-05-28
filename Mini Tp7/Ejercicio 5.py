codigo = input("Ingresá el código de la materia: ")

if codigo.count("-") == 1: #Se valida que tenga un guión
    partes = codigo.split("-")
    izquierda = partes[0].strip()
    derecha = partes[1].strip()

    if izquierda.isalpha() and derecha.isdigit(): #Se valida que la izquierda tenga letras y la derecha tenga números, normalizamos a mayúsculas.
        codigo_validado = codigo.upper()
        print(f"Código válido: {codigo_validado}")
    else:
        print("Código inválido: Debe tener letras antes del guón y sólo números después")
else:
    print("El codigo debe tener un único guión separando las letras de los números.")