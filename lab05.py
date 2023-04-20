genoma = input()
x = int(input()) #por enquanto enquanto n faço as entradas: reverter
y = int(input()) #por enquanto enquanto n faço as entradas: reverter
a = int(input()) #por enquanto enquanto n faço as entradas: transpor
b = int(input()) #por enquanto enquanto n faço as entradas: transpor
c = int(input()) #por enquanto enquanto n faço as entradas: transpor
g = input()      #por enquanto enquanto n faço as entradas: combinar
d = int(input()) #por enquanto n faço as entradas: combinar
genoma_informado = input() #concatenar
w = int(input())
z = int(input())


def reverter(genoma, i,j):
    reversa = genoma[j:i-1:-1]
    genoma = genoma[:i] + reversa + genoma[j+1:]
    return genoma

def transpor(genoma, i, j, k):
    subsequencia1 = genoma[i:j+1]
    subsequencia2 = genoma[j+1:k+1]
    genoma = genoma[:i] + subsequencia2 + subsequencia1 + genoma[k+1:]
    return genoma

def combinar(genoma, g, i):
    genoma = genoma[:i] + g + genoma[i:]
    return genoma

def concatenar(genoma, g):
    genoma = genoma + g
    return genoma

def remover(genoma, i, j):
    genoma = genoma[:i] + genoma[j+1:]
    return genoma


reversao = reverter(genoma, x,y)
transposta = transpor(genoma, a, b, c)
combinacao = combinar(genoma, g, d)
concatenacao = concatenar(genoma, genoma_informado)
remocao = remover(genoma, w, z)
print(reversao)
print(transposta)
print(combinacao)
print(concatenacao)
print(remocao)
 