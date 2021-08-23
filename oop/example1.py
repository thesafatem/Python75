class Cat:
    breed = 'Scottish'
    eye_color = 'blue'

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        return f"{self.breed} {self.eye_color} {self.age} {self.name}"

    def __repr__(self):
        return f"{self.breed} {self.age}"

    def show_object(self):
        return f"{self.breed} {self.eye_color} {self.age} {self.name}"

    def show_age(this):
        print(this.age)

    def show_name(self):
        print(self.name)

cat1 = Cat(3, 'Murka')
cat2 = Cat(2, 'Snezhok')
print(cat1.breed, cat1.eye_color, cat1.age, cat1.name)
print(cat2.breed, cat2.eye_color, cat2.age, cat2.name)

cat1.breed = 'Siam'
print(cat1.breed, cat2.breed)

print(dir(Cat))

print(type(Cat))

cat1.show_age()
cat2.show_name()

print(cat1)
print(cat1.show_object())

cats = [cat1, cat2]
print(cats)
