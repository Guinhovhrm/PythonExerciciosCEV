#Python 07: Desafio 005

valor = int(input('Digite um valor: '))
antecessor = valor - 1
sucessor = valor + 1

print(f'O antecessor do numero {valor} é: {antecessor} e o sucessor é: {sucessor}')

#Python 07: Desafio 006

valor = int(input('Digite um valor: '))
dobro = valor * 2
triplo = valor * 3
square = valor ** 0.5

print(f'O dobro de {valor} é: {dobro}, o triplo é: {triplo} e a raiz quadrada é: {square}')

#Python 07: Desafio 007

n1 = float(input('Digite a nota do primeiro semestre: '))
n2 = float(input('Digite a nota do segundo semestre: '))
media = (n1 + n2)/2

print(f'A media do ano é: {media}')

#Python 07: Desafio 008

metro = float(input('Digite o valor em metros: '))
cm = metro * 100
mm = metro * 1000

print(f'{metro} metros convertido para centímetros são: {cm} e em milímetros são: {mm}')

#Python 07: Desafio 009

valor = int(input('Digite um valor: '))
v2 = valor * 2
v3 = valor * 3
v4 = valor * 4
v5 = valor * 5
v6 = valor * 6
v7 = valor * 7
v8 = valor * 8
v9 = valor * 9
v10 = valor * 10

print(f'A tabuada do numero {valor} é: \n{valor}\n{v2}\n{v3}\n{v4}\n{v5}\n{v6}\n{v7}\n{v8}\n{v9}\n{v10}')

#Python 07: Desafio 010

real = float(input('Digite quantos reais você tem: '))
dolar = real * 3.27
print(f'Você tem {dolar} dólares')

#Python 07: Desafio 011

h = float(input('Digite a altura: '))
base = float(input('Digite a largura: '))
area = base * h
LtTinta = area / 2

print(f'Você precisará de {LtTinta} litros de tinta para pintar a parede')

#Python 07: Desafio 012

preco = float(input('Digite o valor do produto: '))
desc = int(input('Digite o valor do desconto: '))
valordesc = preco * (desc/100)
valorfinal = preco - valordesc

print(f'O produto de {preco} reais com {desc}% de desconto ficará: {valorfinal} reais')

#Python 07: Desafio 013

salario = float(input('Digite seu salario: '))
aumento = int(input('Digite a porcentagem do seu aumento: '))
salarioamtd = salario * (aumento/100)
salariofinal = salario + salarioamtd

print(f'O seu salário aumentará {aumento}%, irá de {salario} reais para {salariofinal} reais')