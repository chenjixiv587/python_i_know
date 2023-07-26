# 5 使用偏函数与类实现装饰器

import time
import functools


class DelayFunc:
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kw):
        print(f"wait for {self.duration} seconds..")
        time.sleep(self.duration)
        return self.func(*args, **kw)

    def eager_call(self, *args, **kw):
        print("Call without delay")
        return self.func(*args, **kw)

# 此时 delay 就是装饰器


def delay(duration):
    """
    装饰器：推迟某个函数的执行 同时提供 .eager_call 方法 立即执行
    """
    # 为了减少额外的函数 直接使用偏函数进行构造实例

    return functools.partial(DelayFunc, duration)


@delay(duration=2)
def add(a, b):
    return a + b


# add(1, 2)
print(add(1, 2))
