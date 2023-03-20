#1
n=int(input())
for i in range(2,n+1): #перебираем все числа от двух до n
    for j in range(2,i): #перебираем делители от 2 до n
        if i%j==0:
            break
    else: print(i, end=" ")

#2
a=1
b=1
while b<11:
    k=a
    while k<11:
        print(k,"*", b,"=", k*b, end="\t")
        k+=1
    b+=1
    print()

#3
a1=int(input())
c1=int(input())
b1=1
while b1<=10:
    k1=a1
    while k1<=c1:
        print(k1, "*", b1, "=", k1 * b1, end="\t")
        k1+=1
    b1+=1
    print()
