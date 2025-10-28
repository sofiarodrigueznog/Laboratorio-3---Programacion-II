from functools import reduce

palabras = ["Hola", " ", "Mundo", "!"]

# reduce con una función lambda que concatena las cadenas
frase = reduce(lambda a, b: a + b, palabras)

if __name__ == "__main__":
    print("Lista original:", palabras)
    print("Frase concatenada:", frase)