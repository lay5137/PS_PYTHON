a = list(map(int, input().split()))
arr = []
cnt = 0

for i in range(1, 1001):
    for _ in range(i):
        arr.append(i)
        cnt = cnt + 1
        if cnt >= a[1]:
            break
    if cnt >= a[1]:
        break

print(sum(arr[a[0]-1:a[1]]))