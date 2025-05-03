#verificaçã de sexo do usuário usando estruturas condicionais
sexo = str(input('Digite seu sexo [M/F]: ')).strip().title()
if sexo == 'M':
    print('Sexo masculino registrado com sucesso!')
elif sexo == 'F':
    print('Sexo feminino registrado com sucesso!')
else:
    print('Opção inválida!')
