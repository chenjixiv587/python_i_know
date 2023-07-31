class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} 已经跑起来了")

    @staticmethod
    def eat():
        print("just eating")

    @classmethod
    def jump(cls, name):
        print(f"{name}跳起来了")


pig = Animal("bob")
pig.run()
Animal.jump("Alice")
pig.jump("pig")
Animal.eat()
pig.eat()

# bob 已经跑起来了
# Alice跳起来了
# pig跳起来了
# just eating
# just eating
