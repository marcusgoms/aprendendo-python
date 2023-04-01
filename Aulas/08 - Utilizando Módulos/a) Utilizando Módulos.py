# Importando o módulo math
import math

# Calculando a raiz quadrada
num = 25
raiz_quadrada = math.sqrt(num)
print("A raiz quadrada de", num, "é", raiz_quadrada)

# Calculando o seno e o cosseno
angulo = 30
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)
print("O seno de", angulo, "graus é", seno)
print("O cosseno de", angulo, "graus é", cosseno)

# Arredondando um número
num = 3.14159
arredondado = round(num, 2)
print("O número", num, "arredondado com 2 casas decimais é", arredondado)
