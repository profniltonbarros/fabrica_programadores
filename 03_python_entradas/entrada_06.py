# Autor: Nilton Barros
# Projeto: IMC com input e f-string

# Declaração de variáveis
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

# exibindo os resultados
print(f'Seu IMC é: {imc:.2f}')