#1.python参数传递是值传递还是引用传递
#都是引用，对于不可改变的数据类型来说，不能改变，如果修改了，事实上我们是新建一个对象来对待。

#2.lambda更简单，省去命名函数名的麻烦
f = lambda x,y:x+y
print("2:")
print("f(1,2):", f(1, 2))
print("\n")

#3.format可以接受参数不限个数，并且位置可以不按顺序
print("3:")
print("{1}-{0}".format("good", 123))
print("{name}-{age}".format(age=23, name="lius"))
print("\n")

#4.


#5.反转
def reverse(text="abc"):
	return text[::-1]
print("5:")
print(reverse("12345"))
print("\n")

#6.按升序合并下面两个list，并去除重复元素
list1 = [2,3,5,2,1]
list2 = [1,3,2,4,6,3,4]
list3 = list1 + list2
print("6:")
print(set(list3))
print("\n")


#7.
ll = [1,2,3,4,5,6,7]
print("7:")
print(ll[10:])    #输出[]
print("\n")

#8.
print("8:")
keys = ["Name", "Sex", "Age"]
values = ["Jack", "Male", 19]
print(dict(zip(keys, values)))
print("\n")

#9.
def extend(val, ll=[]):
	ll.append(val)
	return ll
l1 = extend(1)            #[1, 3]
l2 = extend(123, [])      #[123]
l3 = extend(3)            #[1, 3]
l4 = extend(456, [])      #[456]
print("9:")
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
#with用在支持上下文管理协议的对象中，如file,thread.LockType
#当with语句执行时，便执行上下文表达式（context_expr）来获得一个上下文管理器，上下文管理器的职责是提供一个上下文对象，用于在with语句块中处理细节：
#一旦获得了上下文对象，就会调用它的__enter__()方法，将完成with语句块执行前的所有准备工作，如果with语句后面跟了as语句，则用__enter__()方法的返回值来赋值；
#当with语句块结束时，无论是正常结束，还是由于异常，都会调用上下文对象的__exit__()方法，__exit__()方法有3个参数，如果with语句正常结束，三个参数全部都是 None；如果发生异常，三个参数的值分别等于调用sys.exc_info()函数返回的三个值：类型（异常类）、值（异常实例）和跟踪记录（traceback），相应的跟踪记录对象。
#因为上下文管理器主要作用于共享资源，__enter__()和__exit__()方法干的基本是需要分配和释放资源的低层次工作，
#比如：数据库连接、锁分配、信号量加/减、状态管理、文件打开/关闭、异常处理等。


#13.生成斐波那契数列
def fibs(x):
	result = [0, 1]
	for i in range(x-2):
		result.append(result[-2] + result[-1])
	return result
print("13:")
print(fibs(0))  #[0,1]
print("\n")

#14.反序的迭代一个序列
print("14:")
x = [1,2,3,4,5]
for i in range(len(x)-1, -1, -1):
	print(x[i])
print("\n")

#15.
L1 = [1,2,3,1,2,3,4,5]
L2 = []
[L2.append(i) for i in L1 if i not in L2]
print("15:")
print(L2)
print("\n")

#16.


#17
import os 
#os.remove(filename)


#18.得到list的交集，差集
l1 = [1,2,3,4,6]
l2 = [3,4,5,1,2]
l3 = [i for i in l1 if i not in l2]
l4 = [i for i in l1 if i in l2]
print("18:")
print(l3, l4)
print("\n")

#19
w = "Python is a very funny language"
w.find("Python")
w.replace("Python", "Ruby")

#20.
words = ["This", "is", "a", "dog"]
words.sort(key=lambda x:x.lower())
print("20:")
print(words)
print("\n")

#21.
lists = ["xyz", "abc", "opq"]
lists.sort(key=lambda x:x[1], reverse=True)
print("21:")
print(lists)
print("\n")

#22.解析argv
import sys
for arg in sys.argv[1:]:
	print(arg)

#23装饰器

#24.
class Array:
	__list = []

	def __init__(self):
		print("Array constructor")

	def __del__(self):
		print("Array destructor")

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
print("24:")
a = Array()
a.Add(1)
a.Add(3)
a.DisplayItems()
print(len(a))
print(a)
a.Remove(1)
a.DisplayItems()
print("\n")

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
print("26:")
s = Stack()
s.push(10)
s.push(20)
print(len(s))
print(s.peek())
s.pop()
print(len(s))
print("\n")

#27.
#迭代器，yield
#标准库线程安全的队列是哪一个，不安全是哪一个？logging是线程安全的吗？
#python高并发解决方案
#poll,epoll，select区别，边缘触发，水平触发区别
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


#28.函数式编程
#python变量解析作用域
#assert True则继续执行


#29.
li = [[]] * 5
li[0].append(19)
li[1].append(29)
li.append(39)
print("29:")
print(li)
print("\n")

#30.
def multipliers():
	return [lambda x:i*x for i in range(4)]
print("30:")
print([m(2) for m in multipliers()])
print("\n")


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

print("33:")
o = myClass() 
print(o.normal_method)#<bound method myClass.normal_method of <__main__.myClass object at 0x000000000267F160>>
o.normal_method()
print(o.class_method) #<bound method myClass.class_method of <class '__main__.myClass'>>
o.class_method()
print(o.static_method)#<function myClass.static_method at 0x00000000026737B8>
o.static_method()
o.some_property
o.some_another_property
o.some_property = [1,2,3]
print(o.some_property)
print("\n")

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
print("35:")
print(reduce(lambda x,y:x+y, [1,2,3]))
print("\n")

#36.浏览器一个请求从发送到返回经历了什么
#37短连接如何设计
#38微信红包框架设计



#39
class P(object):
	n = []
	t = "test"
p1 = P()
p2 = P()
print("39:")
print(p1.t)
print(p2.t)
p1.t = "p1"
print(p1.t)   #p1
print(p2.t)   #test
p1.n.append(1)
p2.n.append(20)
print(p1.n)   #[1, 20]
print(p2.n)   #[1, 20]
print("\n")

#40字典推导式
dd = {"one":1, "two":2}
d = {k:v+1 for k,v in dd.items()}
print("40:")
print(d)
print("\n")

#41*args, **kwargs
def print_everthing(*args):
	for count, thing in enumerate(args):
		print("{0}-{1}".format(count, thing))
def table_things(**kwargs):
	for k, v in kwargs.items():
		print("{0}-{1}".format(k, v))
print("41:")
print_everthing("one", "two", "three")
table_things(first=1, second=2)
print("\n")

#42.新式类和旧式类区别
#为了统一type和class
# 在2.2之前，比如2.1版本中，类和类型是不同的，如a是ClassA的一个实例，那么a.__class__返回 ‘ class    __main__.ClassA‘ ，type(a)返回总是<type 'instance'>。而引入新类后，比如ClassB是个新类，b是ClassB的实例，b.__class__和type(b)都是返回‘class '__main__.ClassB' ，这样就统一了。
# 在多继承中，新式类采用广度优先搜索，而旧式类是采用深度优先搜索。
#43.Python2和Python3区别
#统一了字符编码支持
#增加了新的语法，print，格式化字符串变量，nonlocal，yield
#修改了一些语法，map，filter，dict的items/keys/values由返回列表到返回迭代对象
#去掉了一些语法xrange，不再有经典类


#
#44.__new__和__init__的区别


#45.
import copy
a = [1, 2, 3, 4, ['a', 'b']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
a[4].append('c')
print("45:")
print("a=", a)     #[1,2,3,4,['a', 'b', 'c'], 5]
print("b=", b)	   #[1,2,3,4,['a', 'b', 'c'], 5]
print("c=", c)	   #[1,2,3,4,['a', 'b', 'c']]
print("d=", d)	   #[1,2,3,4,['a', 'b']]
print("\n")

#46.is和==
#is比较id，==比较值
a = 1
b = 1
print("46:")
print("a=1, b=1", a is b)
x = 123456789
y = 123456789
print("x=123456789, y=123456789", x is y)
a = "abc"
b = "abc"
print("a=abc, b=abc", a is b)
a = [1, 2]
b = [1, 2]
print("a:[1,2], b:[1,2]", a is b)
print("\n")

#47.调度算法
#先来先服务，最高优先权调度，时间片轮转，短作业优先


#48.死锁
#



#49.
li = [lambda :x for x in range(10)]
print("49:")
print(type(li))
print(type(li[0]))
res = li[0]()
print(res)  #9
print("\n")

#50
name = "peter"
def f1():
	print(name)
def f2():
	name = "bob"
	f1()
print("50:")
f2()  #peter
print("\n")

#51.
def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)      #test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam)   #nonlocal spam
    do_global()
    print("After global assignment:", spam)     #nonlocal spam
print("51:")
scope_test()
print("In global scope:", spam)                 #global spam
print("\n")

#52.闭包
#闭包函数必须含有内嵌函数，内嵌函数需要引用该嵌套函数上一级namespace中的变量，闭包函数必须返回内嵌函数
def greeting_conf(prefix):
	def greeting(name):
		print(prefix, name)
	return greeting

mG = greeting_conf("Good morning")
print("52:")
print("mG name is:", mG.__name__)          #greeting
print("id of mG is:", id(mG))
mG("Lius")                

aG = greeting_conf("Good afternoon")
print("aG name is:", aG.__name__)
print("id of aG is:", id(aG))
aG("Lius")

print(dir(aG))
print(aG.__closure__)
print(type(aG.__closure__[0]))
print(aG.__closure__[0].cell_contents)
print("\n")

#53
class A(object):
    def __init__(self):
        print("Enter A")
        print("Leave A")

class B(A):
    def __init__(self):
        print("Enter B")
        super(B, self).__init__()
        print("Leave B")

class C(A):
    def __init__(self):
        print("Enter C")
        super(C, self).__init__()
        print("Leave C")

class D(A):
    def __init__(self):
        print("Enter D")
        super(D, self).__init__()
        print("Leave D")

class E(B, C, D):
    def __init__(self):
        print("Enter E")
        super(E, self).__init__()
        print("Leave E")

print("53:")
E()
print("\n")

#54.
data = ['1', '2', '3']
print(sum(int(i) for i in data))
print(reduce(lambda x,y:int(x)+int(y), data))