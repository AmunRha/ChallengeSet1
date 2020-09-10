t = int(input())
res = []
for i in range(0, t):
    l, r = map(int, input().split())
    x = l
    y = r - (r%x)
    res.append(f'{x} {y}')

for i in res:
    print(i)