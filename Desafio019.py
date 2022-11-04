from random import choice

a1 = str(input('Digite o nome de um aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome de um terceiro aluno: '))
a4 = str(input('Digite o nome de um quarto aluno: '))
alunos = [a1, a2, a3, a4]
r = choice(alunos)
print(f'O aluno escolhido foi o {r}')
