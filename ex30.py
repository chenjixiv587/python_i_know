"""
If the try statement reaches a break, continue or return statement, 
the finally clause will execute just prior to the break, 
continue or return statement’s execution.

如果try语句里面有 break continue return 语句，
那么 finally 代码块 就会在 break continue return 之前先执行


"""


def add():
    try:
        return 2
    finally:
        print("execute first")


# add()
print(add())
'''
output
execute first
2
'''
