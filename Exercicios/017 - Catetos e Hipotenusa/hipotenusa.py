# Importando a biblioteca math
import math

# Recebendo os valores dos catetos do usuário
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

# Calculando o valor da hipotenusa e imprimindo na tela
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
