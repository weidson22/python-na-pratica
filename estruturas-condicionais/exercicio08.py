#folha de pagamento
valorhora = float(input('Valor da hora (R$/H): '))
horastrabalhadas = int(input('Horas trabalhadas (H): '))
salariobruto = valorhora * horastrabalhadas

#descontos de acordo com o salário bruto
descontoir5 = salariobruto * 0.05 #5%
descontoir10 = salariobruto * 0.10 #10%
descontoir20 = salariobruto * 0.20 #20%
inss = salariobruto * 0.10 #10%
fgts = salariobruto * 0.11 #11%

#desconto total aplicado
descontototal5 = descontoir5 + inss
descontototal10 = descontoir10 + inss
descontototal20 = descontoir20 + inss
salarioliquido0 = salariobruto - inss

#salario líquido
salarioliquido5 = salariobruto - descontototal5
salarioliquido10 = salariobruto - descontototal10
salarioliquido20 = salariobruto - descontototal20

#folha de pagamento
if salariobruto <= 900:
    print(f"""Salário Bruto: ({valorhora} * {horastrabalhadas})          : R${salariobruto:.2f}
    (-) IR (0%)                     : R$   0
    (-) INSS (10%)                  : R${inss:.2f}
    FGTS (11%)                      : R$ {fgts:.2f}
    Total de descontos              : R$ {inss}
    Salário Liquido                 : R$ {salarioliquido0:.2f}""")
elif salariobruto > 900 and salariobruto <= 1500:
    print(f"""Salário Bruto: ({valorhora} * {horastrabalhadas})          : R${salariobruto:.2f}
    (-) IR (5%)                     : R${descontoir5:.2f}
    (-) INSS (10%)                  : R${inss:.2f}
    FGTS (11%)                      : R${fgts:.2f}
    Total de descontos              : R${descontototal5:.2f}
    Salário Liquido                 : R${salarioliquido5:.2f}""")
elif salariobruto > 1500 and salariobruto <= 2500:
    print(f"""Salário Bruto: ({valorhora} * {horastrabalhadas})          : R${salariobruto:.2f}
    (-) IR (10%)                     : R${descontoir10:.2f}
    (-) INSS (10%)                  : R${inss:.2f}
    FGTS (11%)                      : R${fgts:.2f}
    Total de descontos              : R${descontototal10:.2f}
    Salário Liquido                 : R${salarioliquido10:.2f}""")
else: 
    print(f"""Salário Bruto: ({valorhora} * {horastrabalhadas})          : R${salariobruto:.2f}
    (-) IR (20%)                     : R${descontoir20:.2f}
    (-) INSS (10%)                  : R${inss:.2f}
    FGTS (11%)                      : R$ {fgts:.2f}
    Total de descontos              : R$ {descontototal20:.2f}
    Salário Liquido                 : R$ {salarioliquido20:.2f}""")
