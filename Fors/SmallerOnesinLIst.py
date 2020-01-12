
n, k = input().split()
n = int(n)
k = int(k)


a = input().split()
a = list(map(int,a))

for i in a:
    if(i<k):
        print(i, end=' ')