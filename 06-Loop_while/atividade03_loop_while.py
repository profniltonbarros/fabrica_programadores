# Autor: Nilton Barros
# Projeto: Loop while

numero = int(input('Digite a tabuada desejada: '))     
inicio = int(input('Digite o primeiro valor da tabuada')) 
fim = int(input('Digite o último valor da tabuada'))       

while inicio <= fim:
    print(f'{numero} x {inicio} = {numero * inicio}')
    inicio = inicio + 1
