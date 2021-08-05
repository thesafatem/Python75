a = {1, 2, 3}
b = {1, 2, 3, 2}
c = set()
print(a, b)

for el in a:
    print(el)


print(f"Size of set is {len(a)}")

a.add(4)
print(a)
a.add(1)
print(a)

a.update({1, 3, 5})
print(a)

a.remove(3)
print(a)
# a.remove(10) ERROR
# print(a)
a.discard(10)
print(a)
x = a.pop()
print(a, x)
a.clear()
print(a)
del a

b = {1, 2, 3}
c = {2, 4, 6}
d = b.union(c)
print(d)
b.update(c)
print(b)

b = {1, 2, 3}
c = {2, 4, 6}
d = b.intersection(c)
print(d)
b.intersection_update(c)
print(b)

b = {1, 2, 3}
c = {2, 4, 6}
d = b.symmetric_difference(c)
print(d)
b.symmetric_difference_update(c)
print(b)

b = {1, 2, 3, 4, 5}
c = {1, 2, 3}
print(c.issubset(b))
print(b.issuperset(c))
print(b.isdisjoint(c))

a = 5
b = a
b += 1
print(a, b)
print(hex(id(a))) # hexadecimal

a = {1, 2, 3}
b = a
b.add(4)
print(a, b)
c = a.copy()
c.add(5)
print(a, b, c)

