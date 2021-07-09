from datetime import date, time, datetime, timedelta

# ------------------------ TRABALHANDO COM DATE E TIME
def Date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y')
    print('Forma 1 - Data atual:',data_atual,'|',type(data_atual_str))
    print('Forma 2 - Data atual:',data_atual_str,'|',type(data_atual_str))

def Time():
    horario = time(hour=15, minute=18, second=40)
    horario_str = horario.strftime('%H:%M:%S')
    print('Forma 1 - Agora é:',horario,'|',type(horario))
    print('Forma 2 - Agora é:',horario_str,'|',type(horario_str))

def DateTime():
    data_atual = datetime.now()
    print('Forma 01 - Hora do sistema:',data_atual)
    print('Forma 02 - Data do sistema:',data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print('Forma 03 - Hora do sistema:',data_atual.strftime('%c'))
    print('Forma 04 - Hora do sistema:',data_atual.year)
    print('Forma 05 - Hora do sistema:',data_atual.date())

    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print('Forma 06 - Tupla dia da semana Pt_Br:',tupla[data_atual.weekday()])

    tupla = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro',
             'Dezembro')
    print('Forma 07 - Tuple mês Pt_Br:',tupla[data_atual.month])

    data_criada = datetime(2021, 6, 20, 15, 40, 20)
    print('Forma 08 - DateTime manual:', data_criada)
    print('Forma 09 - DateTime manual:',data_criada.strftime('%c'))

    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print('Forma 10 - DateTime string manual convertido:',data_criada.strptime(data_string, '%d/%m/%Y'))

def TimeDelta():
    nova_data = datetime.now()
    nova_data_delta = nova_data - timedelta(days=730, hours=3, minutes=20)
    nova_data_delta_1 = nova_data + timedelta(days=730, hours=3, minutes=20)

    print('Forma 11 - TimeDelta   :',nova_data,'\n'
          'Forma 11 - TimeDelta - :',nova_data_delta,'\n'
          'Forma 11 - TimeDelta + :',nova_data_delta_1,'\n')



if __name__ == '__main__':
    print('# ------------------------ CASO 1 - DATE')
    Date()
    print('')

    print('# ------------------------ CASO 2 - TIME')
    Time()
    print('')

    print('# ------------------------ CASO 3 - DATETIME')
    DateTime()
    print('')

    print('# ------------------------ CASO 4 - TIMEDELTA')
    TimeDelta()
    print('')