for _ in range(int(input())):
    input_char = input()
    count = 0
    for i in input_char:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count == 0:
        print('YES')
    else:
        print('NO')