#1
basketball={"Майкл Джордан": 198,"Леброн Джеймс":206}
print(basketball)
a=input("Действие: Добавить/Удалить/Поиск/Замена ").lower()
while a!="конец":
    if a=="добавить":
        name=input("Введите имя и фамилию: ")
        heiqht=int(input("Введите рост: "))
        basketball.update({name:heiqht})
        print(basketball)
        a = input("Действие: Добавить/Удалить/Поиск/Замена ").lower()
    elif a=="удалить":
        basketball.pop(input("Кого хотите удалить?: "))
        print(basketball)
    elif a=="поиск":
        word=input().lower()
        for i in (basketball):
            if word in i.lower():
                print(i,basketball[i])
                a = input("Действие: Добавить/Удалить/Поиск/Замена ").lower()
    elif a=="замена":
        name = input("Введите имя и фамилию: ")
        heiqht = int(input("Введите рост: "))
        basketball.update({name:heiqht})
        print(basketball)
        a = input("Действие: Добавить/Удалить/Поиск/Замена ").lower()
    else:
        print("Вы ввели что-то не то")
        break
#2