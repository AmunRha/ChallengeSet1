s = []
for i in range(0,5):
    s.append(input().split())

for row, lst in enumerate(s):
    if "1" in lst:
        col =  lst.index("1")
        break 

fin_row = abs(row-2)
fin_col = abs(col-2)
print(fin_col+fin_row)