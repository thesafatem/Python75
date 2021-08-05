a = (1, 2, 3)

for i in range(len(a)):
    print(a[i])

# a[1] = 7 ERROR

b = (1)
print(b, type(b))

c = (1,)
print(c, type(c))

d = (c)
print(d, type(d))

a2 = list(a)
# a2 = [1, 2, 3]
a2[1] = 7
# a2 = [1, 7, 3]
a = tuple(a2)
# a = (1, 7, 3)

