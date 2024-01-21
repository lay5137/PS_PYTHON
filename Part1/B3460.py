T = int(input())

while T > 0:
    n = (int(input()))
    idx = 0

    while n > 0:
        if n % 2 == 1:
            print(idx, end=' ')

        n //= 2
        idx += 1

    T -= 1
