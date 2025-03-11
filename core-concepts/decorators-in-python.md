# Decorators in Python

Decorators are a powerful feature in Python that allow you to modify or extend the behavior of functions or methods without changing their actual code. They play a crucial role in Object-Oriented Programming (OOP) by enabling functionality like logging, access control, and caching.

---

## 🔹 **1. What Are Decorators?**

A **decorator** is a function that takes another function as input, modifies or enhances it, and returns the modified function. Decorators use the `@decorator_name` syntax.

### **Example:**
```python
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```
**Output:**
```
Before the function call
Hello!
After the function call
```

---

## 🔹 **2. How Decorators Work**

1. The function to be decorated is passed to the decorator function.
2. The decorator returns a new function (often called a **wrapper**) that modifies the behavior of the original function.
3. The `@decorator_name` syntax applies the decorator to the target function.

### **Without the `@` Syntax:**
```python
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()
```

The `@decorator_name` syntax is simply shorthand for this manual assignment.

---

## 🔹 **3. Common Use Cases for Decorators**

### **1. Logging:**
Automatically log when a function is called.
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add(a, b):
    return a + b

print(add(3, 5))
```
**Output:**
```
Calling add with arguments: (3, 5), {}
8
```

### **2. Access Control:**
Restrict access to certain functions.
```python
def require_permission(permission):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if permission not in user.get("permissions", []):
                raise PermissionError("Access denied")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_permission("admin")
def delete_user(user, username):
    print(f"User {username} deleted")

admin_user = {"permissions": ["admin"]}
delete_user(admin_user, "test_user")
```

### **3. Caching:**
Cache the results of expensive function calls.
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def expensive_computation(n):
    print("Computing...")
    return n * n

print(expensive_computation(10))  # Output: Computing... 100
print(expensive_computation(10))  # Output: 100 (cached result)
```

---

## 🔹 **4. Decorators with Arguments**

Decorators can accept arguments by defining an additional outer function.

### **Example:**
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```
**Output:**
```
Hello, Alice!
Hello, Alice!
Hello, Alice!
```

---

## 🔹 **5. Built-in Decorators**

Python provides several built-in decorators, such as:

### **1. `@staticmethod`:**
Defines a method that doesn't require access to the class or instance.
```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(3, 5))  # Output: 8
```

### **2. `@classmethod`:**
Defines a method that receives the class (`cls`) as its first argument.
```python
class MyClass:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1

MyClass.increment_count()
print(MyClass.count)  # Output: 1
```

### **3. `@property`:**
Defines a method that can be accessed like an attribute.
```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

person = Person("Alice")
print(person.name)  # Output: Alice
```

---

## 🔹 **6. Combining Decorators in OOP**

Decorators are frequently used in OOP to add reusable behavior to methods.

### **Example:**
```python
class Service:
    @staticmethod
    @log_decorator
    def process_data(data):
        print(f"Processing {data}")

Service.process_data("input_data")
```
**Output:**
```
Calling process_data with arguments: ('input_data',), {}
Processing input_data
```

---

## 🔹 **7. Best Practices**

1. **Use descriptive names:**
   - Name your decorators clearly to reflect their purpose.

2. **Keep wrappers simple:**
   - Avoid overly complex logic inside wrapper functions.

3. **Use `functools.wraps`:**
   - Preserve the original function's metadata.

### **Example:**
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before the function call")
        return func(*args, **kwargs)
    return wrapper
```

4. **Chain decorators carefully:**
   - Ensure the order of decorators does not cause unexpected behavior.

---

## 🔹 **8. Practice Challenges**

### **Challenge 1: Simple Decorator**
Write a decorator that prints "Function executed" before calling a function.
```python
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function executed")
        return func(*args, **kwargs)
    return wrapper

@simple_decorator
def greet():
    print("Hello!")

greet()
```

### **Challenge 2: Decorator with Arguments**
Write a decorator that repeats a function's output `n` times.
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
```

---

## 🔹 **9. Summary**
Decorators are a powerful way to extend and modify the behavior of functions and methods. By using decorators effectively, you can implement cross-cutting concerns like logging, access control, and caching. In OOP, decorators enhance reusability and clean design by keeping functionality separate from business logic.

Continue to the next section: **[Modules and Packages](modules-and-packages.md)**.
