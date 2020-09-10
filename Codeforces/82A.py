 
n = int(input())
res = ""

p = 1
t = 0
while t < n:
    t += 5*(pow(2, p-1))
    p += 1
tn = t - (5*(pow(2, p-2)))
p = p-2
c = int((n-(tn+1))/pow(2,p)) + 1

if c == 1:
    res = "Sheldon"
elif c == 2:
    res = "Leonard"
elif c == 3:
    res = "Penny"
elif c == 4:
    res = "Rajesh"
elif c == 5:
    res = "Howard"

print(res)