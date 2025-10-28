celsius = [0, 10, 20, 30]

# Aplicamos la conversión a cada elemento de la lista
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))

if __name__ == "__main__":
    print("Grados Celsius:", celsius)
    print("Convertidos a Fahrenheit:", fahrenheit)
