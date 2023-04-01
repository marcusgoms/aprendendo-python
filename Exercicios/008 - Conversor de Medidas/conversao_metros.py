# Recebendo um valor em metros do usuário
metros = int(input('Digite um valor em metros: '))

# Convertendo para centímetros e milímetros e imprimindo na tela
centimetros = metros * 100
milimetros = metros * 1000

print('O valor em centímetros é: {}cm'.format(centimetros))
print('O valor em milímetros é: {}mm'.format(milimetros))
