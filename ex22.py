# 自定义 异常

class InputError(Exception):
    def __init__(self, msg):
        self.msg = msg

    # 当我们对对象进行print的时候 返回这个方法里面的值
    def __str__(self):
        return self.msg


# inputError = InputError("waring")
# print(inputError)

def getInput():
    name = input("What is your name?")
    if name == "":
        raise InputError("No information here")


try:
    getInput()
except InputError as e:
    print(e)
finally:
    print("Get the work done! guys")
