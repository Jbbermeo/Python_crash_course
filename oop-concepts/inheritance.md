# Inheritance in Python

Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a class (child class) to acquire the properties and behaviors of another class (parent class). This promotes code reusability and establishes relationships between classes.

## Why Use Inheritance?
- **Code Reusability**: Avoids duplicating code by defining common behaviors in a base class.
- **Modularity**: Helps structure code logically by defining general behavior in a superclass and specific behaviors in subclasses.
- **Extensibility**: Allows extending existing functionality without modifying the original code.

## Basic Syntax of Inheritance
A child class inherits from a parent class using parentheses after the class name.

```python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    pass

c = Child()
print(c.greet())  # Output: Hello from Parent
```

## Types of Inheritance

### 1. Single Inheritance
A child class inherits from a single parent class.

**When to use?**
- When a subclass needs to extend or modify the behavior of a single parent class.
- When code reusability is required but with minimal complexity.

**Advantages:**
- Simple and easy to implement.
- Avoids code duplication.

**Limitations:**
- Only allows inheritance from one class, limiting flexibility if multiple behaviors are needed.

```python
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Bark"

d = Dog()
print(d.speak())  # Output: Bark
```

### 2. Multiple Inheritance
A child class inherits from multiple parent classes.

**When to use?**
- When a class needs features from multiple unrelated parent classes.

**Advantages:**
- Allows sharing multiple functionalities from different classes.

**Limitations:**
- Can cause conflicts when parent classes have methods with the same name.
- Increases complexity and requires careful method resolution order (MRO) management.

```python
class A:
    def method_a(self):
        return "Method from A"

class B:
    def method_b(self):
        return "Method from B"

class C(A, B):
    pass

c = C()
print(c.method_a())  # Output: Method from A
print(c.method_b())  # Output: Method from B
```

### 3. Multilevel Inheritance
A child class inherits from another child class.

**When to use?**
- When a natural hierarchy exists, such as `Grandparent → Parent → Child`.
- When behaviors need to be incrementally extended over multiple generations.

**Advantages:**
- Encourages a logical class hierarchy.
- Helps in gradual extension of features.

**Limitations:**
- Can lead to deep inheritance chains, making debugging difficult.
- Increases complexity if too many levels are used.

```python
class Grandparent:
    def greet(self):
        return "Hello from Grandparent"

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

c = Child()
print(c.greet())  # Output: Hello from Grandparent
```

### 4. Hierarchical Inheritance
Multiple child classes inherit from the same parent class.

**When to use?**
- When different child classes share a common base but have unique behaviors.
- Useful in frameworks where multiple subclasses extend a base class.

**Advantages:**
- Promotes code reusability.
- Makes maintaining shared behavior easier.

**Limitations:**
- If too many subclasses depend on a single base class, modifications to the base can have widespread effects.

```python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()
print(c1.greet())  # Output: Hello from Parent
print(c2.greet())  # Output: Hello from Parent
```

### 5. Hybrid Inheritance
A combination of multiple inheritance types.

**When to use?**
- When complex relationships exist between classes that require different types of inheritance.
- Commonly used in real-world applications where classes have multiple behaviors.

**Advantages:**
- Provides the most flexibility by combining different inheritance models.

**Limitations:**
- Can lead to the **diamond problem** where ambiguity arises from multiple inheritance paths.
- Requires careful use of the `super()` function and method resolution order (MRO).

```python
class Base:
    def base_method(self):
        return "Base method"

class A(Base):
    pass

class B(Base):
    pass

class C(A, B):
    pass

c = C()
print(c.base_method())  # Output: Base method
```

## Method Overriding
A child class can redefine a method from the parent class.

```python
class Parent:
    def show(self):
        return "Parent method"

class Child(Parent):
    def show(self):
        return "Child method"

c = Child()
print(c.show())  # Output: Child method
```

## The `super()` Function
Used to call methods from the parent class inside a child class.

```python
class Parent:
    def show(self):
        return "Parent method"

class Child(Parent):
    def show(self):
        return super().show() + " - Extended in Child"

c = Child()
print(c.show())  # Output: Parent method - Extended in Child
```

## Checking Inheritance Relationships
### Using `issubclass()`
Checks if a class is a subclass of another.

```python
class A:
    pass

class B(A):
    pass

print(issubclass(B, A))  # Output: True
print(issubclass(A, B))  # Output: False
```

### Using `isinstance()`
Checks if an object is an instance of a class.

```python
b = B()
print(isinstance(b, B))  # Output: True
print(isinstance(b, A))  # Output: True
```

## Summary
- **Inheritance enables code reuse and structure.**
- **Different types include single, multiple, multilevel, hierarchical, and hybrid inheritance.**
- **Method overriding allows redefining behaviors in subclasses.**
- **The `super()` function calls parent class methods.**
- **`issubclass()` and `isinstance()` help check inheritance relationships.**

Understanding inheritance allows writing modular, reusable, and scalable object-oriented programs in Python.

