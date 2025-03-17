# Modules and Packages in Python

Modules and packages are essential for organizing and reusing code in Python. They allow you to break large programs into smaller, manageable components and promote code reusability across multiple projects. In Object-Oriented Programming (OOP), modules and packages help structure classes, methods, and data logically.

---

## 🔹 **1. What Are Modules?**

A **module** is a Python file that contains functions, classes, and variables. By importing a module, you can access and reuse its code in other scripts or programs.

### **Example of a Module (`math_utils.py`):**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

### **Using the Module:**
```python
import math_utils

result = math_utils.add(3, 5)
print(result)  # Output: 8
```

You can also import specific functions:
```python
from math_utils import add
print(add(2, 4))  # Output: 6
```

---

## 🔹 **2. What Are Packages?**

A **package** is a collection of related modules organized in a directory. It contains an optional `__init__.py` file to indicate that the directory is a package.

### **Package Structure:**
```
my_package/
    __init__.py
    module1.py
    module2.py
```

### **Example:**
#### `module1.py`
```python
def greet():
    print("Hello from module1")
```

#### `module2.py`
```python
def farewell():
    print("Goodbye from module2")
```

#### Importing from the Package:
```python
from my_package import module1, module2

module1.greet()      # Output: Hello from module1
module2.farewell()   # Output: Goodbye from module2
```

---

## 🔹 **3. The `__init__.py` File**

The `__init__.py` file is used to initialize a Python package. It can also contain package-level code, such as imports or setup logic.

### **Example (`__init__.py`):**
```python
from .module1 import greet
from .module2 import farewell
```

Now you can use:
```python
from my_package import greet, farewell

greet()      # Output: Hello from module1
farewell()   # Output: Goodbye from module2
```

---

## 🔹 **4. Importing Modules and Packages**

### **1. Absolute Imports:**
Use the full path to import a module.
```python
import my_package.module1
my_package.module1.greet()
```

### **2. Relative Imports:**
Use `.` and `..` to refer to the current and parent packages.
```python
from .module1 import greet
from ..subpackage.module3 import some_function
```

---

## 🔹 **5. Built-in and Third-party Modules**

Python includes a rich set of built-in modules, and you can also install third-party modules using `pip`.

### **Built-in Module Example:**
```python
import math
print(math.sqrt(16))  # Output: 4.0
```

### **Installing and Using Third-party Modules:**
```bash
pip install requests
```
```python
import requests
response = requests.get('https://api.github.com')
print(response.status_code)  # Output: 200
```

---

## 🔹 **6. Organizing Code with Modules and Packages**

In OOP, modules and packages help separate different responsibilities into distinct components, improving code maintainability and scalability.

### **Example:**
```
project/
    models/
        __init__.py
        user.py
        product.py
    services/
        __init__.py
        auth_service.py
```

#### `models/user.py`:
```python
class User:
    def __init__(self, username):
        self.username = username
```

#### `services/auth_service.py`:
```python
from models.user import User

def authenticate(username):
    return User(username)
```

---

## 🔹 **7. Best Practices**

1. **Use clear and descriptive names:**
   - Module and package names should reflect their purpose.

2. **Keep modules small:**
   - Break large modules into smaller ones to improve readability.

3. **Use `__all__` to control imports:**
   - Specify the public API of a module or package.
```python
__all__ = ['greet', 'farewell']
```

4. **Avoid circular imports:**
   - Ensure modules do not depend on each other in a circular manner.

5. **Document your modules:**
   - Include docstrings to explain the purpose of each module and function.

---

## 🔹 **8. Practice Challenges**

### **Challenge 1: Create a Module**
Create a module `math_operations.py` with functions for addition and subtraction. Import and use it in another script.
```python
# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```
```python
# main.py
from math_operations import add, subtract
print(add(10, 5))       # Output: 15
print(subtract(10, 5))  # Output: 5
```

### **Challenge 2: Create a Package**
Organize two modules (`greetings.py` and `farewells.py`) into a package. Import and use them.
```python
# greetings.py
def say_hello():
    print("Hello!")
```
```python
# farewells.py
def say_goodbye():
    print("Goodbye!")
```
```python
# main.py
from my_package import say_hello, say_goodbye
say_hello()      # Output: Hello!
say_goodbye()    # Output: Goodbye!
```

---

## 🔹 **9. Summary**
Modules and packages allow you to organize Python code into reusable components. By structuring your projects with modules and packages, you can improve code maintainability, scalability, and reusability. This is especially important in OOP, where classes and methods can be logically separated across modules.

Continue to the next section: **[File Handling](13_file-handling.md)**.