import random

for x in range(1):
    fin = open('{}.in'.format(x), 'w')
    fout = open('{}.out'.format(x), 'w')
    n = random.randint(3,5)
    print(n, file=fin)
    for i in range(n) :
        m = random.randint(1,999)
        print(m, file=fin)
        c = 2
        while c < m:
            if m % c == 0:
                print('No',file=fout)
                print('No',end=' ')
                break
            c += 1
        if c == m:
            print('Yes', file=fout)
            print('Yes',end=' ')
        print(m)
    fin.close()
    fout.close()
