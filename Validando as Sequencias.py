def Rank(element,Sequencia1):
    inicio = 0
    fim = len(Sequencia1) - 1   
    while inicio <= fim:
        meio = (fim + inicio)//2
        if int(Sequencia1[meio]) > element:
            fim = meio - 1
        elif int(Sequencia1[meio]) < element:
            inicio = meio + 1 
        else:
            return meio
    return inicio

def main():
    entrada1 = input()
    Sequencia1 = entrada1.split()

    entrada2 = input()
    Sequencia2 = entrada2.split()

    T = []
    F = []

    for element in Sequencia2:
        i = Rank(int(element),Sequencia1)
        
        if i < len(Sequencia1) and element == Sequencia1[i]:
            T.append(element)
        else:
            F.append(element)

    string1 = " ".join(T)
    string2 = " ".join(F)
    print(string1)
    print(string2)

if __name__ == '__main__':
    main()