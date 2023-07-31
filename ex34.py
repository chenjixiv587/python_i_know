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
