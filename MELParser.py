#(expr) ::= (term) ((‘+’ | ‘-’) (term))*
def expr(parseExpression):
    termo1 = term(parseExpression)
    simbolos: tuple("+","-")

    while True:
        if (parseExpression["expressao"]["posicao"] in simbolos):
            parseExpression["simboloAtual"] = verifSimbolo(parseExpression)
            termo2 = term(parseExpression)

            if (parseExpression["simboloAtual"] == "+"):
                termo1 += termo2
            elif (parseExpression["simboloAtual"] == "-"):
                termo1 -= termo2

#(term) ::= (factor) ((‘*’ | ‘/’ | ‘//’ | ‘%’) (factor))*
def term(parseExpression):
    termo1 = factor(parseExpression)
    simbolos: tuple("*","/","//","%")

    while True:
    
        if (parseExpression["expressao"]["posicao"] in simbolos):
            
            parseExpression["simboloAtual"] = verifSimbolo(parseExpression)
            termo2 = factor(parseExpression)

            if (parseExpression["simboloAtual"] == "*"):
                termo1 *= termo2
            elif (parseExpression["simboloAtual"] == "/"):
                termo1 /= termo2
            elif (parseExpression["simboloAtual"] == "//"):
                termo1 //= termo2
            elif (parseExpression["simboloAtual"] == "%"):
                termo1 %= termo2
        else:
            break

    return termo1


#(factor) ::= (base) (‘^’ (factor))?
def factor(parseExpression):
    
    valor = base(parseExpression)

    if(parseExpression["expressao"]["posicao"] == "^"):
        parseExpression["posicao"] = parseExpression["posicao"] + 1
        return valor ** factor(parseExpression)

    return valor


#(base) ::= (‘+’ | ‘-’) (base)
#| (number)
#| ‘(’ (expr) ‘)’
def base(parseExpression):
    
    if(parseExpression["expressao"]["posicao"] == '+'):
        parseExpression["posicao"] = parseExpression["posicao"] + 1
        return 1*base(parseExpression)

    elif(parseExpression["expressao"]["posicao"] == '-'):
        parseExpression["posicao"] = parseExpression["posicao"] + 1
        return  (-1)*base(parseExpression)

    if(parseExpression["expressao"]["posicao"] == "("):
        parseExpression["posicao"] = parseExpression["posicao"] + 1
        parseExpression = expr(expressao)
        if(parseExpression["expressao"]["posicao"] == ")"):
            parseExpression["posicao"] = parseExpression["posicao"] + 1
            return parseExpression
    
    return number(parseExpression)
    





# (number) ::= (digit)+ ‘.’? (digit)* ((‘E’ | ‘e’) (‘+’ | ‘-’)? (digit)+)?
def number(parseExpression):
    euler: tuple = ('e', 'E')
    sinal: tuple = ('+', '-')
    numero = ''
    ultimoAdd = ''
    breakReturn = False
    for i in range(len(parseExpression["expressao"])):
        k = parseExpression['posicao']
        if digit(parseExpression['expressao'][k]):
            numero = numero + parseExpression['expressao'][k]
            ultimoAdd = parseExpression['expressao'][k]
            parseExpression['posicao']+=1

        elif k == '.':
            if ultimoAdd != parseExpression['expressao'][k]:
                if '.' in numero:
                    breakReturn = True
                    break
                else:
                    numero = numero + parseExpression['expressao'][k]
                    ultimoAdd = parseExpression['expressao'][k]
                    parseExpression['posicao']+=1     

        elif parseExpression['expressao'][k] in euler:
            if ultimoAdd != parseExpression['expressao'][k]:
                if 'e' in numero or 'E' in numero:
                    breakReturn = True
                    break
                else:
                    numero = numero + parseExpression['expressao'][k]
                    ultimoAdd = parseExpression['expressao'][k]
                    parseExpression['posicao']+=1
                    

        elif parseExpression['expressao'][k] in sinal:
            if ultimoAdd != parseExpression['expressao'][k] and (ultimoAdd=='e' or ultimoAdd=='E'):
                numero = numero + parseExpression['expressao'][k]
                ultimoAdd = parseExpression['expressao'][k]
                parseExpression['posicao']+=1                
            else:
                break
        else:
            breakReturn = True
            break
        
    if breakReturn:
        parseExpression["resultado"] = "Expressão errada, favor corrigi-la"
    else:
        numeroF = resultaNumero(numero)
        return numeroF
            
def resultaNumero(numero):
    return numeroF

# (digit) ::= ‘0’ | ‘1’ | ‘2’ | ‘3’ | ‘4’ | ‘5’ | ‘6’ | ‘7’ | ‘8’ | ‘9’
def digit(digito):
    verif = digito.isnumeric()
    return verif

def expSemEspaco(parseExpression):
    parseExpression["expressao"] = "".join(parseExpression["expressao"].split())
    return parseExpression

def main():
    parseExpression= {"posicao" : 0,
                      "expressao" : "",
                      "simboloAtual" : "",
                      "resultado" : 0}
    parseExpression["expressao"] = "-5 E+2 + 3"
    parseExpression = expSemEspaco(parseExpression)
    expVdd = parseExpression["expressao"]

    if(parseExpression["expressao"][0] == '+'):
        parseExpression["expressao"] = parseExpression["expressao"][1:]

    elif(parseExpression["expressao"][0] == '-'):
        parseExpression["expressao"] = parseExpression["expressao"][1:]
        parseExpression["simboloAtual"] = '-'
    
        
    numero = number(parseExpression)
    print(numero)
    
    return 0


if __name__ == '__main__':
    main()


# else:
#             break
    
#         while verif:
#             if not digit(i):
#                 break
#             else:
#                 numeroN = numeroN + i


                
#         if i == '.':
#             while True:
#                 if not digit(i):
#                     break
#                 else:
#                     numeroN = numeroN  + i

#         if i in euler:

#             numeroN = numeroN + i

#             if i in sinal:
#                 numeroN = numeroN + i

#             while True:
#                 if not digit(i):
#                     break
#                 else:
#                     numeroN = numeroN + i

#     return numeroN