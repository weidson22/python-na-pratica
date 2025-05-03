#mostrando se é número par ou ímpar, negativo ou positivo, decimal ou inteiro
import math
num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
print("""[ 1 ] Adição
[ 2 ] subtração
[ 3 ] multiplicação
[ 4 ] divisão """)
adição = num1 + num2
subtração = num1 + num2
multiplicação = num1 * num2
divisão = num1 / num2
resposta = int(input('Opção: '))
if resposta == 1:
    if adição % 2 == 0:
        print(f'A adição desses números resulta {adição}. Portanto é um número par')
    elif adição % 2 != 0:
        print(f'A adição desses números resulta {adição}. Portanto é um número ímpar')
    if adição > 0:
        print(f'A adição desses números resulta {adição}. Portanto é um número positivo')
    elif adição < 0:
        print(f'A adição desses números resulta {adição}. Portanto é um número negativo')
    if math.ceil(adição) > adição:
        print(f'A adição desses números resulta {adição}. Portanto é um número decimal')
    elif math.ceil(adição) == adição:
        print(f'A adição desses números resulta {adição}. Portanto é um número inteiro')
elif resposta == 2:
    if subtração % 2 == 0:
        print(f'A subtração desses números resulta {subtração}. Portanto é um número par')
    elif subtração % 2 != 0:
        print(f'A subtração desses números resulta {subtração}. Portanto é um número ímpar')
    if subtração > 0:
        print(f'A subtração desses números resulta {subtração}. Portanto é um número positivo')
    elif subtração < 0:
        print(f'A subtração desses números resulta {subtração}. Portanto é um número negativo')
    if math.ceil(subtração) > subtração:
        print(f'A subtração desses números resulta {subtração}. Portanto é um número decimal')
    elif math.ceil(subtração) == subtração:
        print(f'A subtração desses números resulta {subtração}. Portanto é um número inteiro')
elif resposta == 3:
    if multiplicação % 2 == 0:
        print(f'A multiplicação desses números resulta {multiplicação}. Portanto é um número par')
    elif multiplicação % 2 != 0:
        print(f'A multiplicação desses números resulta {multiplicação}. Portanto é um número ímpar')
    if multiplicação > 0:
        print(f'A multipicação desses números resulta {multiplicação}. Portanto é um número positivo')
    elif multiplicação < 0:
        print(f'A multiplicação desses números resulta {multiplicação}. Portanto é um número negativo')
    if math.ceil(multiplicação) > multiplicação:
        print(f'A multiplicação desses números resulta {multiplicação}. Portanto é um número decimal')
    elif math.ceil(multiplicação) == multiplicação:
        print(f'A multiplicação desses números resulta {multiplicação}. Portanto é um número inteiro')
elif resposta == 4:
    if divisão % 2 == 0:
        print(f'A divisão desses números resulta {divisão:.2f}. Portanto é um número par')
    elif divisão % 2 != 0:
        print(f'A divisão desses números resulta {divisão:.2f}. Portanto é um número ímpar')
    if divisão > 0:
        print(f'A divisão desses números resulta {divisão:.2f}. Portanto é um número positivo')
    elif divisão < 0:
        print(f'A divisão desses números resulta {divisão:.2f}. Portanto é um número negativo')
    if math.ceil(divisão) > divisão:
        print(f'A divisão desses números resulta {divisão:.2f}. Portanto é um número decimal')
    elif math.ceil(divisão) == divisão:
        print(f'A divisão desses números resulta {divisão:.2f}. Portanto é um número inteiro')
else:
    print('Opção inválida!')
