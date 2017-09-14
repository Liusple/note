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

#装饰器
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