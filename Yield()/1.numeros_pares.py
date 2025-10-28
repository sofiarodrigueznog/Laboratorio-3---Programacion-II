# Generador que devuelve los primeros 10 números pares
def pares_10():
    for i in range(10):
        yield i * 2  # 0, 2, 4, 6, ..., 18

if __name__ == "__main__":
    print("Primeros 10 números pares:")
    for p in pares_10():
        print(p)