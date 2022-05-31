def LeftSon(i):
    return 2*i + 1

def RightSon(i):
    return 2*i + 2

def main():
    
    heap = input()
    heapcom = heap.split()
    heaplist = []

    for element in heapcom:
        heaplist.append(int(element))

    Ileft = 0    
    Iright = 0
    tamanhoheap = len(heaplist)

    nivel = 1

    nivel1 = heaplist[0]
    print("Media do nivel 1 = %.2f"%(nivel1))

    temp = 0

    if tamanhoheap > 1:
        while Ileft < tamanhoheap and temp < tamanhoheap:

            Ileft = LeftSon(Ileft)
            Iright = RightSon(Iright)
            temp = Iright
            if Ileft < tamanhoheap:
                nivel += 1

            if Iright < tamanhoheap:
                pass
            else:
                Iright = tamanhoheap - 1

            Soma = 0
            contadorNumber = 0
            
            for index in range(Ileft,Iright + 1):
                elemento = heaplist[index]
                if elemento == -1:
                    pass
                else:
                    Soma += elemento
                    contadorNumber += 1
            
            m = Soma / contadorNumber

            print("Media do nivel %d = %.2f"%(nivel,m))


if __name__ == "__main__":
    main()