## 数据类型与结构

1 `==` 表示的是两个值是否相等 而 `is` 表示的是 两个变量的地址是否一样，如果 `is` 为真 那么两个值是一样的。

2 通过 `id()` 可以查看变量值的内存地址。

3 Python 中一切都是对象，变量只是对对象的引用。

4 常量通常用大写的名称，然后放在代码的最上方，作为全局变量使用

5 字符串的方法：

- 去除左侧空格  `str.lstrip()`
- 去除右侧空格 `str.rstrip()`
- 去除两边的空格 `str.strip()`
- 判断字符串是否以某字符串开头 `str.startswith()`
- 判断字符串是否以某字符串结尾 `str.endswith()`
- 分割字符串为列表 `str.split("flag")` `flag`为分割的依据
- 判断这个字符串是否是 数字型字符串 `str.isdigit()` 


6 表示数字的时候，我们不仅仅会用 十进制还会使用 十六 或者 八进制 。十六进制的前缀是 `0x` , 里面的内容是 `0-9 a-f` , 八进制的前缀是  `0o`, 表示的内容是 `0-7`，二进制的前缀是 `b`。

7 布尔运算：判断表达式返回的是真或者假的时候，都是布尔运算。 除了 0 None ，非空都是 True， 注意短路运算，其实默认的返回的都是后面的值。

8 `None` 的类型是 `NoneType` 不过他的BOOL值是 False

9 `input` 接收用户的输入，返回值是 **字符串**， 可作为等待用户输入使用，按下Enter键继续


10 `f"{str}"` 字符串格式化

11  位运算 就是把转为二进制 再进行运算

12 

运算符 描述
    ** 指数 (最高优先级)


    ~ + - 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)


    * / % // 乘，除，取模和取整除


    + - 加法减法


    >> << 右移，左移运算符


    & 位 'AND'


    ^ | 位运算符


    <= < > >= 比较运算符


    <> == != 等于运算符


    = %= /= //= -= += *= **= 赋值运算符


    is is not 身份运算符


    in not in 成员运算符


    not or and 逻辑运算符


13 列表  可变

- lst.index('elem') 返回第一个elem 对应的 下标
- lst.count('elem') 返回elem的全部的个数
- list.remove('elem') 删除第一个值为elem的元素
- list.pop() 删除指定位置的元素 默认删除最后一个值 返回被删除的值 
- list.clear() 清空列表
- del list[:] 清空列表 
- del list 直接将 list 从内存中删除  而不是只是简单的清空
- del list[index] 删除指定位置的元素
- del list[start, end] 删除一定范围内的元素 注意左闭右开 [start, end)
- list.reverse() 列表反转 原地单转 改变自身
- list[::-1] 列表反转 形成一个新的列表 对自身没有影响
- 列表只要是切片操作  就会生成一个新的列表’
- reversed(list) 返回的是可迭代对象 需要再list() 转换成list 
- 列表排序  list.sort()
- 列表排序 sorted(list) 
  

14 元组 不可变

- 当创建的元组只有一个元素的时候 需要这样写 (only,)
- 创建空元组  t = tuple()  or  t = ()
- 元组和列表可以互相转换
  

15 字典 可变

- 键 必须是 可以hash的值 也就是不可变的值
- 值 是任意对象
- 查看元素  最好用  dict.get(key, defaultValue) 根据键值来查看元素 如果不存在 就返回 默认的值 
- 设置默认的值 dict.setdefault() 


16 集合 无序的不重复元素序列
- set() 创建集合
- s = {"a", "b"}
- set(["a"]) 可以传入一个列表 生成集合
- set.add() 加入元素 元素必须是可以hash的 字符串 数字等
- set.update() update 函数后可接集合，列表，元组，
字典等。
- set.remove(elem) 删除元素 如果不存在 就会报错
- set.discard(elem) 删除元素 存在则移除 不存在则不报错
- set.pop() 随机删除一个元素 注意不能传递任何参数
- set.clear() 清空集合
- 集合没法查询 修改 只能添加 删除
- 求合(并)集  set2.union(set1)  "|"
- 求差集 set1 中有的 set2 中没有的 找出差异  set1.difference(set2)  "-"
- 求交集 set1.intersection(set2) 得到共有的元素 不更改原本的 "&"
- 求交集 改变原本的集合 set1.intersection_update(set2) 改变了 set1 使得 set1 只保留 都有的部分
- 求两个集合中 不重复的元素 set1.symmetric_difference(set2) 
- 求两个集合中 不重复的元素 但是会改变原来的集合 set1.symmetric_difference_update(set2) 
- 判断两个集合是否有相同的元素 如果有则返回False 没有则返回True set1.isdisjoint(set2)
- 判断一个元素是否属于这个集合 in
- 判断是否是子集  set1.issubset(set2) 
- 
## 迭代器


17 **迭代器**

- 可迭代对象 凡是可以用for循环遍历的 都是可迭代对象 如 列表 字符串 元组 字典 
- 如何判断一个对象是 可迭代的  
  - `from collections.abc import Iterable`
  - `isinstance(elem, Iterable)`
  - 但是这种方式不是很准确 还是要 for 循环判断

- 可迭代协议

①如果一个对象的内部实现了 `__iter__()`方法 并且返回的是一个 迭代器实例 那么就是可迭代对象
```python
from collections.abc import Iterable
class Array:
    mylist = [1, 2, 3]
  # 返回迭代器类的实例
    def __iter__(self):
        return iter(self.mylist)

my_list = Array()
print(isinstance(mylist, Iterable)) # True
for i in my_list:
    print(i)
```

② 如果一个对象没有实现`__iter__()`方法 但是Python解释器`__getitem()__`方法获取元素，如果可行，那么这个对象也是一个可迭代的对象。
```python
from collections.abc import Iterable


class Array:
    mylist = [1, 3, 4]

    def __getitem__(self, item):
        return self.mylist[item]


# 得到一个可迭代的对象
my_list = Array()
print(isinstance(my_list, Iterable))  # False
for i in my_list:
    print(i)

```

此时如果你使用 `isinstance(my_list, Iterable)` 去判断是否是可迭代，就会返回 `False`，因为
`isinstance` 这种方法就是检查对象是否有 __iter__ 方法。这也论证了使用
`isinstance(my_list, Iterable)`去判断是否可迭代是不准确的。


当一个可迭代对象，使用`iter`调用的时候，就会返回一个迭代器对象，使用`next`调用的时候，可以依次取出元素，当全部获取完毕的时候，会抛出 `StopIteration` 错误。

```python
>>> alist = [1, 2, 3, 4]
>>> gen = iter(alist)
>>> next(gen)
1   
>>> next(gen)
2   
>>> next(gen)
3   
>>> next(gen)
4   
>>> next(gen)
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

迭代器协议

对比可迭代对象，迭代器的内部多了一个 `__next__()`函数，正是因为有这个函数，我们才可以使用`next()`来依次获取元素。

创建一个可迭代对象，并在可迭代对象上的基础上，实现一个迭代器
```python
from collections.abc import Iterator
# Iterator 迭代器


class Array:
    index = 0
    my_list = [1, 2, 3]

    # 返回该对象的迭代器类的实例
    # 因为自己就是迭代器 返回自己就可以
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.my_list):
            value = self.my_list[self.index]
            self.index += 1
            return value
        raise StopIteration


# 迭代器
my_iterator = iter(Array())
print(isinstance(my_iterator, Iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

```

## 生成器


18 **生成器** Generator

生成器的最主要目的是延时计算，防止数据量过大的情况下，造成内存消耗过猛。

- 列表推导的时候 使用 () 就是返回生成器

```python
>>> gen = (i for i in range(1, 10))
>>> gen 
<generator object <genexpr> at 0x0000018F6C1FECF0>
>>>
>>> l = list(gen) 
>>> l
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
```

- `yield`
  - yield 功能跟 return 相似 但是也有不同， 
  - 当一个函数运行到 yield 时候，函数会暂停，并会把 yield 后面的值 返回出去
  - 如果 yield 后面没有接任何值 那么就会返回 None
  - yield 虽然返回了 **但是函数并没有结束**



函数中有`yield`
```python
def generator_factory(top=5):
    index = 0
    while index < top:
        print(f"index 的值为: {str(index)}")
        index += 1
        yield index
    raise StopIteration


gen = generator_factory()
print(gen)
# <generator object generator_factory at 0x0000022A93515C10>
```

生成器的使用

- next(gen)
- for 循环取元素

生成器的激活
- next(gen)
- generator.send(None)


**关键是要明白 迭代器 生成器 在哪里使用！！**

生成器的生命周期流程
- `gen_created`:生成器已经被创建 但是并没有激活
- `gen_running`:解释器正在执行， 只有在多线程的时候 才会出现
- `gen_suspended`: 在 `yield` 表达式处 暂停
- `gen_closed` 生成器执行结束

**code implementation:**

```python
>>> gen = (i for i in range(1, 3))  
>>> gen
<generator object <genexpr> at 0x00000257A63BECF0>
>>> from inspect import getgeneratorstate 
>>> getgeneratorstate(gen)
'GEN_CREATED'
>>> next(gen)
1
>>> getgeneratorstate(gen)
'GEN_SUSPENDED'
>>> next(gen)
2
>>> next(gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> getgeneratorstate(gen) 
'GEN_CLOSED'
```

生成器，当自己不手动抛出异常的话，会自己抛出 `StopIteration`异常。

## 流程控制

19 **Flow Control 流程控制**


假值：None False () {} [] 0 等等

真值: True 非空

for 循环

循环的时候 索引 元素一起列出  就需要使用 枚举 `enumerate`函数

```python
for index, elem in enumerate(lst):
    pass

myList = ['apple', 'banana', 'pinapple']
for index, fruit in enumerate(myList):
    print(f"the {index} of fruit is {fruit}")
```

`break` 用来中断循环，当语句执行到break的时候 直接中断本次循环，如果是嵌套的循环，只会中止 break 所在的那层循环。
```python
myList = [10, 20]
for i in range(0, len(myList)):
    for j in range(1, myList[i]):
        print(j, end=" ")
        if myList[i] % j == 3:
            break
# 1 2 3 4 5 6 7  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

```
`continue` 跳过本次循环 开始下一次循环


for 循环后面其实是可以加 else 分支的，那么怎么样会走到else 分支呢， 只要循环没有被 break 掉，那么最终都会走到 else 分支 暂时不知道该在什么场景下使用。


20 **进阶** **五种推导式**


- 列表推导式 `aList = [i for i range(0, 10)]`
- 字典推导式 `dict = {x:x*x for x in range(0, 10)}`
- 集合推导式 `set = {x for x in range(10, 102)}`
- 生成器推导式 `gen = (x for x in range(0, 100))`


推导式 是可以嵌套的 但最好不要超过2次 不然难以理解

## 函数


21 函数

`def func(*args, **kw)` 注意可变参数

`*args` 传递的是元组 接收到的所有按照位置参数方式传递进来的参数，是一个元组类型 也叫 可变位置参数


`**kw` 传递的是 字典 接收到的所有按照关键字参数方式传递进来的参数，是一个字典类型 也叫可变关键字参数


参数的顺序 func(arg1, arg2="a", *args, **kw)

如果参数中 有单数的 * 那么在 * 后面的参数  必须要指定关键字参数传参  

func(a, c, * , m)

func(1, 2, m = 100)

**Warn!!! 
函数的参数 实际上传递的是 对象的内存地址 所以当参数是可变类型的时候，在函数内部进行修改的时候，就算没有返回，外面的值 也同样发生了变化。**


lambda 函数 lambda x: x * 2  他是表达式 不是一个语句  直接返回结果

---

进阶函数

map 函数 map(func, seq) 对序列中的每个元素都进行 func 操作 返回操作之后的序列 注意返回的是新的序列 不会改变原先的序列  默认返回的是 可迭代对象 


 过滤函数 filter(func, seq) 对序列中的元素进行筛选  符合条件的元素组成一个新的序列   filter(lambda x: x < 4, [1, 2, 3, 5, 6]) 默认返回的是 可迭代对象 


reduce 函数  from functools import reduce

functools.reduce(function, iterable[, initializer])

---


反射函数

dir() 返回传递给他的对象的属性名经过排序之后的列表

type() 返回对象的类型

hasattr()  判断对象是否含有某个属性

getattr() 获取到对象的某个属性 

id() 返回对象对应的内存地址  是一个整数

isinstance() 确定一个对象是否是某个特定的类型或定制类的实例 


callable() 确定一个对象是否是可以调用的 函数，类 这些对象都是可以调用的
对象

---

模块里面使用的反射函数  Modules


`__doc__` 查询模块的文档   `json.__doc__`

`__name__` 始终展示模块初始定义的名字 不在乎你在引入模块的时候 用的别名 

`__file__` 展示这个模块的路径明细  注意内建模块没有这个属性

`__dict__` 包含了模块里面可以用的属性名-属性的字典，就是可以使用模块.属性名 访问的对象


---

类中使用的反射函数 Class

`__doc__` 返回文档字符串 如果没有文档字符串 则返回 None


`__name__` 返回的始终是定义时 的类名


`__dict__` 包含了类里面可以用的属性名-属性的字典，就是可以使用模块.属性名 访问的对象


`__module__` 包含该类的定义的模块名；需要注意，是字符串形式的模块名而不是模块对象。

`__bases__` 直接父类对象的元素  注意是直接父类  不能再向上查找 


---

偏函数

偏函数（Partial Function），可以将某个函数的常用参数进行固定，避免每次调用时都要指定

```python
from functools import partial


def pow(x, n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


power_2 = partial(pow, n=2)
power_2(2)
print(power_2(2))
```

**函数进阶**

泛型 *singledispatch*

什么是泛型： 根据传入的参数的类型不同 调用不同的函数逻辑体 就叫做泛型


- 单分派 根据一个参数的类型 以不同的方式执行相同的操作的行为
- 多分派 可根据多个参数的类型选择专门的函数的行为
- 泛函数：多个函数绑在一起组合成一个泛函数

```python
from functools import singledispatch


@singledispatch
def age(obj):
    print("请传入合法类型的参数")


@age.register(int)
def _(age):
    print(f"我已经{age}岁了")


@age.register(str)
def _(age):
    print(f"我已经{age}岁了")


age(23)
age("twenty-three")
age(['23'])

# 我已经23岁了
# 我已经twenty-three岁了
# 请传入合法类型的参数

```

泛型的好处在于 不用再写那些烦人的 If else 判断，而是根据不同的参数 调用不同的函数  而且可以分割函数 有错误的时候 好修改




22 作用域


Python 作用分为 3 种

- L Local  局部作用域
- E Enclosing 闭包函数外的函数中
- G Global 全局作用域
- B Built-in 内建作用域

查找顺序  L  E  G   B 

影响变量 函数作用范围的有 
- 函数   def lambda
- 类  class 
- 关键字  global nonlocal
- 文件 *py
- 推导式 [],{},() 仅限 py3 


**闭包**

> 在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外
函数的返回值是内函数的引用。这样就构成了一个闭包。其实装饰函数，很多都
是闭包。
```python
def outer():
    temp = "just temp"
    def wrapper():
        return temp + "hello world"
    return wrapper
```

**一般情况下，在我们认知当中，如果一个函数结束，函数的内部所有东西都会释放掉，还给内存，
局部变量都会消失。但是闭包是一种特殊情况，如果外函数在结束的时候发现有自己的临时变量将
来会在内部函数中用到(读取)，就把这个临时变量绑定给了内部函数，然后自己再结束。**


如果不使用 += 、 -= 等一类的操作，不加nonlocal也没有关系。这就展示了闭包的特性。

```python
def outer():
    num = 1

    def inner():
        return num + 1
    return inner


res = outer()()
print(res)
# 2
相当于在内部函数读取了 num 的值 不会报错
```
```python
def outer():
    num = 1

    def inner():
        num += 2
        return num
    return inner


res = outer()()
print(res)
# UnboundLocalError: local variable 'num' referenced before assignment
参与赋值 加 运算 就会报错 
```
```python

def outer():
    num = 1

    def inner():
        nonlocal num
        num += 2
        return num
    return inner


res = outer()()
print(res)
# 3
加上nonlocal  就把他编程局部变量 随便运算 赋值 

```


变量集合 
- globals() 以dict的方式存储所有全局变量
- locals() 以dict的方式存储所有局部变量

## 上下文管理器

上下文管理器

```python
with open('test.txt') as f:
    f.readlines()
```


上下文管理器 可以用来 处理异常   

```python
class Resource:
    def __enter__(self):
        print("=====connect to resource")
        return self

    def __exit__(self, exec_type, exec_val, exec_tb):
        print("=====close resource connection")
        return True

    def operate(self):
        return 1 / 0


with Resource() as res:
    res.operate()
```

当出现异常的时候 可以在 `__exit__` 里面进行捕获 然后自己决定如何处理  如果返回 True  就不抛出  默认返回 False

在 写 `__exit__` 函数时，需要注意的事，它必须要有这三个参数：

exc_type：异常类型

exc_val：异常值

exc_tb：异常的错误栈信息

当主逻辑代码没有报异常时，这三个参数将都为None。



---

按照 contextlib 的协议来自己实现一个打开文件（with open）的上下文管理器

```python

import contextlib


@contextlib.contextmanager
def open_func(file_name):
    # __enter__ 方法
    print('open file', file_name, 'in __enter__')
    file_handler = open(file_name, 'r')

    # 重点 yield
    # 处理异常
    try:
        yield file_handler
    except Exception as exc:
        # deal with exception
        print("the exception is thrown")
    finally:
        # __exit__ 方法
        print('close file', file_name, 'in __exit__')
        file_handler.close()
        return


with open_func('test.txt') as file_in:
    for line in file_in:
        1 / 0
        print(line)

```

##  装饰器


装饰器 

装饰器本质上就是一个函数 它可以让其他的函数不改变任何代码的情况下，完成附加的功能 装饰器的返回值 也是一个函数对象

装饰器主要用于有切面的场景 比如 记录日志  性能测试 事务处理  缓存等

主要是代码复用  使得代码更加的优雅

主要掌握 6 种 装饰器的方法 见 ex16 - ex21

1 普通的装饰器

2 带参数的函数装饰器

3 类的装饰器

4 带参数的类的装饰器

5 使用偏函数和类 实现装饰器

6 能装饰类的装饰器



- 基于类装饰器的实现，必须实现 `__call__` 和 `__init__` 两个内置函数。
`__init__` ：接收被装饰函数
`__call__` ：实现装饰逻辑。

- 带参数和不带参数的类装饰器有很大的不同。
`__init__` ：不再接收被装饰函数，而是接收传入参数。
`__call__` ：接收被装饰函数，实现装饰逻辑。

- 除函数之外，类也可以是 callable 对象，只要实现了 `__call__` 函数（上面几个例子已经接触过
了）。
还有容易被人忽略的偏函数其实也是 callable 对象。

- Python 对某个对象是否能通过装饰器（ @decorator ）形式使用只有一个要求：decorator
必须是一个“可被调用（callable）的对象。也就是装饰器必须是个可被调用的对象


## 异常


异常处理

异常的类型可以看官方文档  https://docs.python.org/3/library/exceptions.html#%23


通过 `raise` 抛出异常

如何捕获异常


1 只是捕捉异常但是不具体显示异常

```python
try:
    codeA
except [exception]:
    codeB
```

2 捕捉异常 获取异常信息 把信息展示出来

```python
try:
    1 / 0
except ZeroDivisionError as e:
    print(f"errors happens, the error information is {str(e)}")
```


3 `try ----except ------else`

```python
try:
    codeA
except [exception] as e:
    codeB
else:
    codeC
```

如果 CodeA 有异常， 就进入 CodeB, 如果正常执行，就进 codeC

4 `try------except-------finally`

```python
try:
    codeA
except [exception] as e:
    codeB
finally:
    codeC
```

如果codeA 有异常 就进 CodeB , 不管有没有异常  都得走 finally 走


5 `try  except else finally ` 可以一起使用


捕获异常的前提条件是  你要知道 哪里会产生异常 然后预防性得进行处理


捕获多个异常 

1 一个 try 语句  多个 except 语句 只会找一个对应的异常进行处理 （只能处理一个异常）

```python
try:
    res = 1 / 0
except IOError:
    print("IOError")
except FloatingPointError:
    print("浮点数计算错误")
except ZeroDivisionError:
    print("除数不能为0")

# output  除数不能为0
```

2 一个 except 捕获多个异常

```python
try:
    res = 1 / 0
except IOError:
    print("IOError")
except (ZeroDivisionError, FloatingPointError):
    print("计算错误")

# output 计算错误
```
except 后面可以接多个 异常 只要匹配其中一个 就可以进行处理



自定义异常 需要用到 类的继承

关闭异常的 自动关联上下文


当我们处理异常的时候，如果处理的不当，会再产生异常，这样新的异常再出现的时候，以前的异常也会随着一起出现

```python 

# 如何取消异常处理的上下文管理


try:
    print(1 / 0)
except Exception as e:
    raise RuntimeError("Something bad happens")


"""
output

Traceback (most recent call last):
  File "C:\Users\IT\Desktop\python_i_know\ex23.py", line 5, in <module>
    print(1 / 0)
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\IT\Desktop\python_i_know\ex23.py", line 7, in <module>
    raise RuntimeError("Something bad happens")
RuntimeError: Something bad happens
"""
```

如果在异常处理程序或 finally 块中引发异常，默认情况下，异常机制会隐式工作会将先前的异常
附加为新异常的 `__context__`属性。这就是 Python 默认开启的自动关联异常上下文。 

也就是说 在捕捉异常A的时候 这时候产生了异常B 这时候我们不想显示异常A　或者说是　异常想知道异常B的来源　可以用一下的方式　　


使用 from 可以看到你的新异常是由 哪个引起的  
使用 with_traceback(tb) 更好的追踪异常的来源

> with_traceback(tb) 的官方文档
>
> 
> with_traceback(tb)
This method sets tb as the new traceback for the exception and returns the exception object. It was more commonly used before the exception chaining features of PEP 3134 became available. The following example shows how we can convert an instance of SomeException into an instance of OtherException while preserving the traceback. Once raised, the current frame is pushed onto the traceback of the OtherException, as would have happened to the traceback of the original SomeException had we allowed it to propagate to the caller.

```python
try:
    ...
except SomeException:
    tb = sys.exception().__traceback__
    raise OtherException(...).with_traceback(tb)

```


```python
try:
    print(1 / 0)
except Exception as e:
    raise RuntimeError("something bad happened") from e

"""output


Traceback (most recent call last):
  File "C:\Users\IT\Desktop\python_i_know\ex24.py", line 2, in <module>
    print(1 / 0)
ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:
(上面的异常是下面的异常的最直接原因)

Traceback (most recent call last):
  File "C:\Users\IT\Desktop\python_i_know\ex24.py", line 4, in <module>
    raise RuntimeError("something bad happened") from e
RuntimeError: something bad happened
"""
```

```python 
try:
    print(1 / 0)
except Exception as e:
    # tb = e.__traceback__
    raise RuntimeError("something bad happened").with_traceback(
        e.__traceback__)
"""
Traceback (most recent call last):
  File "C:\Users\IT\Desktop\python_i_know\ex25.py", line 2, in <module>
    print(1 / 0)
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\IT\Desktop\python_i_know\ex25.py", line 5, in <module>
    raise RuntimeError("something bad happened").with_traceback(
  File "C:\Users\IT\Desktop\python_i_know\ex25.py", line 2, in <module>
    print(1 / 0)
RuntimeError: something bad happened


"""

```

不想显示异常A (关闭自动关联异常上下文的机制)


```python
try:
    print(1 / 0)
except Exception as e:
    raise RuntimeError("something is wrong.") from None

"""
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: something is wrong.
"""

```


注意Exception 类的继承顺序问题

```python
"""
except 里面如果是 class 的话 注意继承问题
"""


class A(Exception):
    pass


class B(A):
    pass


class C(B):
    pass

# A 继承于 Exception    B 继承于 A     C 继承于 B


for cls in [A, B, C]:
    try:
        raise cls()
    except C:
        print("C")
    except B:
        print("B")
    except A:
        print("A")


# output
# C
# B
# A


for cls in [A, B, C]:
    try:
        raise cls()
    except A:
        print("A")
    except B:
        print("B")
    except C:
        print("C")

# output
# A
# A
# B

```


一般处理异常的方式是 将异常打印出来或者写在日志里 然后将他们在 raise 出来 进行处理

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error", err)
except ValueError:
    print("could not convert data to int")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

# OS error [Errno 2] No such file or directory: 'myfile.txt'

```


**If the finally clause executes a `break, continue or return statement`, exceptions are not re-raised.**

如果在 `finally` 代码块中 有 `break, continue or return`等语句 那么异常就不会被再次抛出

```python
def divide():
    try:
        print(1 / 0)
    finally:
        return 1


print(divide())
# output
# 1
```


---

If the try statement reaches a break, continue or return statement, the finally clause will execute just prior to the break, continue or return statement’s execution.

如果try语句里面有 break continue return 语句，那么 finally 代码块 就会在 break continue return 之前先执行
```python
def add():
    try:
        return 2
    finally:
        print("execute first")


# add()
print(add())
'''
output
execute first
2
'''
```
---

If a finally clause includes a return statement, the returned value will be the one from the finally clause’s return statement, not the value from the try clause’s return statement.

如果 finally 代码块包含 return 语句，那么返回值 将会是 finally return 语句返回的值 而不是 try 语句里面 return 语句返回的值 

```python

def boolReturn():
    try:
        return True
    finally:
        return False
boolReturn()
# output
# False
```



在现实生活中的应用中，一般  `finally` 代码块 都会用在 释放额外的资源中， 比如文件资源 网络连接 等等，不管是否成功的使用了这些资源。

---

函数的返回值是否可以用 `None`， 可以看函数名，如果函数名可以看出来没有返回值 就可以返回 `None`




## 类


### 类的方法

1 静态方法 有`staticmethod` 装饰的函数

2 类方法 有 `classmethod` 装饰的函数

3 实例方法  没有任何装饰器装饰的普通函数


```python
class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} 已经跑起来了")

    @staticmethod
    def eat():
        print("just eating")

    @classmethod
    def jump(cls, name):
        print(f"{name}跳起来了")


pig = Animal("bob")
pig.run()
Animal.jump("Alice")
pig.jump("pig")
Animal.eat()
pig.eat()

# bob 已经跑起来了
# Alice跳起来了
# pig跳起来了
# just eating
# just eating

```
实例也可以调用静态方法

实例也可以调用类方法  不过注意要填入参数



方法与函数的区别

1. 普通函数（未定义在类里）和静态方法（`@staticmethod`），都是函数（ `function` ）。
   
2. 实例方法和类方法，都是方法（ `method`）。



方法本质上还是函数，但是他与对象（实例或者类）进行了某种绑定，就变得不纯洁，就与函数产生了差别。


### 私有变量与私有方法


下划线：

魔法方法 构造函数需要使用下划线

对于暂时用不到的变量值 可以赋值给`_`进行占位 在 `for` 循环中经常使用


下划线的分类：


- 单前导下划线 `_var`
- 单末尾下划线 `var_`
- 双前导下划线 `__var`
- 双前导和末尾下划线`__var__`
- 单下划线`_`


单前导下划线`_var`

**以单个下划线开头的变量或者方法 仅供内部使用**实际上在创建实例之后，依然是可以访问到的，但是我们约定这样的格式表示内部的，最好不要在外部进行访问。


双前导下划线 `__var`

双下划线前缀会导致Python解释器重写属性名称，以避免子类中的命名冲突。
这也叫做名称修饰(name mangling) - 解释器更改变量的名称，以便在类被扩展的时候不容易产生冲
突

使用双下划线开头的属性方法 就是私有属性或者方法。，必须得通过 `实例._类名__属性名（方法名）`来调用


### 类的封装（Encapsulation）

```python
# 封装
# 保护私有变量 通过接口释放相关的信息


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def is_adult(self):
        return self.__age >= 18


alice = Person("alice", 19)
print(alice.is_adult())

```


### 类的继承（Inheritance）

多继承


```python
# 多继承
class D:
    pass


class C(D):
    pass


class B(C):
    def show(self):
        print("i am B")


class G:
    pass


class F(G):
    pass


class E(F):
    def show(self):
        print("i am E")


class A(B, E):
    pass


a = A()
a.show()
# i am B

```

继承关系 

![继承关系](https://github.com/chenjixiv587/python_i_know/assets/112852746/7e9fa380-3b71-4dda-bd8f-1efa7cb988e0)


### 类的多态（Polymorphism）

 Python 中非常有名鸭子类型：一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可
以被看做是鸭子。

### 类的 property 属性

为了实现属性的合法性校验，Python 引入的 property 属性。

```python
class Student:
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0 and value <= 50:
            self.__age = value
        else:
            raise ValueError("age must be in [1, 50]")


s = Student()
s.age = -20

# Traceback (most recent call last):
#   File "C:\Users\IT\Desktop\python_i_know\ex36.py", line 15, in <module>
#     s.age = -20
#     ^^^^^
#   File "C:\Users\IT\Desktop\python_i_know\ex36.py", line 11, in age
#     raise ValueError("age must be in [1, 50]")
# ValueError: age must be in [1, 50]

```
`@property` 其实就是一个装饰器， 将一个函数改造成一个属性。

在读取属性的时候 就进入 `@property` 所装饰的函数中(函数名就是属性名字)进行执行

在写入属性的时候 就进入`@函数名.setter` 所装饰的函数中 进行执行 一般都是进行数据的校验  

两个装饰器 一定是  `@property` 在前 `@函数名.setter`  在后



### 类的 Mixin 设计模式


Mixin 是增强类 

> 飞行只是飞机做为交通工具的一种（增强）属性，我们可以为这个飞
行的功能单独定义一个（增强）类，称之为 Mixin 类。这个类，是做为增强功能，添加到子类中
的。为了让其他开发者，一看就知道这是个 Mixin 类，一般都要求开发者遵循规范，在类名末尾加
上 Mixin 。


```python

class Vehicle:
    pass
class PlaneMixin:
    def fly(self):
        print("I am flying.")
class Airplane(Vehicle, PlaneMixin):
    pass

```


使用Mixin类实现多重继承要遵循以下几个规范

责任明确：必须表示某一种功能，而不是某个物品；

功能单一：若有多个功能，那就写多个Mixin类；

绝对独立：不能依赖于子类的实现；子类即便没有继承这个Mixin类，也照样可以工作，就是缺
少了某个功能。
 
### 类的魔术方法（超全整理）

**有点基础 有实践后再看**

### 神奇的元类编程（metaclass）

> type通常用法就是用来判断对象的类型。但除此之外，他最大的用途是用来动态创建类。当
Python扫描到class的语法的时候，就会调用type函数进行类的创建。


那么如何使用 type() 来动态的创建类呢 


type() 需要接收三个参数 


    1 类的名称 如果没有指定 也必须要传入空字符串 `""`

    2 父类 注意这个传入的时候要以 tuple 的形式传入  如果没有父类的话 也必须要传入空的tuple （）， 默认继承的是 `object`

    3 绑定的方法或者属性 注意以 `dict`的形式传入


```python
# prepare a base class

class BaseClass:
    def talk(self):
        print("i am people")

# 准备一个方法

def say(self):
    print("hello")


# 使用 type()来动态的创建 User 类


User = type("User", (BaseClass, ), {"name":"user", "say":say})
```


元类 就是创建类的模板

