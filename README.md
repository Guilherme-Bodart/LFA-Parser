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

<p> O código acima mostra a main, onde é criado um dicionário que guardará e atualizará os dados de acordo com as funções chamadas;<p>
<p> No dicionário têm-se quatro chaves, "posicao", para guarda a posicao atual da expressão, "expressão", guarda a expressão toda, "simboloAtual", que guarda os simbolos em ordem, e vai esvaziando assim que é usado, "resultado", que serve como uma variável para colocar o resultado final</p>
<p> Eu guardo a expressão com espaços, caso tenha, para mostrá-la no final e depois tiro os espaços da expressão</p>
<p> Enfim chamo a função expr(parserExpression), que me devolve o resultado da expressão passada</p>



<h3>Gramática do Trabalho</h3>
<p align="center">
  <img src="https://github.com/Guilherme-Bodart/LFA-Parser/blob/master/imagens/Regra%20de%20produ%C3%A7%C3%A3o%20da%20gram%C3%A1tica%20MEL.png?raw=true>
</p>


### Como executar?
Para buildar/executar o app no ambiente Linux basta abrir o CLI no diretório do MELParser.py e digitar o comando:
    
    python3 MELParser.py 
    
O python é na versão 3.7.3, não tenho ciência se terá que baixar a nova versão antes, eu apenas testei o programa no ambiente Windowns.

   
    
### Informações adicionais
Todo o código fonte está hospedado no meu [GitHub](https://github.com/Guilherme-Bodart/LFA-Parser).
