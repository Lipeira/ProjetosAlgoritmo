class Grafo:
 
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = []
        self.antecessores = [-1] * vertices
 
    def adicionarconexao(self, u, v, w):
        self.graph.append([u, v, w])

     
    def BellmanFord(self, inicio):
 
        dist = [9999999999] * self.V
        dist[inicio] = 0

        for l in range(self.V - 1):

            for u, v, w in self.graph:
                if dist[u] != [9999999999] and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        self.antecessores[v] = u

 
        for u, v, w in self.graph:
                if dist[u] != [9999999999] and dist[u] + w < dist[v]:
                        print("Ciclo negativo encontrado!")
                        return

        for i in range(self.V):
            print("Vertice: %d Antecessor: %d Distancia: %d"%(i,self.antecessores[i],dist[i]))

 
def main():
    N = int(input())
    
    for i in range(N):
        linha = input().split()
        M = int(linha[0])
        N = int(linha[1])
        
        g = Grafo(M)

        for i in range(N):
            linhaconexoes = input().split()
            u = int(linhaconexoes[0])
            v = int(linhaconexoes[1])
            w = int(linhaconexoes[2])
            
            g.adicionarconexao(u, v, w)
        
        S = int(input())

        g.BellmanFord(S)

if __name__ == "__main__":
    main()
