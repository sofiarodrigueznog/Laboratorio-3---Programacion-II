def generar_impares(lista_numeros):
    #Recibe una lista y entrega solo los numeros impares
    for numero in lista_numeros:
        if numero % 2 != 0:
            yield numero  # Entrega el número sin devolver toda la lista

if __name__ == "__main__":
    numeros = [4, 7, 10, 13, 22, 5, 6]
    print("Números impares encontrados:")
    for n in generar_impares(numeros):
        print(n)