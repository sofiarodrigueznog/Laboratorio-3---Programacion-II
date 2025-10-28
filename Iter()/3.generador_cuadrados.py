class CuadradosLista:
    #Genera una lista co los cuadrados de los números del 1 al 10
    def obtener_cuadrados(self):
        cuadrados = []
        for numero in range(1, 11):
            cuadrados.append(numero ** 2)
        return cuadrados


if __name__ == "__main__":
    objeto = CuadradosLista()
    resultado = objeto.obtener_cuadrados()
    print("Cuadrados del 1 al 10:")
    print(resultado)