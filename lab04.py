dias = int(input())
pares = []
lista_procedimentos = []

#for d in range(dias):

numero_pares_brigas = int(input())   #M pares

for i in range(numero_pares_brigas):
        par = input().split()
        pares.extend(par) # se for append. ele fica varias listas de 2 em uma lista só

procedimentos_disponíveis = input()
animais_presentes = int(input())

for i in range(animais_presentes):
        animais_procedimentos = input().split()
        lista_procedimentos.extend(animais_procedimentos)

        
        
print(pares)
print(lista_procedimentos)



''''
checa se cachorro [0] tá na lista
checa se cachorro [1] ta na lista
se 0 e 1 estão: brigas += 1












'''












#for i in range(0, len(A), 2)
    #for j in range(0, len(B), 2)

    #if (A[i] == B [j] and A[i+1] == B[j+2]) or (A[i+1] == B [j] and A[i] == B[j+2])
        #brigas += 1
