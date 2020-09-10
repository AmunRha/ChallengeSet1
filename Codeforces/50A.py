m, n = map(int, input().split())

if m%2 == 0 and n%2 == 0:
    res = int(m * (n/2))
elif m%2 != 0 and n%2 !=0:
    res = (m * int(n/2)) + int(m/2)
elif m%2 != 0 and n%2 == 0:
    res = int(m * (n/2))
else:
    res = int(n * (m/2))

print(res)