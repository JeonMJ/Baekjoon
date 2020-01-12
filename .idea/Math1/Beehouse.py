def go(N):
    start = 2
    num = 1
    current = 1
    if N==1:
        return 1
    while current<N:
        current = current + 6*num
        num = num + 1
    return num

a = int(input())
print(go(a))
