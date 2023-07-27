# 6 能装饰类的装饰器
# 装饰器版本的单例

instances: dict = {}


def singleton(cls):
    def get_instance(*args, **kw):
        cls_name = cls.__name__
        print("=====1=====")
        if cls_name not in instances:
            print("======2======")
            instance = cls(*args, **kw)
            instances[cls_name] = instance
        return instances[cls_name]
    return get_instance


@singleton
class User:
    _instance = None

    def __init__(self, name):
        print("=====3=====")
        self.name = name


a = User("chen1")
a.age = 100
b = User("cwei")
print(b.age)
print(a is b)
print(User.__name__)
