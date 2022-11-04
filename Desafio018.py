from math import radians, tan, sin, cos

ang = int(input('Digite um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))
print(f'O seno de {ang} é {sen:.2f}.\nO cosseno de {ang} é {cos:.2f}.\nA tangente de {ang} é {tg:.2f}.')
