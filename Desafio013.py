sa = float(input('Qual o salário de um funcionário? R$'))
aum = float(input('Qual o aumento em % desse salário? '))
novo = sa - (sa * aum / 100)
print(f'O novo salário deste funcionário que era de R${sa:.2f}, agora com {aum:.0f}% de aumento é R${novo:.2f}.')
