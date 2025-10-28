
numeros = [10, 60, 30, 80, 50, 100]

# Usé filter con una lambda que mantiene los números mayores a 50
mayores_a_50 = list(filter(lambda x: x > 50, numeros))

if __name__ == "__main__":
    print("Lista original:", numeros)
    print("Números mayores a 50:", mayores_a_50)