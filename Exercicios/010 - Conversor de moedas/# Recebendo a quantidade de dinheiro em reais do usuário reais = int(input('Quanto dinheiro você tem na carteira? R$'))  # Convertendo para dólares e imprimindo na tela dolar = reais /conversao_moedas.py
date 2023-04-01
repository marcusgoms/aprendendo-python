# Recebendo a quantidade de dinheiro em reais do usuário
reais = int(input('Quanto dinheiro você tem na carteira? R$'))

# Convertendo para dólares e imprimindo na tela
dolar = reais / 5
print('Com R${} você pode comprar US${}'.format(reais, dolar))
