import random
print("|а - два списка вместе",end="")
print("|б - общие элементы без повторов",end="")
print("|в - общие элементы двух списков",end="")
print("|г - уникальные значения",end="")
print("|д - Max/Min|")
a=input("Выберите операцию со списками: ").lower()
size=int(input("Введите размер списка: "))
list=[]
list1=[]
list2=[]
for i in range(size):
    list.append(random.randint(0,9))
    list1.append(random.randint(0,9))
print(list)
print(list1)
Max1=list[0]
Max2=list1[0]
Min1=list[0]
Min2=list1[0]
#список со значениями двух других
if a=="а":
    for i in list:
        list2.append(i)
    for i in list1:
        list2.append(i)
    print(list2)
#Без повторений
elif  a=="б":
    for i in list:
        if i in list1:
            list2.append(i)
    print(list2)
#общие элеиенты
elif a == "в":
    for i in list:
        for j in list1:
            if i==j:
                list2.append(j)
    print(list2)
#Уникальные значения
elif a == "г":
    for i in list:
        if i not in list1:
            list2.append(i)
    for j in list1:
        if j not in list:
            list2.append(j)
    print(list2)
#Минимум и максимум
elif a == "д":
    for i in range(len(list)):
        Max1=max(Max1,list[i])
    for i in range(len(list1)):
        Max2=max(Max2,list1[i])
    list3=[Max1,Max2]
    list2.append(list3)
    for i in range(len(list)):
        Min1=min(Min1,list[i])
    for i in range(len(list1)):
        Min2=min(Min2,list1[i])
    list3=[Min1,Min2]
    list2.append(list3)
    Min1=min(Min1,Min2)
    Max1=max(Max1,Max2)
    list2.append(Max1)
    list2.append(Min1)
    print(list2)
else: print("Вы ввели что-то странное")