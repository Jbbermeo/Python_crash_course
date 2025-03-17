# *args and **kwargs in Python

Python allows functions to accept an arbitrary number of arguments using special syntax: `*args` and `**kwargs`. These features enable flexible function definitions, making it easier to handle dynamic inputs. In Object-Oriented Programming (OOP), this is particularly useful when designing methods with variable argument requirements.

---

## 🔹 **1. What Are `*args` and `**kwargs`?**

- `*args`: Collects additional **positional arguments** passed to a function into a tuple.
- `**kwargs`: Collects additional **keyword arguments** passed to a function into a dictionary.

These can be used individually or together in a function definition.

Example:
```python
def example_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example_function(1, 2, 3, name="Alice", age=30)
```
**Output:**
```
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Alice', 'age': 30}
```

---

## 🔹 **2. Using `*args` for Positional Arguments**

When you don't know how many positional arguments a function might receive, you can use `*args`. Python will pack these arguments into a tuple.

### **Example:**
```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # Output: 10
```

### **Use Case:**
In OOP, you might have a method that needs to accept a variable number of inputs, such as for data aggregation.

```python
class Statistics:
    def calculate_mean(self, *numbers):
        return sum(numbers) / len(numbers) if numbers else 0

stats = Statistics()
print(stats.calculate_mean(10, 20, 30))  # Output: 20.0
```

---

## 🔹 **3. Using `**kwargs` for Keyword Arguments**

`**kwargs` allows functions to accept any number of keyword arguments. These are packed into a dictionary.

### **Example:**
```python
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=30, city="New York")
```
**Output:**
```
name: Alice
age: 30
city: New York
```

### **Use Case:**
In OOP, keyword arguments can be used to set attributes dynamically.

```python
class User:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

user = User(name="Alice", age=30)
print(user.name)  # Output: Alice
print(user.age)   # Output: 30
```

---

## 🔹 **4. Combining `*args` and `**kwargs`**

You can define a function that uses both `*args` and `**kwargs`. The order in the function signature is important: `*args` must come before `**kwargs`.

### **Example:**
```python
def full_function_example(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

full_function_example(1, 2, 3, name="Bob", age=25)
```

### **Order of Parameters:**
1. Regular (positional) parameters
2. `*args`
3. Keyword-only parameters (optional)
4. `**kwargs`

Example:
```python
def example_function(a, b, *args, c=10, **kwargs):
    print(a, b, args, c, kwargs)

example_function(1, 2, 3, 4, c=20, name="Charlie")
```
**Output:**
```
1 2 (3, 4) 20 {'name': 'Charlie'}
```

---

## 🔹 **5. Practical Applications**

### **Flexible Data Handling:**
Functions that handle data with unknown length or structure can benefit from `*args` and `**kwargs`. For example, logging functions often take dynamic inputs.

```python
def log_message(level, *messages, **details):
    print(f"[{level.upper()}]", *messages)
    for key, value in details.items():
        print(f"{key}: {value}")

log_message("info", "Starting process...", user="admin", status="running")
```

### **Method Overriding in OOP:**
In inheritance, `*args` and `**kwargs` allow you to extend methods without changing the original signature.

```python
class Base:
    def process(self, *args, **kwargs):
        print("Base processing", args, kwargs)

class Derived(Base):
    def process(self, *args, **kwargs):
        print("Derived processing")
        super().process(*args, **kwargs)

obj = Derived()
obj.process(1, 2, name="test")
```

---

## 🔹 **6. Best Practices for `*args` and `**kwargs`**

1. **Use descriptive parameter names:**
   - Avoid using generic names like `*a` and `**k`. Use meaningful names to improve readability.

2. **Avoid overusing `*args` and `**kwargs`:**
   - Only use them when necessary. Overuse can make functions harder to understand and debug.

3. **Combine with default values:**
   - You can use default parameters alongside `*args` and `**kwargs` to provide fallback values.

Example:
```python
def example_function(a, *args, message="No message", **kwargs):
    print(a, args, message, kwargs)

example_function(1, 2, 3, message="Hello", name="Alice")
```

## 🔹 **7. Summary**
`*args` and `**kwargs` provide flexibility in Python functions, allowing you to handle variable-length inputs. These features are especially useful in OOP for dynamic method definitions and method overriding. By using these tools effectively, you can write more adaptable and maintainable code.

Continue to the next section: **[Keywords](07_keywords.md)**.
