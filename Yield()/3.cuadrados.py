
class GeneradorCuadrados:
    def __iter__(self):
        for numero in range(1, 11):
            yield numero ** 2  # Entrega el cuadrado de cada número


if __name__ == "__main__":
    print("Cuadrados del 1 al 10:")
    for cuadrado in GeneradorCuadrados():
        print(cuadrado)