def money(array, value):
    for i in range(len(array)):

        for j in range(len(array)):

            if array[i] + array[j] == value:
                return print([i, j])

    return print('Sem cafe da manha dessa vez :/')
    

def main():
    N = int(input())
    money_available = []
    while N > 0:
        money_cash = int(input())
        money_available.append(money_cash)

        N -= 1

    total_cafe = int(input())
    money(money_available, total_cafe)


if __name__ == '__main__':
    main()