def generator_factory(top=5):
    index = 0
    while index < top:
        print(f"the value of index is {str(index)}")
        index += 1
        yield index
    raise StopIteration


gen = generator_factory()
index = gen.send(None)
print(index)
