# Recebendo a largura e altura da parede do usuário
largura = int(input('Largura da parede: '))
altura = int(input('Altura da parede: '))

# Calculando a área da parede
area = largura * altura

# Imprimindo a dimensão e área da parede na tela
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'
    .format(largura, altura, area))

# Calculando a quantidade de tinta necessária para pintar a parede e imprimindo na tela
tinta = int(area / 2)
print('Para pintar essa parede, você precisará de {}l de tinta.'
    .format(tinta))
