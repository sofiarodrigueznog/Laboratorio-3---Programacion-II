def fibonacci_10():
    a, b = 0, 1
    for _ in range(10):   # Repite 10 veces
        yield a           # Entrega el número actual
        a, b = b, a + b   # Actualiza los valores para el siguiente ciclo


if __name__ == "__main__":
    print("Serie de Fibonacci (10 primeros términos):")
    for numero in fibonacci_10():
        print(numero)