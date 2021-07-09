def contadorLetras(lista_Palavras):
    contador = []
    for x in lista_Palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if __name__ == '__main__':
    lista = ['papagaio', 'lobo', 'cobra']
    print('A palavra',lista[0],'possui',len(contadorLetras(lista[0])),'letras.\n'
          'A palavra',lista[1],'possui',len(contadorLetras(lista[1])),'letras.\n'
          'A palavra',lista[2],'possui',len(contadorLetras(lista[2])),'letras.\n')

