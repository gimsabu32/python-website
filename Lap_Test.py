class Zoo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        return

class Dog(Zoo):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def make_sound(self):
        return "Woof!"
    def display_info(self):
        print(f"Dog Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Breed: {self.breed}")
        print(f"Sound: {dog.make_sound()}")
   
class Cat(Zoo):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def make_sound(self):
        return "Meow!"
    def display_info(self):
        print(f"Dog Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Color: {self.color}")
        print(f"Sound: {cat.make_sound()}")


if __name__ == "__main__":
    zoo_animals = []

    try:
        num_dogs = int(input("Enter the number of dogs to add to the zoo: "))
        for i in range(num_dogs):
            print(f"\nEnter dog's details {i+1}:")
            name = input("Enter dog's name: ")
            age = int(input("Enter dog's age: "))
            breed = input("Enter dog's breed: ")
            dog = Dog(name, age, breed)
            zoo_animals.append(dog)

        num_cats = int(input("\nEnter the number of cats to add to the zoo: "))
        for i in range(num_cats):
            print(f"\nEnter cat's details {i+1}:")
            name = input("Enter cat's name: ")
            age = int(input("Enter cat's age: "))
            color = input("Enter cat's color: ")
            cat = Cat(name, age, color)
            zoo_animals.append(cat)

        print("\nZoo Animals: ")
        for animal in zoo_animals:
            print("-" * 20)
            animal.display_info()
    
    except ValueError:
        print("\nInvalid input. Please enter a number for age and animal count.")