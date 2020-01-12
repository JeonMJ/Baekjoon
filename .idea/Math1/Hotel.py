numOfCases = int(input())
rooms = []

for i in range(0,numOfCases):
    h,w,n = map(int,input().split())

    if n%h==0:
        head = h
        body = n//h
    else:
        head= n % h
        body = n//h+1
    if body < 10:
        body = '0'+str(body)
    rooms.append(str(head)+str(body))
for room in rooms:
    print(room)