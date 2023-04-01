# Recebendo o salário do funcionário do usuário
salario = float(input('Qual é o salário do funcionário? R$'))

# Calculando o novo salário com aumento de 15% e imprimindo na tela
aumento = int(salario * 1.15)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${}'
    .format(salario, aumento))
