N = int(input())
people = []

for _ in range(N):
    x, y = map(int, input().split())
    people.append((x, y))

ranks = []
for i in range(N):
    rank = 1
    for j in range(N):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                rank += 1
    ranks.append(rank)

print(" ".join(map(str, ranks)))