H, M = input().split()
H = int(H)
M = int(M)
aH = 0
aM = 0

if(M<45):
    if(H==0):
        aM = abs(M+60 - 45)%60
        aH = 23
    else:
        aM = abs(M+60 - 45)%60
        aH = H - 1


else:
    aH = H
    aM = M - 45

print(aH, aM)
