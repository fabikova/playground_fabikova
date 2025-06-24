
class Animal:
    icon = None

    def __init__(self, name):
        self.name = name

    def speak(self):
        pass # not defined for generic animal

    def __str__(self):
        return f"This {self.icon} is {self.name}."


class Dog(Animal):
    icon = "🐕"

    def speak(self):
        print(f"[{self.name}] Bark!")

class Cat(Animal):
    icon = "🐈"

    def speak(self):
        print(f"[{self.name}] Meow!")

if __name__ == '__main__':

    sparky = Dog("Sparky")
    mittens = Cat("Mittens")

    print(sparky)
    sparky.speak()

    print(mittens)
    mittens.speak()

