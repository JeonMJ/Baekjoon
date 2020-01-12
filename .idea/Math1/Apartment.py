
numOfCases = int(input())

for i in range(0,numOfCases):
    n = int(input())
    x = int(input())
    people = [p for p in range(1,x+1)]
    for ap in range(0,n):
        for fl in range(1,x):
            people[fl] += people[fl-1]
    print(people[x-1])
