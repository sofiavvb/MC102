'''''#Faça um programa que peça 10 números inteiros, calcule e mostre
a quantidade de números pares e a quantidade de números
ímpares.

numeros = input('Digite 10 números inteiros: ').split()
numeros_int = list(map(int, numeros))
pares = 0
impares = 0

for i in numeros_int:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'A quantidade de números pares é {pares} e a de números ímpares é {impares}')
'''

#divisores entre 2 e n de um número inteiro positivo n 
'''
numero = int(input('Digite o número de sua escolha: '))
d = 3
divisores = []
    
while d < numero:
    if numero % d == 0: #se for divisivel
        divisores.append(d)
    d += 1
    
print(f'Os divisores de {numero} entre 2 e {numero} são {divisores}.')
'''


