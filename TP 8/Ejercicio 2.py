mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]

diccionario_ubicacion = {}
tipos_medicion = set()

for medicion in mediciones:
    tipo_medicion = medicion[0]
    valor_medicion = medicion[1]
    ubicacion_medicion = medicion[2]

    if ubicacion_medicion not in diccionario_ubicacion:
    
        diccionario_ubicacion[ubicacion_medicion] = []

    diccionario_ubicacion[ubicacion_medicion].append((tipos_medicion, valor_medicion))
    tipos_medicion.add(tipo_medicion)

print(f"Diccionario Resultante: {diccionario_ubicacion}")
print(f"Conjunto de Tipos de Mediciones: {tipos_medicion}")
