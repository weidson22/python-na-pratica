#reajuste de salários de acordo com o salário do colaborador 
salario = float(input('Salário do colaborador: '))
reajuste20 = salario + (salario * 0.20) #20%
reajuste15 = salario + (salario * 0.15) #15%
reajuste10 = salario + (salario * 0.10) #10%
reajuste5 = salario + (salario * 0.05) #5%
print(f'O colaborador que ganhava R${salario:.2f} .', end=' ')
if salario <= 280:
    print(f'Com um reajuste de 20% no seu salário que corresponde a R${salario * 0.20:.2f}. Ele passa a ganhar R${reajuste20:.2f}')
elif salario > 280 and salario <=700:
    print(f'Com um reajuste de 15% no seu salário que corresponde a R${salario * 0.15:.2f}. Ele passa a ganhar R${reajuste15:.2f}')
elif salario > 700 and salario <=1500:
    print(f'Com um reajuste de 10% no seu salário que corresponde a R${salario * 0.10:.2f}. Ele passa a ganhar R${reajuste10:.2f}')
else:
    print(f'Com um reajuste de 5% no seu salário que corresponde a R${salario * 0.05:.2f}. Ele passa a ganhar R${reajuste5:.2f}')
