p, q = map(int, input().split())

list = []

for i in range(1, p + 1):
    if p % i == 0:
        list.append(i)

if len(list) < q:
    print(0)
else:
    print(list[q - 1])