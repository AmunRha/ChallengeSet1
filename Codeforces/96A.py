s = list(input())
zer = one = 0
found = False
for char in s:
    if char == "0":
        if one != "0":
            one=0
        zer+=1
    elif char == "1":
        if zer != "0":
            zer=0
        one+=1
    if zer == 7 or one == 7:
        found = True
if found != True:
    print("NO")
elif found == True:
    print("YES")