s1 = input()
s2 = input()

s1 = s1.lower()
s2 = s2.lower()

if s1 == s2:
    print(0)
elif s1 < s2:
    print(-1)
elif s2 < s1:
    print(1)