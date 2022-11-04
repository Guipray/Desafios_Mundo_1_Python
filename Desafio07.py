n1 = float(input('\033[1;97mPrimeira nota do aluno: '))
n2 = float(input('\033[1;97mSegunda nota do aluno: \033[m'))
m = (n1 + n2) / 2
print(f'A média entre \033[1;32m{n1:.1f}\033[m e \033[1;32m{n2:.1f}\033[m é \033[1;31m{m:.1f}\033[m.')
