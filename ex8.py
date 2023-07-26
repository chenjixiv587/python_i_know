from functools import singledispatch


@singledispatch
def age(obj):
    print("请传入合法类型的参数")


@age.register(int)
def _(age):
    print(f"我已经{age}岁了")


@age.register(str)
def _(age):
    print(f"我已经{age}岁了")


age(23)
age("twenty-three")
age(['23'])

# 我已经23岁了
# 我已经twenty-three岁了
# 请传入合法类型的参数
