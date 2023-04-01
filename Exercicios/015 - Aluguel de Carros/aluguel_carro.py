# Recebendo a quantidade de km percorridos e a quantidade de dias alugados do usuário
km = float(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias o carro foi alugado? '))

# Calculando o preço total a pagar e imprimindo na tela
preco = (km * 0.15) + (dias * 60)
print('O total a pagar é de R${:.2f}'.format(preco))
