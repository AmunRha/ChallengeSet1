n = int(input())
res = []
for i in range(0, n):
    s = input()
    if(len(s) <= 10):
        res.append(s)
    else:
        fin = s[0] + str(len(s[1:-1])) + s[-1]
        res.append(fin)
for i in res:
    print(i)