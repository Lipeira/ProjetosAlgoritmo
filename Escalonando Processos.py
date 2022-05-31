class Processo:
    def __init__(self,idInit,timeInit):
        self.id = idInit
        self.time = timeInit
        self.proximo = None
        self.anterior = None

def Agendar(cont,Cabeca,ProcessInit,id,time):
    process = Processo(id,time)
    if ProcessInit == None:
        ProcessInit = process
        Cabeca = process
        cont += 1
        
    else:
        process.proximo = ProcessInit
        process.anterior = None
        process.proximo.anterior = process
        ProcessInit = process
        cont += 1
    print("O programa %d foi agendado com sucesso!"%(id))
    return Cabeca,ProcessInit,cont

def Executar(Cabeca,ProcessInit,timeexec,cont):
    y = Cabeca

    if ProcessInit == None:
            timeexec = 0                
    
    while timeexec != 0:
            if timeexec >= y.time and y.anterior == None:
                print("O programa %d executou por %d segundos."%(y.id,y.time))
                print("O programa %d terminou."%(y.id))
                timeexec = 0
                ProcessInit = None
                Cabeca = None
                cont = 0

            if timeexec >= y.time and y.anterior != None:
                timeexec = timeexec - y.time
                print("O programa %d executou por %d segundos."%(y.id,y.time))
                print("O programa %d terminou."%(y.id))
                y = y.anterior
                y.proximo = None
                Cabeca = y
                cont -= 1
            elif timeexec < y.time and Cabeca != None:
                y.time = y.time - timeexec
                ytemporario = y
                print("O programa %d executou por %d segundos."%(y.id,timeexec))
                if cont == 1:
                    ProcessInit = Cabeca
                    Cabeca = ytemporario
                    ProcessInit.proximo = None
                    ProcessInit.anterior = None
                else:
                    y = y.anterior
                    y.proximo = None
                    Cabeca = y
                    ytemporario.proximo = ProcessInit
                    ytemporario.proximo.anterior = ytemporario
                    ytemporario.anterior = None
                    ProcessInit = ytemporario
                timeexec = 0

    print("A linha possui %d programas."%(cont))
    return Cabeca,ProcessInit,cont


def main():
    ProcessInit = None
    Cabeca = None
    cont = 0

    N = int(input())
    for x in range(N):
        command = input()

        if "ADD" in command:
            cs = command.split()
            idInit = int(cs[1])
            timeInit = int(cs[2])

            Cabeca,ProcessInit,cont = Agendar(cont,Cabeca,ProcessInit,idInit,timeInit)

        elif "EXE" in command:
            cs = command.split()
            timeexec = int(cs[-1])
            Cabeca,ProcessInit,cont = Executar(Cabeca,ProcessInit,timeexec,cont)


if __name__ == '__main__':
    main()
