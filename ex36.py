class Student:
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0 and value <= 50:
            self.__age = value
        else:
            raise ValueError("age must be in [1, 50]")


s = Student()
s.age = -20

# Traceback (most recent call last):
#   File "C:\Users\IT\Desktop\python_i_know\ex36.py", line 15, in <module>
#     s.age = -20
#     ^^^^^
#   File "C:\Users\IT\Desktop\python_i_know\ex36.py", line 11, in age
#     raise ValueError("age must be in [1, 50]")
# ValueError: age must be in [1, 50]
