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
