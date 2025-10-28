numeros = [1, 2, 3, 4, 5]

multiplicados = list(map(lambda x: x * 10, numeros))

if __name__ == "__main__":
    print("Lista original:", numeros)
    print("Cada elemento multiplicado por 10:", multiplicados)