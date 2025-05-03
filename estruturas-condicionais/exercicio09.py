#verificando centena, dezena e unidade
número = int(input('Digite um número de 0 a 1000 para ver suas centenas, dezenas e unidade: '))
centena = número // 100
dezena = (número % 100) // 10
unidade = número % 10
if número > 0 and número < 1000:
    print(f'{centena} centenas, {dezena} dezenas e {unidade} unidades')
else:
   print('Número fora do intervalo proposto!')
