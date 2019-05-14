def main():
    parseExpression = {"posicao": 5,
                       "expressao": "",
                       "simboloAtual": "",
                       "resultado": 0}
    parseExpression["expressao"] = "-5E+2/-///////3"
    simbolo = ""
    sinal1: tuple = ('+', '-')
    sinal2: tuple = ('*', '/','//','%')

    simbolo = parseExpression["expressao"][parseExpression['posicao']]
    parseExpression["posicao"] = parseExpression["posicao"] + 1
    if(simbolo in sinal1):
        while True:
            if(parseExpression["expressao"][parseExpression['posicao']] in sinal1):
                parseExpression['posicao'] = parseExpression['posicao'] + 1
            else:
                break
            
    elif(simbolo in sinal2):
        while True:
            if simbolo == "/":
                if parseExpression["expressao"][parseExpression['posicao']] == "/":
                    simbolo = simbolo + parseExpression["expressao"][parseExpression['posicao']]
            if(parseExpression["expressao"][parseExpression['posicao']] in sinal2):
                parseExpression['posicao'] = parseExpression['posicao'] + 1
            else:
                break

    print(simbolo)
    return 0


if __name__ == '__main__':
    main()
