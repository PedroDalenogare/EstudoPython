'''cid = input('Digite o nome da cidade: ').strip()
print('SANTO' in cid.upper()[:5])'''

'''nome = input('Digite seu nome completo: ')
print('SILVA' in nome.upper())'''

'''frase = input('Digite uma frase: ').strip()
quant = frase.upper().count('A')
prim = frase.upper().find('A'[0:])+1
ult = frase.upper().rfind('A')+1
print(f'A letra "A" aparece {quant} vezes.')
print(f'A primeira letra "A" aparece na posição {prim}.')
print(f'A ultima letra "A" aparece na posução {ult}')
print(f'A frase tem {len(frase)} letras no total.')'''

'''total = int(input())
hora = (total)//3600
minuto = (total%3600)//60
segundos = (total)%60
print(f'{hora}:{minuto}:{segundos}')'''

'''n = int(input())
print(n)
print(f'{(n)//100} nota(s) de R$ 100,00')
print(f'{(n%100)//50} nota(s) de R$ 50,00')
print(f'{(n%50)//20} nota(s) de R$ 20,00')
print(f'{(n%100%50%20//10)} nota(s) de R$ 10,00')
print(f'{(n%100%50%20%10)//5} nota(s) de R$ 5,00')
print(f'{(n%100%50%20%10%5)//2} nota(s) de R$ 2,00')
print(f'{(n%100%50%20%10%5%2)} nota(s) de R$ 1,00')'''

'''tempo = int(input())
print(f'{tempo//365} ano(s)')
print(f'{tempo%365//30} mes(es)')
print(f'{tempo%365%30} dia(s)')'''

'''n = float(input())
print('NOTAS:')
print(f'{(n)//100:.0f} nota(s) de R$ 100.00')
print(f'{(n%100)//50:.0f} nota(s) de R$ 50.00')
print(f'{(n%50)//20:.0f} nota(s) de R$ 20.00')
print(f'{(n%100%50%20//10):.0f} nota(s) de R$ 10.00')
print(f'{(n%100%50%20%10)//5:.0f} nota(s) de R$ 5.00')
print(f'{(n%100%50%20%10%5)//2:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
calculo = n%100%50%20%10%5%2
print(f'{(calculo//1):.0f} moeda(s) de R$ 1.00')
print(f'{(calculo%1//0.5):.0f} moeda(s) de R$ 0.50')
print(f'{(calculo%1%0.5//0.25):.0f} moeda(s) de R$ 0.25')
print(f'{(calculo%1%0.5%0.25//0.10):.0f} moeda(s) de R$ 0.10')
print(f'{(calculo%1%0.5%0.25%0.10//0.05):.0f} moeda(s) de R$ 0.05')
print(f'{(calculo%1%0.5%0.25%0.10%0.05/0.01):.0f} moeda(s) de R$ 0.01')'''

'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=6:
    print('Seu carro é novo!')
else:
    print('Seu carro é velho!')
# ou
print('Seu carro é novo!' if tempo<=6 else 'Seu carro é velho!')
print('FIM!!!!')'''

'''nome = input('Qual é o seu nome? ').upper()
if nome == 'MIRELLI,':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome.title()}')'''

'''import random
num = int(input('Estou pensando em um número entre 0 a 5, Advinhe qual é: '))
comp = random.randint(0, 5)
if num == comp:
    print ('Parabéns, você acertou o número!!')
else:
    print(f'Você errou eu pensei no número {comp} e não {num}')'''

'''velocidade = float(input('Qual é a velocidade do veiculo? '))
maximo = 80
if velocidade <=80:
    print('Está dentro do limite de velocidade.')
else:
    print('A Velocidade está acima do limite permitido de 80KM/h.')
    print(f'A multa gerada pela infração é de {(velocidade-maximo)*7}R$.')'''

'''distancia = int(input('Qual a distância da viagem? '))
if distancia <=200:
    print(f'O valor da passagem fica em {distancia*0.5}')
else:
    print(f'O valor da passagem fica em {distancia*0.45}')'''

'''ano = int(input('Qual ano você quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} não é BISSEXTO.')'''

'''lista = input().split(' ')
a, b, c = map(int, lista)
print(f"{max(a,b,c)} eh o maior")
print(f"{min(a,b,c)} eh o menor")'''

'''a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
lista = [a, b, c]
print(f'O maior valor digitado foi {max(lista)}')
print(f'O menor valor digitado foi {min(lista)}')'''

'''salario = float(input('Qual é o salário do funcionário? '))
aumento10 = salario/100*110
aumento15 = salario/100*115
if salario >= 1250.00:
    print(f'O novo salário será {aumento10:.2f}R$.')
else:
    print(f'O novo salário será {aumento15:.2f}R$.')'''

'''num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'O número {num} é PAR.')
else:
    print(f'O número {num} é IMPAR.')'''