preço = float(input('Preço de um produto: R$'))
desc = preço - (preço * 5 / 100)
print(f'Esse produto de R${preço:.2f} agora está com 5% de desconto, sendo assim ele agora vale R${desc:.2f}.')
