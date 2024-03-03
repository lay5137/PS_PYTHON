cnt = 0
maxPeople = 0
people = 0

while(cnt < 10):
    value = list(map(int, input().split()))

    people = people - value[0] + value[1]

    if(maxPeople < people):
        maxPeople = people

    cnt += 1

print(maxPeople)