#Guilherme dos Santos Cordeiro Turma: 10A

def main():
    #todas as entradas das listas são digitadas em uma unica linha separada apenas por espaço
    inicial = ""
    estados = [] #guarda os estados do automato
    alfabeto = [] #guarda o alfabeto do automato
    transicoes = [] #guarda as transicoes do automato
    aceitacao = [] #guarda os estados de aceitacao do automato

    estados = input("Estados: ").split() #lê a os elementos e os separa por espaço
    alfabeto = input("Alfabeto: ").split()

    #guarda as transições numa lista de tuplas, cada transição possui um estado de origem, um símbolo do alfabeto e um estado de destino
    for _ in range(len(estados) * len(alfabeto)):
        origem, destino, caractere = input("Digite as transições no formato: estado origem, estado destino e caractere: ").split()
        transicoes.append((origem, destino, caractere))

    inicial = input("Estado Inicial: ") 
    aceitacao = input("Estados de Aceitação: ").split() 

    palavra = input("Digite a palavra a ser verificada: ") #dá entrada na palavra que será verificada

    estado_atual = inicial #define onde o automato começará a verificar a palavra
    for caractere in palavra:
        encontrado = False
        for transicao in transicoes:
            #verifica se o estado atual é igual ao estado de origem da transição e o caractere é igual ao caractere da transição
            if estado_atual == transicao[0] and caractere == transicao[2]:
                estado_atual = transicao[1] #o estado de destino passa a ser o atual
                encontrado = True
                #caso o caractere seja encontrado, o loop é interrompido e se começa a verificação do próximo caractere
                break

        if not encontrado:
            print("Transição não encontrada para o caractere", caractere)
            return

    if estado_atual in aceitacao: #caso o estado atual seja um estado de aceitação, a palavra é aceita e caso contrario é rejeitada
        print("Palavra aceita!")
    else:
        print("Palavra rejeitada!")

main()

#Linguagem deve ter pelo meno um a e terminar com b
#EXEMPLO DE ENTRADA
#Estados: q0 q1 q2 
#Alfabeto: a b
#Transições: q0 q1 a
#            q0 q0 b
#            q1 q1 a
#            q1 q2 b
#            q2 -  a
#            q2 q2 b
#Estado Inicial: q0
#Estados de Aceitação: q2
#Digite a palavra a ser verificada: aab (aceita)
#Digite a palavra a ser verificada: abb (aceita)
#Digite a palavra a ser verificada: aabbb (aceita)
#Ditite a palavra a ser verificada: abbba (rejeita)
#Digite a palavra a ser verificada: abbbaa (rejeita)
