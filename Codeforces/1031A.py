w, h, k = map(int, input().split())
tot = 0
for i in range(0, k):
    tot += 2*(w+h) - 4
    w = w - 4
    h = h - 4

print(tot)