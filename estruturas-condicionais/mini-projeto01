#calculo do imc de uma  pessoa
peso = float(input('Peso (Kg): '))
altura = float(input('Altura (m): '))
imc = peso/altura**2
print(f'O IMC está em {imc:.2f}')
if imc < 0:
    print('Impossível calcular IMC!')
elif imc <18.5 and imc > 0:
    print('Você está abaixo do peso. Cuidado, você deve alimentar-se melhor!')
elif imc >= 18.5 and imc < 25:
    print('Parabéns, você está no peso normal e saudável!')
elif imc >= 25 and imc < 30:
    print('Preste mais atenção, você já está sobrepeso. Controle sua alimentação e faça exercícios físicos')
elif imc >= 30 and imc < 35:
    print('Você já está na obesidade de grau I. Cuide-se já antes que evolua e procure um médico')
elif imc >=35 and imc < 40:
    print('Você já está na obesidade de grau II. Procure um médico imediatamente')
else:
    print('Você já está na obesidade de grau III. Vamos avaliar seu caso daqui mesmo e chamar especialistas')
