palabras = ["uno", "dos", "tres"]

# Usando map y len directamente
longitudes = list(map(len, palabras))

if __name__ == "__main__":
    print("Lista original:", palabras)
    print("Longitud de cada palabra:", longitudes)