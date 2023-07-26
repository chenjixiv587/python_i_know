other = "test"


def foo():
    name = "chen"
    gender = "male"
    for key, value in locals().items():
        print(key, "=", value)


foo()
print(locals())
print(globals())
# name = chen
# gender = male
