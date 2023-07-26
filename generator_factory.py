def generator_factory(top=5):
    index = 0
    while index < top:
        print(f"index 的值为: {str(index)}")
        index += 1
        yield index
    raise StopIteration


gen = generator_factory()
print(gen)
# <generator object generator_factory at 0x0000022A93515C10>

index = next(gen)
print(index)
