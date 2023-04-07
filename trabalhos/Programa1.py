def Gera_Matriz(M,n):
    for i in range(0,n):
        M.append(0)
        M[i] = []
        for j in range(0,n):
            M[i].append([])
def Funcionalidade_a(M, n, G):
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
                else if resposta == "N" or respota == "n":
                    M[i][j] = 0
                else:
                    print("Insira uma resposta valida")
                    exit(1)
                    





M = []
n= 5
Gera_Matriz(m, n)
G = []
grafos = int(input)
Funcionalidade_a(m, n, G)