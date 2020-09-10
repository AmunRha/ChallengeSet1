n, m, a = map(int, input().split())
i, j = int(n/a), int(m/a)
if n%a != 0:
    i = int(n/a) + 1
if m%a != 0:
    j = int(m/a) + 1
print(i*j)