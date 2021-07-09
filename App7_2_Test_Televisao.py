# ------------------------ CASO 1 - DEFINIÇÕES/DEF (MÉTODO)
print('# ------------------------ CASO 1 - DEFINIÇÕES/DEF (MÉTODO)')
class televisao_1:
    def __init__(self):
        pass

    # ++++ LIGA OU DESLIGA A TELEVISÃO
    def power_on(self, param_1):
        if param_1 == 'L':
            print('A Televisão já está ligada!',True)
            print('Você está no canal: 0', '\n')
        else:
            param_1 = ('Sim!', False)
            print('A televisão continua desligada!')

    # ++++ TROCA DE CANAIS
    def sobe_canal(self):
        if self.ligada:
            self.ligada += 1

    def desce_canal(self):
        if self.ligada:
            self.ligada -= 1

if __name__ == '__main__':
    televisao = televisao_1()
    televisao.power_on(str.upper(input('A TELEVISÃO ESTÁ LIGADA OU DESLIGADA? L/D > ')))

