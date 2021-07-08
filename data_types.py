s = 'abc'
a = 5
b = 5.5
t = True
n = None
# print(type(s))
# print(type(a))
# print(type(b))
# print(type(t))
# print(type(n))

s = '505'
print(type(s))
s = int(s)
print(type(s))

# s = 'abc'
# s = int(s)

b = True
print(b)
b = int(b)
print(b)

print(2 + True)

a = [1, 2, 1, 1, 1, 2, 1, 2, 2]
# print(sum(a))
print(a.count(2))

cnt = 0
for i in range(len(a)):
    cnt += a[i] == 2

b = [None, False, 5.5, -100, 'abc']
print(b.count(None))