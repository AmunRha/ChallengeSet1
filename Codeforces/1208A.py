def xorinacci(n):
    
    if n == 0:
        return int(a)
    elif n == 1:
        return b
    else:
        return int(a ^ b)
 
 
 
t = int(input())
result = []
for i in range (0, t):
    a, b, n = map(int, input().split())
    res = xorinacci(n%3)
    result.append(res)
 
for i in result:
    print(i)