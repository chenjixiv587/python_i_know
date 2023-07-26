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
