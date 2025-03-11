# Design Patterns in Python

Design patterns are **proven solutions** to common software design problems. They provide **best practices** and **guidelines** for structuring code in a way that improves **scalability, reusability, and maintainability**.

## Why Use Design Patterns?
- **Encapsulates Best Practices**: Avoids reinventing the wheel.
- **Enhances Code Readability**: Provides a structured approach to development.
- **Improves Maintainability**: Helps manage complex systems with clear architecture.
- **Encourages Code Reusability**: Promotes modular design principles.

---

## 1. Singleton Pattern
Ensures that a class has **only one instance** and provides a global access point to it.

### Example:
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True
```
**Use Case:**
- Database connections
- Configuration managers

---

## 2. Factory Pattern
Provides an **interface** for creating objects but **allows subclasses to alter the type of objects that will be created**.

### Example:
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()

animal = AnimalFactory.get_animal("dog")
print(animal.speak())  # Output: Woof!
```
**Use Case:**
- Object creation control
- Simplifies object instantiation logic

---

## 3. Observer Pattern
Allows objects (observers) to subscribe to **state changes** in another object (subject) and be notified automatically.

### Example:
```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received update: {message}")

subject = Subject()
observer1 = Observer()
observer2 = Observer()

subject.attach(observer1)
subject.attach(observer2)
subject.notify("New event occurred!")
```
**Use Case:**
- Event-driven systems (GUIs, notifications)
- Real-time monitoring applications

---

## 4. Decorator Pattern
Dynamically **adds behavior to objects** without modifying their structure.

### Example:
```python
def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello"

print(greet())  # Output: HELLO
```
**Use Case:**
- Logging
- Authorization checks

---

## 5. Strategy Pattern
Defines a **family of algorithms** and allows their interchangeability **at runtime**.

### Example:
```python
class Strategy:
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        return "Executing Strategy A"

class ConcreteStrategyB(Strategy):
    def execute(self):
        return "Executing Strategy B"

class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy
    
    def execute_strategy(self):
        return self.strategy.execute()

context = Context(ConcreteStrategyA())
print(context.execute_strategy())  # Output: Executing Strategy A

context.strategy = ConcreteStrategyB()
print(context.execute_strategy())  # Output: Executing Strategy B
```
**Use Case:**
- Algorithm selection (e.g., sorting methods, payment gateways)
- Behavior switching at runtime

---

## Summary of Design Patterns
| Pattern | Purpose | Example Use Case |
|---------|---------|-----------------|
| **Singleton** | Ensures a class has only one instance | Configuration manager |
| **Factory** | Provides a method for creating objects | GUI component creation |
| **Observer** | Allows objects to react to state changes | Event-driven programming |
| **Decorator** | Adds functionality dynamically | Logging, security checks |
| **Strategy** | Allows switching between algorithms | Payment processing strategies |

By applying **design patterns**, Python code becomes **more structured, flexible, and maintainable**. These patterns provide **reusable solutions** that improve the quality of software architecture. 🚀