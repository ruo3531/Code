t = ""
while True:
    try:
        s = input()
        t+=s
    except EOFError:
        break

ns = [u.strip() for u in t.split("()")]
ns.pop(-1)

for p in ns:
    if p=="":
        print("not complete")
        continue

    n = [u for u in p[1:-1:].split(') (')]
    lst = []
    d = {}
    LR = []
    f = 1
    for i in n:
        lst.append(tuple(u for u in i.split(',')))
        if lst[-1][0] == "":
            print("not complete")
            f=0
            break
        LR.append(lst[-1][1])

        tmp = 1
        for j in lst[-1][1]:
            if j == "L":
                tmp*=2
            else:
                tmp = tmp*2+1
        d[tmp] = lst[-1][0]
        #print("j", j, "lst",lst[-1][0])
    # print(LR)
    if f == 0:
        continue
    if "" not in LR:
        print("not complete")
    else:                                                                                                                                      
        for i in LR:
            if i != "" and i[0:-1] not in LR or LR.count(i) != 1:
                print("not complete")
                break
        else:
            flag = 1
            for i in sorted(d.keys()):
                if flag == 0:
                    print(" ",end="")
                print(d[i], end="")
                flag = 0
            print()
