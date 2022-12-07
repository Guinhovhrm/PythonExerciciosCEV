import math
import random

#Python 08: Desafio 016
num = float(input('Digite um valor: '))
print(f'A parte inteira de {num} é: {math.floor(num):.0f}')

#Desafio 017
catA = float(input('Digite o valor do Cateto Adjacente: '))
catO = float(input('Digite o valor do Cateto Oposto: '))
hip = math.hypot(catA, catO)
print(f'Cateto adjacente: {catA}; Cateto oposto {catO} formam a hipotenusa de {hip:.2f}')

#Desafio 018
graus = int(input('Digite o angulo: '))
radia = math.radians(graus)
# radia = graus * (math.pi/180)
seno = math.sin(radia)
cosseno = math.cos(radia)
tangente = math.tan(radia)

print(f'''Angulo: {graus}°; 
Seno: {seno:.2f};
Cosseno: {cosseno:.2f};
Tangente: {tangente:.2f}''')

#Desafio 019
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolh = random.choice(lista)
print(f'O aluno escolhido foi: {escolh}')

#Desafio 020
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem da apresentação será: {lista}')

