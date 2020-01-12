a = int(input())

def find(i):
    num = 1
    while num*(num+1)/2 < i:
        num = num + 1
    return num-1
num = find(a)
if num%2!=0:
    head = a-num*(num+1)/2
    body = -(a - num*(num+1)/2) + num + 2
else:
    head = -(a - num*(num+1)/2) + num + 2
    body = a-num*(num+1)/2

print(int(head),end='/')
print(int(body))