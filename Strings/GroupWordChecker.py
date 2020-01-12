num = int(input())
count = 0
for i in range(0,num):
    checker = []
    a = input()
    check = True
    for c in a:
        if c not in checker:
            checker.append(c)
        else:
            if checker[len(checker)-1]!=c:
                check = False
                break
    if check == True:
        count = count + 1
print(count)
