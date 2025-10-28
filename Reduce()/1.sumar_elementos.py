from functools import reduce

numeros = [5, 10, 15, 20]

# reduce con una función lambda que acumula la suma
suma_total = reduce(lambda a, b: a + b, numeros)

if __name__ == "__main__":
    print("Lista original:", numeros)
    print("Suma total:", suma_total)