# Exemplo de condição simples
velo = float(input('Qual a velocidade do carro: '))
if velo > 80:
    print(f'Você levou uma multa por passar dos 80Km/h!')
    multa = (velo-80) * 7
    print(f'A sua multa por estar a {velo}Km/h é de R${multa:.2f}.')
print('Sua velocidade é muito baixa!')
