#stringIO
from io import StringIO
ss=StringIO('Hello!\nHi!\nGoodBye!\n')
while True:
	s=ss.readline()
	if s=='':
		break
	else:
		print(s.strip())

#systemIO & file IO
import os

print(os.path.abspath('.'))
print([x for x in os.listdir('.') if os.path.isdir(x)])
#print(os.mkdir(os.path.join(os.path.abspath('.'),'newdir')))

#read the files with a exten '.py' in a path
fi=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(fi)
with open(fi[0],'r') as sf:
	print('---------------\n%s'%(sf.read(100).strip()))
	print('%s\n---------------'% sf.readline().strip())


#find files with key in filename from a path and all of its dirs
def findbykey(key,resultfile,findpath,thepath):
	for files in os.listdir(findpath):
		filename = os.path.join(findpath,files)
		filepath = os.path.join(thepath,files)
		if os.path.isfile(filename) and key in files:
			resultfile.append(filepath)		
		elif os.path.isdir(filename):
			findbykey(key,resultfile,filename,filepath)
	return resultfile

def findfilebykey(key,findpath='.'):
	L=list()
	thepath = '\\'
	return findbykey(key,L,findpath,thepath)

print(findfilebykey('fricin','E:\\fricin\\workspace\\Leetcoding'))
print(findfilebykey('test'))