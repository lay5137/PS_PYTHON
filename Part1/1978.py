n = int(input())
arr = list(map(int, input().split()))
cnt = 0

for i in range(n):
    cnt1 = 0
    for j in range(1, arr[i] + 1):
        if arr[i] % j == 0:
            cnt1 = cnt1 + 1
    if cnt1 == 2:
        cnt = cnt + 1
print(cnt)