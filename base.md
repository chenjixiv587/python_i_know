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



















