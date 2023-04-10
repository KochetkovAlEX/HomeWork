class Device():
    def __init__(self,name):
        self.name=name
    def do_smth(self):
        print(f'{self.name} делает что-то')

class CoffeMachine(Device):
    def __init__(self,name):
        super().__init__(name)
    def do_coffe(self):
        print(f'{self.name} кофеварит')

class Blender(Device):
    def __init__(self,name):
        super().__init__(name)
    def mix(self):
        print(f'{self.name} миксерит')

class MeatGrinder(Device):
    def __init__(self,name):
        super().__init__(name)
    def grind(self):
        print(f'{self.name} мясорубит')
#
#
# tv=Device("TV")
# tv.do_smth()
# cf=CoffeMachine("кофей")
# cf.do_coffe()
# mx=Blender("бледа")
# mx.mix()
# gr=MeatGrinder("брбрбр")
# gr.grind()


class Ship:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def swim(self):
        print(f'{self.name} плывет')

    def attack(self):
        print(f'{self.name} атакует')

    def show_info(self):
        print(f"{self.name}|{self.weight}")
class Frigate(Ship):
    def __init__(self, name, weight,machinegun):
        super().__init__(name,weight)
        self.machinegun=machinegun

    def follow(self):
        print(f'{self.name} сопровождает судно')

    def show_info(self):
        print(f"{self.name}|{self.weight}|{self.machinegun}")

class Destroyer(Ship):
    def __init__(self, name, weight,machinegun,rocket_launcher):
        super().__init__(name,weight)
        self.machinegun=machinegun
        self.rocket_launcher=rocket_launcher

    def do_war(self):
        print(f'{self.name} воюет с помощью {self.machinegun} и {self.rocket_launcher}')

    def show_info(self):
        print(f"{self.name}|{self.weight}|{self.machinegun}|{self.rocket_launcher}")

class Cruiser(Ship):
    def __init__(self, name, weight,machinegun,rocket_launcher):
        super().__init__(name,weight)
        self.machinegun = machinegun
        self.rocket_launcher = rocket_launcher

    def show_info(self):
        print(f"{self.name}|{self.weight}|{self.machinegun}|{self.rocket_launcher}")

    def scare(self):
        print(f"{self.weight} кг... да, {self.name} огромен")

# sp1=Ship("Катер",20)
# sp1.swim()
# cr1=Cruiser("Бостон",136*10**5,"12 пулеметов 127мм","ЗРК 'Терьер'")
# cr1.swim()
# cr1.attack()
# cr1.scare()

class Money:
    def __init__(self,full,cent):
        self.full=full
        self.cent=cent
        if self.cent>99:
            self.full+=self.cent//100
    def show_info(self):
        print(f"{self.full},{self.cent}")
    def __add__(self, other):
        cent1 = self.full * 100 + self.cent
        cent2 = other.full * 100 + other.cent
        cent3 = cent1 + cent2
        return Money(cent3//100,cent3%100)

    def __sub__(self, other):
        cent1 = self.full * 100 + self.cent
        cent2 = other.full * 100 + other.cent
        cent3 = cent1 - cent2
        return Money(cent3 // 100, cent3 % 100)

# mn1=Money(1,3)
# mn2=Money(1,1)
# mn1.show_info()
# mn2.show_info()
# mn3=(mn1+mn2)
# mn3.show_info()
# mn1.show_info()
# mn2.show_info()
# mn4=mn1-mn2
# mn4.show_info()
