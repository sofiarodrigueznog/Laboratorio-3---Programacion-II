class Impares:
    def __iter__(self):
        for numero in range(1, 21):
            if numero % 2 != 0:
                yield numero  # Entrega el número impar

if __name__ == "__main__":
    print("Números impares del 1 al 20:")
    for n in Impares():
        print(n)
