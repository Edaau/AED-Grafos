def Gera_Matriz(M,n,t):
    for i in range(0,n):
        M.append(0)
        M[i] = []
        for j in range(0,t):
            M[i].append([])

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