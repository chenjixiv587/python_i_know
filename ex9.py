from functools import singledispatch


def check_type(func):
    def wrapper(*args):
        arg1, arg2 = args[:2]
        if type(arg1) != type(arg2):
            return "【错误】不同的类型 不能进行拼接"
        return func(*args)
    return wrapper


@singledispatch
def add(one_obj, another_obj):
    raise TypeError


@add.register(str)
@check_type
def _(one_obj, another_obj):
    one_obj += another_obj
    return one_obj


@add.register(list)
@check_type
def _(one_obj, another_obj):
    one_obj.extend(another_obj)
    return one_obj


@add.register(dict)
@check_type
def _(one_obj, another_obj):
    one_obj.update(another_obj)
    return one_obj


@add.register(tuple)
@check_type
def _(one_obj, another_obj):
    return (one_obj, another_obj)


print(add('hello', ', world'))
print(add([1, 2, 3], [4, 5, 6]))
print(add({'name': 'wangbm'}, {'age': 25}))
print(add(('apple', 'huawei'), ('vivo', 'oppo')))
# list 字符串 无法拼接
print(add([1, 2, 3], '4,5,6'))
print(add(2, 3))
# hello, world
# [1, 2, 3, 4, 5, 6]
# {'name': 'wangbm', 'age': 25}
# (('apple', 'huawei'), ('vivo', 'oppo'))
# 【错误】不同的类型 不能进行拼接
# TypeError
