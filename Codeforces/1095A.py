n = int(input())
s = list(input())
j = 0
for i in range(1,n+1):
    j += i
    try:
        print(s[j-1], end='')
    except:
        break
print()