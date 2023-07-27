import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error", err)
except ValueError:
    print("could not convert data to int")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

# OS error [Errno 2] No such file or directory: 'myfile.txt'
