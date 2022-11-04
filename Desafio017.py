import math
'''co = float(input('Qual o cateto oposto: '))
ca = float(input('Qual o cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print(f'A hipotenusa do triângulo retângulo tem {hi:.2f} de comprimento')'''

co = float(input('Qual o cateto oposto: '))
ca = float(input('Qual o cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa do triângulo retângulo tem {hi:.2f} de comprimento.')
