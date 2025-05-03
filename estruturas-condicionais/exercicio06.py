#verificando quem é maior ou menor e se tem número iguais nos número digitados pelo usuário
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite mais outro número: '))
if n1 > n2 and n2 > n3:
    print(f'O maior número é o {n1}')
elif n1 > n3 and n3 > n2:
    print(f'O maior número é o {n1}')
elif n2 > n1 and n1 > n3:
    print(f'O maior número é o {n2}')
elif n2 > n3 and n3 > n1:
    print(f'O maior número é o {n2}')
elif n3 > n1 and n1 > n2:
    print(f'O maior número é o {n3}')
elif n3 > n2 and n2 > n1:
    print(f'O maior número é o {n3}')
elif n1 == n2 == n3:
    print('Todos os valores digitados têm o mesmo valor!')
elif n1 == n2 > n3:
    print(f'O maior número é {n1}')
elif n1 == n2 < n3:
    print(f'O maior número é {n3}')
elif n2 == n3 > n1:
    print(f'O maior número é o {n2}')
elif n2 == n3 < n1:
    print(f'O maior número é o {n1}')
elif n3 == n1 > n2:
    print(f'Omaior número é o {n3}')
elif n3 == n1 < n2:
    print(f'O maior número é o {n2}')
