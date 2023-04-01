# Recebendo a temperatura em graus Celsius do usuário
tempC = float(input('Informe a temperatura em °C: '))

# Convertendo a temperatura para Fahrenheit e imprimindo na tela
tempF = (tempC * 9/5) + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(tempC, tempF))
