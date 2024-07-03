import sys

input = sys.stdin.readline
from collections import Counter

def find_modes(data):
    counts = Counter(data)
    max_count = max(counts.values())
    modes = [key for key, value in counts.items() if value == max_count]
    return modes


re_list = list()

for _ in range(int(input())):
    temp_num = int(input())
    re_list.append(temp_num)

re_list.sort()

meni = find_modes(re_list)
meni.sort()

re_num = meni[-1] if len(meni) == 1 else meni[1]

print(round(sum(re_list) / len(re_list)))
print(re_list[len(re_list) // 2])
print(re_num)
print(max(re_list) - min(re_list))