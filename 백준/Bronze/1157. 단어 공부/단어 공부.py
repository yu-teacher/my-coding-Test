data = input().lower()
datas = {}

for ch in data:
    if ch in datas:
        temp = datas[ch]
        datas[ch] = (temp + 1)
    else:
        datas[ch] = 1

max_count = max(datas.values())

if list(datas.values()).count(max_count) > 1:
    print('?')
else:
    for key, value in datas.items():
        if value == max_count:
            print(key.upper())
            break
