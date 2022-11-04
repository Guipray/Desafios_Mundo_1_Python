cid = str(input('Qual o nome da sua cidade? ')).strip()
#print(cid[:5].upper() == 'SANTO')
cidm = cid.upper()
print(f'A cidade em que você mora possui o nome Santo?', 'SANTO' in cidm)
