import random
#1
line=input("Введите выражение ")
num1=""
num2=""
for i in range(len(line)):
    if line[i].isdigit() == False:
        sym=line[i]
        index=i
        for j in range(0,index):
            num1+=line[j]
        for j in range(index+1,len(line)):
            num2+=line[j]
        if sym=="+":
            num=int(num1)+int(num2)
            print(num1+sym+num2+"="+str(num))
        elif sym=="-":
            num=int(num1)-int(num2)
            print(num1+sym+num2+"="+str(num))
        elif sym=="*":
            num=int(num1)*int(num2)
            print(num1+sym+num2+"="+str(num))
        elif sym=="/":
            num=int(num1)/int(num2)
            print(num1+sym+num2+"="+str(num))
            
#2
list=["","","","","","","","","",""]
count1=0
count2=0
count3=0
for i in range(len(list)):
    list[i]=random.randint(-10,10)
print(list)
Max=list[0]
Min=list[0]
for i in list:
    if i<0:count1+=1
    elif i>0:count2+=1
    else:count3+=1
for i in range(1,len(list)):
    Max=max(Max,list[i])
    Min=min(Min,list[i])
print("Минимальное число: ",Min)
print("Максимальное число: ",Max)
print("Кол-во отрицательных чисел: ",count1)
print("Кол-во положительных чисел: ",count2)
print("Кол-во нулей ",count3)