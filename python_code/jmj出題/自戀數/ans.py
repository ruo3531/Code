n, m = map(int, input().split())
w = len(str(m))
sum = str(m)
msum = 0
for i in range(w) :
    msum += (int(sum[w-i-1])-int('0')) * (n ** i)
sum2 = 0
for i in range(w) :
    sum2 += int(sum[i]) ** w
if sum2 == msum : print("YES")
else : print("NO")
