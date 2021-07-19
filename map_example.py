l = input()
print(l, type(l))

s = l.split()
print(s, type(s))

# for i in range(len(s)):
#     s[i] = int(s[i])
# print(s)

s = list(map(int, s))
print(s)


def f(x):
    return x + 1

# s = [1, 2, 3, 4, 5]


for i in range(len(s)):
    s[i] = f(s[i])


s = list(map(f, s))
print(s)


names = ['Zhandos', 'Bekaidar', 'Ildar', 'Dulat']


def f(name):
    return len(name)


len_names = list(map(f, names))

print(len_names)


def how_many_vowels(name):
    def f(ch):
        return ch in ['a', 'o', 'u', 'i', 'e']
    return sum(list(map(f, name.lower())))


vowels = list(map(how_many_vowels, names))
print(vowels)