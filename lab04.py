dias = int(input()) #vou precisar de um for grandão para rodar os dias
pares = []
procedimentos_solicitados = []
procedimentos_disponiveis = []
quantidades_disponiveis = []
cachorros_atendidos = []
nao_disponiveis = []
nao_existe = 0
presente = -1
brigas = 0
#for d in range(dias):

numero_pares_brigas = int(input())   #M pares

for i in range(numero_pares_brigas):
    par = input().split()
    pares.append(par)#lista dos cachorros que brigam
                         # se for append. ele fica varias listas de 2 em uma lista só

procedimentos= input().split()
for n in range(len(procedimentos)//2):
	procedimentos_disponiveis.append(procedimentos[2*n])
	quantidades_disponiveis.append(procedimentos[2*n+1])

animais_presentes = int(input())

for n in range(animais_presentes):
    animais_procedimentos = input().split()
    procedimentos_solicitados.extend(animais_procedimentos) #animal e o procedimento que ele quer

#algoritmo que calcula o número de brigas:
for lista in range(len(pares)):
	presente = -1
	for k in range(2):
		for j in range(0, len(procedimentos_solicitados), 2):
			if pares[lista][k] == procedimentos_solicitados[j]:
				presente = presente + 1
				break
	if presente == -1:    #primeiro cachorro nao ta, nem adianta ver se o segundo ta
		break
	elif presente == 1:
		brigas += 1
#algoritmo para achar os atendimentos
for i in range(1, len(procedimentos_solicitados), 2):
	nao_existe = 0
	for j in range(len(procedimentos_disponiveis)):
		if (procedimentos_solicitados[i] == procedimentos_disponiveis[j]):
			cachorros_atendidos.append(procedimentos_solicitados[i-1])
			nao_existe += 1
			break
	if nao_existe == 0:
		nao_disponiveis.append(procedimentos_solicitados[i-1])

			

print(nao_disponiveis)
print(cachorros_atendidos)
print(brigas)       
print(pares)
print(procedimentos_solicitados)
