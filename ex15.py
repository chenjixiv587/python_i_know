import contextlib


@contextlib.contextmanager
def open_func(file_name):
    # __enter__ 方法
    print('open file', file_name, 'in __enter__')
    file_handler = open(file_name, 'r')

    # 重点 yield
    # 处理异常
    try:
        yield file_handler
    except Exception as exc:
        # deal with exception
        print("the exception is thrown")
    finally:
        # __exit__ 方法
        print('close file', file_name, 'in __exit__')
        file_handler.close()
        return


with open_func('test.txt') as file_in:
    for line in file_in:
        1 / 0
        print(line)
