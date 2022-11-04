num = int(input('Digite um número entre 0 e 9999: '))
'''Ex com string, porém só funciona com 4 dígitos.
n = str(num)
print(f'A unidade de milhar é: {n[0]}')
print(f'A centena é: {n[1]}')
print(f'A dezena é: {n[2]}')
print(f'A unidade é: {n[3]}')'''

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'A unidade de milhar é: {m}')
print(f'A centena é: {c}')
print(f'A dezena é: {d}')
print(f'A unidade é: {u}')
