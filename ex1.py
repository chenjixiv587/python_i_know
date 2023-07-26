from collections.abc import Iterable


class Array:
    mylist = [1, 2, 3]

    # 返回迭代器类的实例
    def __iter__(self):
        return iter(self.mylist)


my_list = Array()
print(isinstance(my_list, Iterable))  # True
for i in my_list:
    print(i)
