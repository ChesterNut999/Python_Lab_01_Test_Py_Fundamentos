# ------------------------ CASO 1 - LAMBDA | FUNÇÕES ANÔNIMAS
print('# ------------------------ CASO 1 - LAMBDA | FUNÇÕES ANÔNIMAS COM IMPUT DO USUÁRIO')
contador_Letras = lambda lista: [len(x) for x in lista]

lista_Animais = ['Gato', 'Pato']
print(lista_Animais[0],'possui',len(contador_Letras(lista_Animais[0])),'letras.\n',
      lista_Animais[1],'possui',len(contador_Letras(lista_Animais[1])),'letras.\n')

soma = lambda a, b: a + b
print('A soma é igual a:', soma(a=int(input('Digite o 1° valor: ')), b=int(input('Digite o 2° valor: '))),'\n')

multiplicacao = lambda a, b: a * b
print('A multiplicacao é igual a:', multiplicacao(a=int(input('Digite o 1° valor: ')), b=int(input('Digite o 2° valor: '))),'\n')

# ------------------------ CASO 2 - LAMBDA | FUNÇÕES ANÔNIMAS
print('# ------------------------ CASO 2 - LAMBDA | FUNÇÕES ANÔNIMAS COM DICIONÁRIOS E PARÂMETROS')
calculadora_dic = {
    'soma': lambda a, b: a + b,
    'multiplicacao': lambda a, b: a * b,
}
print(type(calculadora_dic))

soma = calculadora_dic['soma']
multiplicacao = calculadora_dic['multiplicacao']
print('Soma com parâmetros: {}' .format(soma(10, 7)))
print('Multiplicação com parâmetros: {}' .format(multiplicacao(100, 6)))
