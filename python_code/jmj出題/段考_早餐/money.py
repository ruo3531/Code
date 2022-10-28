
import random

for i in range(10):
   fin = open('{}.in'.format(i), 'w')
   fout = open('{}.out'.format(i), 'w')
   m = random.randint(1, 150)
   if m > 100 : s = 'Mos Burger'
   elif m>50 and m<=100 : s = 'Sally'
   elif m>30 and m<=50 : s = '7-11'
   else : s = 'Dust'
   print(m, s)
   print(m, file=fin)
   print(s, file=fout)
   fin.close()
   fout.close()
