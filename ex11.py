def outer():
    num = 1

    def inner():
        nonlocal num
        num += 2
        return num
    return inner


res = outer()()
print(res)
# 3
