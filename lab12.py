ORDEM_FORCA = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                   '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'J': 11, 'Q': 12, 'K': 13}
    
ORDEM_NAIPE = {'O': 1, 'E': 2, 'C': 3, 'P': 4}


def main():
    jogadores = int(input())
    maos: dict[str, list] = {} #{jogador x:  cartas}
    pilha = []
    sem_mao_vazia = True

    for jogador in range(jogadores):
        mao = input().split(", ")
        maos[f"Jogador {jogador + 1}"] = mao
        
    jogada_ate_duvido = int(input())

    for jogador in maos:
        maos[jogador] = ordenar_cartas(maos[jogador])
    
    #Todo início de rodada deve-se imprimir as mãos dos jogadores em ordem decrescente
    #de força das cartas (ordenadas) e a pilha de descarte na ordem em que foi construída
    #(desordenada) ou vazia.
    jogador = 1
    # while grande para enquanto alguem n ganha
    while sem_mao_vazia:
        #sei q vou ter que mudar esse mao_vazia de pos
        mao_vazia = all(maos.values())
        
        for i in range(jogada_ate_duvido): 
            #inicio de rodada
            imprime_maos(maos)
            imprime_pilha(pilha)
            #para o caso da pilha vazia
            if i == 0:
                #posso colocar isso tudo em uma funcao dps
                descarte = []
                mao_crescente = list(reversed(maos[f"Jogador {jogador}"]))
                menor_carta = mao_crescente[0]
                #busca a menor carta, mas tem que ver se tem mais de uma, pq ai joga todas da mesma força
                for carta in mao_crescente:
                    if carta[0] == menor_carta[0]:
                        descarte.append(carta)
                    else:
                        break
                    
                pilha.extend(descarte)
                print(f"[Jogador {jogador}] {len(pilha)} carta(s) {menor_carta[0]}")
                imprime_pilha(pilha)
                jogador += 1
            else:
                topo = pilha[-1]
                menor_carta_idx = busca_binaria(maos[f"Jogador {jogador}"], topo)
                
                
                if menor_carta_idx == "nao achou":
                    pass
                
                
                #Pilha: AC
                #Jogador 1
                #Mão: QC QE 10P 7E 2P AC
                #Jogador 2
                #Mão: 8E 6P 6C 5C 3E 3O
                #Jogador 3
                #Mão: KP QP 10E 6E 4C 2C
                #Jogador 4
                #Mão: KE JO 9O 4O 3C AO
                #[Jogador 2] 2 carta(s) 3
                #Pilha: AC 3O 3E
            
        #o duvido eh fora do loop
def busca_binaria(cartas, alvo):
    inicio = 0
    fim = len(cartas) - 1
    
    while inicio <= fim:
        meio = (inicio + fim)//2
        
        if cartas[meio][0] == alvo[0]:
            return meio
        elif ORDEM_FORCA[alvo[0]] > ORDEM_FORCA[cartas[meio][0]]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return "nao achou"


def ordenar_cartas(cartas):
    '''Ordena as cartas em ordem decrescente.'''
    n = len(cartas)

    for i in range(n-1):
        for j in range(n-i-1):
            #se a carta atual for menor, muda ela de posicao com a maior
            if not comparar_cartas(cartas[j], cartas[j+1]):
                cartas[j], cartas[j+1] = cartas[j+1], cartas[j]
    
    return cartas


def comparar_cartas(carta1, carta2):
    '''Retorna True se a carta1 for maior do que carta2, False caso contrário e 
    0 caso sejam iguais.'''

    #primeiro olharemos a primeira posicao - QO e QE
    #se forem diferentes, ok nao precisamos olhar os naipe
    if carta1[0] != carta2[0]:
        return ORDEM_FORCA[carta1[0]] > ORDEM_FORCA[carta2[0]]
    else:
        if carta1[1] != carta2[1]:
            return ORDEM_NAIPE[carta1[1]] > ORDEM_NAIPE[carta2[1]]
        else:
            #quando as cartas são iguais
            return 0


def checa_intervalos(index_carta, mao_crescente, alvo):
    for i in range(index_carta + 1, len(mao_crescente)):
        if mao_crescente[i] == alvo[0]:
            maior_index = i
        else:
            break
    return maior_index

def imprime_maos(maos):
    
    for jogador in maos:
        print(jogador)
        print(f"Mão: {' '.join(maos[jogador])}")


def imprime_pilha(pilha):
    print(f"Pilha: {' '.join(pilha)}")


if __name__ == "__main__":
    main()