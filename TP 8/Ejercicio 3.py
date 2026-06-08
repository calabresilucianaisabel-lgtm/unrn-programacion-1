lista_nombres = []

while len(lista_nombres) < 4:
    nombre = input("Ingrese su nombre: ")
    nombre_normal = nombre.strip().capitalize()

    if nombre.isalpha and nombre != "":
        lista_nombres.append(nombre)

archivo = open("alumnos.txt", "w")

for nombre in lista_nombres:
    archivo.write(f"{nombre} \n")
archivo.close()