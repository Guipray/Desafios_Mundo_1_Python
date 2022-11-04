nome = str(input('Qual o seu nome completo? ')).strip()
nomes = nome.split()
print(f'O seu primeiro nome é: {nomes[0]}')
print(f'O último nome é: {nomes[len(nomes)-1]}')
