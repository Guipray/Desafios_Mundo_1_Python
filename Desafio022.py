nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome é :', nome.upper())
print('Seu nome é:', nome.lower())
nomedividido = nome.split()
print(f'Seu nome tem', len(''.join(nomedividido)), 'letras ao todo.')
print(f'O seu primeiro nome é {nomedividido[0]} e ele tem {len(nomedividido[0])} letras.')

'''Outra forma de fazer:
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')'''