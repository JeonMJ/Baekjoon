
fc, vc, r = map(int,input().split())

i = 0

if(r < vc  ):
    print(-1)
else:
    i = (fc//(r-vc))+1
    print (i)

