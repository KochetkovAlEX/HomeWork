#1
a=int(input())
b=int(input())
if a>b: a,b=b,a
while a<=b:
    if a%7==0:
        print(a)
        a += 1
    else: a+=1

#2
a1=int(input())
b1=int(input())
z=input()
count=0
if a1>b1: a1,b1=b1,a1
if z=="range":
    while a1<=b1:
        print(a1, end=" ")
        a1+=1
elif z=="reverse":
    while b1>=a1:
        print(b1,end=" ")
        b1-=1
elif z=="//7":
    while a1<=b1:
        if a1%7==0:
            print(a1, end=" ")
        a1+=1
elif z=="//5":
    while a1<=b1:
        if a1%5==0:
            count+=1
        a1+=1
    print(count)

#3
a2=int(input())
b2=int(input())
if a2>b2: a2,b2=b2,a2
while a2<=b2:
    if a2%3==0 and a2%5==0:
        print("Fizz Buzz")
    elif a2%5==0:
        print("Buzz")
    elif a2%3==0:
        print("Fizz")
    elif a2%5!=0 and a2%3!=0:
        print(a2)
    a2+=1