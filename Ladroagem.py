def calculamaximo(listaInit, n):
    if n == 0:
        valormaximo = 0
        return valormaximo
 
    valor = listaInit[0]

    if n == 1:
        return valor
 
    valor2 = -999999

    if listaInit[0] > valor2:
        valor2 = listaInit[0]
    
    if listaInit[1] > valor2:
        valor2 = listaInit[1]
    
    if n == 2:
        return valor2
 
    valormax = None
 
    for i in range(2, n):

        valormax = -99999

        if (listaInit[i]+valor) > valormax:
            valormax = listaInit[i]+valor
    
        if valor2 > valormax:
            valormax = valor2


        valor = valor2
        valor2 = valormax
 
    return valormax
 
def main():
 
    N = int(input())
    line = input().split()

    lista = []
    
    for i in line:
        lista.append(int(i))

    valormaximo = calculamaximo(lista, N)
 
    print("%d reais podem ser roubados hoje!"%(valormaximo))
 
if __name__ == '__main__':
    main()