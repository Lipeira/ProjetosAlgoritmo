class NoArvore:
    def __init__(self,nomeInit,pontuacaoInit):
        self.nome = nomeInit
        self.pontuacao = pontuacaoInit
        self.direita = None
        self.esquerda = None
        self.pai = None


def Insertion(RaizArvore,nome,pontuacao):
    no = NoArvore(nome,pontuacao)
    x = RaizArvore
    y = None
    
    while x != None:
        y = x
        if no.pontuacao < x.pontuacao:
            x = x.esquerda
        elif no.pontuacao > x.pontuacao:
            x = x.direita
        else:
            print("%s ja esta no sistema."%(nome))
            return RaizArvore


    no.pai = y

    if y == None:
        RaizArvore = no
    
    elif no.pontuacao < y.pontuacao:
        y.esquerda = no
    
    else:
        y.direita = no
    
    print("%s inserido com sucesso!"%(nome))

    return RaizArvore


def BuscaBinaria(RaizArvore,pontuacao):
    
    y = RaizArvore
    while y != None and pontuacao != y.pontuacao:
        if pontuacao < y.pontuacao:
            y = y.esquerda
        else:
            y = y.direita

    return y

def Maximo(x):
    y = x
    while y.direita != None:
        y = y.direita

    return y

def Minimo(x):
    y = x
    while y.esquerda != None:
        y = y.esquerda

    return y

def Sucessor(no):
    if no.direita != None:
        return Minimo(no.direita)
    y = no.pai
    while y != None and no == y.direita:
        no = y
        y = y.pai
    return y

def Predecessor(no):
    if no.esquerda != None:
        return Maximo(no.esquerda)
    y = no.pai
    while y!= None and no == y.esquerda:
        no = y
        y = y.pai
    return y


def Proximidades(RaizArvore,pontuacao):

    y = BuscaBinaria(RaizArvore,pontuacao)

    if y.pai == None and y.direita == None and y.esquerda == None:
        print("Apenas %s existe no sistema..."%(y.nome))
    
    elif y == Maximo(RaizArvore):
        pred = Predecessor(y).nome

        print("%s e o maior! e logo atras vem %s"%(y.nome,pred))

    elif y == Minimo(RaizArvore):
        suc = Sucessor(y).nome

        print("%s e o menor! e logo apos vem %s"%(y.nome,suc))
    
    else:
        suc = Sucessor(y).nome
        pred = Predecessor(y).nome

        print("%s vem apos %s e antes de %s"%(y.nome,pred,suc))



def main():

    RaizArvore = None

    K = int(input())
    for i in range(K):
        command = input()

        if "ADD" in command:
            listacomando = command.split()
            Nome = listacomando[1]
            Pontuacao = int(listacomando[2])
            RaizArvore = Insertion(RaizArvore,Nome,Pontuacao)
            
        elif "PROX" in command:
            listacomando = command.split()
            Pontuacao = int(listacomando[1])
            Proximidades(RaizArvore,Pontuacao)

if __name__ == '__main__':
    main()
