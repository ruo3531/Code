import random

for x in range(10):
    fin = open('{}.in'.format(x), 'w')
    fout = open('{}.out'.format(x), 'w')
    n = random.randint(2, 10)
    print(n, file=fin)
    m = random.randint(10, 10000)
    s = ''
    strm = m
    while strm > 0 :
        s += str(strm % n)
        strm //= n
    rs = s[::-1]
    print(rs, file=fout)
    w = len(str(m))
    sum = str(m)
    sum2 = 0
    for i in range(w) :
        sum2 += int(sum[i]) ** w
    if sum2 == m : print("YES")
    else : print("NO")
    fin.close()
    fout.close()