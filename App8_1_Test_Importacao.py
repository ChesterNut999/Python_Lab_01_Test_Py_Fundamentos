from App7_2_Test_Televisao import televisao_1
from App7_1_Test_Calculadora import operacoes_Matematicas_1
from App8_2_Test_ContadorLetras import contadorLetras

# ------------------------ CASO 1 - IMPORTANDO METODOS/ FUNÇOES DE OUTROS MODULOS
if __name__ == '__main__':
    televisao = televisao_1()
    televisao.power_on('D')

    calculadora = operacoes_Matematicas_1
    calculadora(1, 3)
    print('')

    lista = ['gato', 'pato', 'ganso']
    print('A palavra {}' .format(lista[0]),'possui {}' .format(len(contadorLetras(lista[0]))),'letras.\n'
          'A palavra {}' .format(lista[1]),'possui {}' .format(len(contadorLetras(lista[1]))),'letras.\n'
          'A palabra {}' .format(lista[2]),'possui {}' .format(len(contadorLetras(lista[2]))),'letras.')


