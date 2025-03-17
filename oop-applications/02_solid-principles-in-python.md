# 🔹SOLID Principles in Python

The **SOLID** principles are five design principles in **Object-Oriented Programming (OOP)** that help in creating **maintainable, scalable, and readable** software. They were introduced by **Robert C. Martin (Uncle Bob)** to promote better software architecture.

## Why Are SOLID Principles Important?
- **Enhances Code Maintainability**: Reduces code complexity and dependencies.
- **Improves Scalability**: Makes it easier to extend software without modifying existing code.
- **Encourages Code Reusability**: Promotes modular design practices.
- **Minimizes Bugs and Errors**: Reduces the risk of unintended side effects.

---

## 🔹1. Single Responsibility Principle (SRP)
A class should have **only one reason to change**. This means a class should only have **one responsibility**.

### Example:
```python
class ReportGenerator:
    def generate_report(self):
        pass  # Handles report generation

class ReportSaver:
    def save_report(self, report):
        pass  # Handles saving the report
```
**Why?**
- **Good separation of concerns**: One class should not handle multiple responsibilities.
- **Easier to modify**: Changes in one functionality do not affect other parts of the code.

---

## 🔹2. Open-Closed Principle (OCP)
A class should be **open for extension but closed for modification**.

### Example:
Instead of modifying an existing class, extend it:
```python
class Animal:
    def speak(self):
        pass  # To be overridden

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```
**Why?**
- **No need to modify existing classes** when adding new behaviors.
- **Prevents breaking existing functionality**.

---

## 🔹3. Liskov Substitution Principle (LSP)
Subclasses should be replaceable for their base classes **without altering the correctness of the program**.

### Example:
```python
class Bird:
    def fly(self):
        return "I can fly!"

class Penguin(Bird):
    def fly(self):
        raise Exception("I cannot fly!")
```
**Why is this bad?**
- **A Penguin is a Bird but cannot fly**, violating expectations.
- **Instead, use composition:**
```python
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        return "I can fly!"

class Penguin(Bird):
    def swim(self):
        return "I can swim!"
```
- This ensures **objects behave as expected** when substituted.

---

## 🔹4. Interface Segregation Principle (ISP)
A class should **not be forced to implement methods** it does not use.

### Example:
**Bad Design:**
```python
class Worker:
    def work(self):
        pass
    def eat(self):
        pass
```
A **robot** is a worker but does not eat!

**Better Design:**
```python
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        return "Working"
    def eat(self):
        return "Eating"

class Robot(Workable):
    def work(self):
        return "Working non-stop"
```
**Why?**
- **Prevents unnecessary dependencies**.
- **Ensures classes only implement what they need.**

---

## 🔹5. Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules. **Both should depend on abstractions.**

### Example:
**Bad Design:**
```python
class MySQLDatabase:
    def connect(self):
        return "Connecting to MySQL"

class Application:
    def __init__(self):
        self.db = MySQLDatabase()
```
The `Application` class is **tightly coupled** to `MySQLDatabase`. If we change the database, we must modify `Application`.

**Better Design:**
```python
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connecting to MySQL"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connecting to PostgreSQL"

class Application:
    def __init__(self, db: Database):
        self.db = db
```
**Why?**
- `Application` depends on an **abstract `Database` class**, not a concrete implementation.
- We can **easily switch databases** without modifying `Application`.

---

## 🔹Summary
| Principle | Description |
|-----------|-------------|
| **SRP** | A class should have only one responsibility. |
| **OCP** | A class should be open for extension but closed for modification. |
| **LSP** | Subtypes must be substitutable for their base types. |
| **ISP** | Classes should not be forced to implement unnecessary methods. |
| **DIP** | High-level modules should depend on abstractions, not concrete implementations. |

By following **SOLID principles**, Python code becomes **more modular, flexible, and maintainable**. These principles help build **scalable and robust applications** that are easy to extend and modify. 🚀


Continue to the next section: **[Desing patterns](03_design-patterns.md)**.