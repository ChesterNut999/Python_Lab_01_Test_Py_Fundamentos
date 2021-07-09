#------------------------ CASO 1 - CONDICIONAL IF | ELIF | ELSE
print('#-------- CASO 1 - CONDICIONAL IF | ELIF | ELSE')
a = int(input('Digite o 1° valor: '))
b = int(input('Digite o 2° valor: '))
c = int(input('Digite o 3° valor: '))

print('')
if a > b and a > c:
    print('O maior número é {}'.format(a))
elif b > a and b > c:
    print('O maior número é {}'.format(b))
else:
    print('O maior número é {}'.format(c))
print('')

#------------------------ CASO 2 - CONDICIONAL IF | ELIF | ELSE
print('#-------- CASO 2 - CONDICIONAL IF | ELIF | ELSE')
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
resto_a = a % 2
resto_b = b % 2

print('')
if resto_b == 0 or not resto_b > 0:
    print('Você digitou um número par!')
else:
    print('Nenhum número impar foi digitado!')
print('')

#------------------------ CASO 3 - CONDICIONAL IF | ELIF | ELSE
print('#-------- CASO 3 - CONDICIONAL IF | ELIF | ELSE')
a = float(input('Digite a primeira nota 1° bimestre: '))
b = float(input('Digite a primeira nota 2° bimestre: '))
c = float(input('Digite a primeira nota 3° bimestre: '))
d = float(input('Digite a primeira nota 4° bimestre: '))
media = (a + b + c + d) / 4

print('')
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('Sua nota média geral é: {}'.format(media))
else:
    print('Entre somente com valores de 0 a 10')
print('')

#------------------------ CASO 4 - CONDICIONAL IF | ELIF | ELSE
print('#-------- CASO 4 - CONDICIONAL IF | ELIF | ELSE')
a = float(input('Digite a primeira nota 1° bimestre: '))
if a > 10:
    a = float(input('Você digitou uma nota inválida (1° bimestre): '))

b = float(input('Digite a primeira nota 2° bimestre: '))
if b > 10:
    b = float(input('Você digitou uma nota inválida (2° bimestre): '))

c = float(input('Digite a primeira nota 3° bimestre: '))
if c > 10:
    c = float(input('Você digitou uma nota inválida (3° bimestre): '))

d = float(input('Digite a primeira nota 4° bimestre: '))
if d > 10:
    d = float(input('Você digitou uma nota inválida (4° bimestre): '))

media = (a + b + c + d) / 4

print('')
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('Sua nota média geral é: {}'.format(media))
else:
    print('Entre somente com valores de 0 a 10')
print('')











