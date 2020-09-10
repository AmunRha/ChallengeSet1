lst = list(map(int, input().split()))
lst.sort()
i = -1
count = 0
while True:
    if lst[0] + lst[1] - 1 >= lst[2]:
        break
    else:
        if i < 0:
            lst[0]+=1
        else:
            lst[1]+=1
        count+=1
        i*=(-1)
print(count)