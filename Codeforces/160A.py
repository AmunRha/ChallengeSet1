n = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)
tot = sum(a)
res = count = 0
for i in a:
    res += i
    count+=1
    if res > tot/2:
        break
print(count)