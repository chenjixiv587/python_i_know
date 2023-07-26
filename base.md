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

16 **迭代器**

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









