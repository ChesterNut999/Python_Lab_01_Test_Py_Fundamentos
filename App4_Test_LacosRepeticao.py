# ------------------------ CASO 1 - LAÇOS DE REPETIÇÃO FOR | WHILE
print('#-------- CASO 1 - LAÇOS DE REPETIÇÃO FOR')
NUM: float = int(input('Digite um número: '))
DIV: float = 0

for x in range(1, NUM + 1):
    resto = NUM % x
    print('Dividindo ', NUM, ' por ', x, ' | Resto = ', resto)

    if resto == 0:
        DIV += 1

print('')
if DIV == 2:
    print('NÚMERO {} É PRIMO!'.format(NUM))
else:
    print('NÚMERO {} NÃO É PRIMO!'.format(NUM))
print('')

# ------------------------ CASO 2 - LAÇOS DE REPETIÇÃO FOR | WHILE
print('#-------- CASO 2 - LAÇOS DE REPETIÇÃO FOR')
primo = 10

print('Até ', primo, ' existem os números primos: ')
for num in range(primo):

    DIV = 0
    for x in range(1, num + 1):
        resto = num % x

        if resto == 0:
            DIV += 1

    if DIV == 2:
        print(num, '|', end="")
print('\n')

# ------------------------ CASO 3 - LAÇOS DE REPETIÇÃO FOR | WHILE
print('#-------- CASO 3 - LAÇOS DE REPETIÇÃO WHILE')
a = 0

while a <= 10:
    print(a, '|', end="")
    a += 1
print('\n')

# ------------------------ CASO 4 - LAÇOS DE REPETIÇÃO FOR | WHILE
print('#-------- CASO 4 - LAÇOS DE REPETIÇÃO WHILE')
a = float(input('Digite a nota do 1° bimestre: '))
while 10 < a > 0:
    a = float(input('Você digitou uma nota inválida (1° bimestre). Digite novamente: '))

b = float(input('Digite a nota do 2° bimestre: '))
while 10 < b > 0:
    b = float(input('Você digitou uma nota inválida (2° bimestre). Digite novamente: '))

c = float(input('Digite a nota do 3° bimestre: '))
while 10 < c > 0:
    c = float(input('Você digitou uma nota inválida (3° bimestre). Digite novamente: '))

d = float(input('Digite a nota do 4° bimestre: '))
while 10 < d > 0:
    d = float(input('Você digitou uma nota inválida (4° bimestre). Digite novamente: '))
print('')

media: float = ((a + b + c + d) / 4)
if media >= 5:
    print('APROVADO COM MÉDIA {}!'.format(media))
else:
    print('REPROVADO COM MÉDIA {}!'.format(media))
print('')
