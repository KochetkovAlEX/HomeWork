list=[2,3,4,5,6,7]
def f(list):
    c=1
    for i in range(len(list)):
        c=list[i]*c
    return c
print(f(list))

def min_list(list):
    return min(list)
print(min_list(list))


list1=[5,6,7,8,11]
def simpl_list(list1):
    count=0
    for i in (list1):
        flag=True
        for j in range(2,int((i**0.5))+2):
            if i%j==0:
                flag=False
                break
        if flag:
            count+=1
    return count
print(simpl_list(list1))

list3=[1, 2, 2, 3, 4, 2]
def remove_list(a,list3):
    count=0
    while a in list3:
        list3.remove(a)
        count+=1
    return count
print(remove_list(2,list3))

list4=[1,2,3]
list5=[4,5,6]
def copy_list(list4,list5):
    m=[]
    for i in list4:
        m.append(i)
    for i in list5:
        m.append(i)
    return m
print(copy_list(list4,list5))

list6=[1,2,-3,5]
def power_list(power,list6):
    plist=[]
    for i in list6:
        plist.append(i**power)
    return plist
print(power_list(2,list6))