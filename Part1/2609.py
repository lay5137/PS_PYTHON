def gcd(a, b):
    if a % b == 0:
        return b
    else:
        m = a % b
        return gcd(b, m)


def lcm(a, b):
    k = a
    num = 2
    while(True):
        if k % b == 0:
            return k
        else:
            k = a * num
            num = num + 1


arr = list(map(int, input().split()))

print(gcd(arr[0], arr[1]))
print(lcm(arr[0], arr[1]))