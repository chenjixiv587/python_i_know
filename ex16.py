# 1 简单的装饰器

def logger(func):
    def wrapper(*args, **kw):
        print(f"ready to execute the func {func.__name__}")

        # 真正的执行
        func(*args, **kw)

        print("the execute is ending")
    return wrapper


@logger
def add(x, y):
    print(f"{x} + {y} = {x + y}")


add(2, 3)
