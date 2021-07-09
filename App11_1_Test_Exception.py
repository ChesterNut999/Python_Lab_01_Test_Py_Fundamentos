# ------------------------ TRABALHANDO COM EXCESSÕES
lista = [1, 10]
arquivo = open('/home/Maurilio/PycharmProjects/Python_Lab_01_Test/resources/files/exceptions.txt', 'w')

try:
    print('Abrindo arquivo!')
    arquivo.write('#### EXCEPTIONS | ERROS | FALHAS ####\n\n')

    divisao = 10 / 1
    numero = lista[1]
    x = 1

except ZeroDivisionError:
    print('Não é possivel realizar divisão por 0!')
except ArithmeticError:
    print('Falha ao realizar a operação aritmética!')
except IndexError:
    print('Erro ao acessar um índice inexistente!')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Código executado com sucesso!')
finally:
    print('Fechando arquivo!')
    arquivo.close()
