while True:
    input_char = input()
    if input_char == ".":
        break
    count = []
    check = 0
    for i in input_char:
        if i == '(':
            count.append('(')
        elif i == '[':
            count.append('[')
        if i == ')':
            if count and count[-1] == '(':
                count.pop()
            else:
                break
        if i == ']':
            if count and count[-1] == '[':
                count.pop()
            else:
                break
        check += 1
    if check == len(input_char) and not count:
        print('yes')
    else:
        print('no')