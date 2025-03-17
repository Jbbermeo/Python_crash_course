# Functions and Variable Scope in Python

Functions and variable scope are essential concepts in Python that help organize and control data flow in your programs. In Object-Oriented Programming (OOP), understanding these concepts allows you to design classes and methods that handle data effectively without causing unintended side effects.

---

## 🔹 **1. What Are Functions?**
Functions are reusable blocks of code that perform a specific task. They allow you to organize code into logical sections, making your programs more readable and maintainable.

### **Defining a Function:**
```python
def greet(name):
    return f"Hello, {name}!"
```
- `greet` is the function name.
- `name` is a parameter.
- The function returns a formatted string.

### **Calling a Function:**
```python
print(greet("Alice"))  # Output: Hello, Alice!
```

---

## 🔹 **2. Naming Conventions for Functions and Variables**
Python follows the **PEP 8** style guide for naming functions and variables. Consistent naming improves code readability and maintainability.

### **Functions:**
- Use lowercase letters with words separated by underscores (`snake_case`).
- Function names should be descriptive and concise.

Example:
```python
def calculate_total(price, tax):
    return price + (price * tax)
```

### **Variables:**
- Use lowercase letters with words separated by underscores (`snake_case`).
- Avoid single-letter names except for temporary variables (e.g., loop counters).

Example:
```python
item_price = 100
sales_tax = 0.07
```

### **Constants:**
- Use all uppercase letters with underscores (`UPPER_CASE`).
- Constants are usually defined at the top of the module.

Example:
```python
PI = 3.14159
MAX_USERS = 100
```

### **Avoiding Reserved Keywords:**
Do not use Python's reserved keywords (e.g., `def`, `return`, `if`, `for`) as variable or function names.

---

## 🔹 **3. Types of Variables in Python**

### **Global Variables:**
- Defined outside any function or class.
- Accessible throughout the program.

Example:
```python
x = 10  # Global variable

def print_global():
    print(x)

print_global()  # Output: 10
```

### **Local Variables:**
- Defined inside a function and only accessible within that function.

Example:
```python
def print_local():
    y = 5  # Local variable
    print(y)

print_local()  # Output: 5
```

Attempting to access `y` outside the function would raise an error.

### **Nonlocal Variables:**
- Used in nested functions. They refer to variables in the nearest enclosing scope that is not global.

Example:
```python
def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"
    inner()
    print(x)

outer()  # Output: inner
```

---

## 🔹 **4. Variable Scope in Python**

Scope defines where a variable is accessible. Python follows the **LEGB rule**:
1. **Local:** Variables defined inside the current function.
2. **Enclosing:** Variables in the enclosing (outer) function.
3. **Global:** Variables defined at the module level.
4. **Built-in:** Variables and functions provided by Python (e.g., `print`, `len`).

Example of variable scope:
```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)
    inner()

outer()  # Output: local
```

---

## 🔹 **5. Function Parameters**

### **Positional Arguments:**
Arguments are matched based on their position.
```python
def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5
```

### **Keyword Arguments:**
Arguments are matched based on their names.
```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet(name="Alice", message="Hi"))  # Output: Hi, Alice!
```

### **Default Arguments:**
You can provide default values for parameters.
```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Bob"))  # Output: Hello, Bob!
```

### **Variable-Length Arguments:**
- `*args` allows functions to accept any number of positional arguments.
- `**kwargs` allows functions to accept any number of keyword arguments.

Example:
```python
def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_args(1, 2, 3, name="Alice", age=30)
```

---

## 🔹 **6. Returning Values and Side Effects**
Functions can return values or modify data outside their scope (side effects).

### **Returning Values:**
```python
def square(n):
    return n * n

result = square(4)
print(result)  # Output: 16
```

### **Side Effects:**
Functions that modify global or mutable data can have side effects.
```python
my_list = [1, 2, 3]

def modify_list(lst):
    lst.append(4)

modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
```

---

## 🔹 **7. Best Practices for Functions and Scope**

1. **Limit the use of global variables:**
   - Use local variables to prevent conflicts and improve code readability.

2. **Avoid side effects:**
   - Minimize modifications to global or mutable data inside functions.

3. **Use meaningful parameter names:**
   - Clear parameter names improve function readability and maintainability.

4. **Use default values carefully:**
   - Avoid mutable default arguments.

Example:
```python
def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst
```

5. **Follow naming conventions:**
   - Use `snake_case` for function and variable names.
   - Use `UPPER_CASE` for constants.

---

## 🔹 **8. Summary**
Functions and variable scope are crucial for structuring Python programs. Understanding how scope works allows you to control data flow, avoid conflicts, and write maintainable code. Following naming conventions ensures consistency and readability. In OOP, these principles become even more important when designing class methods and managing object state.

Continue to the next section: **[args-and-kwargs](06_args-and-kwargs.md)**.
