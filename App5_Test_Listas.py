# ------------------------ CASO 1 - LISTAS
print('# ------------------------ CASO 1 - LISTAS')

lista = [1, 3, 5, 7]
lista_animais = ['cachorro', 'gato', 'elefante']

print(lista)
print(lista_animais[1])
print('')

# ------------------------ CASO 2 - LISTAS COM LAÇOS DE REPETIÇÃO
print('# ------------------------ CASO 2 - LISTAS COM LAÇOS DE REPETIÇÃO')
soma: float = 0
for x in lista:
    print(x,' | ',end="")
    soma += x
print('\n')
print('Soma dos valores da lista: ', sum(lista))
print('Maior valor da lista: ', max(lista))
print('Menor valor da lista: ', min(lista))
print('')

# ------------------------ CASO 3 - LISTAS COM CONDICIONAIS
print('# ------------------------ CASO 3 - LISTAS COM CONDICIONAIS')
insert_animal: str = input('Busque na lista um animal pelo seu nome: ')
print('')

if insert_animal in lista_animais:
    print('Existe gato na lista!')
else:
    print('Não existe ',insert_animal,' na lista!\n')
    lista_animais.append(insert_animal)
    print('Lista atualizada:\n',
          lista_animais)
print('')

# ------------------------ CASO 4 - REMOVENDO ITENS DA LISTAS
print('# ------------------------ CASO 4 - REMOVENDO ITENS DA LISTAS')

lista_animais.pop()
print('Removendo última posição da lista!')
print(lista_animais)
print('')

lista_animais.pop(1)
print('Removendo posição específica da lista por índice')
print(lista_animais)
print('')

lista_animais.remove('cachorro')
print('Removendo posição específica da lista por elemento conhecido')
print(lista_animais)
print('')

# ------------------------ CASO 5 - ORDENANDO LISTAS
print('# ------------------------ CASO 5 - ORDENANDO LISTAS')
lista_carros = ['Mitsubshi', 'Subaru', 'Nissan', 'GM', 'Tesla']
lista_idades = [10, 30, 86, 29, 45, 90, 117]

lista_idades.sort()
print(lista_idades)
lista_idades.reverse()
print(lista_idades)
print('')

# ------------------------ CASO 6 - TUPLAS
print('# ------------------------ CASO 6 - TUPLAS')
tupla = (1, 10, 2, 4, 64, 89)

print('1° - Elementos da tupla', tupla)
print('2° - Qtd. elementos da tupla: ', len(tupla))
print('')

