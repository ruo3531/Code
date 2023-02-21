import random

for x in range(10):
    fin = open('{}.in'.format(x), 'w')
    fout = open('{}.out'.format(x), 'w')
    n = random.randint(2, 201)
    print(n, file=fin)
    str1 = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(n):
        m = random.randint(2, 50)
        ans = ""
        for j in range(m):
            ans+= random.choice(str1)
        print(ans, file=fin)
    fin.close()
    fout.close()