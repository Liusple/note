1. ```
   python2 input和python3作用不一致，python2输入使用raw_input()
   ```

2. ```python
   import keyword
   #显示关键字
   keyword.kwlist 
   ```

3. ```python
   print("%d %d" %(a, b)) #无逗号
   print("", end="")
   ```

4. ```python
   import random
   random.randint(1, 4)
   ```

5. ```python
   #切片
   word="super"
   word[:]       #super
   word[2:-1]    #pe
   word[::-1]    #repus
   word[-1::-1]  #repus
   word[:-1]     #supe
   ```

6. ```python
   #字符串操作
   find/rfind
   count
   startswith/endswith
   capitalize/title
   	w="it's good" 
   	w.capitalize() #It's good
   	w.title() #It'S Good   s也大写了
   split
   	#可以用strip去除空格,\n,\t,\r
   	s="For\tever young, For\rever lo\nve."
       s.split() #['For', 'ever', 'young,', 'For', 'ever', 'lo', 've.']
       
   center
   ljust
   rjust
   	w="simple"  
       w.center(30) #'            simple            '
       w.ljust(30)  #'simple                        '
       w.rjust(30)  #'                        simple'
       
   strip  #去除两端空格,\t,\n
   lstrip #去除左边空格,\t,\n
   rstrip #去除右边空格,\t,\n

   isalpha #字符串是否纯数字，不包含空格
   isdigit #字符串是否纯字母，不包含空格
   isalnum #字符串是否只包含数字和字母，不包含空格

   splitlines #按换行分割 
   	w="he\rll\no"  #\r也分割了
   	w.splitlines() #['he', 'll', 'o']

   isspace() #是否纯空格

   partition
   rpartition
   	w="How are you?"
       w.partition("o")   #('H', 'o', 'w are you?')
       w.rpartition("o ") #('How are y', 'o', 'u?')
   ```

7. ```python
   #append和extend
   l=["12", "34"]
   ll=["56", "78"]
   l.append(ll)   #['12', '34', ['56', '78']]
                  #l.append(ll)返回None

   l=["12", "34"]
   ll=["56", "78"]
   l.extend(ll)   #['12', '34', '56', '78']
   ```

8. ```
   字典获取用get(),没有返回None，不会异常
   ```

9. ```python
   g_name = "simple" #函数使用全局变量，全局变量需求在函数调用之前定义

   def fun():
       g_name = "alex" #相当于定义了局部变量g_name，修改全局需用global
       print(g_name)   #alex

   fun()
   print(g_name)  #simple
   ```

10. ```python
   #排序
   l=[{"name":"alex", "age":20}, {"name":"king", "age":18}, {"name":"kate", "age":17}]
   l.sort(key=lambda x:x["name"], reverse=True)
   ```

11. ```python
    1）
    a=100
    def fun(tmp):
    	tmp+=tmp
    	print(tmp)
    fun(a)
    print(a)
    #200
    #100

    2)
    a=[100]
    def fun(tmp):
    	tmp+=tmp  #care here
    	print(tmp)
    fun(a)
    print(a)
    #[100, 100]
    #[100, 100]

    3)
    a=[100]
    def fun(tmp):
    	tmp=tmp+tmp #相当于返回了一个新的变量
    	print(tmp)
    fun(a)
    print(a)
    #[100, 100]
    #[100]
    ```

12. ```python
    import os
    os.remove()
    os.rename()
    os.listdir()
    os.mkdir()
    os.rmdir()
    ```

13. ```python
    #匿名函数做参数
    def f(x, y, fun):
    	return fun(x, y)
    f(1, 2, lambda x, y:x+y)
    ```

14. ```python
    class T():
    	def __f(self):  #私有方法,__f变为了_T__f
    		print("__f")
    t=T()
    t.f()      #error
    t._T__f()  #__f 
    ```

15. ```python
    class T():
    	def __del__(self):
    		print("__del__")
    t = T()
    del t  #__del__  删除对象时候会调用__del__方法
    ```

16. ```python
    #查看对象引用个数
    import sys
    sys.getrefcount(t)
    ```

17. ```python
    class Dog():
    	def bark(self):
    		print("Wang Wang")
    		
    class Alaska(Dog):
    	def bark(self):
    		print("Woo Woo")
    		Dog.bark(self)   #两种调用父类方法的方法
    		#super().bark()
    ```

18. ```python
    #类有一个__mro__属性
    ```

19. ```python
    #类方法和类属性
    class T():
    	num=0
    	@classmethod  #类方法用来修改类属性的
    	def add(cls):
    		cls.num += 1
    	
    	@staticmethod
    	def fun():
    		pass
    #类和实例对象都可以调用类方法和静态方法
    t=T()
    t.add()
    T.add()
    t.fun()
    T.fun()

    class Tool:
        num = 0
        def __init__(self):
            Tool.num += 1
    ```

20. ```python
    #__new__ 创建对象是被调用
    class Dog(object):
        def __init__(self):
            print("__init__")
        def __new__(cls):
            return object.__new__(cls)
    lucky = Dog()  #new返回了一个对象给init           
    #单例
    class Dog(object):
        __instance = None
        def __new__(cls):
            if cls.__instance:
                return cls.__instance
           	else:
                cls.__instance = object.__new__(cls)
                return cls.__instance
        
    ```

21.  ```python
    __all__=["", ""] #限制导入
    ```

22. ```python
    [i for i in range(3) for j in range(2)] #[0, 0, 1, 1, 2, 2]
    ```

23. ```python
    a=[1,2,3]
    b=[1,2,3]
    a==b   #True
    a is b #False

    c=100
    d=100
    c==d   #True
    c is d #True 数字一定范围内is为True
    ```

24. ```python
    import copy
    a=[1,2]
    b=[3,4]
    c=[a,b]
    d=copy.deepcopy(c) #会递归拷贝
    print(id(c))
    print(id(d))
    #print(id(c[0]))和print(id(d[0]))不等
    print(id(c[0]))
    print(id(d[0]))

    a=[1,2]
    b=[3,4]
    c=[a,b]
    d = copy.copy(c) #如果是a第一层是列表，会拷贝第一层，如果a第一层是元组，将不拷贝，更深层都不拷贝
    #print(id(c))和print(id(d))不相等
    print(id(c))
    print(id(d))

    c=(a,b) #改为元组
    d=copy.copy(c)
    #print(id(c))和print(id(d))相等
    print(id(c))
    print(id(d))
    ```




25. ```python
    __slots__ = ("name", "age")#限制给类添加属性
    ```

26. ```python
    from collections import Iterable, Iterator
    a="abc"
    isinstance(a, Iterable) #True
    isinstance(a, Iterator) #False
    a=iter(a)  #转为迭代器，迭代器可以next()
    ```

27. ```
    globals()
    locals()
    LEGB原则：locals->enclosing fuction->global->buildin
    ```

28. ```python
    #动态添加方法
    from types import MethodType
    class Student():
    	pass

    def set_age(self, age):
    	self.age = age
    	
    @staticmethod
    def test_static():
    	print("test staticmethod")
    	
    @classmethod
    def test_class(cls):
    	print("test classmethod")
    	
    s = Student()
    s.set_age = MethodType(set_age, s)#set_age只对s生效

    Student.test_static = test_static
    Student.test_class = test_class
    ```



29. ```python
    #property
    class User():
        def __init__(self):
            self.__age = 19
    	@property
    	def age(self):
    		return self.__age
    	
    	@age.setter
    	def age(self, age):
    		self.__age = age
    ```

30. ```python
    class T():
        def __init__(self):
            self.__num = 10
    t = T()
    t.__num = 100   #相当于给T增加了一个__num属性
    print(t.__num)  #100
    ```




31. ```python
    #通用装饰器
    import functools
    def log(tag=None):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwarg):
                print(tag)
                return func(*args, **kwarg)
            return wrapper
        return decorator

    @log("first tag")
    def run(*args, **kwarg):
        print("run")

    run()
    print(run.__name__)
    ```


32. ​

```
1)
def counter(start=0):
	count = [start]
	def incr():
		count[0] += 1
		return count[0]
	return incr
c1 = counter(4)
print(c1())

2)
def counter(start=0):
	def incr():
		nonlocal start
		start += 1
		return start
	return incr
c1 = counter(5)
print(c1())
```

33.

```
class CarStore(object):
	def __init__(self):
		self.factory = Factory()
	def order(self, type):
		return self.factory.select_car_by_type(type)
		
class Factory(object):
	def select_car_by_type(type):
		if type = "":
			return 
		
carStore = CarStore()
car = carStore.order("")
```

34.

```python
def w1(func):
    print("w1")
    def inner():
        print("in w1")
        func()
   	return inner

def w2(func):
    print("w2")
    def inner():
        print("in w2")
        func()
    return inner

@w1
@w2
def log():
    print("in log")
    
#output
w2
w1
in w1
in w2
in log
```

35.

```python
def f1():
	while True:
        print("f1")
       	yield 1
def f2():
    while True:
        print("f2")
        yield 2
 
while True:
    f1().__next__()
    f2().__next__()
```

36.

```
_num = 20 
from sth import * # _num无法被导入
import sth        # sth._num可以使用
```

