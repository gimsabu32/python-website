'''Python is a versatile, high-level programming language known for its readability and simplicity. It supports multiple programming paradigms, including procedural, functional, and, most notably, **object-oriented programming (OOP)**. OOP is a programming model based on the concept of "objects," which can contain data and code.

## Object-Oriented Programming (OOP)

OOP in Python is a paradigm that structures programs by bundling related properties and behaviors into individual **objects**. This approach helps manage complexity, promotes code reusability, and makes programs easier to maintain. Key principles of OOP include:

  * **Encapsulation**: Bundling data (attributes) and methods (functions) that operate on the data into a single unit called a **class**. It hides the internal state and functionality of an object, exposing only what is necessary.
  * **Inheritance**: A mechanism where a new **class** (**subclass**) can inherit attributes and methods from an existing **class** (**superclass**). This allows for code reuse and the creation of a hierarchy of classes.
  * **Polymorphism**: The ability of an object to take on many forms. In Python, this is often achieved through **method overriding**, where a subclass provides its own implementation of a method that is already defined in its superclass.
  * **Abstraction**: Hiding complex implementation details and showing only the essential features of an object. This is often achieved through abstract classes and methods, which define a blueprint for subclasses to follow.

-----

## Classes and Objects

A **class** is a blueprint or a template for creating objects. It defines a set of attributes (data) and methods (functions) that the objects created from it will have. Think of a class like a cookie cutter and an object as the actual cookie. You can create many cookies (objects) from a single cookie cutter (class).

An **object** is an instance of a class. When you create an object, you are instantiating the class, and the object holds its own unique data.

### Creating a Class

To define a class in Python, use the `class` keyword followed by the class name. Class names are conventionally written in **PascalCase** (e.g., `MyClass`).

**Example 1: Basic Class Definition**

```python
class Dog:
    # A simple class with no attributes or methods
    pass

# Create an object (an instance of the Dog class)
my_dog = Dog()
```

### The `__init__` Method

The `__init__` method is a special method called a **constructor**. It is automatically called when a new object is created from a class. It is used to initialize the object's attributes.

The `self` parameter is a reference to the instance of the class itself. It is the first parameter of any method in a class and is used to access the object's attributes and methods.

**Example 2: Class with `__init__` and Attributes**

```python
class Dog:
    def __init__(self, name, age):
        # Initialize attributes
        self.name = name
        self.age = age

# Create objects with initial data
dog1 = Dog("Buddy", 5)
dog2 = Dog("Lucy", 2)

print(f"Dog 1's name is {dog1.name} and age is {dog1.age}.")
print(f"Dog 2's name is {dog2.name} and age is {dog2.age}.")
```

### Methods

**Methods** are functions defined inside a class. They represent the behaviors or actions that an object can perform.

**Example 3: Adding Methods to a Class**

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} is barking loudly!"

    def get_age_in_dog_years(self):
        return self.age * 7

# Create an object
my_dog = Dog("Max", 3)

# Call the methods
print(my_dog.bark())
print(f"{my_dog.name} is {my_dog.get_age_in_dog_years()} dog years old.")
```

-----

## Detailed Examples and Exercises

### Exercise 1: Create a `Car` Class

**Goal**: Create a class `Car` that has attributes for `make`, `model`, and `year`. Include a method `get_description()` that returns a string summarizing the car.

**Code:**

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_description(self):
        return f"This is a {self.year} {self.make} {self.model}."

# Create an object
my_car = Car("Toyota", "Camry", 2020)

# Print the description
print(my_car.get_description())
```

-----

### Exercise 2: Inheritance - The `ElectricCar` Subclass

**Goal**: Create a subclass `ElectricCar` that inherits from `Car`. Add a new attribute `battery_size` and a method `get_battery_info()` to the subclass.

**Code:**

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_description(self):
        return f"This is a {self.year} {self.make} {self.model}."

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        # Call the parent class's constructor
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def get_battery_info(self):
        return f"The battery size is {self.battery_size} kWh."

# Create an ElectricCar object
my_tesla = ElectricCar("Tesla", "Model S", 2023, 100)

# Access methods from both parent and subclass
print(my_tesla.get_description())
print(my_tesla.get_battery_info())
```

-----

### Exercise 3: Polymorphism - Overriding a Method

**Goal**: In the `ElectricCar` class, override the `get_description()` method to include the battery size.

**Code:**

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_description(self):
        return f"This is a {self.year} {self.make} {self.model}."

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    # Override the get_description method
    def get_description(self):
        return f"This is a {self.year} {self.make} {self.model} with a {self.battery_size} kWh battery."

# Create an ElectricCar object
my_tesla = ElectricCar("Tesla", "Model 3", 2024, 75)

# Call the overridden method
print(my_tesla.get_description())
```

-----

### Exercise 4: Encapsulation - Using Private Attributes

**Goal**: Modify the `Car` class to make the `make` and `model` attributes "private" by convention, and use methods to access them.

**Code:**

```python
class Car:
    def __init__(self, make, model):
        # Use a leading underscore to indicate "private" by convention
        self._make = make
        self._model = model

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def set_make(self, new_make):
        self._make = new_make

# Create an object
my_car = Car("Ford", "Focus")

# Access attributes using methods
print(f"Original make: {my_car.get_make()}")

# Modify an attribute
my_car.set_make("Honda")
print(f"New make: {my_car.get_make()}")
```

-----

### Exercise 5: A `Bank Account` Class

**Goal**: Create a `BankAccount` class with attributes `account_number`, `owner_name`, and `balance`. Include methods for `deposit`, `withdraw`, and `get_balance`. Ensure the `withdraw` method doesn't allow a negative balance.

**Code:**

```python
class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return f"Account balance for {self.owner_name} ({self.account_number}): ${self.balance}."

# Create an account
my_account = BankAccount("123456", "Alice", 500)

# Perform transactions
print(my_account.get_balance())
my_account.deposit(200)
my_account.withdraw(150)
my_account.withdraw(600)  # This should fail
print(my_account.get_balance())
```

-----

### Exercise 6: A `Shape` Class Hierarchy

**Goal**: Create a base `Shape` class with a method `area()` that returns 0. Then, create subclasses like `Circle` and `Rectangle` that inherit from `Shape` and provide their own implementations of the `area()` method.

**Code:**

```python
import math

class Shape:
    def area(self):
        """Returns the area of the shape."""
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create objects of different shapes
my_circle = Circle(5)
my_rectangle = Rectangle(4, 6)

# Calculate and print their areas
print(f"Area of the circle: {my_circle.area():.2f}")
print(f"Area of the rectangle: {my_rectangle.area()}")
```'''
from abc import ABC, abstractmethod

class Animal(ABC): # ABC means it's an Abstract Base Class
    @abstractmethod
    def make_sound(self):
        pass # This method must be implemented by subclasses

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# animal = Animal() # This will cause a TypeError, as Animal is abstract
dog = Dog()
dog.make_sound()

print("************")

cat = Cat()
cat.make_sound()