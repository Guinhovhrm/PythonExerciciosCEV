#Python 09: Desafio 022

Nome = input('Digite seu nome: ').strip()
print(f'Seu nome é: {Nome}')
print(f'Maiúsculo: {Nome.upper()}')
print(f'Minúsculo: {Nome.lower()}')
print(f'Total de letras sem espaço: {len(Nome.replace(" ", ""))}')
Divid = Nome.split()
print(f'Letras no primeiro nome: {len(Divid[0])}')

#Desafio 023

Valor = int(input('Digite um valor: '))
Valor = str(Valor)
print(f'Milhar: {Valor[0]}')
print(f'Centena: {Valor[1]}')
print(f'Dezena: {Valor[2]}')
print(f'Unidade: {Valor[3]}')

#Desafio 024

Cidade = input('Digite o nome de uma cidade: ').strip()
CidDiv = Cidade.split()
Tem = 'Santo' in CidDiv[0].title()
print(f'{Cidade.title()} começa com "Santo"? {Tem}')

#Desafio 025

Nome = input('Digite seu nome: ').strip()
Tem = 'Silva' in Nome.title()
print(f'Tem "Silva" em {Nome.title()}? {Tem}')

#Desafio 026

Frase = input('Digite uma frase: ').strip()
Frase = Frase.lower()
print(f'Quantas vezes aparece a letra "A/a"? {Frase.count("a")}')
print(f'Qual posição ela aparece pela 1° vez? {Frase.find("a")}')
print(f'Qual posição ela aparece pela última vez? {Frase.rfind("a")}')

#Desafio 027

Nome = input("Digite seu nome completo: ").strip()
NomeDiv = Nome.split()
print(f'''O primeiro nome é: {NomeDiv[0]} 
O último nome é: {NomeDiv[-1]}''')