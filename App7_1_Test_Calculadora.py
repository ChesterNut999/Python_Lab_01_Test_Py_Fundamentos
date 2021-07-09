from _pytest.python import Class
print('ENTRADA DE VALORES:')
val_1 = int(input('Insira o primeiro valor: '))
val_2 = int(input('Insira o segundo valor: '))
print('')

# ------------------------ CASO 1 - DEFINIÇÕES/DEF (FUNÇÕES) E CLASSES
print('# ------------------------ CASO 1 - DEFINIÇÕES/DEF (FUNÇÕES) E CLASSES')
# ++++ Função soma valores
def soma(a, b):
    return a + b

#+++ Função subtrai valores
def subtracao(a, b):
    return a - b

print('Valor total da soma é: ', soma(val_1, val_2))
print('Valor total da subtração é: ', subtracao(val_1, val_2), '\n')

# ------------------------ CASO 2 - CLASSES/ CLASS
class operacoes_Matematicas_1:
    def __init__(self, param_1, param_2):
        self.value_1 = param_1
        self.value_2 = param_2

    def soma_1(self):
        return self.value_1 + self.value_2

    def subtracao_1(self):
        return self.value_1 - self.value_2

    def divisao_1(self):
        return self.value_1 / self.value_2

    def multiplicacao_1(self):
        return self.value_1 * self.value_2

class Operacoes_Matematicas_2:
    def __init__(self):
        pass

    def soma_2(self, param_1, param_2):
        return param_1 + param_2

    def subtracao_2(self, param_1, param_2):
        return param_1 - param_2

    def divisao_2(self, param_1, param_2):
        return param_1 / param_2

    def multiplicacao_2(self, param_1, param_2):
        return param_1 * param_2

if __name__ == '__main__':
    operacoes_matematicas_1  = operacoes_Matematicas_1(val_1, val_2)
    print('Total da soma é: ', operacoes_matematicas_1.soma_1())
    print('Total da subtração é: ', operacoes_matematicas_1.subtracao_1())
    print('Total da divisão é: ', operacoes_matematicas_1.divisao_1())
    print('Total da multiplicação é: ', operacoes_matematicas_1.multiplicacao_1())
    print('')

    print('# ------------------------ CASO 2 - CLASSES/ CLASS')
    operacoes_matematicas_2  = Operacoes_Matematicas_2()
    print('Valor 1 para soma: ', val_1)
    print('Valor 2 para soma: ', val_2)
    print('Total da soma é: ', operacoes_matematicas_2.soma_2(val_1, val_2), '\n')

    val_3 = int(input('Valor 1 para subtração: ', ))
    val_4 = int(input('Valor 2 para subtração: ', ))
    print('Total da subtração é: ', operacoes_matematicas_2.subtracao_2(val_3, val_4), '\n')

    val_5 = int(input('Valor 1 para divisão: ', ))
    val_6 = int(input('Valor 2 para divisão: ', ))
    print('Valor total da divisão é: ', operacoes_matematicas_2.divisao_2(val_5, val_6), '\n')

    val_7 = int(input('Valor 1 para multiplicação: ', ))
    val_8 = int(input('Valor 2 para multiplicação: ', ))
    print('Valor total da multiplicação é: ', operacoes_matematicas_2.multiplicacao_2(val_7, val_8), '\n')


