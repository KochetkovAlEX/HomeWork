import random
#1
basketball={"Майкл Джордан": 198,"Леброн Джеймс":206}
print(basketball)
a = input("Действие: Добавить/Удалить/Поиск/Замена/Конец ").lower()
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

dict_en_fr={"hello":"Bonjour","goodbye":"au revoir"}
print(dict_en_fr)
a = input("Действие: Добавить/Удалить/Поиск/Замена/Конец ").lower()
while a!="конец":
    if a=="добавить":
        english = input("Введите слово ")
        french = input("Введите перевод: ")
        dict_en_fr.update({english: french})
        print(dict_en_fr)
        a = input("Действие: Добавить/Удалить/Поиск/Замена ").lower()
    elif a=="удалить":
        dict_en_fr.pop(input("Что хотите удалить?: "))
        print(dict_en_fr)
        a = input("Действие: Добавить/Удалить/Поиск/Замена ").lower()
    elif a=="поиск":
        word=input().lower()
        for i in (dict_en_fr):
            if word in i.lower():
                print(i,dict_en_fr[i])
                a = input("Действие: Добавить/Удалить/Поиск/Замена ").lower()
    elif a=="замена":
        english= input("Введите слово ")
        french = input("Введите перевод: ")
        dict_en_fr.update({english:french})
        print(dict_en_fr)
        a = input("Действие: Добавить/Удалить/Поиск/Замена ").lower()
    else:
        print("Вы ввели что-то не то")
        break

#3
name1=["Язькова Вероника Александровна","Мащенко Олег Викентиевич","Иванцов Борис Пахомович"]
mail=["crittefajaudoi-7863@yopmail.com","wubutridetto-3251@yopmail.com","queupreusufreppa-1207@yopmail.com"]
nick=["Boris","Vadim","Valeriy"]
post=["Актриса","Адвокат","Окулист"]
i="+7928123"+str(random.randint(10,100))
k=random.randint(1,100)
name=name1[random.randint(0,len(name1)-1)]
j=mail[random.randint(0,len(mail)-1)]
z=nick[random.randint(0,len(nick)-1)]
v=post[random.randint(0,len(post)-1)]
company={name:[i,j,k,z,v]}
print(company)
a=input("Действие: Добавить/Удалить/Поиск/Замена/Конец ").lower()
while a!="конец":
    if a=="добавить":
        i = "+7928123" + str(random.randint(10, 100))
        k = random.randint(1, 100)
        j = mail[random.randint(0, len(mail) - 1)]
        z = nick[random.randint(0, len(nick) - 1)]
        v = post[random.randint(0, len(post) - 1)]
        name0 = input("Введите ФИО ")
        company.update({name0:[i,j,k,z,v] })
        print(company)
        a = input("Действие: Добавить/Удалить/Поиск/Замена/Конец ").lower()
    elif a=="удалить":
        company.pop(input("Кого хотите удалить?: "))
        print(company)
        a = input("Действие: Добавить/Удалить/Поиск/Замена/Конец ").lower()
    elif a=="поиск":
        word=input().lower()
        for g in (company):
            if word in g.lower():
                print(g,company[g])
                a = input("Действие: Добавить/Удалить/Поиск/Замена/Конец ").lower()
    elif a=="замена":
        i = "+7928123" + str(random.randint(10, 100))
        k = random.randint(1, 100)
        j = mail[random.randint(0, len(mail) - 1)]
        z = nick[random.randint(0, len(nick) - 1)]
        v = post[random.randint(0, len(post) - 1)]
        name0 = input("Введите ФИО ")
        company.update({name0: [i, j, k, z, v]})
        print(company)
        a = input("Действие: Добавить/Удалить/Поиск/Замена/Конец ").lower()
    else:
        print("Вы ввели что-то не то")
        break

#4
num=random.randint(100,10000)
autor="Чак Паланик"
book="Бойцовский клуб"
year=2023
page=256
publish="ACT"
library={num:[autor,book,page,publish,year]}
print(library)
a=input("Действие: Добавить/Удалить/Поиск/Замена/Конец ").lower()
while a!="конец":
    if a=="добавить":
        num=random.randint(100,10000)
        autor = input("Введите автора: ")
        book =input("Введите название книги: ")
        year=int(input("Введите год выпуска: "))
        page =int(input("Введите количество страниц: "))
        publish = input("Введите название издательства: ")
        library.update({num:[autor,book,page,publish,year]})
        print(library)
        a = input("Действие: Добавить/Удалить/Поиск/Замена/Конец ").lower()
    elif a=="удалить":
        library.pop(int(input("Введите номер удаляемой книги: ")))
        print(library)
        a = input("Действие: Добавить/Удалить/Поиск/Замена/Конец ").lower()
    elif a=="поиск":
        key=int(input("Введите номер книги: "))
        for g in (library):
            if key in g:
                print(g,library[g])
                a = input("Действие: Добавить/Удалить/Поиск/Замена/Конец ").lower()
            else:
                print("Ничего не обнаружено")
                a = input("Действие: Добавить/Удалить/Поиск/Замена/Конец ").lower()
    elif a=="заменить":
        num = int(input("введите номер изменяемой книги: "))
        autor = input("Введите автора: ")
        book = input("Введите название книги: ")
        year = int(input("Введите год выпуска: "))
        page = int(input("Введите количество страниц: "))
        publish = input("Введите название издательства: ")
        library.update({num: [autor, book, page, publish, year]})
        print(library)
        a = input("Действие: Добавить/Удалить/Поиск/Замена/Конец ").lower()
    else:
        print("Вы ввели что-то не то")
        break