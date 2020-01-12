a =int(input())
count = 0

for i in range(1,a+1):
    x = (i%1000)//100
    y = (i%100)//10
    z = (i%10)

    if(i<100):
        count = count + 1
    elif((x+z)==2*y):
        if(i == 1000):
            continue
        count = count + 1



print(count)