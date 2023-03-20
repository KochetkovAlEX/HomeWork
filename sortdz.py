list=[1,33,54,7,123,5,1321,222,334,321]
Len=len(str(max(list)))
raz=8
flag=False
for i in range(Len):
    print(list)
    list2=[[] for x in range(raz)]
    for j in list:
        num=j//10**i %10
        list2[num].append(j)
        flag=True
    list.clear()
    for j in range(raz):
        list+= list2[j]
        flag=True
    if flag:
        print(list)