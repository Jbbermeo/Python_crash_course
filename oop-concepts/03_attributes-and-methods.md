# 🔹Attributes and Methods in Python Classes

In Object-Oriented Programming (OOP), classes encapsulate data and behavior using **attributes** and **methods**. Below, we will explore these concepts in detail.

## 🔹Attributes in Classes

**Attributes** are variables associated with a class or its instances. They store relevant information for objects.

### Types of Attributes

1. **Instance Attributes:**  
   These are specific to each object and are defined inside the `__init__` method using `self`.

   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name  # Instance attribute
           self.age = age    # Instance attribute

   p1 = Person("Anna", 30)
   p2 = Person("John", 25)

   print(p1.name)  # Anna
   print(p2.name)  # John
   ```

2. **Class Attributes:**  
   These are shared by all instances of the class.

   ```python
   class Person:
       species = "Human"  # Class attribute

       def __init__(self, name):
           self.name = name

   p1 = Person("Anna")
   p2 = Person("John")

   print(p1.species)  # Human
   print(p2.species)  # Human
   ```

   If we modify `species`, it affects all instances.

   ```python
   Person.species = "Homo sapiens"
   print(p1.species)  # Homo sapiens
   print(p2.species)  # Homo sapiens
   ```

## 🔹Methods in Classes

### What Are Methods?
Methods are functions that are defined inside a class. They describe behaviors that an object (an instance of a class) can perform. 
For example, a `Car` class might have methods like `start_engine()` or `drive()`. 

Think of a method as a recipe for an action that an object can execute.

### Types of Methods in Python Classes

In Object-Oriented Programming (OOP), **methods** define the behaviors of a class and its objects. There are three main types of methods in Python: **instance methods, class methods, and static methods**. Each serves a different purpose and is used in different scenarios. Below, we will break down each type in detail, explaining its use case and importance.

### 1. Instance Methods

#### What are Instance Methods?
Instance methods are the most common type of methods in Python classes. They **operate on a specific instance** of the class and can access or modify the instance’s attributes.

#### When to Use Instance Methods?
- When each object (instance) needs its own unique behavior.
- When a method needs to modify or use instance-specific data.
- When the method logically belongs to an individual object rather than the whole class.

#### Example of an Instance Method
```python
class Dog:
    def __init__(self, name):
        self.name = name  # Instance attribute

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())  # Buddy says Woof!
```

#### Why Are Instance Methods Important?
- They allow objects to **maintain state** through instance attributes.
- They make code more **modular and reusable**, as each object can have its own attributes while sharing common behaviors.

---

### 🔹2. Class Methods

#### What are Class Methods?
Class methods work at the **class level** rather than the instance level. They are defined using the `@classmethod` decorator and take `cls` as their first parameter, which refers to the class itself.

#### When to Use Class Methods?
- When you need to **modify or access class attributes**.
- When you need to create alternative constructors (methods that return a new instance of the class).
- When you want behavior that applies to the entire class rather than individual objects.

#### Example of a Class Method
```python
class Animal:
    species = "Mammal"  # Class attribute

    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

print(Animal.species)  # Mammal
Animal.change_species("Reptile")
print(Animal.species)  # Reptile
```

#### Why Are Class Methods Important?
- They **modify class-wide behavior** without needing an instance.
- They allow **alternative ways to instantiate objects**.

Example of using a class method to create objects:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2024 - birth_year)

p1 = Person.from_birth_year("Alice", 2000)
print(p1.name, p1.age)  # Alice 24
```

---

### 3. Static Methods

#### What are Static Methods?
Static methods do not depend on **instance attributes (`self`) or class attributes (`cls`)**. They behave like regular functions but are placed inside a class for logical grouping.

#### When to Use Static Methods?
- When a function **logically belongs to a class** but does not need access to instance or class data.
- When you want to keep related functionality within the class, even if it doesn’t use `self` or `cls`.
- When creating **utility/helper methods**.

#### Example of a Static Method
```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))  # 8
```

#### Why Are Static Methods Important?
- They **keep related functionality inside the class**, making code more organized.
- They allow functions to be used without creating an instance of the class.

---

## Choosing the Right Type of Method

| Method Type     | When to Use | Access to Instance (`self`) | Access to Class (`cls`) |
|----------------|------------|---------------------------|-------------------------|
| **Instance Method** | When working with instance-specific data | ✅ Yes | ❌ No |
| **Class Method** | When modifying class attributes or creating alternative constructors | ❌ No | ✅ Yes |
| **Static Method** | When a function logically belongs to the class but does not use class or instance data | ❌ No | ❌ No |

---


## 🔹Relationship Between Methods and Attributes

Methods allow objects to **interact** with their attributes.

For example, a **Counter** class can have a method that modifies its internal attribute:

```python
class Counter:
    def __init__(self):
        self.value = 0  # Attribute

    def increment(self):
        self.value += 1  # Modifies attribute

    def get_value(self):
        return self.value

counter = Counter()
counter.increment()
print(counter.get_value())  # 1
```

Here:
- `increment` increases `value` by 1.
- `get_value` returns the current count.

## Using `@property` and Other Decorators for Methods

### What is `@property`?
The `@property` decorator allows defining methods that act like attributes. It is useful when you want to control access to an attribute without exposing it directly.

### When to Use `@property`?
- When you want to make an attribute **read-only**.
- When you need to **validate** data before assigning it.
- When you want an attribute that is dynamically computed.

### Example of `@property`
```python
class Person:
    def __init__(self, name, age):
        self._name = name  # Convention to indicate a "private" attribute
        self._age = age

    @property
    def name(self):
        return self._name  # This method behaves like an attribute

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            raise ValueError("Age must be positive")

p = Person("Alice", 30)
print(p.name)  # Alice
print(p.age)   # 30

p.age = 35  # Allowed
# p.age = -5  # Raises ValueError
```

### Other Useful Method Decorators

1. **`@property`** → Makes a method act like an attribute.
2. **`@method.setter`** → Allows modifying a `@property` attribute.

---

## 🔹Summary

Attributes and methods are the foundation of OOP in Python. 

- **Instance attributes** belong to specific objects, while **class attributes** are shared among all instances.
- **Instance methods** work with object-specific data.
- **Class methods** modify class attributes.
- **Static methods** act like normal functions inside a class.
- **Properties (`@property`)** allow controlled access to attributes.

By understanding attributes and methods, you can better structure your code and create reusable objects with defined behaviors.

Continue to the next section: **[Encapsulation](04_encapsulation.md)**.





