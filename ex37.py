

# 使用 type()来动态的创建 User 类

# prepare a base class

class BaseClass:
    def talk(self):
        print("i am people")

# 准备一个方法


def say(self):
    print("hello")


# 使用 type()来动态的创建 User 类


User = type("User", (BaseClass, ), {"name": "user", "say": say})

user = User()

print(user.name)





