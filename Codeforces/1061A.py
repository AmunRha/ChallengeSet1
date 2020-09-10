n, s = map(int, input().split())

count = 1
tmp = int(n)
while s > tmp:
    count+=1
    tmp+=n
print(count)