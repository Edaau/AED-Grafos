def Gera_Matriz(m,n):
    for i in range(0,n):
        m.append(0)
        m[i] = []
        for j in range(0,n):
            m[i].append([])
def Funcionalidade_a(m, n):
    cont = 0
    for i in range(0,n):
        for j in range(0,n):
            if i == j:
                m[i][j] = 0
            else:
                resposta = input("Existe aresta entre os vertices %d e %d ? responda com S/N" % (i , j))
                if resposta == "S" or resposta == "s":
                    m[i][j] = 1
                else:
                    m[i][j] = 0
                    



m = []
n= 5
Gera_Matriz(m, n)
Funcionalidade_a(m, n)