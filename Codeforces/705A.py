n = int(input())

s1 = "I hate "
s2 = "I love "
that = "that "
it = "it "
res = ""
if n == 1:
    res = s1 + it
else:
    for i in range(0, n):
        if i%2 == 0:
            res += s1 + that
        else:
            res += s2 + that
    res = res[:-5] + it

print(res)