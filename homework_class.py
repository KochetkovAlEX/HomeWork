import random
class Car():
    def __init__(self,model,year,engine,creator,color,price):
        self.__model=model
        self.__year=year
        self.__engine=engine
        self.__creator=creator
        self.__color=color
        self.__price=price

    def getModel(self):
        print(self.__model)
    def getYear(self):
        print(self.__year)
    def getEngine(self):
        print(self.__engine)
    def getColor(self):
        print(self.__color)
    def getCreator(self):
        print(self.__creator)
    def getPrice(self):
        print(self.__price)

    def show_info(self):
        print(f"{self.__model}|{self.__color}|{self.__year}|{self.__engine}|{self.__creator}|{self.__price}")

    def change_model(self,model_new):
        self.__model = model_new
    def change_color(self,color_new):
        self.__color = color_new
    def change_year(self,year_new):
        self.__year = year_new
    def change_engine(self,engine_new): #это тюнинг?
        self.__engine = engine_new
    def change_creator(self,creator_new): #а вот это уже странно
        self.__creator = creator_new
    def change_price(self,price_new): #перекупы надоели
        self.__price = price_new

car1=Car("Lada 10",2000,"V2","Дядя Валера","White","15000")
car1.show_info()
car1.change_color("Black")
car1.show_info()
car1.getModel()


class Book():
    def __init__(self,name,year,publisher,genre,author,cost): #genre-жанр(ого) cost==price(не повторяемся)
        self.__name=name
        self.__year = year
        self.__publisher = publisher
        self.__author= author
        self.__genre=genre
        self.__cost = cost

    def getName(self):
        print(self.__name)
    def getYear(self):
        print(self.__year)
    def getPublisher(self):
        print(self.__publisher)
    def getGenre(self):
        print(self.__genre)
    def getAuthor(self):
        print(self.__author)
    def getCost(self):
        print(self.__cost)

    def show_info(self):
        print(f"{self.__name}|{self.__genre}|{self.__author}|{self.__year}|{self.__publisher}|{self.__cost}")
    def change_name(self,name_new):
        self.__name = name_new
    def change_genre(self,genre_new):
        self.__genre=genre_new
    def change_author(self,author_new):
        self.__author=author_new
    def change_year(self,year_new):
        self.__year=year_new
    def change_publisher(self,publisher_new):
        self.__publisher=publisher_new
    def change_cost(self,cost_new):
        self.__cost=cost_new


book1=Book("Хроники хищных городов",2001,"ACT","Фантастика","Филип Рив",2000)
book1.show_info()
book1.change_publisher("Азбука")
book1.show_info()
book1.getName()
book1.getCost()
book1.getCost()

class Stadiun():
    def __init__(self,name,year,city,country,capacity): #genre-жанр(ого) cost==price(не повторяемся)
        self.__name=name
        self.__year = year
        self.__city=city
        self.__country=country
        self.__capacity=capacity

    def getName(self):
        print(self.__name)
    def getYear(self):
        print(self.__year)
    def getCIty(self):
        print(self.__city)
    def getCountry(self):
        print(self.__country)
    def getCapacity(self):
        print(self.__capacity)

    def show_info(self):
        print(f"{self.__name}|{self.__year}|{self.__city}|{self.__country}|{self.__capacity}")
    def change_name(self,name_new):
        self.__name = name_new
    def change_genre(self,city_new):
        self.__city=city_new
    def change_author(self,country_new):
        self.__country=country_new
    def change_year(self,year_new):
        self.__year=year_new
    def change_publisher(self,capacity_new):
        self.__capacity=capacity_new



st1=Stadiun("Олимп",1980,"Moscow","Russian",20000)
st1.show_info()
st1.change_year(1930)
st1.show_info()

