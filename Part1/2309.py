arr = []
total = 0
for _ in range(9):
    a = int(input())
    arr.append(a)
    total = total + a

arr.sort()

for i in range(0, 8):
    for j in range(i + 1, 9):
        if 100 == total - arr[i] - arr[j]:
            for k in range(len(arr)):
                if k == i or k == j:
                    pass
                else:
                    print(arr[k])
            exit()
