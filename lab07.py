def main():
    operacao = input()
    operando1 = input()
    operando2 = input()
    numero_linhas = int(input())
    lista_mensagem = []
    

    for i in range(numero_linhas): #mudar para while?
        mensagem = list(input())
        lista_mensagem.extend(mensagem)

    chave = acha_chave(operando1, operando2, operacao, lista_mensagem)
    print(chave)
    print(descriptografa(lista_mensagem, chave))

def acha_operando(operando, lista_mensagem):
    vogais = "AaEeIiOoUu"
    numeros ="0123456789"
    consoantes = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"
    if operando == "vogal":
        for i in lista_mensagem:
            if i in vogais:
                return i
    elif operando == "numero":
        for i in lista_mensagem:
            if i in numeros:
                return i
    elif operando == "consoante":
        for i in lista_mensagem:
            if i in consoantes:
                return i
    else:
        return operando

def acha_chave(operando1, operando2, operacao, lista):
    if operacao == "+":
        return lista.index(acha_operando(operando1, lista)) + lista.index(acha_operando(operando2, lista))
    elif operacao == "-":
        return lista.index(acha_operando(operando1, lista)) - lista.index(acha_operando(operando2, lista))
    else:
        return lista.index(acha_operando(operando1, lista)) * lista.index(acha_operando(operando2, lista))

def descriptografa(lista: list[str], chave: int):
    mensagem = []
    for i in lista:
        decodifica = ord(i) + chave
        if decodifica > 127:
            decodifica 
        revela = chr(decodifica) 
        mensagem.append(revela)
    return "".join(mensagem)
        

if __name__ == "__main__":
    main()