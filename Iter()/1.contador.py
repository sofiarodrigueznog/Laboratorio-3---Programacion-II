# Creamos un iterable usando range()
contador = range(10, 16)

# Convertimos el iterable en un iterador
it = iter(contador)

print("Contador del 10 al 15:")

# Obtenemos los valores uno por uno con next()
# (StopIteration ocurre al intentar pasar del 15)
while True:
    try:
        numero = next(it)
        print(numero)
    except StopIteration:
        break  # Cuando no hay más elementos, termina el bucle
