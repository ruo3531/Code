
import random

for i in range(10):
   fin = open('{}.in'.format(i), 'w')
   fout = open('{}.out'.format(i), 'w')
   h = random.randint(6, 12)
   m = random.randint(00, 59)
   T=h*60+m
   t = random.randint(1,150)
   T-=t
   H=T//60
   M=T%60
   print(h, m, t)
   print(H, M)
   print(h, m, t, sep='\n', file=fin)
   print(H, M, file=fout)
   fin.close()
   fout.close()
