def hanoi(number, from_, to_, via_):
    if number == 1:
        print(from_, to_)
    else:
        hanoi(number - 1, from_, via_, to_)
        print(from_, to_)
        hanoi(number - 1, via_, to_, from_)


N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3, 2)