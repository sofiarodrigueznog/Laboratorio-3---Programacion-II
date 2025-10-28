primer_elemento = lambda lista: lista[0] if lista else None

if __name__ == "__main__":
    valores = [50, 30, 20, 90]
    print("Lista original:", valores)
    print("Primer elemento:", primer_elemento(valores))