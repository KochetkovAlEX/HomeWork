#1
a=int(input())
b=int(input())
c=int(input())
z=input()
mult=(a*b*c)
sr=((a+b+c)/3)
if z=="mult":
    print(mult)
elif z=="sr":
    print(sr)
else:
    print(0)


#2
a1=int(input())
b1=int(input())
c1=int(input())
z1=input()
if z1=="max":
    if a1>b1 and a1>c1:
        print(a1)
    elif b1>a1 and b1>c1:
        print(b1)
    else:
        print(c1)
elif z1=="min":
    if a1<b1 and a1<c1:
        print(a1)
    elif b1<a1 and b1<c1:
        print(b1)
    else:
        print(c1)
elif z1=="sr1":
    print((a1+b1+c1)/3)
else:
    print(0)


#3
a2=int(input())
z2=input()
if z2=="mile":
    print(a2*(0.000621371))
elif z2=="yard":
    print(a2*(1.09361))
elif z2=="inch":
    print(a2*(39.3701))
else: print(0)