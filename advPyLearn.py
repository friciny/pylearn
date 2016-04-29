from PIL import Image
im = Image.open('y.png')
print (im.format,im.size,im.mode)

im.thumbnail((200,100))
im.save('thmb.jpg','JPEG')


#return a function that can be called after,if wanna call imediate append a () like in line18
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum
print(lazy_sum(1,3,4,5,7))
print(lazy_sum(1,3,4,5,7)())
f=lazy_sum(1,3,4,5,7)
print (f())


class Student(object):

	def __init__(self,name,score=0):
		self.name = name
		self.score = score

	def print_score(self):
		print ("%s:%s" % (self.name,self.score))

std1=Student('Tencent',80)
std2=Student('Huawei')
std1.print_score()
std2.print_score()
std2.score = 10
std2.print_score()


class Student2(object):

	def __init__(self,name,score=0):
		self.__name = name
		self.__score = score

	def set_score(self,score):
		self.__score = score

	def set_name(self,name):
		self.__name = name

	def printSelf(self):
		print ("%s:%s" % (self.__name,self.__score))

std1=Student2('Tencent',80)
std2=Student2('Huawei')
std1.printSelf()
std2.printSelf()
std2.__score = 10
print ('std2.__score:',std2.__score)
std2.printSelf() #we cant modify attributes named __attiname
#print (std2.__name)


class Pupil(Student2):

	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	#def set_score(self,score):
	#	self.__score = score

	#def print_score(self):
	#	print("%s,%s"%(self.__name,self.__score))

pup = Pupil("BaiDu",89)
#pup.printSelf()#calling _Student2__printSelf(_student2)
print(dir(pup))#before calling set_score&set_name ,pup has no attribute of _Student__score&_Student__name 
pup.set_score(30)
pup.set_name("Ali")
pup.printSelf()
print(dir(pup))#after calling set_score&set_name, pup has attributes of _Student__score&_Student__name

