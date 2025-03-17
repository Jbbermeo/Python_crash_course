# 🔹Using Dataclasses in Python

Dataclasses in Python provide a **simpler, cleaner, and more readable** way to define classes that primarily store data. Introduced in **Python 3.7**, the `dataclasses` module eliminates boilerplate code by automatically generating **`__init__`**, **`__repr__`**, **`__eq__`**, and other methods.

## 🔹Why Use Dataclasses?
- **Reduces Boilerplate Code**: Eliminates the need to manually define constructors and representation methods.
- **Enhances Readability**: Provides a clean and structured way to represent data.
- **Immutable Option**: Allows defining immutable data structures.
- **Performance Improvement**: Optimized for better memory efficiency compared to regular classes.

---

## 🔹Defining a Basic Dataclass
Using `@dataclass`, we can define a class **without manually implementing** an `__init__` method.

### Example:
```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person("Alice", 30)
print(p)  # Output: Person(name='Alice', age=30)
```
**What happens here?**
- `@dataclass` automatically creates `__init__`, `__repr__`, and `__eq__` methods.
- No need to manually define `__init__` to assign attributes.

---

## 🔹Adding Default Values
Dataclasses support **default values**, reducing the need for explicit initializations.

### Example:
```python
@dataclass
class Car:
    brand: str = "Toyota"
    model: str = "Corolla"
    year: int = 2022

c = Car()
print(c)  # Output: Car(brand='Toyota', model='Corolla', year=2022)
```
- If values are **not provided**, defaults are used.
- We can override values when creating an instance.

---

## 🔹Making a Dataclass Immutable
To **prevent modifications**, set `frozen=True`.

### Example:
```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(3, 4)
# p.x = 10  # This will raise a `FrozenInstanceError`
```
**Why use `frozen=True`?**
- Ensures **immutability**, similar to tuples.
- Useful for **hashable** objects (e.g., dictionary keys).

---

## 🔹Customizing Methods in Dataclasses
Dataclasses allow custom methods **while still benefiting from auto-generated methods**.

### Example:
```python
@dataclass
class Rectangle:
    width: float
    height: float
    
    def area(self) -> float:
        return self.width * self.height

r = Rectangle(5.0, 10.0)
print(r.area())  # Output: 50.0
```
- We can add **custom methods** like `area()` for extra functionality.

---

## 🔹Controlling Field Behavior with `field()`
The `field()` function allows **fine-grained control** over attributes, such as default values and excluding fields from methods like `__repr__`.

### Example:
```python
from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    salary: float = field(default=50000.0)
    password: str = field(repr=False)  # Excludes from `__repr__`

emp = Employee("John Doe", 70000, "secret123")
print(emp)  # Output: Employee(name='John Doe', salary=70000.0)
```
**Key Features of `field()`:**
- `default`: Assigns a default value.
- `repr=False`: Excludes field from `__repr__`.
- `compare=False`: Excludes field from `__eq__`.

---

## 🔹Converting Dataclasses to Dictionaries
Dataclasses can be easily converted to dictionaries using `asdict()`.

### Example:
```python
from dataclasses import asdict

d = asdict(emp)
print(d)  # Output: {'name': 'John Doe', 'salary': 70000.0, 'password': 'secret123'}
```
- **Useful for serialization (e.g., JSON, API responses).**

---

## 🔹Inheriting from Dataclasses
Dataclasses **support inheritance**, allowing structured and extendable designs.

### Example:
```python
@dataclass
class Animal:
    species: str
    legs: int

@dataclass
class Dog(Animal):
    breed: str
    name: str

d = Dog("Canine", 4, "Labrador", "Buddy")
print(d)  # Output: Dog(species='Canine', legs=4, breed='Labrador', name='Buddy')
```
- Inherits attributes from `Animal`.
- The subclass `Dog` adds additional fields.

---

## 🔹Summary
Dataclasses simplify class definitions in Python by:
- **Eliminating boilerplate code** with automatic method generation.
- **Providing default values and immutability options** (`frozen=True`).
- **Allowing custom methods** for additional functionality.
- **Supporting inheritance** to create structured and reusable code.
- **Offering fine-grained control** over fields using `field()`.
- **Facilitating data serialization** via `asdict()`.

They are a powerful alternative to regular classes, making Python code more readable and maintainable.

Continue to the next section: **[Object Serialization](05_object-serialization.md)**.