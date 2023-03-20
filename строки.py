#1
line = input("Введите слово: ").lower()
line=line.replace(" ","") #удаляет пробел
if line==line[::-1]: #срез помогает перевернуть строку
    print("Слово палиндром")
else:print("Нет")

#2
line1=input("Введите текст: ")
c=input()
while len(c)!=0:
        line1=line1.replace(c,c.upper()) #заменяем элемент строки на наше слово с верхним регистром
        print(line1)
        c=input()



#3
line3 = input("Введите текст: ")
count=0
for i in range(len(line3)):
    if line3[i]=="." or line3[i]=="!"or line3[i]=="?" or line3[i]=="...":
        count+=1
print(count)

