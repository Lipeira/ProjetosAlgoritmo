def merge(salarios_totais,esq,meio,dir,aux):
    i = esq
    j = meio + 1
    for k in range(esq,dir+1):
        aux[k] = salarios_totais[k]
    for k in range(esq,dir+1):
        if i > meio:
            salarios_totais[k] = aux[j]
            j += 1
        elif j > dir:
            salarios_totais[k] = aux[i]
            i += 1
        elif aux[i] > aux[j]: 
            salarios_totais[k] = aux[j]
            j += 1
        else:
            salarios_totais[k] = aux[i]
            i += 1

def TD_mergesort(salarios_totais,esq,dir,aux,salarios_m_array):
    meio = len(salarios_m_array) - 1
    merge(salarios_totais,esq,meio,dir,aux)


def main():
    salarios_m = input()
    salarios_m_array = salarios_m.split()

    salarios_n = input()
    salarios_n_array = salarios_n.split()

    salarios_totais = []
    for i in salarios_m_array:
        salarios_totais.append(int(i))
    for i in salarios_n_array:
        salarios_totais.append(int(i))


    aux = list(salarios_totais)
    tamanho_lista = len(salarios_totais)
    TD_mergesort(salarios_totais,0,tamanho_lista - 1,aux,salarios_m_array)
    
    if tamanho_lista % 2 == 0:
        mediana = (salarios_totais[tamanho_lista//2] + salarios_totais[(tamanho_lista//2) - 1]) / 2
        print("%.2f" % mediana)
    else:
        mediana = salarios_totais[tamanho_lista//2]
        print("%.2f" % mediana)

if __name__ == "__main__":
    main()