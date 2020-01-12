numOfCases = int(input())
overTheAvg = []
for i in range(0, numOfCases):
    a = input().split()
    a = list(map(int,a))
    num = a[0]
    del a[0]
    Avg = sum(a)/num
    count = 0

    for i in a:
        if(i>Avg):
            count = count + 1
    overTheAvg.append(count/num)

for i in overTheAvg:
    print(format(i,"<10.3%").rstrip())


