numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usé filter con una función lambda que selecciona los impares
impares = list(filter(lambda x: x % 2 != 0, numeros))

if __name__ == "__main__":
    print("Lista original:", numeros)
    print("Números impares filtrados:", impares)