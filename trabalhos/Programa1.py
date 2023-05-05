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
    print(name)
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
    print(name)
    print("O valor de |E|: %d" % cont)

def Gera_Matriz_Estrela(M,n,G,h):
    cont = 0
    for i in range(0,int(n)):
        for j in range(0,int(n)):
            if M[j][i] == 0:
                next
            else:
                M[i][j] = 0
                M[j][i] = 0
    for i in range(1, int(n)):
        M[0][i] = 1
        M[i][0] = 1
        cont += 1
    name = "estrela_%d" % (int(n))
    G[h][0] = name
    G[h][1] = M
    G[h][2] = cont
    for i in range(0,int(n)):
        for j in range(0,int(n)):
            print(M[i][j], end= ' ')
        print()
    print(name)
    print("O valor de |E|: %d" % cont)
def Gera_Matriz_Caminho(M,n,G,h):
    for i in range(0,int(n)):
        for j in range(0,int(n)):
            if M[j][i] == 0:
                next
            else:
                M[i][j] = 0
                M[j][i] = 0
    cont = 0
    for i in range(0,int(n)-1):
        M[i][i+1] = 1
        M[i+1][i] = 1
        cont += 1
    name = "caminho_%d" % (int(n))
    G[h][0] = name
    G[h][1] = M
    G[h][2] = cont
    for i in range(0,int(n)):
        for j in range(0,int(n)):
            print(M[i][j], end= ' ')
        print()
    print(name)
    print("O valor de |E|: %d" % cont)
    
def Gera_Matriz_Ciclo(M,n,G,h):
    for i in range(0,int(n)):
        for j in range(0,int(n)):
            if M[j][i] == 0:
                next
            else:
                M[i][j] = 0
                M[j][i] = 0
    cont = int(n)
    for i in range(0,int(n)):
        M[i][(i+1)%int(n)] = 1
        M[i][(i-1)%int(n)] = 1
    M[0][int(n)-1] = 1
    M[int(n)-1][0] = 1
    name = "ciclo_%d" % (int(n))
    G[h][0] = name
    G[h][1] = M
    G[h][2] = cont
    for i in range(0,int(n)):
        for j in range(0,int(n)):
            print(M[i][j], end= ' ')
        print()
    print(name)
    print("O valor de |E|: %d" % cont)

def Gera_Matriz_Roda(M,n,G,h):
    for i in range(0,int(n)+1):
        for j in range(0,int(n)+1):
            if M[j][i] == 0:
                next
            else:
                M[i][j] = 0
                M[j][i] = 0
    cont = 2*int(n)
    for i in range(0,int(n)):
        M[i][(i+1)%int(n)] = 1
        M[i][(i-1)%int(n)] = 1
    M[0][int(n)-1] = 1
    M[int(n)-1][0] = 1
    for i in range(0,int(n)+1):
        for j in range(0,int(n)+1):
            if i == int(n) or j == int(n):
                M[i][j] = 1
    M[int(n)][int(n)] = 0
    name = "roda_%d" % (int(n))
    G[h][0] = name
    G[h][1] = M
    G[h][2] = cont
    for i in range(0,int(n)+1):
        for j in range(0,int(n)+1):
            print(M[i][j], end= ' ')
        print()
    print(name)
    print("O valor de |E|: %d" % cont)

def Gera_Matriz_Cubo(M,n,G,h):
    if int(n) == 0:
        M[0][0] = 0
        name = "cubo_%d" % (int(n))
        cont = 0
        G[h][0] = name
        G[h][1] = M
        G[h][2] = cont
        for i in range(0,2**int(n)):
            for j in range(0,2**int(n)):
                print(M[i][j], end= ' ')
            print()
        print(name)
        print("O valor de |E|: %d" % cont)
    elif int(n) ==1:
        M[0][0] = 0
        M[0][1] = 1
        M[1][0] = 1
        M[1][1] = 0
        cont = 1
        name = "cubo_%d" % (int(n))
        G[h][0] = name
        G[h][1] = M
        G[h][2] = cont
        for i in range(0,2**int(n)):
            for j in range(0,2**int(n)):
                print(M[i][j], end= ' ')
            print()
        print(name)
        print("O valor de |E|: %d" % cont)
    else:
        for i in range(0,2**int(n)):
            for j in range(0,2**int(n)):
                if M[j][i] == 0:
                    next
                else:
                    M[i][j] = 0
                    M[j][i] = 0
        cont = (2**(int(n)))*int(n)
        for i in range(0,2**int(n)):
            for j in range(0,int(n)):
                if ((i >> j) & 1) == 0:
                    v = i + (1 << j)
                    if v < 2**int(n):
                        M[i][v] = 1
                        M[v][i] = 1 
                else:
                    v = i - (1 << j)
                    if v >= 0:
                        M[i][v] = 1
                        M[v][i] = 1
        name = "cubo_%d" % (int(n))
        cont = cont//2
        G[h][0] = name
        G[h][1] = M
        G[h][2] = cont
        for i in range(0,2**int(n)):
            for j in range(0,2**int(n)):
                print(M[i][j], end= ' ')
            print()
        print(name)
        print("O valor de |E|: %d" % cont)

def is_conexo(M):
    num_vertices = len(M)
    visitados = set()
    atual = 0
    visitados.add(atual)
    pilha = [atual]
    while pilha:
        atual = pilha.pop()
        for adjacente in range(num_vertices):
            if M[atual][adjacente] == 1 and adjacente not in visitados:
                visitados.add(adjacente)
                pilha.append(adjacente)
    
    return len(visitados) == num_vertices

def num_componentes_conexas(M):
    num_vertices = len(M)
    visitados = set()
    num_componentes = 0
    for i in range(num_vertices):
        if i not in visitados:
            num_componentes += 1
            atual = i
            visitados.add(atual)
            pilha = [atual]
            while pilha:
                atual = pilha.pop()
                for adjacente in range(num_vertices):
                    if M[atual][adjacente] == 1 and adjacente not in visitados:
                        visitados.add(adjacente)
                        pilha.append(adjacente)
    
    return num_componentes
    
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
            if is_conexo(M):
                print("O grafo é conexo")
            else:
                print("O grafo não é conexo")

            num_componentes = num_componentes_conexas(M)
            print("O grafo possui", num_componentes, "componente(s) conexa(s)")
            exit(0)
    print("Grafo nao encontrado.")

G = []
grafos = input("Quantos Grafos deseja inserir? ")
if(grafos.isnumeric()):
    Gera_Matriz(G, int(grafos), 3)
else:
    print("Insira um numero valido.")
    exit(1)
especial = input("Os grafos serao especiais ou nao? Resposta com S/N ")
if especial == "S" or especial == "s":
    for i in range(0, int(grafos)):
        classe = input("De qual classe sera o grafo: ")
        if classe.upper() == "COMPLETO":
            M = []
            n = input("Quantos vertices existem nesse grafo? ")
            if(n.isnumeric()):
             Gera_Matriz(M,int(n),int(n))
            else:
                print("Insira um numero valido.")
                exit(1)
            Gera_Matriz_Completo(M, int(n), G, i)
        elif classe.upper() == "BIPARTIDO COMPLETO" or classe.upper() == "BIPARTIDOCOMPLETO":
            M = []
            n1 = input("Insira o valor de n1: ")
            if(n1.isnumeric()):
                n2 = input("Insira o valor de n2: ")
                if(n2.isnumeric()):
                    n3 = int(n1)+int(n2)
                    Gera_Matriz(M,n3,n3)
                else:
                    print("Insira um numero valido.")
                    exit(1)
            else:
                print("Insira um numero valido1.")
                exit(1)
            Gera_Matriz_Bipartido(M, n1, n2, G, i)
        elif classe.upper() == "ESTRELA":
            M = []
            n = input("Quantos vertices existem nesse grafo? ")
            if(n.isnumeric()):
             Gera_Matriz(M,int(n),int(n))
            else:
                print("Insira um numero valido.")
                exit(1)
            Gera_Matriz_Estrela(M, n, G, i)
        elif classe.upper() == "CAMINHO":
            M = []
            n = input("Quantos vertices existem nesse grafo? ")
            if(n.isnumeric()):
             Gera_Matriz(M,int(n),int(n))
            else:
                print("Insira um numero valido.")
                exit(1)
            Gera_Matriz_Caminho(M, n, G, i)
        elif classe.upper() == "CICLO":
            M = []
            n = input("Quantos vertices existem nesse grafo? ")
            if(n.isnumeric() and int(n) >= 3):
             Gera_Matriz(M,int(n),int(n))
            else:
                print("Insira um numero valido.")
                exit(1)
            Gera_Matriz_Ciclo(M, n, G, i)
        elif classe.upper() == "RODA":
            M = []
            n = input("Quantos vertices existem nesse grafo? ")
            if(n.isnumeric() and int(n) >= 3):
             Gera_Matriz(M,int(n)+1,int(n)+1)
            else:
                print("Insira um numero valido.")
                exit(1)
            Gera_Matriz_Roda(M, int(n), G, i)
        elif classe.upper() == "CUBO":
            M = []
            n = input("Insira o valor de n:")
            if(n.isnumeric()):
             Gera_Matriz(M,2**int(n),2**int(n))
            else:
                print("Insira um numero valido.")
                exit(1)
            Gera_Matriz_Cubo(M, n, G, i)
        else:
            print("Insira uma classe valida na proxima execucao")
            exit(1)

elif especial == "N" or especial == "n":
    for i in range(0, int(grafos)):
        M = []
        n = input("Quantos vertices existem nesse grafo? ")
        if(n.isnumeric()):
            Gera_Matriz(M,int(n),int(n))
        else:
            print("Insira um numero valido.")
            exit(1)
        Funcionalidade_a(M, n, G, i)
else:
    print("Entre com uma resposta valida na proxima execucao.")

pergunta = input("Deseja encontrar algum grafo e saber se ele é conexo?: Responda com S/N ")
if pergunta == "S" or pergunta == "s":
    nome = input("Insira o nome do grafo que deseja procurar: ")
    Funcionalidade_b(G, nome, int(grafos))
    

elif pergunta == "N" or pergunta == "n":
    exit(0)
else:
    print("Entre com uma resposta valida na proxima execucao.")