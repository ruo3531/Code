
import random

for x in range(10):
   fin = open('{}.in'.format(x), 'w')
   fout = open('{}.out'.format(x), 'w')
   n = random.randint(1, 50)
   print(n, file=fin)
   m = 101
   for i in range(n):
       r = random.randint(10, 90)
       y = random.randint(r, 120)
       print(y, file=fin)
       if y < m :
           m = y
   print(m, file=fout)
   print(m)
   fin.close()
   fout.close()
