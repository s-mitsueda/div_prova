"""
Crie duas funções:
    A primeira função receberá dois parâmetros, e retornará como resultado
    uma concatenação de texto colocando uma vírgula entre os dois parâmetros ao uní-los.

    A segunda função não receberá parâmetros;
    será feito a leitura de duas entradas que o usuário digitar;
    irá chamar a primeira função passando como argumento os dois textos lidos;
    por fim esta segunda função irá imprimir para o usuário
    o resultado que se obteve na chamada à primeira função.
"""
"""
    Exemplo da primeira entrada: “Olá”.
    Exemplo da segunda entrada: “Mundo”.
    Exemplo da saída do sistema: “Olá,Mundo”.
"""

def concat(str1:str, str2:str) -> str:
    return ",".join([str1, str2])

def receive_input() -> None:
    input1 = input()
    input2 = input()

    print(concat(input1, input2))

receive_input()