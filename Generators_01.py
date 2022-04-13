def mygenerator():
    yield 3
    yield 1
    yield 2

g = mygenerator()
print(sorted(g))