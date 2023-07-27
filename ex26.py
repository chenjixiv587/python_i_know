"""
except 里面如果是 class 的话 注意继承问题
"""


class A(Exception):
    pass


class B(A):
    pass


class C(B):
    pass

# A 继承于 Exception    B 继承于 A     C 继承于 B


for cls in [A, B, C]:
    try:
        raise cls()
    except C:
        print("C")
    except B:
        print("B")
    except A:
        print("A")


# output
# C
# B
# A


for cls in [A, B, C]:
    try:
        raise cls()
    except A:
        print("A")
    except B:
        print("B")
    except C:
        print("C")

# output
# A
# A
# B
