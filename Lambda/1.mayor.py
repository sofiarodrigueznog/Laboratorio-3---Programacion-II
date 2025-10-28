mayor = lambda a, b: a if a > b else b

if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print(f"El mayor entre {num1} y {num2} es:", mayor(num1, num2))