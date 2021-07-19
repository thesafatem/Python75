def f(x):
    return x + 1
    # print(x + 1)


f2 = lambda x: x + 1

print(f(5), f2(5))


is_vowel = lambda ch: ch in ['a', 'o', 'u', 'i', 'e']
print(is_vowel('a'), is_vowel('b'))


how_many_vowels = lambda name: sum(list(map(is_vowel, name.lower())))


names = ['Zhandos', 'Bekaidar', 'Ildar', 'Dulat']
print(list(map(how_many_vowels, names)))


