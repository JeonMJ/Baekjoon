aList = []

for i in range(0,10001):
    aList.append(i)

def d(n):
    return n+n%10+(n%100)//10+(n%1000)//100+(n%10000)//1000
for i in range(0,10001):
    if d(i) in aList:
        aList.remove(d(i))

for i in aList:
    print(i)

