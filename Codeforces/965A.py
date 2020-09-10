k, n, s, p = map(int, input().split())
min_pk = 0
if s > n:
    if k % p != 0:
        min_pk = int((k/p)) + 1
    else:
        min_pk = k/p
else:
    sh_rq = 0
    if n % s != 0:
        sh_rq = int((n/s)) + 1
    else:
        sh_rq = n/s
    tt_sh = sh_rq * k
    if tt_sh % p != 0:
        min_pk = int((tt_sh/p)) + 1
    else:
        min_pk = tt_sh/p
print(int(min_pk))