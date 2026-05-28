entrada = input("Ingresa tu edad: ")
edad_limpia = entrada.strip()

if edad_limpia.isnumeric():
    edad = int(edad_limpia)
    if 0 <= edad <= 120:
        print(f"Edad registrada: {edad}")
    else:
        print("La edad ingresada debe estar entre 0 y 120 años.")
else:
    print("El dato ingresado no es un número válido.")