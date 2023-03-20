import random
def gen(size,Min,Max):
    list=[]
    if Min>Max: Min,Max=Max,Min
    for i in range(size):
        list.append(random.randint(Min,Max))
    return list
list=gen(100,1,100)
print(list)

def summ(list):
    count=0
    summ = sum(list[0:10])
    for i in range(1,92):
        summ2=sum(list[i:(i+10)])
        print(summ,summ2,i)
        if summ>summ2:
            summ=min(summ,summ2)
            count=i
    return count
print(summ(list))