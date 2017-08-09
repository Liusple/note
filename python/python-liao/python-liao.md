1. ```
   计算机内存中，统一使用Unicode编码，当保存到硬盘或者需要传输时，转为utf-8.
   浏览网页时，服务器会把动态生成的Unicode内容转为utf-8，在传输给浏览器。
   由于 Python 的字符串类型是 str，在内存中以 Unicode 表示，一个字符
   对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把
   str 变为以字节为单位的 bytes。
   Python 对 bytes 类型的数据用带 b 前缀的单引号或双引号表示。
   以 Unicode 表示的 str 通过 encode()方法可以编码为指定的 bytes。
   ```

2. ```
   对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
   ```

3. ```
   定义默认参数要牢记一点：默认参数必须指向不变对象！
   ```

4. ```
   命名关键字参数：
   如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收 city 和 job 作为关键字参数。这种方式定义的函数如下：
   def person(name, age, *, city, job):
   print(name, age, city, job)
   命名关键字参数可以有缺省值，从而简化调用：
   def person(name, age, *, city='Beijing', job):
   print(name, age, city, job)
   ```

5. ```
   在 Python 中定义函数，可以用必选参数、默认参数、可变参数、关键
   字参数和命名关键字参数，这5种参数都可以组合使用，除了可变参数
   无法和命名关键字参数混合。但是请注意，参数定义的顺序必须是：必
   选参数、默认参数、可变参数/命名关键字参数和关键字参数。
   ```

6. ```
   如果给定一个list 或 tuple，我们可以通过 for 循环来遍历这个list 或
   tuple，这种遍历我们称为迭代（Iteration）。
   ```

7. ```
   默认情况下，dict 迭代的是key。如果要迭代 value，可以用 for value in 
   d.values()，如果要同时迭代 key 和 value，可以用 for k, v in d.items()。
   ```

8. ```
   通过collections模块的Iterable类型判断一个对象是否是可迭代对象。
   ```

9. ```
   >>> for i, value in enumerate(['A', 'B', 'C']):
   ... print(i, value)
   ...
   0 A
   1 B
   2 C
   ```

10. ```
   在 Python 中，这种一边循环一边计算的机制，称为生成器：generator。
   可以通过 next()函数获得 generator 的下一个返回值。
   但正确的用法是使用for循环获取generator返回值。
   ```

11. ```
    1）generator函数，在每次调用 next()的时候执行，遇到 yield 语句返回，
    再次执行时从上次返回的 yield 语句处继续执行。
    2）用 for 循环调用 generator 时，发现拿不到 generator 的 return 语句
    的返回值。如果想要拿到返回值，必须捕获 StopIteration 错误，返回值
    包含在 StopIteration 的 value 中。
    3）对于函数改成的 generator 来说，遇到 return 语句或者执行到函数体最后一行语句，就是结束 generator的指令，for 循环随之结束。 
    ```

12. ```
    1）可以直接作用于 for 循环的数据类型有以下几种：
    一类是集合数据类型，如 list、tuple、dict、set、str 等；
    一类是 generator，包括生成器和带 yield 的 generator function。
    这些可以直接作用于 for 循环的对象统称为可迭代对象：Iterable。
    2）生成器不但可以作用于 for 循环，还可以被 next()函数不断调用并返
    回下一个值，直到最后抛出 StopIteration 错误表示无法继续返回下一个值。
    3）可以被 next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
    生成器都是 Iterator 对象，但 list、 dict、 str 虽然是 Iterable，却不是Iterator。
    4）把 list、dict、str 等 Iterable 变成 Iterator 可以使用 iter()函数。
    ```

13. ```
    1)map()函数接收两个参数，一个是函数，一个是 Iterable，map 将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator 返回。 
    2)reduce 把一个函数作用在一个序列[x1, x2, x3, ...]
    上，这个函数必须接收两个参数，reduce 把结果继续和序列的下一个元
    素做累积计算。

    一个 str2int 的函数就是：
    from functools import reduce
    def char2num(s):
    	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 	6, '7': 7, '8': 8, '9': 9}[s]
    def str2int(s):
    	return reduce(lambda x, y: x * 10 + y, map(char2num, s))
    	
    3） filter()也接收一个函数和一个序列。和 map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是 True 还是 False 决定保留还是丢弃该元素。
    把一个序列中的空字符串删掉，可以这么写：
    def not_empty(s):
    	return s and s.strip()
    list(filter(not_empty, ['A', '', 'B', None, 'C', ' ']))
    ```

14. ```
     sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, 
     ```
    reverse=True)
    ​```

15. ```
    高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
    返回闭包时牢记的一点就是：返回函数不要引用任何循环变量， 或者后
    续会发生变化的变量。
    ```

16. ```
    同样，也可以把匿名函数作为返回值返回，比如：
    def build(x, y):
    	return lambda: x * x + y * y
    ```

17. ```
    1)本质上， decorator 就是一个返回函数的高阶函数。
    @log
    def now():
    	print('2015-3-25')
    把@log 放到 now()函数的定义处，相当于执行了语句：now = log(now)。
    由于 log()是一个 decorator，返回一个函数，所以，原来的 now()函数仍
    然存在，只是现在同名的 now 变量指向了新的函数，于是调用 now()将
    执行新函数，即在 log()函数中返回的 wrapper()函数。

    2)通用decorator：
    import functools
    def log(text):
    	def decorator(func):
    		@functools.wraps(func)
    		def wrapper(*args, **kw):
    			print('%s %s():' % (text, func.__name__))
    			return func(*args, **kw)
    		return wrapper
    	return decorator
    	
    3)在面向对象（OOP）的设计模式中，decorator 被称为装饰模式。OOP
    的装饰模式需要通过继承和组合来实现，而 Python 除了能支持 OOP 的
    decorator 外，直接从语法层次支持 decorator。Python 的 decorator 可以
    用函数实现，也可以用类实现。
    ```

18. ```
    functools.partial 的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
    >>> import functools
    >>> int2 = functools.partial(int, base=2)
    >>> int2('1000000')
    64
    >>> int2('1010101')
    85
    ```

19. ```
    默认情况下， Python 解释器会搜索当前目录、所有已安装的内置模块和
    第三方模块，搜索路径存放在 sys 模块的 path 变量中:
    >>> import sys
    >>> sys.path
    ```

20. ```
    而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象
    都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执
    行就是一系列消息在各个对象之间传递。
    ```

21. ```
    “开闭”原则：
    对扩展开放,对修改封闭.
    ```

22. ```
    元类
    ```

23. ```
    #判断一个对象是否是函数
    >>> type(fn)==types.FunctionType
    True
    >>> type(abs)==types.BuiltinFunctionType
    True
    >>> type(lambda x: x)==types.LambdaType
    True
    >>> type((x for x in range(10)))==types.GeneratorType
    True

    #判断class类型
    >>> isinstance(h, Dog)
    Tru
    ```

24. ```
    getattr()/setattr()/hasattr()
    ```

25. ```
    MixIn 的目的就是给一个类增加多个功能，这样，在设计类的时候，我
    们优先考虑通过多重继承来组合多个 MixIn 的功能，而不是设计多层次
    的复杂的继承关系。
    ```

26. ```
    通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
    __repr__ = __str__
    ```

27. ```
    如果一个类想被用于 for ... in 循环，类似 list 或 tuple 那样，就必须实
    现一个__iter__()方法，该方法返回一个迭代对象，然后，Python 的 for
    循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
    直到遇到 StopIteration 错误时退出循环。
    ```

28. ```
    要表现得像 list 那样按照下标取出元素，需要实现__getitem__()方法。
    ```

29. ```
    __getattr__，只有在没有找到属性的情况下，才调用__getattr__。

    利用完全动态的__getattr__，我们可以写出一个链式调用：
    class Chain(object):
    	def __init__(self, path=''):
    		self._path = path
    	def __getattr__(self, path):
    		return Chain('%s/%s' % (self._path, path))
    	def __str__(self):
    		return self._path
    	__repr__ = __str__
    试试：
    >>> Chain().status.user.timeline.list
    '/status/user/timeline/list'
    ```

30. ```
    任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
    ```

31. ```
    能被调用的对象就是一个 Callable 对象，比如函数和上面定义的带__call__()的类实例：
    >>> callable(Student())
    True
    >>> callable(max)
    True
    ```

32. ```
    from enum import Enum, unique 
    @unique
    class Weekday(Enum):
    	Sun = 0 # Sun 的 value 被设定为 0
    	Mon = 1
    	Tue = 2
    	Wed = 3
    	Thu = 4
    	Fri = 5
    	Sat = 6
    ```

33. ```
    既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
    import logging
    def foo(s):
    	return 10 / int(s)
    def bar(s):
    	return foo(s) * 2
    def main():
    	try:
    		bar('0')
    	except Exception as e:
    		logging.exception(e)
    main()
    print('END')
    ```

34. ```
    1）assert地方的代码应该是 True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
    如果断言失败，assert 语句本身就会抛出 AssertionError。
    启动 Python 解释器时可以用-O 参数来关闭 assert。

    2）
    import logging
    logging.basicConfig(level=logging.INFO)

    logging.info('n = %d' % n) 
    logging 的好处，它允许你指定记录信息的级别，有 debug， info，
    warning，error 等几个级别。
    ```

35. ```
    单元测试：
    import unittest
    from mydict import Dict
    class TestDict(unittest.TestCase):
    	def setUp(self):
    		print('setUp...')
    	def tearDown(self):
    		print('tearDown...')
    	def test_init(self):
    		d = Dict(a=1, b='test')
    		self.assertEqual(d.a, 1)
    		self.assertEqual(d.b, 'test')
    		self.assertTrue(isinstance(d, dict))
    		
    	def test_keyerror(self):
    		d = Dict()
    		with self.assertRaises(KeyError):
    			value = d['empty']
    			
    if __name__ == '__main__':
    	unittest.main()
    ```

36. ```
    文档测试
    ```

37. ```
    with open('/path/to/file', 'r') as f:
    	print(f.read())
    调用 readline()可以每次读取一行内容，调用 readlines()一次读取所有内容并按行返回 list。

    要读取非 UTF-8 编码的文本文件，需要给 open()函数传入 encoding 参数，
    例如，读取 GBK 编码的文件：
    >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')

    StringIO/BytesIO
    ```

38. ```
    >>> os.path.splitext('/path/to/file.txt')
    ('/path/to/file', '.txt')
    >>> os.path.split('/Users/michael/testdir/file.txt')
    ('/Users/michael/testdir', 'file.txt')
    ```

39. ```
    >>> d = dict(name='Bob', age=20, score=88)
    >>> pickle.dumps(d)
    >>> f = open('dump.txt', 'wb')
    >>> pickle.dump(d, f) 
    >>> f.close()

    >>> f = open('dump.txt', 'rb')
    >>> d = pickle.load(f)
    >>> f.close()
    ```

40. ```
    >>> import json
    >>> d = dict(name='Bob', age=20, score=88)
    >>> json.dumps(d)
    '{"age": 20, "score": 88, "name": "Bob"}'

    >>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    >>> json.loads(json_str)
    {'age': 20, 'score': 88, 'name': 'Bob'} 

    #json处理类
    import json
    class Student(object):
    	def __init__(self, name, age, score):
    		self.name = name
    		self.age = age
    		self.score = score
    s = Student('Bob', 20, 88)

    def student2dict(std):
        return {
        	'name': std.name,
       	 	'age': std.age,
        	'score': std.score
        }
    >>> print(json.dumps(s, default=student2dict))
    {"age": 20, "name": "Bob", "score": 88}
    #print(json.dumps(s, default=lambda obj: obj.__dict__))

    def dict2student(d):
    	return Student(d['name'], d['age'], d['score'])
    >>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    >>> print(json.loads(json_str, object_hook=dict2student))
    <__main__.Student object at 0x10cd3c190>
    ```

41. ```python
    #进程：
    1）
    import os
    pid = os.fork()
    if pid == 0:
        print("Child process(%s)" %(os.getpid()))
    else:
        print("Parent process(%s)" %(os.getpid()))
        
    2）
    from multiprocessing import Process
    import os
    def fun(name):
    	print("Run child process %s(%s)" %(name, os.getpid()))
    	
    print('Parent process %s.' % os.getpid()) 
    p = Process(target=fun, args=("test",))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

    3）
    from multiprocessing import Pool
    import os, time, random
    def long_time_task(name):
     	print('Run task %s (%s)...' % (name, os.getpid()))
        start = time.time()
        time.sleep()
        end = time.time()
        print('Task %s runs %0.2f seconds.' % (name, (end - start)))
        
    print('Parent process %s.' % os.getpid()))
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))
    print('Waiting for all subprocesses done...') 
    p.close()
    p.join()
    print('All subprocesses done.')
    #对 Pool 对象调用 join()方法会等待所有子进程执行完毕，调用 join()
    #之前必须先调用 close()，调用 close()之后就不能继续添加新的Process了。

    4）
    #subprocess模块可以非常方便地启动一个子进程，然后控制其输入和输出。
    import subprocess
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, 
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)

    5）#进程间通信
    from multiprocessing import Process, Queue
    import os, time, random
    def write(q):
    	print('Process to write: %s' % os.getpid())
    	for value in ['A', 'B', 'C']:
    		print('Put %s to queue...' % value)
    		q.put(value)
    		time.sleep(random.random())

    def read(q):
    	print('Process to read: %s' % os.getpid())
    	while True:
    		value = q.get(True)
    		print('Get %s from queue.' % value)

    # 父进程创建 Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

    6）#分布式进程
    ```

42. ```
    import time, threading

    def loop():
    	print('thread %s is running...' % threading.current_thread().name)
    	n = 0
    	while n < 5:
    		n = n + 1
    		print('thread %s >>> %s' % (threading.current_thread().name, n))
    		time.sleep(1)
    	print('thread %s ended.' % threading.current_thread().name)
    	
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)

    多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份
    拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线
    程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程
    之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
    创建一个锁就是通过threading.Lock()来实现：
    lock.acquire()
    try:
    	change_it(n)
    finally:
    # 改完了一定要释放锁:
    	lock.release()
    	
    因为 Python 的线程虽然是真正的线程，但解释器执行代码时，有一个GIL 锁：Global Interpreter Lock，任何 Python 线程执行前，必须先获得GIL 锁，然后，每执行 100 条字节码，解释器就自动释放 GIL 锁，让别的线程有机会执行。这个 GIL 全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在 Python 中只能交替执行，即使 100 个线程跑在 100 核 CPU 上，也只能用到 1 个核。所以，在 Python 中，可以使用多线程，但不要指望能有效利用多核。
    不过，也不用过于担心， Python 虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个 Python 进程有各自独立的 GIL 锁，互不影响。

    import threading
    # 创建全局 ThreadLocal 对象:
    local_school = threading.local()
    def process_student():
    # 获取当前线程关联的 student:
    	std = local_school.student
    	print('Hello, %s (in %s)' % (std, 					threading.current_thread().name))
    	
    def process_thread(name):
    	# 绑定 ThreadLocal 的 student:
    	local_school.student = name
    	process_student()
    	
    t1 = threading.Thread(target= process_thread, args=('Alice',), 
    name='Thread-A')
    t2 = threading.Thread(target= process_thread, args=('Bob',), 
    name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    ThreadLocal 最常用的地方就是为每个线程绑定一个数据库连接，HTTP
    请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以
    非常方便地访问这些资源。
    ```

43. ```
    考虑到 CPU 和 IO 之间巨大的速度差异，一个任务在执行的过程中大部
    分时间都在等待 IO 操作，单进程单线程模型会导致别的任务无法并行
    执行，因此，我们才需要多进程模型或者多线程模型来支持多任务并发执行。
    现代操作系统对 IO 操作已经做了巨大的改进，最大的特点就是支持异
    步 IO。如果充分利用操作系统提供的异步 IO 支持，就可以用单进程单
    线程模型来执行多任务，这种全新的模型称为事件驱动模型，Nginx 就
    是支持异步 IO 的 Web 服务器，它在单核 CPU 上采用单进程模型就可
    以高效地支持多任务。对应到 Python 语言，单进程的异步编程模型称为协程。
    ```

44. ```
    regex	
    ```

45. ```
    time
    ```

46. ```
    #collections
    >>> from collections import namedtuple
    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> p = Point(1, 2)
    >>> p.x
    1
    >>> p.y
    2

    >>> from collections import deque
    >>> q = deque(['a', 'b', 'c'])
    >>> q.append('x')
    >>> q.appendleft('y')
    >>> q
    deque(['y', 'a', 'b', 'c', 'x'])

    >>> from collections import defaultdict
    >>> dd = defaultdict(lambda: 'N/A')
    >>> dd['key1'] = 'abc'
    >>> dd['key1'] # key1 存在
    'abc'
    >>> dd['key2'] # key2 不存在，返回默认值
    'N/A'

    >>> from collections import OrderedDict
    >>> d = dict([('a', 1), ('b', 2), ('c', 3)])
    >>> d # dict 的 Key 是无序的
    {'a': 1, 'c': 3, 'b': 2}
    >>> od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    >>> od # OrderedDict 的 Key 是有序的
    OrderedDict([('a', 1), ('b', 2), ('c', 3)])

    >>> from collections import Counter
    >>> c = Counter()
    >>> for ch in 'programming':
    ... c[ch] = c[ch] + 1
    ...
    >>> c
    Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
    ```

47. ```
    Base64 是一种用 64 个字符来表示任意二进制数据的方法。
    >>> import base64
    >>> base64.b64encode(b'binary\x00string')
    b'YmluYXJ5AHN0cmluZw=='
    >>> base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
    b'binary\x00string' 
    ```

48. ```
     Python 提供了一个 struct 模块来解决 bytes 和其他二进制数据类型
    的转换。
    >>> import struct
    >>> struct.pack('>I', 10240099)
    b'\x00\x9c@c'

    >>> struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
    (4042322160, 32896) 
    ```

49. ```
    import hashlib
    md5 = hashlib.md5()
    md5.update('how to use md5 in '.encode('utf-8'))
    md5.update('python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())

    import hashlib
    sha1 = hashlib.sha1()
    sha1.update('how to use sha1 in '.encode('utf-8'))
    sha1.update('python hashlib?'.encode('utf-8'))
    print(sha1.hexdigest())
    ```

50. ```
    #itertools
    1)
    >>> import itertools
    >>> natuals = itertools.count(1)
    >>> for n in natuals:
    ... print(n)
    ...
    1
    2
    3
    ...

    2)
    >>> import itertools
    >>> cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
    >>> for c in cs:
    ... print(c)
    ...
    'A' 
    'B'
    'C'
    'A'
    'B'
    'C'
    ...

    3)
    >>> ns = itertools.repeat('A', 3)
    >>> for n in ns:
    ... print(n)
    ...
    A
    A
    A

    4)
    >>> natuals = itertools.count(1)
    >>> ns = itertools.takewhile(lambda x: x <= 10, natuals)
    >>> list(ns)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    5)
    >>> for c in itertools.chain('ABC', 'XYZ'):
    ... print(c)
    # 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'

    6)
    >>> for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: 
    c.upper()):
    ... print(key, list(group))
    ...
    A ['A', 'a', 'a']
    B ['B', 'B', 'b']
    C ['c', 'C']
    A ['A', 'A', 'a']
    ```

51. ```
    XML/HTMLPaser
    ```

52. ```
    urllib 提供了一系列用于操作 URL 的功能。
    ```

53. ```
    IP 协议负责把数据从一台计算机通过网络发送到另一台计算机。数据被
    分割成一小块一小块，然后通过 IP 包发送出去。
    IP 包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。
    TCP 协议则是建立在 IP 协议之上的。TCP 协议负责在两台计算机之间
    建立可靠连接，保证数据包按顺序到达。 TCP 协议会通过握手建立连接，
    然后，对每个 IP 包编号，确保对方按顺序收到，如果包丢掉了，就自
    动重发。许多常用的更高级的协议都是建立在 TCP 协议基础上的，比如用于浏
    览器的 HTTP 协议、发送邮件的 SMTP 协议等。
    ```

54. ```
    1)
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.sina.com.cn', 80))
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: 
    close\r\n\r\n')
    buffer = []
    while True:
    	d = s.recv(1024)
    	if d:
    		buffer.append(d)
    	else:
    		break
    	data = b''.join(buffer)
    s.close()
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open('sina.html', 'wb') as f:
    	f.write(html) 
    	
    2)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print('Waiting for connection...')
    while True:
    	sock, addr = s.accept()
    	t = threading.Thread(target=tcplink, args=(sock, addr))
    	t.start()
    def tcplink(sock, addr):
    	print('Accept new connection from %s:%s...' % addr)
    	sock.send(b'Welcome!')
    	while True:
    		data = sock.recv(1024)
    		time.sleep(1)
    		if not data or data.decode('utf-8') == 'exit':
    			break
    		sock.send(('Hello, %s!' % data).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    ```

55. ```
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 9999))
    print('Bind UDP on 9999...')
    while True:
    	data, addr = s.recvfrom(1024)
    	print('Received from %s:%s.' % addr)
    	s.sendto(b'Hello, %s!' % data, addr)
    	
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b'Michael', b'Tracy', b'Sarah']:
    	s.sendto(data, ('127.0.0.1', 9999))
    	print(s.recv(1024).decode('utf-8'))
    s.close()
    ```

56. ```
    SQLAlchemy
    ```

57. ```
    当我们编写一个页面时，我们只需要在 HTTP 请求中把 HTML发送出去，不需要考虑如何附带图片、视频等，浏览器如果需要请求图片和视频，它会发送另一个 HTTP 请求，因此，一个 HTTP 请求只处理一个资源。
    当遇到连续两个\r\n 时，Header 部分结束，后面的数据全部是 Body。
    Body 的数据类型由 Content-Type 头来确定，如果是网页，Body 就是文
    本，如果是图片，Body 就是图片的二进制数据。 
    ```

58. ```
    #WSGI
    WSGI 接口定义非常简单，它只要求 Web 开发者实现一个函数，就可以
    响应 HTTP 请求。
    一个最简单的 Web 版本的“Hello, web!”：
    def application(environ, start_response):
    	start_response('200 OK', [('Content-Type', 'text/html')])
    	return [b'<h1>Hello, web!</h1>']
    environ：一个包含所有 HTTP 请求信息的 dict 对象；
    start_response：一个发送 HTTP 响应的函数。
    有了 WSGI，我们关心的就是如何从 environ 这个 dict 对象拿到 HTTP请求信息，然后构造 HTML，通过 start_response()发送 Header，最后返回 Body。
    application()函数必须由 WSGI 服务器来调用。

    # hello.py
    def application(environ, start_response):
    	start_response('200 OK', [('Content-Type', 'text/html')])
    	return [b'<h1>Hello, web!</h1>']
    	
    # server.py
    from wsgiref.simple_server import make_server
    from hello import application
    # 创建一个服务器，IP 地址为空，端口是 8000，处理函数是 application:
    httpd = make_server('', 8000, application)
    print('Serving HTTP on port 8000...')
    # 开始监听 HTTP 请求:
    httpd.serve_forever()

    无论多么复杂的 Web 应用程序，入口都是一个 WSGI 处理函数。 HTTP请求的所有输入信息都可以通过 environ 获得，HTTP 响应的输出都可以通过 start_response()加上函数返回值作为 Body。
    ```

59. ```
    在 IO 操作的过程中，当前线程被挂起，而其他需要 CPU 执行的代码就
    无法被当前线程执行了。因为一个 IO 操作就阻塞了当前线程，导致其他代码无法执行，所以我们必须使用多线程或者多进程来并发执行代码，为多个用户服务。每个用户都会分配一个线程，如果遇到 IO 导致线程被挂起，其他用户的线
    程不受影响。多线程和多进程的模型虽然解决了并发问题。
    由于我们要解决的问题是 CPU 高速执行能力和 IO 设备的龟速严重不匹
    配，多线程和多进程只是解决这一问题的一种方法。
    另一种解决 IO 问题的方法是异步 IO。当代码需要执行一个耗时的 IO
    操作时，它只发出 IO 指令，并不等待 IO 结果，然后就去执行其他代码
    了。一段时间后，当 IO 返回结果时，再通知 CPU 进行处理。

    消息模型是如何解决同步 IO 必须等待 IO 操作这一问题的呢？当遇到
    IO 操作时，代码只负责发出 IO 请求，不等待 IO 结果，然后直接结束
    本轮消息处理，进入下一轮消息处理过程。当 IO 操作完成后，将收到
    一条“IO 完成”的消息，处理该消息时就可以直接获取 IO 操作结果。
    在“发出 IO 请求”到收到“IO 完成”的这段时间里，同步 IO 模型下，主线
    程只能挂起，但异步 IO 模型下，主线程并没有休息，而是在消息循环
    中继续处理其他消息。这样，在异步 IO 模型下，一个线程就可以同时
    处理多个 IO 请求，并且没有切换线程的操作。对于大多数 IO 密集型的
    应用程序，使用异步 IO 将大大提升系统的多任务处理能力。
    ```

60. ```
    def consumer():
    r = ''
    while True:
    	n = yield r
    	if not n:
    		return
    	print('[CONSUMER] Consuming %s...' % n)
    	r = '200 OK'
    def produce(c):
    	c.send(None)
    	n = 0
    	while n < 5:
    		n = n + 1
    		print('[PRODUCER] Producing %s...' % n)
    		r = c.send(n)
    		print('[PRODUCER] Consumer return: %s' % r)
    	c.close()
    c = consumer()
    produce(c)
    ```

61. ```
    import threading
    import asyncio
    @asyncio.coroutine
    def hello():
    	print('Hello world! (%s)' % threading.currentThread())
    	yield from asyncio.sleep(1)
    	print('Hello again! (%s)' % threading.currentThread())
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    import asyncio
    @asyncio.coroutine
    def wget(host):
    	print('wget %s...' % host)
    	connect = asyncio.open_connection(host, 80)
    	reader, writer = yield from connect
    	header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    	writer.write(header.encode('utf-8'))
    	yield from writer.drain()
    	while True:
    		line = yield from reader.readline()
    		if line == b'\r\n':
    			break
    		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    	# Ignore the body, close the socket
    	writer.close()
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 
    'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    ```

62. ```
    async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")
    ```

63. ```
    import asyncio
    from aiohttp import web
    async def index(request):
    	await asyncio.sleep(0.5)
    	return web.Response(body=b'<h1>Index</h1>')
    async def hello(request):
    	await asyncio.sleep(0.5)
    	text = '<h1>hello, %s!</h1>' % request.match_info['name']
    	return web.Response(body=text.encode('utf-8'))
    async def init(loop):
    	app = web.Application(loop=loop)
    	app.router.add_route('GET', '/', index)
    	app.router.add_route('GET', '/hello/{name}', hello)
    	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    	print('Server started at http://127.0.0.1:8000...')
    	return srv
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()
    ```

64. ​

