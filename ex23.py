# 如何取消异常处理的上下文管理


try:
    print(1 / 0)
except Exception as e:
    raise RuntimeError("Something bad happens")


"""
output

Traceback (most recent call last):
  File "C:\Users\IT\Desktop\python_i_know\ex23.py", line 5, in <module>
    print(1 / 0)
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\IT\Desktop\python_i_know\ex23.py", line 7, in <module>
    raise RuntimeError("Something bad happens")
RuntimeError: Something bad happens
"""