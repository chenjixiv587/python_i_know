# 4 带参数的类装饰器
class Logger:
    def __init__(self, level="INFO"):
        self.level = level

    def __call__(self, func):  # 接受函数
        # 再次嵌套
        def wrapper(*args, **kw):
            print(f"{self.level}: the function {func.__name__} is running")
            func(*args, **kw)
        return wrapper  # 返回函数


@Logger(level="WARNING")
def say(something):
    print(f"say {something}")


say("fight!")
