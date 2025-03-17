# 🔹Refactoring with OOP in Python

Refactoring is the process of **restructuring existing code** without changing its external behavior. Object-Oriented Programming (OOP) makes refactoring easier by promoting **modularity, reusability, and maintainability**.

## 🔹Why Refactor Code?
- **Improves Code Readability**: Makes the code easier to understand.
- **Enhances Maintainability**: Reduces complexity and makes modifications easier.
- **Increases Reusability**: Helps eliminate redundancy and allows efficient code reuse.
- **Optimizes Performance**: Refactored code often runs more efficiently.

---

## 🔹Key OOP-Based Refactoring Techniques
Refactoring with OOP involves applying **best practices** and **design patterns** to improve code structure.

### 🔹1. Extracting Classes (Encapsulation)
When a class does too much, break it into **smaller, focused classes**.

**Before:**
```python
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def calculate_bonus(self):
        return self.salary * 0.1
```
**After (Encapsulating Bonus Calculation in a Separate Class):**
```python
class BonusCalculator:
    @staticmethod
    def calculate_bonus(salary):
        return salary * 0.1

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def get_bonus(self):
        return BonusCalculator.calculate_bonus(self.salary)
```

### 🔹2. Replacing Conditionals with Polymorphism
If a class uses too many `if` statements to decide behavior, refactor it using **polymorphism**.

**Before:**
```python
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def get_salary(self):
        if self.role == "Manager":
            return 80000
        elif self.role == "Developer":
            return 60000
        else:
            return 40000
```
**After (Using Inheritance and Polymorphism):**
```python
class Employee:
    def __init__(self, name):
        self.name = name

    def get_salary(self):
        pass

class Manager(Employee):
    def get_salary(self):
        return 80000

class Developer(Employee):
    def get_salary(self):
        return 60000

# Usage
employees = [Manager("Alice"), Developer("Bob")]
for emp in employees:
    print(emp.name, emp.get_salary())
```

### 🔹3. Using Composition Over Inheritance
Prefer **composition** over deep inheritance trees to make code more flexible and reusable.

**Before (Inheritance-Based Approach):**
```python
class Engine:
    def start(self):
        return "Engine started"

class Car(Engine):
    def drive(self):
        return "Car is moving"
```
**After (Composition-Based Approach):**
```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        return self.engine.start() + " and Car is moving"
```

### 🔹4. Extracting Methods for Reusability
If a method does multiple things, extract separate methods to improve clarity and reusability.

**Before:**
```python
class Order:
    def process_order(self, items):
        total = sum(item.price for item in items)
        print(f"Total: ${total}")
        print("Processing payment...")
```
**After (Splitting Methods for Clarity):**
```python
class Order:
    def calculate_total(self, items):
        return sum(item.price for item in items)

    def process_payment(self, total):
        print(f"Total: ${total}")
        print("Processing payment...")
```

---

## 🔹Common OOP Refactoring Patterns
| Pattern | Purpose |
|---------|---------|
| **Encapsulation** | Hides details inside smaller, reusable classes. |
| **Polymorphism** | Eliminates conditionals by using dynamic method selection. |
| **Composition** | Avoids deep inheritance trees and promotes flexibility. |
| **Extract Method** | Breaks down large functions into smaller, focused ones. |

---

## 🔹Summary
- **Refactoring makes code cleaner, more maintainable, and scalable.**
- **Apply OOP principles** such as **encapsulation, polymorphism, and composition**.
- **Use patterns** like **Extract Class, Replace Conditionals with Polymorphism, and Extract Method**.

By following these OOP refactoring techniques, developers can **enhance code quality and performance** while keeping systems easy to modify and extend! 🚀

Continue to the next section: **[Testing classes and methods](07_testing-classes-and-methods.md)**.
