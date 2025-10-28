longitud = lambda cadena: len(cadena)

if __name__ == "__main__":
    texto = input("Ingrese una palabra o frase: ")
    print(f"La longitud de '{texto}' es:", longitud(texto))