class stack():
    def __init__(self,numInit):
        self.chave = numInit
        self.proximo = None
        self.anterior = None

def InserirElemento(numInsert,NoInicial):
    no = stack(numInsert)
    if NoInicial != None:
        no.anterior = NoInicial
        no.proximo = None
        no.anterior.proximo = no
        NoInicial = no
    else:
        NoInicial = no
    return NoInicial

def Pop(NoInicial):
    y = NoInicial
    print(y.chave)
    if NoInicial != None and NoInicial.anterior == None :
        NoInicial = None
    else:
        NoInicial = NoInicial.anterior
        NoInicial.proximo = None
    return NoInicial


def getMin(NoInicial):
    y = NoInicial
    numMin = 9999999
    while y != None:
        if y.chave < numMin:
            numMin = y.chave
        y = y.anterior
    return numMin

def getMax(NoInicial):
    x = NoInicial
    numMax = -9999999
    while x != None:
        if x.chave > numMax:
            numMax = x.chave
        x = x.anterior
    return numMax



def main():
    NoInicial = None
    qtdcomandos = int(input())

    for x in range(qtdcomandos):

        command = input()

        if "push" in command:
            op = command.split()
            num = int(op[1])
            NoInicial = InserirElemento(num,NoInicial)

            
        elif command == "pop":
            if NoInicial == None:
                print("empty stack")
            else:
                NoInicial = Pop(NoInicial)
                        
        elif "getMin" in command:
            if NoInicial == None:
                print("empty stack")
            else:
                nummin = getMin(NoInicial)
                print(nummin)

        elif "getMax" in command:
            if NoInicial == None:
                print("empty stack")
            else:
                nummax = getMax(NoInicial)
                print(nummax)
            
    

if __name__ == '__main__':
    main()