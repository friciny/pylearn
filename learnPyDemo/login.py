# coding:utf-8

import hashlib
from collections import defaultdict

db=defaultdict(lambda:'N/A')

def  register():
	usrname = input('pls input username')
	passwd = input('pls input password')
	db[usrname]=getmd5(usrname+passwd+'the salt')
	print('Register successe!')

def login():
	usrname = input('pls input username')
	passwd = input('pls input password')
	if db[usrname]==getmd5(usrname+passwd+'the salt'):
		print('login successe!')
		return True
	else:
		print('login failed')
		return False

def getmd5(s):
	md5=hashlib.md5()
	md5.update(s.encode('utf-8'))
	return md5.hexdigest()

def main():
	print('Register...')
	register()
	print('login...')
	b=login()
	while not b:
		b=login()

if __name__=='__main__':
	main()
