#------------ INSERÇÃO DE VALORES
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
print("")

#------------------------------------------------------------------------------------

#------------ VARIÁVEIS E LÓGICAS
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

#------------------------------------------------------------------------------------

#------------ PRINTS
print("Soma de         |   ",a,"+",b,"    |   é igual a", soma)
print("Convertendo Int para String = "+str(soma))
print("")

print("Divisão de      |   ",a,"/",b,"    |   é igual a", divisao)
print("Convertendo Float para Int = ", int(divisao))
print("")

print("Subtração de    |   ",a,"-",b,"    |   é igual a", subtracao)
print("")

print("Multiplicação de|   ",a,"*",b,"    |   é igual a", multiplicacao)
print("")

print("Resto de        |   ",a,"%",b,"    |   é igual a", resto)
print("")

print(
    f'\nSoma:{soma}. '  
    f'\nSubtração:{subtracao}.'
    f'\nMultiplicação:{multiplicacao}. '    
    f'\nDivisão:{divisao}. '
    f'\nResto:{resto}. '
        .format(soma, subtracao, multiplicacao, divisao, resto))
print("")
