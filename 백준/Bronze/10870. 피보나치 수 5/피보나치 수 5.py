def pivo(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return pivo(num - 1) + pivo(num - 2)


print(pivo(int(input()) + 1))