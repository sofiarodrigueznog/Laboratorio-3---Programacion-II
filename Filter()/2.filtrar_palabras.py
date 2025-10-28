palabras = ["perro", "gato", "pato", "hamster"]

# Usé filter con una lambda que verifica si la palabra comienza con 'p'
empiezan_con_p = list(filter(lambda palabra: palabra.startswith("p"), palabras))

if __name__ == "__main__":
    print("Lista original:", palabras)
    print('Palabras que empiezan con "p":', empiezan_con_p)