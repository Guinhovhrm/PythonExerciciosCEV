import random

#Python 10: Desafio 28

numPc = random.randint(0, 5)
numUser = int(input('Qual o número sorteado pelo computador? '))

if numUser == numPc:
    print('Você acerto!! Parabéns!')
else:
    print('Você errou! :(')

print(f'O numero sorteado foi: {numPc}')

#Desafio 29

velCar = float(input('Qual a velocidade do carro? '))
if velCar > 80:
    multa = (velCar - 80) * 7
    print(f'Você foi multado! O valor da multa é: R${multa}')

#Desafio 30

num = int(input('Digite um valor: '))

if (num % 2) > 0:
    print('Impar')
else:
    print('Par')
    
#Desafio 31

dist = float(input('Qual a distancia da viagem? '))

if dist <= 200:
    dist = (dist * 0.50)
    print(f'O valor da viagem é: {dist}')
else:
    dist = (dist * 0.45)
    print(f'O valor da viagem é: {dist}')

#Desafio 32

from datetime import date
ano = int(input('Qual ano analisar? Digite 0 para analisar o atual do computador! '))
if ano == 0:
    ano = date.today().year

if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0: #peguei da resolução
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto')

#Desafio 33

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

if n1 > n2 and n1 > n3:
    print(f'O maior numero é: {n1}')
if n2 > n1 and n2 > n3:
    print(f'O maior numero é: {n2}')
if n3 > n1 and n3 > n2:
    print(f'O maior numero é: {n3}')

if n1 < n2 and n1 < n3:
    print(f'O menor numero é: {n1}')
if n2 < n1 and n2 < n3:
    print(f'O menor numero é: {n2}')
if n3 < n1 and n3 < n2:
    print(f'O menor numero é: {n3}')

#Desafio 34

salario = float(input('Digite seu salário atual:'))

if salario > 1250:
    reajuste = (salario * 0.10) + salario
    print(f'O seu novo salário é: {reajuste}')

else:
    reajuste = (salario * 0.15) + salario
    print(f'O seu novo salário é: {reajuste}')

#Desafio 35

r1 = float(input('Digite o primeiro comprimento: '))
r2 = float(input('Digite o segundo comprimento: '))
r3 = float(input('Digite o terceiro comprimento: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Podem formar um triangulo!')

else: 
    print('Não podem formar um triangulo!')