# ------------------------ CASO 1 - LISTAS
print('# ------------------------ CASO 1 - CONJUNTOS')
conjunto_1 = {1, 3, 4, 6, 10}

print(type(conjunto_1))
print(conjunto_1)
print('')

# ------------------------ CASO 2 - ADICIONANDO, REMOVENDO E UNINDO ELEMENTOS DO CONJUNTO
print('# ------------------------ CASO 2 - ADICIONANDO, REMOVENDO E UNINDO ELEMENTOS DO CONJUNTO')
conjunto_2 = {1, 3, 4, 6, 10}
conjunto_3 = {1, 3, 5, 7, 9}
conjunto_4 = {2, 4, 6, 8, 10}

#++++ Adicionando
conjunto_2.add(111)
print('Adicionando elemento conjunto 2:\n',
      conjunto_2)

#++++ Removendo
conjunto_2.discard(1)
print('Removendo elemento conjunto 2:\n',
      conjunto_2)

#++++ Unindo
print('Unindo conjuntos 3 e 4:\n',
      conjunto_3.union(conjunto_4))

#++++ Intersecção
print('Intersecção dos elementos dos conjutos 2, 3 e 4 (tudo que existe em comum):\n',
      conjunto_2.intersection(conjunto_3))

#++++ Diferença
print('Diferença dos elementos dos conjuntos 3 e 4 e vice-versa:\n',
      conjunto_3.difference(conjunto_4),'\n',
      conjunto_4.difference(conjunto_3))

#++++ Diferença simétrica
print('Diferença simétrica dos conjuntos 3 e 4 (tudo que não existe nos conjuntos):\n',
      conjunto_3.symmetric_difference(conjunto_4))
print('')

# ------------------------ CASO 3 - PERTINÊNCIA | SUBCONJUNTO
print('# ------------------------ CASO 3 - PERTINÊNCIA | SUBCONJUNTO')
conjunto_5: float = {1, 3, 5, 7, 9}
conjunto_6: float = {2, 4, 6, 8, 10}
conjunto_7: float = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto_8: float = {1, 1.5, 3, 2.5, 5, 3.5, 7, 4.5, 9}

#++++ Pertinência
print('Conjunto 5 é um subconjunto do conjunto 8?:\n',
      conjunto_5.issubset(conjunto_6))
print('')

print('Conjunto 6 é um subconjunto do conjunto 7?:\n',
      conjunto_6.issubset(conjunto_7))
print('')

print('Soma dos elementos do conjunto 8:\n',
      sum(conjunto_8))
print('')

print('Conjunto 8 é um superconjunto do conjunto 5?:\n',
      conjunto_8.issuperset(conjunto_5))
print('')

# ------------------------ CASO 4 - LISTA COM CONJUNTOS
print('# ------------------------ CASO 4 - LISTA COM CONJUNTOS')
lista_animais2 = ['lobo', 'vaca', 'sapo']
lista_animais3 = ['esquilo','papagaio','lobo']

print('Convertendo lista para conjunto com o comando set:\n',
      set(lista_animais2.__add__(lista_animais3)))




