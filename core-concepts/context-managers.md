# Context Managers in Python

Context managers provide a structured way to manage resources such as files, database connections, and locks in Python. They ensure that resources are properly allocated and released, reducing the risk of resource leaks. In Object-Oriented Programming (OOP), context managers improve code reliability and maintainability by automating resource management.

---

## 🔹 **1. What Are Context Managers?**

A **context manager** is a Python object that defines how to allocate and release a resource using the `with` statement. It uses two special methods:
- `__enter__()`: Called when the `with` block is entered.
- `__exit__()`: Called when the `with` block is exited, even if an exception occurs.

### **Example:**
```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

Here, the file is automatically closed after the `with` block is executed, even if an error occurs inside the block.

---

## 🔹 **2. How to Create a Custom Context Manager**

You can create a custom context manager by defining the `__enter__()` and `__exit__()` methods in a class.

### **Example:**
```python
class CustomContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with CustomContext() as context:
    print("Inside the context")
```
**Output:**
```
Entering context
Inside the context
Exiting context
```

The `__exit__()` method handles any cleanup operations, ensuring that resources are properly released.

---

## 🔹 **3. Using the `contextlib` Module**

Python's `contextlib` module provides utilities for creating and managing context managers.

### **1. `contextmanager` Decorator:**
The `@contextmanager` decorator simplifies the creation of context managers by allowing you to use a generator function.

### **Example:**
```python
from contextlib import contextmanager

@contextmanager
def custom_context():
    print("Entering context")
    yield
    print("Exiting context")

with custom_context():
    print("Inside the context")
```
**Output:**
```
Entering context
Inside the context
Exiting context
```

### **2. Closing Resources:**
The `closing()` function ensures that resources with a `close()` method are properly closed.
```python
from contextlib import closing
import urllib.request

with closing(urllib.request.urlopen('https://www.python.org')) as page:
    content = page.read()
    print(content[:100])
```

---

## 🔹 **4. Common Use Cases for Context Managers**

### **1. File Handling:**
Automatically open and close files.
```python
with open('data.txt', 'r') as file:
    data = file.read()
```

### **2. Database Connections:**
Manage connections to databases.
```python
import sqlite3

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
```

### **3. Locking Mechanisms:**
Ensure that locks are acquired and released properly.
```python
from threading import Lock

lock = Lock()
with lock:
    print("Lock acquired")
```

### **4. Temporary Changes:**
Temporarily modify the environment or configuration.
```python
import os
from contextlib import contextmanager

@contextmanager
def change_directory(path):
    original_path = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(original_path)

with change_directory('/tmp'):
    print(os.getcwd())
```

---

## 🔹 **5. Handling Exceptions in Context Managers**

The `__exit__()` method can handle exceptions raised inside the `with` block. It receives three arguments:
- `exc_type`: The exception type.
- `exc_value`: The exception instance.
- `traceback`: The traceback object.

If `__exit__()` returns `True`, the exception is suppressed.

### **Example:**
```python
class SuppressException:
    def __enter__(self):
        print("Entering context")

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exception suppressed: {exc_value}")
        return True

with SuppressException():
    raise ValueError("An error occurred")
```
**Output:**
```
Entering context
Exception suppressed: An error occurred
```

---

## 🔹 **6. Context Managers in OOP**

Context managers can be integrated into class-based designs to manage resources efficiently.

### **Example:**
```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

with FileManager('example.txt') as file:
    content = file.read()
    print(content)
```

---

## 🔹 **7. Best Practices**

1. **Use the `with` statement:**
   - Always use context managers to handle resources like files and database connections.

2. **Keep context manager logic simple:**
   - Avoid adding complex logic to `__enter__()` and `__exit__()` methods.

3. **Use `contextlib` utilities:**
   - Leverage `contextmanager` and `closing()` for concise and readable context managers.

4. **Handle exceptions appropriately:**
   - Implement error handling within the `__exit__()` method if needed.

---

## 🔹 **8. Practice Challenges**

### **Challenge 1: Create a Custom Context Manager**
Write a custom context manager that logs when a resource is opened and closed.
```python
class ResourceLogger:
    def __enter__(self):
        print("Resource opened")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource closed")

with ResourceLogger() as resource:
    print("Using resource")
```

### **Challenge 2: Use `contextlib.contextmanager`**
Create a context manager using the `@contextmanager` decorator to manage a temporary file.
```python
from contextlib import contextmanager
import tempfile
import os

@contextmanager
def temporary_file():
    temp = tempfile.NamedTemporaryFile(delete=False)
    try:
        yield temp.name
    finally:
        os.remove(temp.name)

with temporary_file() as filename:
    print(f"Temporary file created: {filename}")
```

---

## 🔹 **9. Summary**
Context managers automate resource management, ensuring that resources like files, connections, and locks are properly allocated and released. By mastering context managers, you can write more reliable and maintainable Python code, especially in OOP projects.

Continue to the next section: **[What is Object-Oriented Programming?](file_handling.md)**.
