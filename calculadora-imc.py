peso = float(input('Informe seu peso:'))
altura = float(input('Informe sua altura:'))
imc = peso / (pow(altura, 2))

print(f'Seu IMC é { imc: .2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 24.9:
    print('Peso Normal')
elif 25 <= imc < 29.9:
    print('Sobrepeso')
elif 30 <= imc < 34.9:
    print('Obesidade grau I')
elif 35 <= imc < 39.9:
    print('Obesidade grau II')
else:
    print('Obesidade grau I')
