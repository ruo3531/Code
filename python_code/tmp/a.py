num = int(input())
tmp = "012345678"
Ans = ""
while num > 0:
    print(num)
    print(tmp[num%9])
    Ans+=tmp[num%9]
    num = num//9
print(Ans[::-1])