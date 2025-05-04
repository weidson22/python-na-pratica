#caixa eletrônico
saque = int(input("Digite o valor do saque (entre R$10 e R$600): "))

if saque < 10 or saque > 600:
    print("Valor inválido! O saque deve ser entre R$10 e R$600.")
else:
notas100 = saque // 100
restante = saque % 100

notas50 = restante // 50
restante = restante % 50

notas10 = restante // 10
restante = restante % 10

notas5 = restante // 5
restante = restante % 5

notas1 = restante 

# Impressão com condições para mostrar só as notas usadas
if notas100 > 0:
  print(f'{notas100} nota(s) de R$100,00.')
if notas50 > 0:
  print(f'{notas50} nota(s) de R$50,00.')
if notas10 > 0:
  print(f'{notas10} nota(s) de R$10,00.')
if notas5 > 0:
  print(f'{notas5} nota(s) de R$5,00.')
if notas1 > 0:
  print(f'{notas1} nota(s) de R$1,00.')
