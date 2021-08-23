from abc import ABC, abstractmethod

class Pet(ABC):
    @abstractmethod
    def __init__(self, name, age, breed, color):
        self.__name = name
        self.age = age
        self.breed = breed
        self.color = color


    def __str__(self):
        return f"{self.__name}\n{self.age}\n{self.breed}\n{self.color}"

    @abstractmethod
    def voice(self):
        pass


class Cat(Pet):
    def __init__(self, name, age, breed, color, eye_color):
        self.eye_color = eye_color
        super().__init__(name, age, breed, color)

    def __str__(self):
        return f"{super().__str__()}\n{self.eye_color}"

    def voice(self):
        print("Meow")


class Dog(Pet):
    def __init__(self, name, age, breed, color, food):
        self.food = food
        super().__init__(name, age, breed, color)

    def __str__(self):
        return f"{super().__str__()}\n{self.food}"

    def voice(self):
        print("Bark")


cat1 = Cat('Murka', 2, 'Scottish', 'white', 'blue')
dog1 = Dog('Muhtar', 5, 'Ovcharka', 'brown', 'bone')

print(cat1, dog1, sep='\n')

cat2 = Cat('Murka', 2, 'Scottish', 'white', 'blue')
dog2 = Dog('Muhtar', 5, 'Ovcharka', 'brown', 'bone')

pets = [cat1, dog2, dog1, cat2]
for pet in pets:
    pet.voice()

# pet1 = Pet('A', 1, 'breed', 'black')
# print(pet1)

print(cat1.color)
# print(cat1._Cat__name)
print(dir(cat1))

class A:
    def __init__(self, x):
        self.__x = x

a = A(5)

# print(dir(a))
print(a._A__x)