num1 = int(input('Digite um primeiro número: '))
num2 = int(input('Digite um segundo número: '))
num3 = int(input('Digite um terceiro número: '))

# Verificando quem é menor

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

# Verificando quem é o maior

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'Dentre os números que você digitou, o número {menor} é o menor, e o {maior} é o maior deles.')
