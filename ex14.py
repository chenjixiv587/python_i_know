class Resource:
    def __enter__(self):
        print("=====connect to resource")
        return self

    def __exit__(self, exec_type, exec_val, exec_tb):
        print("=====close resource connection")

    def operate(self):
        print("=====in operation====")


with Resource() as res:
    res.operate()

'''
=====connect to resource
=====in operation====
=====close resource connection
'''
