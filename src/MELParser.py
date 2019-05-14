#(expr) ::= (term) ((‘+’ | ‘-’) (term))*
def expr(parseExpression):
    termo1 = term(parseExpression)
    simbolos: tuple = ("+","-")

    while True:
        if parseExpression['posicao'] < len(parseExpression["expressao"]):
            if parseExpression["expressao"][parseExpression['posicao']] in simbolos:
                parseExpression["simboloAtual"] = verifSimbolo(parseExpression)
                termo2 = term(parseExpression)
                tam = len(parseExpression["simboloAtual"])

                if parseExpression["simboloAtual"][tam-1] == "+" and termo2!=None:
                    termo1 += termo2
                    parseExpression["simboloAtual"] = parseExpression["simboloAtual"][0:tam-1]

                elif parseExpression["simboloAtual"][tam-1] == "-" and termo2!=None:
                    termo1 -= termo2
                    parseExpression["simboloAtual"] = parseExpression["simboloAtual"][0:tam-1]
            
            else:
                break
        else:
            break
    
    return termo1

#(term) ::= (factor) ((‘*’ | ‘/’ | ‘//’ | ‘%’) (factor))*
def term(parseExpression):
    termo1 = factor(parseExpression)
    
    
    simbolos: tuple = ('*', '/','//','%')
    if(termo1==None):
        termo1 = 1
    while True:
        if parseExpression['posicao'] < len(parseExpression["expressao"]):
            if parseExpression["expressao"][parseExpression['posicao']] in simbolos:
                
                parseExpression["simboloAtual"] = verifSimbolo(parseExpression)
                termo2 = factor(parseExpression)
                tam = len(parseExpression["simboloAtual"])
                if parseExpression["simboloAtual"][tam-1] == "*" and termo2!=None:
                    termo1 *= termo2
                    parseExpression["simboloAtual"] = parseExpression["simboloAtual"][0:tam-1]

                elif parseExpression["simboloAtual"][(tam-2):(tam)]=="//"  and termo2!=None:
                    termo1 //= termo2
                    parseExpression["simboloAtual"] = parseExpression["simboloAtual"][0:tam-2]

                elif parseExpression["simboloAtual"][tam-1] == "/" and termo2!=None:
                    termo1 /= termo2
                    parseExpression["simboloAtual"] = parseExpression["simboloAtual"][0:tam-1]               
                

                elif parseExpression["simboloAtual"][tam-1] == "%" and termo2!=None:
                    termo1 %= termo2
                    parseExpression["simboloAtual"] = parseExpression["simboloAtual"][0:tam-1]
            else:
                break
        else:
            break

    return termo1
 

#Verifica qual é o simbolo atual e adiciona na String de simbolos do dicionário
def verifSimbolo(parseExpression):
    simbolo = ""
    sinal1: tuple = ('+', '-')
    sinal2: tuple = ('*', '/','//','%')

    simbolo = parseExpression["expressao"][parseExpression['posicao']]
    parseExpression["posicao"] = parseExpression["posicao"] + 1
    
    if(simbolo in sinal1):
        
        while True:
            if parseExpression['posicao'] < len(parseExpression["expressao"]):
                if(parseExpression["expressao"][parseExpression['posicao']] in sinal1):
                    parseExpression['posicao'] = parseExpression['posicao'] + 1
                else:
                    break
            else:
                break
            
    elif(simbolo in sinal2):
        while True:
            if parseExpression['posicao'] < len(parseExpression["expressao"]):
                if simbolo == "/":
                    if parseExpression["expressao"][parseExpression['posicao']] == "/":
                        simbolo = simbolo + parseExpression["expressao"][parseExpression['posicao']]
                if(parseExpression["expressao"][parseExpression['posicao']] in sinal2):
                    parseExpression['posicao'] = parseExpression['posicao'] + 1
                else:
                    break
            else:
                break

    if simbolo == "+":
        parseExpression["simboloAtual"] = parseExpression["simboloAtual"] +  "+"
    elif simbolo == "-":
        parseExpression["simboloAtual"] = parseExpression["simboloAtual"] +  "-"
    elif simbolo == "*":
        parseExpression["simboloAtual"] = parseExpression["simboloAtual"] +  "*"
    elif simbolo == "/":
        parseExpression["simboloAtual"] = parseExpression["simboloAtual"] +  "/"
    elif simbolo == "//":
        parseExpression["simboloAtual"] = parseExpression["simboloAtual"] +  "//"
    elif simbolo == "%":
        parseExpression["simboloAtual"] = parseExpression["simboloAtual"] +  "%"
    
    return parseExpression["simboloAtual"]

#(factor) ::= (base) (‘^’ (factor))?
def factor(parseExpression):
    
    valor = base(parseExpression)
    if parseExpression['posicao'] < len(parseExpression["expressao"]):
        if parseExpression["expressao"][parseExpression['posicao']] == "^":
            parseExpression["posicao"] = parseExpression["posicao"] + 1
            return valor ** factor(parseExpression)

    return valor


#(base) ::= (‘+’ | ‘-’) (base)
#| (number)
#| ‘(’ (expr) ‘)’
def base(parseExpression):
    
    if parseExpression['posicao'] < len(parseExpression["expressao"]):
        if parseExpression["expressao"][parseExpression['posicao']] == '+':
            parseExpression["posicao"] = parseExpression["posicao"] + 1
            return 1*base(parseExpression)

        elif parseExpression["expressao"][parseExpression['posicao']] == '-':
            parseExpression["posicao"] = parseExpression["posicao"] + 1
            return  (-1)*base(parseExpression)

        if parseExpression["expressao"][parseExpression['posicao']] == "(":
            parseExpression["posicao"] = parseExpression["posicao"] + 1
            resultado = expr(parseExpression)
            if parseExpression["expressao"][parseExpression['posicao']] == ")":
                parseExpression["posicao"] = parseExpression["posicao"] + 1
                return resultado
        
        return number(parseExpression)
    else:
        return number(parseExpression) 





# (number) ::= (digit)+ ‘.’? (digit)* ((‘E’ | ‘e’) (‘+’ | ‘-’)? (digit)+)?
def number(parseExpression):
    euler: tuple = ('e', 'E')
    sinal: tuple = ('+', '-')
    numero = ''
    ultimoAdd = ''
    for i in range(len(parseExpression["expressao"])):
        k = parseExpression['posicao']

        if k < len(parseExpression["expressao"]):
            if digit(parseExpression['expressao'][k]):
                numero = numero + parseExpression['expressao'][k]
                ultimoAdd = parseExpression['expressao'][k]
                parseExpression['posicao']+=1

            elif parseExpression['expressao'][k] == '.':
                
                if ultimoAdd != parseExpression['expressao'][k]:
                    if '.' in numero:
                        break
                    else:
                        numero = numero + parseExpression['expressao'][k]
                        ultimoAdd = parseExpression['expressao'][k]
                        parseExpression['posicao']+=1     

            elif parseExpression['expressao'][k] in euler:
                if ultimoAdd != parseExpression['expressao'][k]:
                    if 'e' in numero or 'E' in numero:
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
                break
        else:
            break
        
    numeroF = resultaNumero(numero)
    return numeroF


#Devolve a String passada como um numero calculável          
def resultaNumero(numero):
    numeroF = 0
    splite = []
    if "e" in numero:
        splite = numero.split("e")
    elif "E" in numero:
        splite = numero.split("E")
    else:
        numeroF = float(numero)
    
    if splite!=[]:
        if(splite[1]=="" or splite[1]=="+" or splite[1]=="-"):
            splite[1]=0
        numeroF = float(splite[0])*(10**float(splite[1]))
    

    return numeroF


# (digit) ::= ‘0’ | ‘1’ | ‘2’ | ‘3’ | ‘4’ | ‘5’ | ‘6’ | ‘7’ | ‘8’ | ‘9’
def digit(digito):
    verif = digito.isnumeric()
    return verif

#Retira todos os espaços da expressão passada
def expSemEspaco(parseExpression):
    parseExpression["expressao"] = "".join(parseExpression["expressao"].split())
    return parseExpression

def main():
    parseExpression= {"posicao" : 0,
                      "expressao" : "",
                      "simboloAtual" : "",
                      "resultado" : 0}
    parseExpression["expressao"] = input("Entre com a expressão que deseja: ")
    expVdd = parseExpression["expressao"]   
    parseExpression = expSemEspaco(parseExpression)
    

    print("Expressao: ",expVdd)
    parseExpression["resultado"] = expr(parseExpression)
    print("Resultado: ",parseExpression["resultado"])
    
    return 0

if __name__ == '__main__':
    main()

