## 🔹 **Classes and Objects in Python**

### What is a Class?
A **class** is a blueprint or template for creating objects. It defines a structure that encapsulates **attributes** (data) and **methods** (behavior) that its instances will have. A class allows for the modular and organized design of code, making it reusable and scalable.

#### Characteristics of a Class:
- It serves as a template for creating objects.
- It defines attributes (variables) and methods (functions) that objects instantiated from it will possess.
- It helps organize code logically and promotes reusability.

---

### How to Define a Class in Python
To define a class in Python, use the `class` keyword followed by the class name.

#### Syntax:
```python
class ClassName:
    # Class body (attributes and methods)
    pass
```

#### Naming Conventions for Classes
- Class names should be written in **PascalCase** (also known as **CamelCase** where each word starts with an uppercase letter).
- Class names should be **descriptive** and avoid abbreviations.
- Class names should not start with a number or contain special characters.

#### Example:
```python
class Car:
    pass
```

---

### What is `self` in Python Classes?
`self` is a reference to the current instance of the class. It allows access to instance attributes and methods.

#### Importance of `self`:
- It differentiates between instance attributes and local variables.
- It allows modification of attributes within methods.
- It ensures that each instance operates independently.

#### Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance Attribute
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
```

---

### What is the Constructor Method (`__init__`)?
The `__init__` method is a **special method** (also called a constructor) that is automatically called when an object is instantiated from a class. It is used to initialize instance attributes.

#### Constructor Syntax:
```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Instance Attribute
        self.model = model
        self.year = year
```

- `self` refers to the instance being created.
- The `__init__` method initializes instance attributes.
- Attributes defined inside `__init__` are unique to each instance.

#### Instantiating a Class:
```python
my_car = Car("Toyota", "Corolla", 2022)
print(my_car.brand)  # Output: Toyota
```

---

### Magic Methods (Dunder Methods)
Magic methods, also known as **dunder (double underscore) methods**, are special methods in Python that begin and end with double underscores (`__`). These methods define built-in behaviors of objects and allow for operator overloading and customization of standard operations.

#### Common Magic Methods and Their Uses:

#### **1. Object Initialization: `__init__`**
This method is called when an instance of a class is created. It initializes object attributes.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

#### **2. String Representation: `__str__` and `__repr__`**
- `__str__`: Defines how an object is printed using `print()`.
- `__repr__`: Provides an official string representation of the object.
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def __str__(self):
        return f"Car: {self.brand} {self.model}"
    
    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}')"

car = Car("Tesla", "Model S")
print(car)       # Output: Car: Tesla Model S
print(repr(car)) # Output: Car('Tesla', 'Model S')
```

#### **3. Arithmetic Operations: `__add__`, `__sub__`, `__mul__`, etc.**
Magic methods allow objects to support arithmetic operations.
```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return Number(self.value + other.value)

n1 = Number(10)
n2 = Number(20)
n3 = n1 + n2  # Calls `__add__`
print(n3.value)  # Output: 30
```

#### **4. Length and Size: `__len__`**
Defines the behavior of `len(obj)`.
```python
class Team:
    def __init__(self, members):
        self.members = members
    
    def __len__(self):
        return len(self.members)

team = Team(["Alice", "Bob", "Charlie"])
print(len(team))  # Output: 3
```

#### **5. Object Deletion: `__del__`**
Called when an object is deleted.
```python
class Example:
    def __del__(self):
        print("Object is being deleted")

obj = Example()
del obj  # Output: Object is being deleted
```

#### **6. Indexing and Iteration: `__getitem__`, `__setitem__`, `__iter__`**
- `__getitem__`: Allows index-based access.
- `__setitem__`: Allows item assignment.
- `__iter__`: Makes an object iterable.
```python
class CustomList:
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, index):
        return self.data[index]

cl = CustomList([1, 2, 3, 4])
print(cl[2])  # Output: 3
```

#### **7. Object Comparison: `__eq__`, `__lt__`, `__le__`, `__gt__`, etc.**
Defines behavior for comparison operators (`==`, `<`, `>`, etc.).
```python
class Box:
    def __init__(self, volume):
        self.volume = volume
    
    def __eq__(self, other):
        return self.volume == other.volume

box1 = Box(100)
box2 = Box(100)
print(box1 == box2)  # Output: True
```


### Class Variables vs. Instance Variables
Python classes have two types of variables:

#### **1. Instance Variables**
- Defined inside the `__init__` method.
- Unique to each instance.
- Accessed using `self`.

```python
class Dog:
    def __init__(self, name):
        self.name = name  # Instance Variable
```

#### **2. Class Variables**
- Defined outside methods inside the class.
- Shared across all instances of the class.

```python
class Animal:
    kingdom = "Animalia"  # Class Variable

print(Animal.kingdom)  # Output: Animalia
```

---

### Name Mangling in Python (`__variable`)
Python provides **name mangling** to avoid conflicts in subclassing.
- A variable prefixed with double underscores (`__`) gets modified internally by Python.
- This prevents accidental modification in subclasses.

#### Example:
```python
class Example:
    def __init__(self):
        self.__private_var = "I am private"

obj = Example()
print(obj.__private_var)  # AttributeError
```
However, it can still be accessed using name mangling:
```python
print(obj._Example__private_var)  # Output: I am private
```

---
### Variables with a Single Underscore (`_variable`)
A single leading underscore is a **convention** indicating that a variable is intended for internal use.
- It does **not** enforce privacy.
- It serves as a warning that the variable should not be accessed directly.

#### Example:
```python
class Example:
    def __init__(self):
        self._protected_var = "This is a protected variable"

obj = Example()
print(obj._protected_var)  # Output: This is a protected variable
```

Although `_protected_var` is accessible, it is meant to be used **only within the class or its subclasses**.

---
### Printing Class Variables and Instance Variables
To print class variables and instance variables:

#### Example:
```python
class Car:
    wheels = 4  # Class Variable
    
    def __init__(self, brand, model):
        self.brand = brand  # Instance Variable
        self.model = model
    
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}, Wheels: {Car.wheels}")
```

#### Accessing and Printing Variables:
```python
my_car = Car("Ford", "Mustang")
my_car.display_info()
# Output: Car Brand: Ford, Model: Mustang, Wheels: 4
```

---

### What is an Object?
An **object** is an instance of a class. It is a concrete entity that has unique attributes and behaviors defined by the class from which it is instantiated.

#### Characteristics of an Object:
- It is an individual instance of a class.
- It contains **instance attributes**, which hold unique data.
- It can execute **methods** defined in its class.
- Objects interact with each other within a program.

#### Creating an Object (Instantiation):
To create an object, we instantiate a class by calling it as if it were a function.
```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Instance Attribute
        self.model = model
        self.year = year
    
    def honk(self):
        print("Beep beep!")

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2022)
print(my_car.brand)  # Output: Toyota
my_car.honk()        # Output: Beep beep!
```

---

### How Objects Work in Memory
When an object is instantiated, Python:
1. **Allocates memory** for the new object.
2. **Calls the `__init__` method** to initialize attributes.
3. **Returns a reference** to the object, which is assigned to a variable.
4. The variable stores the memory reference, not the actual object.

```python
car1 = Car("Honda", "Civic", 2021)
car2 = Car("Ford", "Focus", 2020)
print(id(car1))  # Unique memory address of car1
print(id(car2))  # Unique memory address of car2
```

---

### Object Attributes
Objects have attributes that store their data. Attributes can be:

#### **1. Instance Attributes**
- Defined inside the `__init__` method.
- Unique to each object.

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance Attribute
        self.age = age
```

#### **2. Class Attributes**
- Shared across all instances of a class.
- Defined outside methods inside the class.

```python
class Animal:
    kingdom = "Animalia"  # Class Attribute
print(Animal.kingdom)  # Output: Animalia
```

#### Modifying Object Attributes
```python
p1 = Person("Alice", 25)
p1.age = 26  # Modifies only this instance
```

#### Checking Object Attributes
```python
print(hasattr(p1, "name"))  # Output: True
print(getattr(p1, "age"))   # Output: 26
```

---

### Object Methods
Methods define an object's behavior. They operate on an object's attributes.

#### **Instance Methods**
- Use `self` to access attributes and call other methods.

```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says woof!")
```

#### **Calling Methods on Objects**
```python
dog = Dog("Buddy")
dog.bark()  # Output: Buddy says woof!
```

---

### Object Interactions
Objects can interact with each other by storing references to other objects.
```python
class Owner:
    def __init__(self, name):
        self.name = name

def assign_owner(pet, owner):
    pet.owner = owner

owner1 = Owner("John")
dog1 = Dog("Rex")
assign_owner(dog1, owner1)
print(dog1.owner.name)  # Output: John
```

---

### Deleting Objects (`del`)
Objects can be deleted using the `del` keyword. This calls the `__del__` method (if defined) before the object is removed from memory.
```python
class Example:
    def __del__(self):
        print("Object deleted")
obj = Example()
del obj  # Output: Object deleted
```

---

### Summary
- **Objects** are instances of classes and store data in attributes.
- **Instance attributes** are unique to each object, while **class attributes** are shared.
- **Methods** define object behavior and operate on attributes.
- **Objects interact** by referencing other objects.
- **Deleting an object** removes it from memory.

Understanding objects is key to mastering Object-Oriented Programming in Python.

