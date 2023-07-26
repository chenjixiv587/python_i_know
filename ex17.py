# 2 带参数的函数装饰器

def say_hello(country):
    def wrapper(func):
        def deco(*args, **kw):
            if country == "china":
                print("你好")
            elif country == "america":
                print("hello")
            else:
                return
        # 真正执行函数的地方
            func(*args, **kw)
        return deco
    return wrapper


@say_hello("china")
def xiaoming():
    pass


@say_hello("america")
def jack():
    pass


xiaoming()
print("-------")
jack()
