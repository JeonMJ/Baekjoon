a = int(input())
count = 0
c = a%15
d = (a//15)*3
if a in [1,2,4,7]:
    count = -1
else:
    if c == 0:
        count = d
    elif c ==1:
        count = d-3+4
    elif c==2:
        count = d-3+5
    elif c==3:
        count = d+1
    elif c==4:
        count = d-3+5
    elif c==5:
        count = d + 1
    elif c==6:
        count = d + 2
    elif c==7:
        count = d-3+6
    elif c==8:
        count = d + 2
    elif c==9:
        count = d + 3
    elif c==10:
        count = d + 2
    elif c==11:
        count = d + 3
    elif c==12 or c==14:
        count = d + 4
    elif c==13:
        count = d + 3

print(count)