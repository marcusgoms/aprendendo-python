# Importando a biblioteca math
import math

# Recebendo o valor do ângulo em graus do usuário
angulo = float(input('Digite o angulo que você deseja: '))

# Calculando o valor do seno, cosseno e tangente e imprimindo na tela
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
