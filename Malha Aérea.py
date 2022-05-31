class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []
 
    def adicionarconexao(self, u, v, w):
        self.grafo.append([u, v, w])
 
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    def union(self, parent, rank, x, y):
        xraiz = self.find(parent, x)
        yraiz = self.find(parent, y)
 
        if rank[xraiz] < rank[yraiz]:
            parent[xraiz] = yraiz
        elif rank[xraiz] > rank[yraiz]:
            parent[yraiz] = xraiz
 
        else:
            parent[yraiz] = xraiz
            rank[xraiz] += 1

    def Kruskal(self):
 
        resultado = [] 
         
        i = 0
        e = 0

        quicksort(self.grafo,len(self.grafo))
 
        parent = []
        rank = []
 
        for no in range(self.V):
            parent.append(no)
            rank.append(0)
 
        while e < self.V - 1:
 
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            if x != y:
                e = e + 1
                resultado.append([u, v, w])
                self.union(parent, rank, x, y)
 
        custominimo = 0
        for u, v, peso in resultado:
            custominimo += peso

        return custominimo
 
def quicksort(lista,N):
    qs(lista,0,N-1)

def qs(lista,esq,dir):
    if esq >= dir:
        return
    p = particao(lista,esq,dir)
    qs(lista,esq,p-1)
    qs(lista,p+1,dir)    

def particao(lista,esq,dir):
    pivo = lista[esq][2]
    i = esq
    j = dir + 1
    while True:
        i += 1
        while lista[i][2] < pivo: 
            if i >= dir:
                break
            i += 1
        j -= 1
        while lista[j][2] > pivo: 
            if j <= esq:
                break
            j -= 1
        if i >= j:
            break
        trocar(lista,i,j)
    trocar(lista,esq,j)
    return j

def trocar(unsortedlist,i,min):
    temp = unsortedlist[i]
    unsortedlist[i] = unsortedlist[min]
    unsortedlist[min] = temp

def main():
    
    linha = input().split()
    M = int(linha[0])
    N = int(linha[1])
    
    g = Graph(M)

    for i in range(N):
        linhaconexoes = input().split()
        u = int(linhaconexoes[0])
        v = int(linhaconexoes[1])
        w = int(linhaconexoes[2])
        
        g.adicionarconexao(u, v, w)
    
    preco = g.Kruskal()
    print(preco)

if __name__ == "__main__":
    main()
