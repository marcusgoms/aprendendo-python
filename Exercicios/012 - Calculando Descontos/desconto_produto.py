# Recebendo o preço do produto do usuário
preco = float(input('Qual é o preço do produto? R$'))

# Calculando o novo preço com desconto de 5% e imprimindo na tela
desconto = int(preco * 0.95)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${}'
    .format(preco, desconto))
