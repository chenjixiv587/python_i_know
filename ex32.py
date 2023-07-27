
# 3.11 新特性 异常组
def f():
    raise ExceptionGroup(
        "group1", [OSError(1), SystemError(2), ExceptionGroup("group2", [OSError(3), RecursionError(4)])])


try:
    f()

except* OSError as e:
    print("there were OSErrors")

except* SystemError as e:
    print("there were SystemErrors")


# there were OSErrors
# there were SystemErrors
#   + Exception Group Traceback (most recent call last):
#   |   File "C:\Users\IT\Desktop\python_i_know\ex32.py", line 9, in <module>
#   |     f()
#   |   File "C:\Users\IT\Desktop\python_i_know\ex32.py", line 4, in f
#   |     raise ExceptionGroup(
#   | ExceptionGroup: group1 (1 sub-exception)
#   +-+---------------- 1 ----------------
#     | ExceptionGroup: group2 (1 sub-exception)
#     +-+---------------- 1 ----------------
#       | RecursionError: 4
#       +------------------------------------
