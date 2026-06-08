Ejercicio 5 — Interpretación de código

```python
def limpiar(texto):
    return texto.strip().capitalize()

def es_valido(nombre):
    if len(nombre) >= 3:
        return True
    return False

nombres = [" bart ", "ED", " walter", "rick "]
validos = []

for nombre in nombres:
    nombre_limpio = limpiar(nombre)

    if es_valido(nombre_limpio):
        validos.append(nombre_limpio)

print(validos)
```

¿Qué hace el programa?
El programa da una lista de nombres. Limpia los espacios, corrige mayúscula y guarda en una lista nueva los nombres que tengan al menos 3 letras.

¿Qué hace la función limpiar?
La funcion limpiar toma un texto, elimina en blanco del principio y del final(con strip), convierte la primera letra en mayúscula dejando el resto en minúsculas (con capitalize).

¿Qué hace la función es_valido?
La función es_valido comprueba si el texto que recibe tiene 3 caracteres o mas. Si es así, nos devuelve True, si tiene menos de 3, nos devuelve False.

¿Qué nombres quedan almacenados en validos?
Quedan guardados los nombres ya limpios y que superaron las 3 letras, en este caso: "Bart", "Walter" y "Rick". "Ed" se decarta porque sólo tiene 2 letras.

¿Qué imprime el programa al finalizar?
El programa al finalizar imrpime la lista: ['Bart', 'Walter', 'Rick']
