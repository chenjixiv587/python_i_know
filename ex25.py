try:
    print(1 / 0)
except Exception as e:
    # tb = e.__traceback__
    raise RuntimeError("something bad happened").with_traceback(
        e.__traceback__)
"""
Traceback (most recent call last):
  File "C:\Users\IT\Desktop\python_i_know\ex25.py", line 2, in <module>
    print(1 / 0)
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\IT\Desktop\python_i_know\ex25.py", line 5, in <module>
    raise RuntimeError("something bad happened").with_traceback(
  File "C:\Users\IT\Desktop\python_i_know\ex25.py", line 2, in <module>
    print(1 / 0)
RuntimeError: something bad happened


"""