# -*- coding:utf-8 -*-
import math
#resolution to ax^2+bx+c=0
def quadratic(a,b,c):
	if a == 0 :
		return -c/b
	elif b**2-4*a*c < 0 :
		print ('No resolutions')
		return None
	else:
		delta = math.sqrt(b**2-4*a*c)
		if delta == 0:
			return -b/(2*a)
		else:
			return (-b+delta)/(2*a),(-b-delta)/(2*a)
print (quadratic(1,3,-4))


class screen(object):

	@property
	def width(self):
	    return self._width
	@width.setter	
	def width(self,width):
		if not isinstance(width,int):
			raise ValueError('width must be int')
		if width<0:
			raise ValueError('width must > 0')
		self._width = width

	@property
	def height(self):
	    return self._height
	@height.setter	
	def height(self,height):
		if not isinstance(height,int):
			raise ValueError('height must be int')
		if height<0:
			raise ValueError('height must > 0')
		self._height = height 

	@property
	def resolution(self):
	    return self._width*self._height

s = screen()
s.width=10
s.height=20
print(s.width)
print(s.resolution)


from enum import Enum

Month=Enum('Month',('Jan','feb','Mar'))
print([key for key,value in Month.__members__.items()])
print(Month(1))

