m = float(input('diga um valor em metros: '))
km = m / 1000
hm = m / 100
cm = m * 100
mm = m * 1000
print(f'\033[1;97m{m}m\033[m em centímetros é \033[1;97m{cm:.0f}cm\033[m, e em milímetros é \033[1;97m{mm:.0f}mm\033[m.\nEm quilômetros é \033[1;97m{km:.3f}km\033[m, em hectômetros é \033[1;97m{hm:.2f}hm\033[m.')
