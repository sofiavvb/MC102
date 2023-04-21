def main():
    genoma = input()
    while True:
        operacao = input().split()

        if operacao[0] == "reverter":
                i = int(operacao[1])
                j = int(operacao[2])
                if j > len(genoma):
                    j = len(genoma)
                if i > len(genoma):
                    i = len(genoma)
                genoma = reverter(genoma, i, j)
                operacao = []

        elif operacao[0] == "transpor":
            i = int(operacao[1])
            j = int(operacao[2])
            k = int(operacao[3])
            if j > len(genoma):
                j = len(genoma)
            if k > len(genoma):
                k = len(genoma)
            if i > len(genoma):
                i = len(genoma)
            genoma = transpor(genoma, i, j, k)
            operacao = []
        
        elif operacao[0] == "combinar":
            g = operacao[1]
            i = int(operacao[2])
            if i > len(genoma):
                i = len(genoma)
            genoma = combinar(genoma, g, i)
            operacao = []
        
        elif operacao[0] == "concatenar":
            g = operacao[1]
            genoma = concatenar(genoma, g)
            operacao = []
        
        elif operacao[0] == "remover":
            i = int(operacao[1])
            j = int(operacao[2])
            if j > len(genoma):
                j = len(genoma)
            if i > len(genoma):
                i = len(genoma)
            genoma = remover(genoma, i, j)
            operacao = []

        elif operacao[0] == "transpor_e_reverter":
            i = int(operacao[1])
            j = int(operacao[2])
            k = int(operacao[3])
            if j > len(genoma):
                j = len(genoma)
            if k > len(genoma):
                k = len(genoma)
            if i > len(genoma):
                i = len(genoma)
            genoma = transpor_e_reverter(genoma, i, j, k)
            operacao = []

        elif operacao[0] == "buscar":
            g = operacao[1]
            print(buscar(genoma, g))
            operacao = []

        elif operacao[0] == "buscar_bidirecional":
            g = operacao[1]
            print(buscar_bidirecional(genoma, g))
            operacao = []

        elif operacao[0] == "mostrar":
            mostrar(genoma)

        elif operacao[0] == "sair":
            break


def reverter(genoma, i, j):
    reversa = genoma[i:j+1]
    revertida = reversa[::-1]
    genoma = genoma[:i] + revertida + genoma[j+1:]
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
    if (i<= len(genoma)):
        genoma = genoma[:i] + genoma[j+1:]
    return genoma

def transpor_e_reverter(genoma, i, j , k):
    genoma = transpor(genoma, i, j, k)
    genoma = reverter(genoma, i, k)
    return genoma

def buscar(genoma, g):
    achou = genoma.count(g)
    return achou

def buscar_bidirecional(genoma, g):
    achou = buscar(genoma, g) + buscar(genoma[::-1], g)
    return achou
    
def mostrar(genoma):
    print(genoma)

main()
