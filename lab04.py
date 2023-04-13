dias = int(input()) #vou precisar de um for grandão para rodar os dias
pares = []
lista_procedimentos = []
presente = -1
brigas = 0
#for d in range(dias):

numero_pares_brigas = int(input())   #M pares

for i in range(numero_pares_brigas):
        par = input().split()
        pares.append(par)#lista dos cachorros que brigam
                         # se for append. ele fica varias listas de 2 em uma lista só

procedimentos_disponíveis = input()
animais_presentes = int(input())

for n in range(animais_presentes):
        animais_procedimentos = input().split()
        lista_procedimentos.extend(animais_procedimentos) #animal e o procedimento que ele quer

#algoritmo que calcula o número de brigas:
for lista in range(len(pares)):
    presente = -1
    for k in range(2):
        for j in range(0, len(lista_procedimentos), 2):
        
            if pares[lista][k] == lista_procedimentos[j]:
                presente = presente + 1
                break 
            
    if presente == -1:    #primeiro cachorro nao ta, nem adianta ver se o segundo ta
        break
    elif presente == 1:
        brigas += 1

print(brigas)       
print(pares)
print(lista_procedimentos)



''''
checa se cachorro [0] tá na lista
checa se cachorro [1] ta na lista
se 0 e 1 estão: brigas += 1
presente = =1
brigas = 0

for lista in range(len(pares)):
    presente == -1
    for i in range(2):
        for j in range(0, len(lista_procedimentos), 2):
        
            se pares[lista][i] == lista_procedimentos[j]
                presente == presente + 1
                break 
            
    se presente == -1    #primeiro cachorro nao ta, nem adianta ver se o segundo ta
        break
    elif presente == 1
        brigas += 1
