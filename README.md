# LFA-Parser
Implementação de um parser descendente recursivo para uma Linguagem Livre de Contexto, chamada de MEL.

### Informações gerais
- **Autor**: Guilherme Bodart de Oliveira Castro
- **Linguagem de programação**: Python (versão 3.7.3)
- **Ambiente de desenvolvimento**: Visual Studio Code (versão 1.33.1)

### Descrição geral do código fonte
O código fonte está estruturado em um único arquivo principal;

##### MELParser.py
É o arquivo onde contém a main e as funções utilizadas para resolver o exercício;

```python
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
```

<p>O código acima mostra a main, onde é criado um dicionário que guardará e atualizará os dados de acordo com as funções chamadas;<p>


<p align="center">
  <img src="https://github.com/HaraHeique/LFA-MEL-parser/blob/master/images/Regra%20de%20produ%C3%A7%C3%A3o%20da%20gram%C3%A1tica%20MEL.png?raw=true">
</p>

##### build.py
É o módulo que é buildado e que contém a execução principal do programa, o qual utiliza o módulo `ParserMEL.py` que contém a classe do parser e instancia um objeto fazendo chamada o método `parseExpression` passando como argumento a expressão e recebendo um valor como resultado. Como se pode notar no trecho abaixo a expressão é digitada pelo usuário.

```python
from models.ParserMEL import ParserMEL

def main():
    parserMEL: ParserMEL = ParserMEL()

    while True:
        try:
            inputExpression: str = input("Enter your math expression: ")
            parserMEL.parseExpression(inputExpression)
            print("Expression result: {0} = {1}".format(parserMEL.expression, parserMEL.result))
        except Exception:
            print("Invalid input expression. Please check your expression and try again.")
        finally:
            # Somente para pular uma linha no terminal xD
            print()

    return 0

if __name__ == '__main__' :
    main()
```

### Como executar?
Para buildar/executar o app no ambiente Linux basta abrir o CLI(Command Line Interface) no diretório __/source__ e digitar o seguinte comando:
    
    python3 build.py

Neste comando como o SO é o Linux dist. Ubuntu 18.04 e já contém as versões ***2.7.15 e 3.6.7*** como default, o que torna fácil a execução de código utilizando esta linguagem. O outro comando seria a execução do arquivo .sh criado no mesmo diretório. Abaixo execute o mesmo comando que produzirá a mesma ação do primeiro comando mostrado acima:

    sh trab1.sh
    
### Informações adicionais
Todo o código fonte está hospedado no meu [GitHub](https://github.com/HaraHeique/LFA-MEL-parser).