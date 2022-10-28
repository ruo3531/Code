import random

for x in range(10):
   fin = open('{}.in'.format(x), 'w')
   fout = open('{}.out'.format(x), 'w')
   n = random.randint(1, 1000000000)
   print(n, file=fin)
   N = n
   x = len(str(n))
   sum = 0
   for i in range(x):
       sum+=n%10
       n//=10
   print(sum, N)
   print(sum, file=fout)
   fin.close()
   fout.close()
