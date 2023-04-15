def Gera_Matriz(M,n,t):
    for i in range(0,n):
        M.append(0)
        M[i] = []
        for j in range(0,t):
            M[i].append([])
def Gera_Matriz_Completo(M,n,G,h):
    for i in range(0,int(n)):
        for j in range(0,int(n)):
            if i == j:
                M[i][j] = 0
                M[j][i] = 0
            elif M[j][i] == 0:
                next
            elif M[i][j] == 1:
                next
            elif i != j:
                M[i][j] = 1
                M[j][i] = 1
    name = "completo_%d" % n
    G[h][0] = name
    G[h][1] = M
    cont = (n*(n-1))/2
    G[h][2] = cont
    for i in range(0,int(n)):
        for j in range(0,int(n)):
            print(M[i][j], end= ' ')
        print()
    print("O valor de |E|: %d" % cont)

def Gera_Matriz_Bipartido(M,n,m,G,h):
    total = int(n) + int(m)
    for i in range(0,total):
        for j in range(0,total):
            if M[j][i] == 0:
                next
            else:
                M[i][j] = 0
                M[j][i] = 0

    for i in range(0,int(n)):
        for j in range(int(n),total):
            M[i][j] = 1
            M[j][i] = 1
    name = "bipartido_completo_%d%d" % (int(n),int(m))
    G[h][0] = name
    G[h][1] = M
    cont = int(n)*int(m)
    G[h][2] = cont
    for i in range(0,total):
        for j in range(0,total):
            print(M[i][j], end= ' ')
        print()
    print("O valor de |E|: %d" % cont)



def Funcionalidade_a(M, n, G, h):
    cont = 0
    for i in range(0,int(n)):
        for j in range(0,int(n)):
            if i == j:
                M[i][j] = 0
            elif M[j][i] == 0:
                next
            elif M[i][j] == 1:
                next
            else:
                resposta = input("Existe aresta entre os vertices %d e %d ? responda com S/N " % (i , j))
                if resposta == "S" or resposta == "s":
                    M[i][j] = 1
                    M[j][i] = 1
                    cont += 1
                elif resposta == "N" or resposta == "n":
                    M[i][j] = 0
                    M[j][i] = 0
                else:
                    print("Insira uma resposta valida")
                    exit(1)
    name = input("Insira o nome do grafo: ")
    G[h][0] = name
    G[h][1] = M
    G[h][2] = cont
    for i in range(0,int(n)):
        for j in range(0,int(n)):
            print(M[i][j], end= ' ')
        print()
    print("O valor de |E|: %d" % cont)

def Funcionalidade_b(G, name, grafos):
    for i in range(0, grafos):
        if G[i][0] == name:
            for k in range(0,len(G[i][1])):
                for j in range(0,len(G[i][1])):
                    print(G[i][1][k][j], end= ' ')
                print()
            print("O valor de |E|: %d" % G[i][2])
            exit(0)
    print("Grafo nao encontrado.")

 


G = []
grafos = input("Quantos Grafos deseja inserir? ")
if(grafos.isnumeric()):
    Gera_Matriz(G, int(grafos), 3)
else:
    print("Insira um numero valido.")
    exit(1)
for i in range(0, int(grafos)):
    M = []
    n = input("Quantos vertices existem nesse grafo? ")
    if(n.isnumeric()):
        Gera_Matriz(M,int(n),int(n))
    else:
        print("Insira um numero valido.")
        exit(1)
    Funcionalidade_a(M, n, G, i)
pergunta = input("Deseja encontrar algum grafo?: Responda com S/N ")
if pergunta == "S" or pergunta == "s":
    nome = input("Insira o nome do grafo que deseja procurar: ")
    Funcionalidade_b(G, nome, int(grafos))
elif pergunta == "N" or pergunta == "n":
    exit(0)
else:
    print("Entre com uma resposta valida na proxima execucao.")