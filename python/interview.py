#1.python参数传递是值传递还是引用传递
#2.lambda更简单，省去命名函数名的麻烦
f = lambda x,y:x+y
print(f(1, 2))

#3.format可以接受参数不限个数，并且位置可以不按顺序
print("{1}{0}".format("good", 123))
print("{name}-{age}".format(age=14, name="lius"))

#4.


#5.反转
def reverse(text="abc"):
	return text[::-1]
print(reverse("12345"))

#6.按升序合并下面两个list，并去除重复元素
list1 = [2,3,5,2,1]
list2 = [1,3,2,4,6,3,4]
list3 = list1 + list2
print(set(list3))

#7.
ll = [1,2,3,4,5,6,7]
print(ll[10:])    #输出[]


#8.
keys = ["Name", "Sex", "Age"]
values = ["Jack", "Male", 19]
print(dict(zip(keys, values)))

#9.
def extend(val, ll=[]):
	ll.append(val)
	return ll
l1 = extend(1)            #[1, 3]
l2 = extend(123, [])      #[123]
l3 = extend(3)            #[1, 3]
l4 = extend(456, [])      #[456]
print(l1, l2, l3, l4)

#10.什么是GIL

#11.python3取消iteritems

#12.
try:
	with open("text.txt") as f:
		while True:
			line = f.readline()
			if not line:
				break
			print(line)
except FileNotFoundError:
	print("No text.txt")
#with语句使用上下文管理器对代码块进行包装，允许上下文管理器实现一些设置和清理操作



#13.生成斐波那契数列
def fibs(x):
	result = [0, 1]
	for i in range(x-2):
		result.append(result[-2] + result[-1])
	return result

print(fibs(0))  #[0,1]


#14.反序的迭代一个序列
x = [1,2,3,4,5]
for i in range(len(x)-1, -1, -1):
	k = x[i]


#15.
L1 = [1,2,3,1,2,3,4,5]
L2 = []
[L2.append(i) for i in L1 if i not in L2]
print(L2)

#16.python拷贝


#17
import os 
#os.remove(filename)


#18.得到list的交集，差集
l1 = [1,2,3,4,6]
l2 = [3,4,5,1,2]
l3 = [i for i in l1 if i not in l2]
l4 = [i for i in l1 if i in l2]
print(l3, l4)

#19
w = "Python is a very funny language"
w.find("Python")
w.find("is")
w.find("world")
w.replace("Python", "Ruby")

#20.
words = ["This", "is", "a", "dog"]
words.sort(key=lambda x:x.lower())
print(words)

#21.
lists = ["xyz", "abc", "opq"]
lists.sort(key=lambda x:x[1], reverse=True)
print(lists)

#22.解析argv
import sys
for arg in sys.argv[1:]:
	print(arg)

#23装饰器

#24.
class Array:
	__list = []

	def __init__(self):
		print("constructor")

	def __del__(self):
		print("destructor")

	def __str__(self):
		return "this self-defined array class"

	def __getitem__(self, key):
		return self.__list[key]

	def __len__(self):
		return len(self.__list)

	def Add(self, value):
		self.__list.append(value)

	def Remove(self, index):
		del self.__list[index]

	def DisplayItems(self):
		for item in self.__list:
			print(item)

a = Array()
a.Add(1)
a.Add(3)
a.DisplayItems()
print(len(a))
print(a)
a.Remove(1)
a.DisplayItems()


#25.单例
#杰瑞的专栏
#

#26.stack
class Stack:
	def __init__(self):
		self._items = list()

	def isEmpty(self):
		return len(self) == 0

	def __len__(self):
		return len(self._items)

	def peek(self):
		assert not self.isEmpty()
		return self._items[-1]

	def pop(self):
		assert not self.isEmpty()
		return self._items.pop()

	def push(self, item):
		self._items.append(item)

#27.
#迭代器，yield
#标准库线程安全的队列是哪一个，不安全是哪一个？logging是线程安全的吗？
#python高并发解决方案
#epoll，select区别，边缘触发，水平触发区别
#tcp/udp区别，tcp粘包，如何处理
#time_wait是什么情况，出现过多的close_wait原因
#mysql字符集，排序规则
#varchar/char区别，大小限制，utf8字符集下varchar最多能存多少字符
#外键有什么用，外键一定需要索引吗
#myisam和innodb区别，innodb的两阶段锁定协议是什么情况
#索引有什么用，大致原理是？
#什么场景用redis？为什么mysql不适合
#redis事务？
#redis内存满了怎么办
#
#sql注入怎么产生的，如何避免
#xss如何预防
#csrf是什么
#https过程
#
#
#28.函数式编程
#coopy/deepcopy
#with作用，原理
#property
#新式类和旧式类区别
#python变量解析作用域
#assert True则继续执行
#__new__和__init__区别
#
#
#29.
list = [[]] * 5
list[0].append(19)
list[1].append(29)
list.append(39)

#30.
def multipliers():
	return [lambda x:i*x for i in range(4)]

print([m(2) for m in multipliers()])

#31.
#如何设计deepcopy
#设计模式
#编码/解码
#列表推导和生成器优劣
#在函数之后进行装饰？
#正则匹配邮箱
#垃圾回收：引用计数、分代回收、孤立引用环
#range、xrange
#socket长连接
#http一次链接的全过程
#get post区别
#restful
#mysql锁种类，死锁如何产生的
#char，varchar，text区别
#join种类
#索引类型，BTree和hash索引区别
#session，cookie区别，为什么说session是安全的
#uwsgi，ngix作用
#python用递归判断字符串是否是回文
#快排，堆排，几种常用排序算法复杂度是，快排平均复杂度，快排平均复杂度
#一个列表A=[A1,A2,A3...An] 列出所有组合情况
#用一行python写出1+2+3+...10**8
#单向链表长度未知，如何判断是否回环
#单项链表如何使用快速排序算法排序
#一个长度n的无序数字元素列表，如何求中位数
#
#32.猴子补丁
#在函数活对象定义之后再去改变他们的行为
#@staticmethod,@classmethod区别
#
#
##33
class myClass(object):
	def __init__(self):
		self._some_property = "some property"
		self._some_another_property = "some another property"

	def normal_method(*args, **kwargs):
		print("calling normal method{0},{1}".format(args, kwargs))

	@classmethod
	def class_method(*args, **kwargs):
		print("calling class method{0},{1}".format(args, kwargs))

	@staticmethod
	def static_method(*args, **kwargs):
		print("calling static method{0},{1}".format(args, kwargs))

	@property
	def some_property(self, *args, **kwargs):
		print("calling some property getter{0},{1},{2}".format(self, args, kwargs))
		return self._some_property

	@some_property.setter
	def some_property(self, *args, **kwargs):
		print("calling some_property setter{0},{1},{2}".format(self, args, kwargs))
		self._some_property = args[0]

	@property
	def some_another_property(self, *args, **kwargs):
		print("calling some another property getter{0},{1},{2}".format(self, args, kwargs))
		return self._some_another_property


o = myClass()
print(o.normal_method)
o.normal_method()
print(o.class_method)
o.class_method()
print(o.static_method)
o.static_method()
o.some_property
o.some_another_property
o.some_property = [1,2,3]
print(o.some_property)

#34
def print_content_name(path):
	import os
	for sChild in os.listdir(path):
		sChildPath = os.path.join(path, sChild)
		if os.path.isdir(sChildPath):
			print_content_name(sChildPath)
		else:
			print(sChildPath)

#35
from functools import reduce
reduce(lambda x,y:x+y, [1,2,3])

#36.实现一个字典类，要求元素只能设置1次
class ODict(dict):
	def __setitem__(self, key, value):
		print(key, value)
		if self.__contains__(key):
			raise ValueError("Exists")
		else:
			super
d = ODict()
d["hello"] = "first"
d["hello"] = "second"
print(d["hello"])