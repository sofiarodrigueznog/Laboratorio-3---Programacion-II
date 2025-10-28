from functools import reduce

numeros = [7, 3, 9, 1, 5]

# reduce con una lambda que conserva el número mayor entre dos
mayor = reduce(lambda a, b: a if a > b else b, numeros)

if __name__ == "__main__":
    print("Lista original:", numeros)
    print("El número mayor es:", mayor)