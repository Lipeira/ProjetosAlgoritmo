def quicksort(lista,N,pivo):
    qs(lista,0,N-1,pivo)

def qs(lista,esq,dir,pivo):
    if esq >= dir:
        return
    p = particao(lista,esq,dir,pivo)
    qs(lista,esq,p-1,pivo)
    qs(lista,p+1,dir,pivo)    

def particao(lista,esq,dir,pivoinit):
    pivo = pivoinit[esq]
    i = esq
    j = dir + 1
    while True:
        i += 1
        while lista[i] < pivo: 
            if i >= dir:
                break
            i += 1
        j -= 1
        while lista[j] > pivo:  
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
    K = int(input())

    for i in range(K):
        Chaves = input()
        ChaveList = Chaves.split()
        Cadeados = input()
        CadeadosList = Cadeados.split()

        tamanho_chave = len(ChaveList)
        tamanho_cadeado = len(CadeadosList)

        for i in range(33,0,-1):        
            quicksort(ChaveList,tamanho_chave,CadeadosList)
            quicksort(CadeadosList,tamanho_cadeado,ChaveList)

        string = " ".join(ChaveList)
        string2 = " ".join(CadeadosList)


        print(string2)
        print(string2)

if __name__ == "__main__":
    main()