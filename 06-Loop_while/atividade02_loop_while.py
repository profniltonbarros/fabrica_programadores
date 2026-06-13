# Autor: Nilton Barros
# Projeto: Loop while
numero = int(input('Digite a tabuada desejada: '))
i = int(input('Digite o início da tabuada: '))
f = int(input('Digite o fim da tabuada: '))

while i <= f:
    print(f'{numero} x {i} = {numero * i}')
    i = i + 1