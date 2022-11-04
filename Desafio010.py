r = float(input('\033[1;97mQuantos reais você possuia em 2017? R$\033[m'))
d = r / 3.27
print(f'Com \033[1;32mR${r:.2f}\033[m você pode comprar \033[1;31mUS${d:.2f} dólares\033[m\n')

ra = float(input('\033[1;97mQuantos reais você tem atualmente? R$\033[m'))
da = ra / 4.91
print(f'Você atualmente pode comprar \033[1;31mUS${da:.2f}\033[m com \033[1;32mR${ra:.2f}\033[m. ')
