def Gera_Matriz(M,n,t):
    for i in range(0,n):
        M.append(0)
        M[i] = []
        for j in range(0,t):
            M[i].append([])

def Funcionalidade_a(M, n, G, h):
    cont = 0
    for i in range(0,n):
        for j in range(0,n):
            if i == j:
                M[i][j] = 0
            else:
                resposta = input("Existe aresta entre os vertices %d e %d ? responda com S/N" % (i , j))
                if resposta == "S" or resposta == "s":
                    M[i][j] = 1
                    cont += 1
                elif resposta == "N" or respota == "n":
                    M[i][j] = 0
                else:
                    print("Insira uma resposta valida")
                    exit(1)
    name = input("Insira o nome do grafo: ")
    G[h][0] = name
    G[h][1] = M
    G[h][2] = cont


G = []
grafos = input("Quantos Grafos deseja inserir? ")
if(grafos.isNumeric()):
    Gera_Matriz(G, int(grafos), 3)
else:
    print("Insira um numero valido.")
    exit(1)
for i in range(0, int(grafos)):
    M = []
    n = input("Quantos vertices existem nesse grafo? ")
    if(n.isNumeric()):
        Gera_Matriz(M,n,n)
    else:
        print("Insira um numero valido.")
        exit(1)
    Funcionalidade_a(M, n, G, h)