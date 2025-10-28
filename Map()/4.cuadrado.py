numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda x: x ** 2, numeros))

if __name__ == "__main__":
    print("Lista original:", numeros)
    print("Cuadrado de cada número:", cuadrados)