a = [1, 2, 3, 4, 5]
#    0  1  2  3  4
#   -5 -4 -3 -2 -1

slice = a[1:4]
print(slice)  # тоже лист

slice = a[1:2]
print(slice)

slice = a[:-1]
print(slice)

slice = a[2:]
print(slice)

length = len(a)
s = sum(a)
mx = max(a)
mn = min(a)

a.append(6)
a.insert(2, 0)
print(a)

# a.remove(8)
# print(a)

a.pop(3)
print(a)

x = a.pop()
print(x, a)

del a[3]
print(a)

print(f'There is {a.count(1)} elements that equal to 1 in the list')

mx = max(a)
print(a.index(mx))

a.sort()
print(a)

a.reverse()
print(a)

a.sort(reverse=True)
print(a)

b = ['Bekaidar', 'Dulat', 'Ildar', 'Zhandos']


def f(name):
    return name[-1]


b.sort(key=f)


b.sort(key=lambda name: name[-1])
print(b)

c = a + b
print(c)

a.extend(b)
print(a)

a.extend((1, 2, 3))
print(a)

# a = a + (1, 2, 3)
# print(a)

d = []
for i in range(11):
    d.append(i)
print(d)

d = [i for i in range(11)]
print(d)

d = [i for i in range(11) if i % 2 == 0]
print(d)

d = [i * j for i in range(1, 3) for j in range(1, 3)]
print(d)

for i in range(1, 3):
    for j in range(1, 3):
        d.append(i * j)


