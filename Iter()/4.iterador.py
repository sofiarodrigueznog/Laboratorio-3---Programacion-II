class MayusIterador:
    def __init__(self, cadenas):
        self.cadenas = cadenas      # Lista original
        self.indice = 0             # Posición actual del iterador

    def __iter__(self):
        return self                 # Devuelve el propio objeto como iterador

    def __next__(self):
        if self.indice < len(self.cadenas):
            palabra = self.cadenas[self.indice].upper()  # Convierte a mayúsculas
            self.indice += 1
            return palabra
        else:
            raise StopIteration      # Finaliza la iteración cuando no quedan elementos

if __name__ == "__main__":
    palabras = ["hola", "mundo", "python", "temuco"]
    print("Palabras en mayúsculas:")
    for p in MayusIterador(palabras):
        print(p)