#verificando média de alunos 
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'A média foi de {media:.1f}')
if media >= 7 and media < 10:
    print('Aprovado!')
elif media < 7:
    print('Reprovado!')
elif media == 10:
    print('Aprovado com distinção!')
else:
    print('Média inválida. Reveja uma das notas dos bimestres!')
