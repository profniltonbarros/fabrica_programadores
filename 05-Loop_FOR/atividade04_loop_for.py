# Autor: Nilton Barros
# Projeto: Loop FOR - variáveis de início e fim

numero = int(input('Digite a tabuada desejada: '))
inicio = int(input('Digite o início da tabuada: '))
fim = int(input('Digite o fim da tabuada: '))

# loop FOR
for i in range (inicio, fim + 1):
    print(f'{numero} x {i} = {i * numero}')
