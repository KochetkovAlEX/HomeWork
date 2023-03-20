import random
c=input("Хотите сыграть в игру? ").lower()
win=0
lose=0
game=0
if c=="да" or c=="yes":
    count=7
    a = random.randint(1, 9)
    while c=="да" or c=="yes":
        if count>0:
            b=int(input("Введите число: "))
            if b==0:
                print("Конец игры")
                print("Победы: " + str(win))
                print("Поражения: " + str(lose))
                print("Всего игр: " + str(game))
                c = input("Повторим? ")
                if c == "да" or c == "yes":
                    a = random.randint(1, 9)
                    count = 7
                elif c == "нет" or c == "no":
                    print("Как хотите")
                    break
            elif a>b:
                print("Моё число больше вашего")
                count-=1
            elif a<b:
                print("Моё число меньше вашего")
                count -= 1
            elif a==b:
                print("Это моё число. Вы молодец!")
                win+=1
                game+=1
                c=input("Повторим? ")
                if c=="да" or c=="yes":
                    a=random.randint(1, 9)
                    count=7
                elif c=="нет"  or c=="no":
                    print("Как хотите")
                    print("Победы: " + str(win))
                    print("Поражения: " + str(lose))
                    print("Всего игр: " + str(game))
        else:
            print("Попытки закончились")
            lose+=1
            game+=1
            c = input("Повторим? ")
            if c=="да" or c=="yes":
                a = random.randint(1, 9)
                count=7
            elif c == "нет" or c=="no":
                print("Как хотите")
                print("Победы: " + str(win))
                print("Поражения: " + str(lose))
                print("Всего игр: " + str(game))
elif c=="no" or c=='нет':
    print("Жаль")
else: print('Что? Либо "Да", либо "Нет"' )
