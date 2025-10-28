from functools import reduce

numeros = [2, 3, 4]

# reduce con una función lambda que multiplica los valores
producto_total = reduce(lambda a, b: a * b, numeros)

if __name__ == "__main__":
    print("Lista original:", numeros)
    print("Producto total:", producto_total)