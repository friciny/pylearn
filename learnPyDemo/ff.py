def fablacci(max):
	n,a,b = 0,1,0
	while n<max:
		yield a
		a,b=a+b,a
		n=n+1
print ([i for i in fablacci(10)])


def myabs(i,fun):
	return fun(i)
f=abs
print (myabs(-10,f))

from functools import reduce
def fablacciSum(max):
	def f(x,y):
		return x+y
	l=[i for i in fablacci(max)]
	print (l)
	return reduce(f,l),sum(l)
print (fablacciSum(10))


def fablacciMuti(max):
	return reduce(lambda x,y:x*y,[i for i in fablacci(max)])
print (fablacciMuti(10))


def corName(namelist):
	def f(name):
		return name[0].upper()+name[1:].lower()
	return list(map(f,[name for name in namelist]))
print (corName(["JKA","fHS","GirL","H"]))


def corName2(namelist):
	return list(map(lambda name:name[0].upper()+name[1:].lower(),[name for name in namelist]))
print (corName2(["JKA","fHS","GirL","H"]))

#return a list of sushu in 0~max
def SuSu(max):
	if max<2:
		return []
	else:
		def issu(ii):
			for i in range(2,(ii//2+1)):
				if ii%i == 0:
					return False
			return True
		return list(filter(lambda i:issu(i),[i for i in range(2,max+1)]))
print (SuSu(100))

#define sort key function to sort a name list
def mysort(list):
	def ignoreCase(a):
		return a[0].upper()
	return sorted(list,key=ignoreCase) 		
print (mysort(["Teng","ali","BaiDu","hua","Wei"]))