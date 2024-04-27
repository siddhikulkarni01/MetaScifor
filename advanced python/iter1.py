def itr():
    yield 1
    yield 2
    yield 3

gen = itr()

for i in gen:
    print(i)