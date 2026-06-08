archivo = open ("temperaturas.txt", "r")
diccionario = {}

for linea in archivo:
    linea = linea.strip()
    ciudad, temperatura = linea.split(";")
    if ciudad not in diccionario:
        diccionario[ciudad] = [temperatura]
    else:
        diccionario[ciudad].append(temperatura)

archivo.close()

print(diccionario)