# 🔹Operator Overloading in Python

Operator Overloading is a powerful feature in **Object-Oriented Programming (OOP)** that allows us to define how operators like `+`, `-`, `*`, `/`, and others work with **user-defined objects**. It makes code more **intuitive, readable, and expressive**.

## Why Use Operator Overloading?
- **Enhances Code Readability**: Allows objects to be used naturally with operators.
- **Customizes Object Behavior**: Enables user-defined classes to mimic built-in data types.
- **Improves Code Reusability**: Standard operations can be applied to complex objects.

---

## 🔹Understanding Operator Overloading
By default, Python does **not** know how to perform operations like `object1 + object2`. To enable this, we define special **dunder (double underscore) methods**, also known as **magic methods**.

### Common Magic Methods for Overloading
| Operator | Magic Method |
|----------|-------------|
| `+` (Addition) | `__add__(self, other)` |
| `-` (Subtraction) | `__sub__(self, other)` |
| `*` (Multiplication) | `__mul__(self, other)` |
| `/` (Division) | `__truediv__(self, other)` |
| `==` (Equality) | `__eq__(self, other)` |
| `!=` (Not Equal) | `__ne__(self, other)` |
| `<` (Less Than) | `__lt__(self, other)` |
| `>` (Greater Than) | `__gt__(self, other)` |

---

## 🔹Example: Overloading the `+` Operator
Consider a `Vector` class where we want to add two vector objects using `+`.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
result = v1 + v2  # This will call __add__
print(result)  # Output: Vector(6, 8)
```
### Explanation:
- We define `__add__` to **override** the behavior of `+`.
- `v1 + v2` calls `__add__`, returning a **new** `Vector` object.
- `__str__` helps in **pretty-printing** the object.

---

## 🔹Example: Overloading `==` (Equality Comparison)
To compare two objects using `==`, we override `__eq__`.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

book1 = Book("Python Basics", "John Doe")
book2 = Book("Python Basics", "John Doe")
book3 = Book("Advanced Python", "Jane Doe")

print(book1 == book2)  # Output: True
print(book1 == book3)  # Output: False
```
### Explanation:
- `__eq__` allows us to compare two `Book` objects using `==`.
- Without it, `book1 == book2` would compare **memory addresses**, not content.

---

## 🔹Example: Overloading `*` (Multiplication)
Let's say we want to multiply a `BankAccount` balance by a number.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def __mul__(self, factor):
        return BankAccount(self.balance * factor)
    
    def __str__(self):
        return f"BankAccount Balance: ${self.balance}"

account = BankAccount(1000)
doubled = account * 2  # Calls __mul__
print(doubled)  # Output: BankAccount Balance: $2000
```
### Explanation:
- `__mul__` allows us to multiply the balance of `BankAccount`.
- `account * 2` creates a **new** object with the updated balance.

---

## 🔹Summary
| Concept | Description |
|---------|-------------|
| **Operator Overloading** | Customizing how operators work with user-defined objects |
| **Magic Methods** | Special dunder methods (e.g., `__add__`, `__eq__`) for overloading |
| **Benefits** | Improves readability, reusability, and flexibility |

**Operator Overloading** allows Python objects to behave **intuitively**, making code more expressive and natural. 🚀

Continue to the next section: **[Metaclasses in Python](11_metaclasses-in-python.md)**.