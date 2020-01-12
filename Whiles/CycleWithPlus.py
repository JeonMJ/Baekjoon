a = input()
a = int(a)

currentA = a
ans = True
count = 0
while(ans):
    currentA = (currentA%10)*10 + (currentA//10 + currentA%10)%10
    count = count +1
    if(a==currentA):
        ans = False
print(count)
