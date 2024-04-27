l1 = ['a','b','c','d','e']

ilist = iter(l1)

print(next(ilist))
print(next(ilist))
print(next(ilist))
print(next(ilist))
print(next(ilist))

l2 = [10,20,30,40,50]
iterlist = l2.__iter__()

for i in iterlist:
    print(i)

# print(iterlist.__next__())
# print(iterlist.__next__())
# print(iterlist.__next__())
# print(iterlist.__next__())
# print(iterlist.__next__())
