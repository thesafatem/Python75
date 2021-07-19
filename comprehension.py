a = []
for i in range(1, 11):
    a.append(i)
print(a)

b = [i for i in range(1, 11)]
print(b)

c = [i ** 2 for i in range(1, 11)]
print(c)

d = [i for i in range(2, 21, 2)]
print(d)

e = [i for i in range(2, 21) if i % 2 == 0]
# for i in range(2, 21):
#     if i % 2 == 0:
#         e.append(i)
print(e)

# for i in range(1, 4):
#     for j in range(1, 4):
#         f.append(i * j)
f = [i * j for i in range(1, 4) for j in range(1, 4)]
print(f)