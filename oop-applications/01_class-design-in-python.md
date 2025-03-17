# 🔹Class Design in Python

Designing classes effectively is crucial in **Object-Oriented Programming (OOP)**. A well-designed class improves **code maintainability, reusability, and scalability**.

## 🔹Why Is Class Design Important?
- **Encapsulation**: Hides implementation details, exposing only necessary functionality.
- **Code Reusability**: Promotes modularity and prevents redundancy.
- **Scalability**: Allows easy extension of functionality without modifying existing code.
- **Readability & Maintainability**: Clear class structures make debugging easier.

---

## 🔹Principles of Good Class Design
A well-designed class follows these key principles:

### 1. **Single Responsibility Principle (SRP)**
Each class should have **only one reason to change**.

**Example:**
```python
class ReportGenerator:
    def generate_report(self):
        pass  # Handles report generation

class ReportSaver:
    def save_report(self, report):
        pass  # Handles saving the report
```
Instead of a single **monolithic** class, responsibilities are split into separate classes.

---

## 🔹2. **Encapsulation and Information Hiding**
Encapsulation ensures that class **attributes and methods** are not directly accessed but controlled via methods.

**Example:**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```
- The balance is **hidden** (private attribute `__balance`).
- Access is controlled via methods (`deposit()` and `get_balance()`).

---

## 🔹3. **Composition Over Inheritance**
Prefer **composition** instead of deep inheritance trees to keep classes flexible and decoupled.

**Example:**
```python
class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition
    
    def drive(self):
        self.engine.start()
        print("Car is moving!")
```
- The `Car` class **uses** an `Engine` instead of inheriting from it.
- This makes `Engine` reusable in other contexts.

---

## 🔹4. **Avoid Overuse of Static Methods**
Static methods can be useful, but overusing them removes the benefits of OOP.

**Good Use Case:** Utility functions that don't require object state.
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
```
For stateful operations, prefer **instance methods**.

---

### 🔹5. **Follow the Open-Closed Principle (OCP)**
A class should be **open for extension but closed for modification**.

**Example:** Instead of modifying an existing class, extend it.
```python
class Animal:
    def speak(self):
        pass  # To be overridden

class Dog(Animal):
    def speak(self):
        return "Woof!"
```
Adding a new animal does not modify the existing `Animal` class.

---

## 🔹Common Class Design Patterns
| Pattern | Purpose |
|---------|---------|
| **Singleton** | Ensures only one instance of a class exists. |
| **Factory Method** | Creates objects without specifying exact class. |
| **Observer** | Allows objects to notify others about state changes. |
| **Decorator** | Dynamically adds functionality to an object. |

---

## 🔹Summary
- **Well-designed classes improve modularity, maintainability, and scalability.**
- Follow **principles** like **SRP, Encapsulation, and Composition Over Inheritance**.
- Use **design patterns** to solve common architectural problems.

By following these principles, Python classes become **clean, efficient, and easier to extend**! 🚀

Continue to the next section: **[Solid principles in python](02_solid-principles-in-python.md)**.
