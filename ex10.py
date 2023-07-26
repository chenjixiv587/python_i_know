def outer():
    lst = [1, 3, 4]

    def inner():
        lst.append(45)
        return lst
    return inner


res = outer()()
print(res)
