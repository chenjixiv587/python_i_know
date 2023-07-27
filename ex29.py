"""
If the finally clause executes a `break, continue or return statement`, 
exceptions are not re-raised.

如果在 `finally` 代码块中 有 `break, continue or return`等语句 
那么异常就不会被再次抛出
"""


def divide():
    try:
        print(1 / 0)
    finally:
        return 1


print(divide())
# output
# 1
