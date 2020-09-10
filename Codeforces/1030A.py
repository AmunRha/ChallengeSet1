n = int(input())
hard = False
    
i = input().split()
for j in range(0,n):
    if int(i[j]) == 1:
        hard = True
        break

if hard == True:
    print("HARD")
else :
    print("EASY")