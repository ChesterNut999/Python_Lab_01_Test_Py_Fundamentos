import shutil

dir_arq = '/home/Maurilio/PycharmProjects/Python_Lab_01_Test/resources/files/teste.txt'

# ------------------------ CASO 1 - GERAR, MOVER E TRATAR ARQUIVO
print('# ------------------------ CASO 1 - GERAR, MOVER E TRATAR ARQUIVO')

def escrever_Arquivo(texto):
    arquivo = open(dir_arq, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_Arquivo(texto):
    arquivo = open(dir_arq, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_Arquivo(nome_arquivo):
    arquivo = open(dir_arq, 'r')
    texto = arquivo.read()
    print(texto)

def copiar_Arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '/home/Maurilio/PycharmProjects/Python_Lab_01_Test/resources/files/teste_copy.txt')

def mover_Arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '')

def calcular_MediaNotas(dir_arq):
    arquivo = open(dir_arq, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print (aluno_nota)
    lista_media = []

    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        #print(aluno)
        #print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas])/4
        #print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media
        #print(sum(lista_notas))


if __name__ == '__main__':
    lista_media = calcular_MediaNotas(dir_arq)
    print(lista_media)
    #escrever_Arquivo('NOTAS TRIMESTRAIS!\n\n')

    atualizar_Arquivo('MAURILIO, 10, 10, 10 \n'
                      'MAURICIO, 5, 6, 6, \n'
                      'MAURO, 2, 1, 5 \n')

    calcular_MediaNotas(dir_arq)

    ler_Arquivo(dir_arq)

