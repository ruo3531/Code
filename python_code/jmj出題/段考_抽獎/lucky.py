
import random

for x in range(10):
   fin = open('{}.in'.format(x), 'w')
   fout = open('{}.out'.format(x), 'w')
   n = random.randint(5, 10)
   arr = [random.randint(1, 100) for i in range(n)]
   f = random.choice(arr)
   print(arr)
   fin.close()
   fout.close()
