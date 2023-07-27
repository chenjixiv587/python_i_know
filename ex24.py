try:
    print(1 / 0)
except Exception as e:
    raise RuntimeError("something bad happened") from e

"""output


Traceback (most recent call last):
  File "C:\Users\IT\Desktop\python_i_know\ex24.py", line 2, in <module>
    print(1 / 0)
ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\IT\Desktop\python_i_know\ex24.py", line 4, in <module>
    raise RuntimeError("something bad happened") from e
RuntimeError: something bad happened
"""