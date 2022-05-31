def Parente(i):
    pai = i // 2
    return pai


def MaxHeap(heap):

    for k in range (2,len(heap)):
        if heap[Parente(k)] >= heap[k]:
            pass
        else:
            return False
    
    return True

def MinHeap(heap):

    for k in range (2,len(heap)):
        if heap[Parente(k)] <= heap[k]:
            pass
        else:
            return False
    
    return True

def HeapType(heap):

    condition = MaxHeap(heap)
    if condition == True:
        print("E uma Heap de maximo!")
        return 

    condition = MinHeap(heap)
    if condition == True:
        print("E uma Heap de minimo!")
        return 

    print("Nao e uma Heap!")
    

def main():
    sequencia = input()
    heapzero = sequencia.split()
    heap = [None]

    for i in heapzero:
        heap.append(int(i))

    HeapType(heap)

if __name__ == '__main__':
    main()
