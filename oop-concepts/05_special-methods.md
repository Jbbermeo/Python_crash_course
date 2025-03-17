# 🔹Special Methods (Dunder Methods) in Python

Special methods, also known as **dunder (double underscore) methods**, are predefined methods in Python that allow objects to interact with built-in functions and operators. These methods typically begin and end with double underscores, such as `__init__`, `__str__`, and `__len__`.

## 🔹Why Use Dunder Methods?
Dunder methods allow objects to behave like built-in types, enabling custom classes to interact naturally with Python’s syntax and operators. This is useful for:
- Customizing object initialization (`__init__`)
- Defining string representation (`__str__`, `__repr__`)
- Supporting built-in functions like `len()`, `iter()`, `next()`
- Enabling arithmetic and comparison operations
- Making objects callable (`__call__`)
- Managing resource allocation and cleanup (`__enter__`, `__exit__`)

## 🔹How Are Dunder Methods Used?
Dunder methods are defined within a class and are automatically invoked in response to built-in operations. They can define how an object interacts with itself or with other objects. If a class does not implement a dunder method, Python defaults to the behavior of the parent class or raises an error.

---

## 🔹Object Initialization and Representation

### `__init__` - Object Initialization (Constructor)
This method is automatically called when a new instance of the class is created. It allows us to initialize attributes for the object.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p.name, p.age)  # Output: Alice 30
```

### `__str__` - Human-Readable String Representation
Defines how an object should be represented when converted to a string, e.g., when passed to `print()` or `str()`.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

p = Person("Alice", 30)
print(p)  # Output: Person(name=Alice, age=30)
```

### `__repr__` - Unambiguous String Representation
This method should return a string that ideally allows recreating the object. It is used by `repr()` and in interactive consoles.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 30)
print(repr(p))  # Output: Person('Alice', 30)
```
**When to use?**
- Use `__str__` for a user-friendly representation (e.g., printing an object).
- Use `__repr__` when debugging or logging (e.g., storing object state in logs).

---

## 🔹Collection-Like Behavior

### `__len__` - Define Object Length
Allows the object to be used with `len()`.
```python
class Team:
    def __init__(self, members):
        self.members = members
    
    def __len__(self):
        return len(self.members)

team = Team(["Alice", "Bob", "Charlie"])
print(len(team))  # Output: 3
```

### `__getitem__`, `__setitem__`, `__delitem__` - Indexing and Slicing
These methods allow objects to behave like lists or dictionaries.
```python
class Container:
    def __init__(self):
        self.data = {}
    
    def __getitem__(self, key):
        return self.data.get(key, "Key not found")
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __delitem__(self, key):
        del self.data[key]

c = Container()
c["name"] = "Alice"
print(c["name"])  # Output: Alice
del c["name"]
print(c["name"])  # Output: Key not found
```

---

## 🔹Callable Objects

### `__call__` - Making Objects Callable
Allows an instance to be used as a function.
```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        return value * self.factor

triple = Multiplier(3)
print(triple(10))  # Output: 30
```

---

## 🔹Comparison and Arithmetic Operations

### `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__` - Comparisons
Define object comparison behavior.
```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value

n1 = Number(10)
n2 = Number(20)
print(n1 == n2)  # Output: False
print(n1 < n2)   # Output: True
```

### `__add__`, `__sub__`, `__mul__`, `__truediv__` - Arithmetic Operations
Allow custom classes to support mathematical operations.
```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return Number(self.value + other.value)
    
    def __mul__(self, other):
        return Number(self.value * other.value)

n1 = Number(10)
n2 = Number(5)
result = n1 + n2
print(result.value)  # Output: 15
```

---

## 🔹Resource Management

### `__enter__` and `__exit__` - Context Managers
Used with `with` statements for resource cleanup.
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager("test.txt", "w") as f:
    f.write("Hello, world!")
```

---

## 🔹Summary
- **Use `__init__`** to initialize objects.
- **Use `__str__`** for user-friendly representations.
- **Use `__repr__`** for debugging/logging.
- **Use `__len__`, `__getitem__`, etc.** for list-like behavior.
- **Use `__call__`** to make objects callable.
- **Use `__eq__`, `__lt__`, etc.** for comparisons.
- **Use `__enter__` and `__exit__`** for managing resources.

Mastering dunder methods makes classes more intuitive, expressive, and powerful in Python.

Continue to the next section: **[Inheritance](06_inheritance.md)**.


