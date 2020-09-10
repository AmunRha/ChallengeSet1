s = input().split("+")
one = two = three = 0
fin = ""
for char in s:
    if char == "1":
        one+=1
    elif char == "2":
        two+=1
    else:
        three+=1

for i in range(0,one):
    fin += "1+"
for i in range(0,two):
    fin += "2+"
for i in range(0,three):
    fin += "3+"
fin = fin[:-1]
print(fin)