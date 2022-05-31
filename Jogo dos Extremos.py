def parent(i):
    pai = (i // 2)
    return pai

def esquerda(i):
    noesquerdo = 2 * i
    return noesquerdo

def direita(i):
    nodireito = (2 * i) + 1
    return nodireito

def maxheapfy(lista,i,heaplenght):
    ie = esquerda(i)
    id = direita(i)

    if ie < heaplenght and lista[ie] > lista[i]:
        maior = ie
    else:
        maior = i

    if id < heaplenght and lista[id] > lista[maior]:
        maior = id

    if maior != i:
        vartemp = lista[maior]
        lista[maior] = lista[i]
        lista[i] = vartemp

        maxheapfy(lista,maior,heaplenght)

def extractmin(lista,tamanho):
    min = 99999999999
    meio = tamanho//2
    for el in lista[meio:]:
        if el < min:
            min = el
    return min


def buildmaxheap(lista):
    heaplenght = len(lista)
    for i in range((heaplenght//2),0,-1):
        maxheapfy(lista,i,heaplenght)

def acharRodadas(lista,constante):
    R = 0
    tamanho = len(lista)
    buildmaxheap(lista)
    nummin = extractmin(lista,tamanho)
    while tamanho > 1:
        nummax = lista[1]

        k = nummax - abs(nummin * constante)
        if k > 0:
            lista[1] = k
            R += 1
            if k < nummin:
                nummin = k
            maxheapfy(lista,1,tamanho)
            
        else:
            vartemp = lista[1]
            lista[1] = lista[-1]
            lista[-1] = vartemp
            tamanho -= 1
            R +=1
            maxheapfy(lista,1,tamanho)
                     

    return R


def main():
   
    sequencia = input()
    listadefault = sequencia.split()

    lista = [99999999]
    for i in listadefault:
        lista.append(int(i))
    
    constante = int(input())

    
    R = acharRodadas(lista,constante)

    print("%d rodadas!"%(R))

if __name__ == '__main__':
    main()