class Array():
	__count = 0
	#вывод и создание
	def __init__(self,size):
		self.size=size
		self.list=["" for i in range(self.size)]
	def show(self):
		for i in range(self.__count):
			if i!=self.__count-1:
				print(self.list[i],end=" | ")
			else:print(self.list[i],end=" ")
		print()
	def print(self):
		print(self.list)
	def show_size(self):
		print(self.__count)

	#добавление
	def start_push(self, num):
		if self.__count==self.size:
			raise IndexError("Элементы в списке закончились")
		else:
			self.list.insert(0,num)
			self.list.pop(self.size)
			self.__count+=1

	def back_push(self, num):
		if self.__count==self.size:
				raise IndexError("Элементы в списке закончились")
		else:
			self.list[self.__count]=num
			self.__count+=1


	def index_push(self,num,index):
		if self.__count==self.size:
				raise IndexError("Элементы в списке закончились")
		else:
			for i in range(len(self.list)):
				if i==index and self.list[i]=="":
					self.list[index]=num
					self.__count+=1
					break
				if  i==index and self.list[i]!="":
					raise Exception("Данная позиция занята")

	#удаление
	def back_pop(self):
		if self.__count==0: raise IndexError("Список пуст")
		else:self.__count-=1


	def start_pop(self):
		if self.__count==0: raise Exception("Список пуст")
		for i in range(len(self.list)-1):
			self.list[i]=self.list[i+1]
		self.__count-=1

	def index_pop(self,index):
		if self.__count==0: raise IndexError("Список пуст")
		elif index<self.size:
			self.list=self.list[0:index]+self.list[index+1:]
			self.__count -= 1
		else:
			raise Exception("Введите корректный индекс")


if __name__=="__main__":
	lst1=Array(4)
	try:
		lst1.start_push(1)
		lst1.start_push(2)
		lst1.back_push(3)
		lst1.back_push(4)
		lst1.print()
		lst1.start_pop()
		lst1.show()
		lst1.show_size()
	except Exception as er:
		print(er)
