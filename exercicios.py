'''km = int(input(''))
tempo = (km*2)
print(f'{tempo} minutos')'''

'''lista = input().split(' ')
a, b, c = map(int, lista)
print(f"{max(a,b,c)} eh o maior")'''

# ou

'''lista = input().split(' ')
a, b, c = (lista)
print(f"{max(int(a), int(b), int(c))} eh o maior")'''

'''nome = input('Qual é o seu nome ? ')
print(f'MAISCULO : {nome.upper()}')
print(f'MINUSCULO : {nome.lower()}')
junto = (nome.split())
print(f'Seu nome ao todo tem {len(''.join(junto))} letras.')
print(f'O primeiro nome é {junto[0]} e tem {len(junto[0])} letras')'''

# ou

'''nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {nome.find(' ')} letras')'''

'''num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analizando o número: {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')'''
