dis = float(input('Qual a distância da sua viagem? '))
# print(f'A sua passagem é para uma viagem de {dis}Km.')
if dis <= 200:
    # preço = dis * 0.50
    print(f'A sua passagem tem uma distância de {dis}Km.\nO preço dela será de R${dis*0.50:.2f}.')
else:
    # preço = dis * 0.45
    print(f'A sua passagem tem uma distãncia de {dis}Km.\nO preço dela será de R${dis*0.45:.2f}.')
print('Tenha uma boa viagem!')

# Forma Simplificada
"""dis = float(input('Qual a distância da sua viagem? '))
print(f'A sua passagem é para uma viagem de {dis}Km.')
preço = dis * 0.50 if dis <= 200 else dis * 0.45
print(f'O preço dela será de R${preço:.2f}')"""
