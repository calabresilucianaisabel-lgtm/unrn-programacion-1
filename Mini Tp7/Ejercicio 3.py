nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]

#Se crea una lista nueva recorriendo la original, limpiando espacios y acomodando las letras.
nombres_normalizados = []
for nombre in nombres:
    nombre_puro = nombre.strip().capitalize()
    nombres_normalizados.append(nombre_puro)

print(nombres_normalizados)