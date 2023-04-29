def main() -> None:
    lista_vetor = input().split(',')
    vetor = []
    for i in lista_vetor:
        vetor.append(int(i))

    while True:
        operacao = input()  # string

        if operacao == "soma_vetores":
            lista_vetor2 = input().split(',')
            vetor2 = []
            for i in lista_vetor2:
                vetor2.append(int(i))
            vetor = soma_vetores(vetor, vetor2)
            print(vetor)

        elif operacao == "subtrai_vetores":
            lista_vetor2 = input().split(',')
            vetor2 = []
            for i in lista_vetor2:
                vetor2.append(int(i))
            vetor = subtrai_vetores(vetor, vetor2)
            print(vetor)

        elif operacao == "multiplica_vetores":
            lista_vetor2 = input().split(',')
            vetor2 = []
            for i in lista_vetor2:
                vetor2.append(int(i))
            vetor = multiplica_vetores(vetor, vetor2)
            print(vetor)

        elif operacao == "divide_vetores":
            lista_vetor2 = input().split(',')
            vetor2 = []
            for i in lista_vetor2:
                vetor2.append(int(i))
            vetor = divide_vetores(vetor, vetor2)
            print(vetor)

        elif operacao == "multiplicacao_escalar":
            escalar = int(input())
            vetor = multiplicacao_escalar(vetor, escalar)
            print(vetor)

        elif operacao == "n_duplicacao":
            n = int(input())
            vetor = n_duplicacao(vetor, n)
            print(vetor)

        elif operacao == "soma_elementos":
            vetor = [soma_elementos(vetor)]
            print(vetor)

        elif operacao == "produto_interno":
            lista_vetor2 = input().split(',')
            vetor2 = []
            for i in lista_vetor2:
                vetor2.append(int(i))
            vetor = [produto_interno(vetor, vetor2)]
            print(vetor)

        elif operacao == "multiplica_todos":
            lista_vetor2 = input().split(',')
            vetor2 = []
            for i in lista_vetor2:
                vetor2.append(int(i))
            vetor = multiplica_todos(vetor, vetor2)
            print(vetor)

        elif operacao == "correlacao_cruzada":
            lista_mascara = input().split(',')
            mascara = []
            for i in lista_mascara:
                mascara.append(int(i))
            vetor = correlacao_cruzada(vetor, mascara)
            print(vetor)

        elif operacao == "fim":
            break


def adiciona_zero(vetor1: list[int], vetor2: list[int]) -> list[int]:
    if len(vetor1) < len(vetor2):
        for k in range(len(vetor2) - len(vetor1)):
            vetor1.append(0)
        return vetor1
    elif len(vetor1) > len(vetor2):
        for k in range(len(vetor1) - len(vetor2)):
            vetor2.append(0)
        return vetor2
    return vetor1


def adiciona_um(vetor1: list[int], vetor2: list[int]) -> list[int]:
    if len(vetor1) < len(vetor2):
        for k in range(len(vetor2) - len(vetor1)):
            vetor1.append(1)
        return vetor1
    elif len(vetor1) > len(vetor2):
        for k in range(len(vetor1) - len(vetor2)):
            vetor2.append(1)
        return vetor2
    return vetor1


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
    if len(vetor1) > len(vetor2):  # segundo vetor é menor adiciona 1
        vetor2 = adiciona_um(vetor1, vetor2)
    elif len(vetor1) < len(vetor2):  # primeiro vetor é menor adiciona 0
        vetor1 = adiciona_zero(vetor1, vetor2)

    for i in range(len(vetor1)):
        resultado.append(vetor1[i] // vetor2[i])
    return resultado


def multiplicacao_escalar(vetor: list[int], escalar: int) -> list[int]:
    resultado = []
    for i in range(len(vetor)):
        resultado.append(vetor[i] * escalar)

    return resultado


def n_duplicacao(vetor: list[int], n: int) -> list[int]:
    resultado: list[int] = []
    if n == 0:
        return resultado
    else:
        resultado.extend(vetor * n)
    return resultado


def soma_elementos(vetor: list[int]) -> int:
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    return soma


def produto_interno(vetor1: list[int], vetor2: list[int]) -> int:
    produto = 0
    resultado = 0
    if len(vetor1) > len(vetor2):
        vetor2 = adiciona_um(vetor1, vetor2)
    elif len(vetor1) < len(vetor2):
        vetor1 = adiciona_um(vetor1, vetor2)

    for i in range(len(vetor1)):
        produto = vetor1[i] * vetor2[i]
        resultado += produto
    return resultado


def multiplica_todos(vetor1: list[int], vetor2: list[int]) -> list[int]:
    resultado = []
    for i in range(len(vetor1)):
        produto, soma = 0, 0
        for j in range(len(vetor2)):
            produto = vetor1[i] * vetor2[j]
            soma += produto
        resultado.append(soma)
    return resultado


def correlacao_cruzada(vetor1: list[int], mascara: list[int]) -> list[int]:
    resultado = []
    for i in range(len(vetor1) - len(mascara) + 1):
        resultado.append(produto_interno(vetor1[i:len(mascara) + i], mascara))
    return resultado


if __name__ == "__main__":
    main()
