# 3 不带参数的类 装饰器
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kw):
        print(f"[INFO]: the function {self.func.__name__} is running!")
        return self.func(*args, **kw)


@Logger
def say(something):
    print(f"say {something}!")


say("hello")
