# Recebendo uma entrada do usuário
algo = input('Digite algo: ')

# Verificando o tipo primitivo da entrada
print('O tipo primitivo desse valor é', type(algo))

# Verificando se a entrada só contém espaços
print('Só tem espaços?', algo.isspace())

# Verificando se a entrada é um número
print('É um número?', algo.isnumeric())

# Verificando se a entrada é alfabética
print('É alfabético?', algo.isalpha())

# Verificando se a entrada é alfanumérica
print('É alfanumérico?', algo.isalnum())

# Verificando se a entrada está em maiúsculas
print('Está em maiúsculas?', algo.isupper())

# Verificando se a entrada está em minúsculas
print('Está em minúsculas?', algo.islower())

# Verificando se a entrada está capitalizada
print('Está capitalizada?', algo.istitle())
