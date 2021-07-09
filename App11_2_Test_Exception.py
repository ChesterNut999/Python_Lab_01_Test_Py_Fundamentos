
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('De 0 a 10, digite a primera nota: '))
        print('A nota digitada é:',x)

        if x > 10:
            raise InputError('ERRO - Nota não pode ser maior que 10!\n')
        elif x < 0:
            raise InputError('ERRO - Nota não pode ser menos que 0!\n')

        break

    except ValueError:
        print('Valor inválido! Entre apenas com números de 0 a 10!')

    except InputError as ex:
        print(ex)