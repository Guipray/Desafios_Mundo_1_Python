import math
salário = float(input('Qual o salário do funcionário? R$'))

if salário <= 1250:
    aumento = salário + (salário * 15/100)
else:
    aumento = salário + (salário * 10/100)
print(f'O salário que antes era de R${salário:.2f} ganhou um aumento, se tornando R${aumento:.2f}!')
