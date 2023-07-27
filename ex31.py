# 处理多个异常

def f():
    excs = [OSError("error 1"), SystemError("error 2")]
    raise ExceptionGroup("there were problems", excs)

# 执行 f() 得到如下的结果
# f()


# + Exception Group Traceback (most recent call last):
#   |   File "C:\Users\IT\Desktop\python_i_know\ex31.py", line 11, in <module>
#   |     f()
#   |   File "C:\Users\IT\Desktop\python_i_know\ex31.py", line 8, in f
#   |     raise ExceptionGroup("there were problems", excs)
#   | exceptiongroup.ExceptionGroup: there were problems (2 sub-exceptions)
#   +-+---------------- 1 ----------------
#     | OSError: error 1
#     +---------------- 2 ----------------
#     | SystemError: error 2
#     +------------------------------------


try:
    f()
except Exception as e:
    print(f" caught {type(e)} : e")
#  caught <class 'exceptiongroup.ExceptionGroup'> : e
