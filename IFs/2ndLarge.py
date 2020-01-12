a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
L= 0
sL = 0

if((a-b)>=0):
    if((a-c)>=0):
        if(b>=c):
            sL = b
        else:
            sL = c
    else:
        sL = a
else:
    if(b>=c):
        if(a>=c):
            sL = a
        else:
            sL = c
    else:
        sL = b


print(sL)