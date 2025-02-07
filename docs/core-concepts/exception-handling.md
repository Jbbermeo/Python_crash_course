# Exception Handling in Python

Exception handling is crucial for building robust Python programs. It allows you to gracefully handle errors and prevent your program from crashing unexpectedly. In Object-Oriented Programming (OOP), proper exception handling helps maintain clean, maintainable code and ensures that errors are managed consistently.

---

## 🔹 **1. What Are Exceptions?**

Exceptions are runtime errors that disrupt the normal flow of a program. Common exceptions in Python include:

- `ValueError`: Raised when a function receives an argument of the correct type but with an invalid value.
- `TypeError`: Raised when an operation or function is applied to an object of inappropriate type.
- `KeyError`: Raised when a dictionary key is not found.
- `ZeroDivisionError`: Raised when a division by zero occurs.

### **Example of an Exception:**
```python
x = int("abc")  # This raises a ValueError
```

Without exception handling, this error would cause the program to terminate.

---

## 🔹 **2. The `try-except` Block**

Python uses the `try-except` block to catch and handle exceptions.

### **Basic Syntax:**
```python
try:
    # Code that might raise an exception
    x = int("abc")
except ValueError:
    print("Invalid input. Please enter a valid number.")
```

### **How It Works:**
1. The code inside the `try` block is executed.
2. If an exception occurs, Python jumps to the `except` block.
3. If no exception occurs, the `except` block is skipped.

---

## 🔹 **3. Catching Multiple Exceptions**

You can handle multiple exceptions using multiple `except` blocks or by grouping exceptions.

### **Example:**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid value.")
```

### **Handling Multiple Exceptions Together:**
```python
try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print(f"An error occurred: {e}")
```

---

## 🔹 **4. The `finally` Block**

The `finally` block contains code that will always execute, regardless of whether an exception was raised or not. This is useful for cleanup operations, such as closing files or releasing resources.

### **Example:**
```python
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
```

---

## 🔹 **5. Raising Exceptions**

You can raise exceptions intentionally using the `raise` keyword.

### **Example:**
```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Valid age.")

check_age(-5)  # This raises a ValueError
```

### **Use Case:**
In OOP, raising exceptions helps enforce data validation within class methods.

```python
class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.balance = balance
```

---

## 🔹 **6. Custom Exceptions**

You can define custom exceptions by inheriting from Python's built-in `Exception` class.

### **Example:**
```python
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for this transaction.")
        self.balance -= amount
```

### **Using Custom Exceptions:**
```python
try:
    account = BankAccount(100)
    account.withdraw(200)
except InsufficientFundsError as e:
    print(e)
```

---

## 🔹 **7. Best Practices for Exception Handling**

1. **Catch specific exceptions:**
   - Avoid using a generic `except:` block. Always specify the exceptions you want to catch.

2. **Log errors:**
   - Use logging to record exceptions for debugging and monitoring.

3. **Use `finally` for cleanup:**
   - Ensure that resources like files or database connections are properly closed.

4. **Avoid silent failures:**
   - Do not suppress exceptions without providing meaningful error messages or handling logic.

5. **Raise meaningful exceptions:**
   - Provide informative error messages to help users and developers understand the issue.

---

## 🔹 **8. Practice Challenges**

### **Challenge 1: Handling Exceptions**
Write a function that takes two numbers and returns their division. Handle division by zero.
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."

print(safe_divide(10, 0))  # Output: Cannot divide by zero.
```

### **Challenge 2: Custom Exception**
Create a custom exception `NegativeValueError` and use it in a function that checks for negative input.
```python
class NegativeValueError(Exception):
    pass

def check_positive(value):
    if value < 0:
        raise NegativeValueError("Negative value not allowed.")

try:
    check_positive(-10)
except NegativeValueError as e:
    print(e)
```

---

## 🔹 **9. Summary**
Exception handling helps prevent unexpected program crashes and ensures graceful error recovery. By using `try-except` blocks, raising custom exceptions, and following best practices, you can build more reliable and maintainable Python applications.

Continue to the next section: **[Iterators and Generators](iterators-and-generators.md)**.
