import random

for x in range(10):
   fin = open('{}.in'.format(x), 'w')
   fout = open('{}.out'.format(x), 'w')
   y = random.randint(1900, 2020)
   m = random.randint(1, 12)
   d = random.randint(1, 31)
   s = str(y)+str(m)+str(d)
   l = len(s)
   print(s, file=fin)
   s = int(s)
   while s>=10:
       sum = 0
       for i in range(l):
        sum+=s%10
        s//=10
       s = sum
   print(s, y, m, d)
   print(s, file=fout)
   fin.close()
   fout.close()
