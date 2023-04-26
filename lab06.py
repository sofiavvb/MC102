def main():
    lista_vetor = input().split(',')
    vetor = []
    for i in lista_vetor:
        vetor.append(int(i))

    while True:
        operacao = input()

        if operacao == "soma_vetores":
            lista_vetor2 = input().split(',')
            vetor2 = []
            for i in lista_vetor2:
                vetor2.append(int(i))
            vetor = soma_vetores(vetor, vetor2)
            print(vetor)

        elif operacao == "fim":
            break

def adiciona_zero(vetor1: list[int], vetor2: list[int]) -> int:
    if len(vetor1) < len(vetor2):
        for k in range(len(vetor2) - len(vetor1)):
            vetor1.append(0)
        return vetor1
    elif len(vetor1) > len(vetor2):
        for k in range(len(vetor1) - len(vetor2)):
            vetor2.append(0)
        return vetor2


def adiciona_um(vetor1: list[int], vetor2: list[int]) -> int:
    if len(vetor1) < len(vetor2):
        for k in range(len(vetor2) - len(vetor1)):
            vetor1.append(1)
        return vetor1
    elif len(vetor1) > len(vetor2):
        for k in range(len(vetor1) - len(vetor2)):
            vetor2.append(1)
        return vetor2


def soma_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    resultado = []
    if len(vetor1) > len(vetor2):
        vetor2 = adiciona_zero(vetor1, vetor2)
    elif len(vetor1) < len(vetor2):
        vetor1 = adiciona_zero(vetor1, vetor2)

    for i in range(len(vetor1)):
        resultado.append(vetor1[i] + vetor2[i])
    
    return resultado


def subtrai_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    resultado = []
    if len(vetor1) > len(vetor2):
        vetor2 = adiciona_zero(vetor1, vetor2)
    elif len(vetor1) < len(vetor2):
        vetor1 = adiciona_zero(vetor1, vetor2)

    for i in range(len(vetor1)):
        resultado.append(vetor1[i] - vetor2[i])

    return resultado


def multiplica_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    resultado = []
    if len(vetor1) > len(vetor2):
        vetor2 = adiciona_um(vetor1, vetor2)
    elif len(vetor1) < len(vetor2):
        vetor1 = adiciona_um(vetor1, vetor2)

    for i in range(len(vetor1)):
        multiplica = vetor1[i] * vetor2[i]
        resultado.append(multiplica)

    return resultado


def divide_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    resultado = []
    if len(vetor1) > len(vetor2): #segundo vetor é menor adiciona 1
        vetor2 = adiciona_um(vetor1, vetor2)
    elif len(vetor1) < len(vetor2): #primeiro vetor é menor adiciona 0
        vetor1 = adiciona_zero(vetor1, vetor2)

    for i in range(len(vetor1)):
        resultado.append(vetor1[i] // vetor2[i])

    return resultado


def multiplica_escalar(vetor:list[int], escalar: int) -> list[int]:
    resultado = []
    for i in range(len(vetor)):
        resultado.append(vetor[i] * escalar)
    
    return resultado


if __name__ == "__main__":
    main()