r1 = float(input('Qual o comprimento da primeira reta: '))
r2 = float(input('Qual o comprimento da segunda reta: '))
r3 = float(input('Qual o comprimento da terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas formam um triângulo!')
else:
    print('Essas retas NÃO formam um triãngulo!')
