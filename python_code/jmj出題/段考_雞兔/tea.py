
import random

for i in range(10):
   fin = open('{}.in'.format(i), 'w')
   fout = open('{}.out'.format(i), 'w')
   r = random.randint(1, 1000)
   m = random.randint(1, 1000)
   sum =r*15+m*20
   n=r+m
   print(r, m, n, sum)
   print(n, sum, sep='\n', file=fin)
   print( r, m, file=fout)
   fin.close()
   fout.close()
