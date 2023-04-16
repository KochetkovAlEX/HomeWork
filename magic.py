from math import pi as pi

class Circle:
    def __init__(self,R):
        self.R=R

    def __add__(self, other):
        return self.R + other

    def __sub__(self,other):
        return self.R - other

    def __iadd__(self, other):#сумма с присваиванием
        return self.R + other

    def __isub__(self, other):#вычитание с присваиванием
        return self.R - other

    def __eq__(self, other):
        return self.R == other.R

    def __lt__(self, other):
        return 2*pi*self.R < 2*pi*other.R

    def __le__(self, other):
        return 2*pi*self.R <= 2*pi*other.R

    def __gt__(self, other):
        return 2*pi*self.R > 2*pi*other.R


    def __ge__(self, other):
        return 2 * pi * self.R >= 2 * pi * other.R
# cr1=Circle(10)
# cr2=Circle(11)
# print(cr1+5)
# print(cr1<=cr2)





class Complex:

    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def show(self):
        if self.imag>0:
            print(f"{self.real}+{self.imag}i")
        else:
            print(f"{self.real}{self.imag}i")


    def __add__(self, other):
        if self.imag + other.imag>0:
            return str(self.real+other.real)+"+"+ str(self.imag + other.imag)+"i"
        else: return str(self.real+other.real)+str(self.imag + other.imag)+"i"

    def __sub__(self, other):
        if (self.imag - other.imag)>0:
            return str(self.real-other.real)+"+"+ str(self.imag - other.imag)+"i"
        else:return str(self.real-other.real)+str(self.imag - other.imag)+"i"
    def __mul__(self, other):
        if (self.imag*other.real + self.real*other.imag)<0:
            return str((self.real*other.real - int((self.imag*other.imag).real)))+ str((self.imag*other.real + self.real*other.imag))+"i"
        else: return str((self.real*other.real - int((self.imag*other.imag).real)))+"+"+str((self.imag*other.real + self.real*other.imag))+"i"

    def __truediv__(self, other):
        n1=(self.real*other.real + self.imag*other.imag)/(other.real**2 + other.imag**2)
        n2=(self.imag*other.real-self.real*other.imag)/(other.real**2 + other.imag**2)
        if n2<0:
            return str(n1) + str(n2)+"i"
        else: return str(n1)+"+"+str(n2)+"i"

# cm1=Complex(2,5)
# cm2=Complex(1,8)
# cm1.show()
# print(cm1+cm2)
# print(cm1-cm2)
# print(cm1*cm2)
# print(cm1/cm2)#самое интересное то, что это правильный ответ

class Airplane:
    def __init__(self,type,max_peoples,passenger):
        self.type=type
        self.max_peoples=max_peoples
        self.passenger=passenger

    def __sub__(self, other):
        return self.passenger-other

    def __add__(self, other):
        return self.passenger+other

    def __iadd__(self, other):
        return self.passenger + other

    def __isub__(self, other):
        return self.passenger-other

    def __eq__(self, other):
        return self.type.lower()==other.type.lower()

    def __lt__(self, other):
        return self.max_peoples<other.max_peoples

    def __le__(self, other):
        return self.max_peoples <= other.max_peoples

    def __gt__(self, other):
        return self.max_peoples > other.max_peoples

    def __ge__(self, other):
        return self.max_peoples >= other.max_peoples

# air1=Airplane("AIR",100,0)
# air2=Airplane("air",110,10)
# print(air2==air1)
# air2+=1
# print(air2)

class Flat:
    def __init__(self,s,price):
        self.price=price
        self.s=s

    def __eq__(self, other):
        return self.s==other.s

    def __ne__(self, other):
        return self.s != other.s

    def __lt__(self, other):
        return self.price<other.price


    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price
    def __ge__(self, other):
        return self.price >= other.price

# fl1=Flat(100,10)
# fl2=Flat(100,11)
# print(fl1==fl2)
# print(fl1>fl2)
# print(fl1<=fl2)