d = {}
d = dict()
d = {
    'Masha': 5,
    'Petya': 5,
    'Ruslan': 4,
    'Eva': 5
}

print(d['Ruslan'])
print(d.get('Petya'))
# print(d['Sasha']) ERROR
print(d.get('Sasha'))

d['Eva'] = 3
print(d)
# d.get('Eva') = 5 SYNTAX ERROR

d['Sasha'] = 4
print(d)

d.update({
    'Nina': 5,
    'Vova': 3
})
print(d)

d.update({
    'Nina': 4,
    'Vova': 4
})
print(d)

d.pop('Sasha')
print(d)

d.popitem()
print(d)

del d['Ruslan']
print(d)

d.clear()
print(d)

del d
# print(d)


d = {
    'Masha': 5,
    'Petya': 5,
    'Ruslan': 4,
    'Eva': 5
}

for x in d:
    print(x, end=' ')
print()

print(d.keys(), type(d.keys()))
for key in d.keys():
    print(key, end=' ')
print()

print(d.values(), type(d.values()))
for value in d.values():
    print(value, end=' ')
print()

print(d.items(), type(d.items()))
for key, value in d.items():
    print(key, value)

# a = [(1, 2, 0), (3, 4, 0), (5, 6, 0)]
# for x, y, z in a:
#     print(x, y, z)

a = {
    1: 2,
    3: 4
}
b = a
b[5] = 6
print(a, b)
c = a.copy()
c[7] = 8
print(a, c)

marks = {
    'math': {
        'Masha': 5,
        'Petya': 4
    },
    'russian': {
        'Masha': 4,
        'Petya': 5
    },
    'physics': {
        'Masha': 3,
        'Petya': 3
    }
}
print(marks['russian']['Masha'])
