n = int(input())
count = 0
for i in range(0, n):
    s = input()
    if "++" in s:
        count+=1
    elif "--" in s:
        count-=1

print(count)