frase = str(input('Escreva uma frase qualquer: ')).strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes.')
print('A posição do primeiro A fica no número:', frase.find('A')+1)
print('A posição do último A fica no número:', frase.rfind('A')+1)
