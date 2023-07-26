def foo():
    print("i am a function")


def bar():
    foo = "i am a fake"
    foo_dump = globals().get("foo")
    foo_dump()


bar()
# i am a function
