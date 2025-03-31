from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract Base Class
    @abstractmethod
    def make_sound(self):
        pass  # Must be implemented by subclasses

    @abstractmethod
    def move(self):
        pass  # Each animal moves differently

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

    def move(self):
        return "Runs on four legs"

class Bird(Animal):
    def make_sound(self):
        return "Chirp! Chirp!"

    def move(self):
        return "Flies in the sky"

class Fish(Animal):
    def make_sound(self):
        return "Blub! Blub!"

    def move(self):
        return "Swims in water"

# Using the subclasses
dog = Dog()
bird = Bird()
fish = Fish()

print(f"Dog: {dog.make_sound()}, {dog.move()}")
print(f"Bird: {bird.make_sound()}, {bird.move()}")
print(f"Fish: {fish.make_sound()}, {fish.move()}")
