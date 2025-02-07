# Keywords, Whitespace, Namespaces, and Core Concepts in Python

Python has a set of reserved keywords, rules regarding whitespace, and important concepts like namespaces and object comparisons that are crucial for writing clean, efficient code. Understanding these helps avoid common mistakes and improve code readability.

---

## 🔹 **1. Keywords in Python**

Keywords are reserved words that have special meanings in Python. You cannot use them as variable names or function names.

### **Common Python Keywords:**

| Keyword      | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `and`        | Logical "AND" operator.                                                    |
| `as`         | Used to create aliases for imports or with `with`.                         |
| `assert`     | Verifies that a condition is true; raises an error if not.                  |
| `async`      | Defines an asynchronous function or block.                                  |
| `await`      | Waits for an asynchronous function (coroutine) to complete.                 |
| `break`      | Exits a loop (`for` or `while`).                                            |
| `class`      | Defines a class.                                                            |
| `continue`   | Skips the rest of the current loop iteration and moves to the next.          |
| `def`        | Defines a function.                                                         |
| `del`        | Deletes a variable or an element from a list/dictionary.                    |
| `elif`       | "Else if" conditional statement.                                            |
| `else`       | Executes a block if the condition is not met.                               |
| `except`     | Handles exceptions in `try` blocks.                                         |
| `False`      | Boolean value "false".                                                     |
| `finally`    | Block that always executes, regardless of exceptions.                       |
| `for`        | Loop that iterates over a sequence.                                         |
| `from`       | Imports specific parts of a module.                                         |
| `global`     | Declares a global variable within a function.                               |
| `if`         | Conditional statement that executes a block if a condition is true.          |
| `import`     | Imports a module or library.                                                |
| `in`         | Checks if a value exists within a sequence.                                 |
| `is`         | Compares if two objects have the same identity.                             |
| `lambda`     | Defines an anonymous (unnamed) function.                                    |
| `None`       | Represents the absence of a value.                                          |
| `nonlocal`   | Declares a nonlocal variable in a nested function.                          |
| `not`        | Logical "NOT" operator.                                                     |
| `or`         | Logical "OR" operator.                                                      |
| `pass`       | Null statement (does nothing).                                              |
| `raise`      | Manually raises an exception.                                               |
| `return`     | Returns a value from a function.                                            |
| `True`       | Boolean value "true".                                                      |
| `try`        | Block that handles exceptions.                                              |
| `while`      | Loop that runs while a condition is true.                                   |
| `with`       | Simplifies resource management (e.g., file handling).                       |
| `yield`      | Returns a value from a generator function.                                   |

You can view all Python keywords using the `keyword` module:
```python
import keyword
print(keyword.kwlist)
```

---

## 🔹 **2. Whitespace and Indentation**

Python uses **indentation** to define code blocks, instead of braces (`{}`) or keywords like `begin` and `end`. Incorrect indentation will result in a `IndentationError`.

### **Example of Correct Indentation:**
```python
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, world!")
```

### **Common Mistakes:**
- Mixing spaces and tabs.
- Incorrect indentation levels.

**Tip:** Use four spaces per indentation level for consistency.

---

## 🔹 **3. Namespaces and Variable Scope**

A **namespace** is a mapping between names and objects. Python has different types of namespaces:

### **Types of Namespaces:**
1. **Built-in:** Contains Python’s built-in functions and exceptions (e.g., `print`, `len`).
2. **Global:** Contains variables defined at the module level.
3. **Local:** Contains variables defined within a function.
4. **Enclosing:** Contains variables in the nearest enclosing function (in nested functions).

Python resolves variable names using the **LEGB rule** (Local, Enclosing, Global, Built-in).

### **Example:**
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

## 🔹 **4. Equality and Identity in Python**

Python provides two ways to compare objects:

### **1. `==` (Equality)**
- Checks if the values of two objects are the same.
- Calls the `__eq__()` method of the object.

### **2. `is` (Identity)**
- Checks if two objects refer to the same memory location.
- Calls the `id()` function internally.

### **Example:**
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Output: True (values are the same)
print(a is b)  # Output: False (different memory locations)

c = a
print(a is c)  # Output: True (same object)
```

### **Common Pitfall:**
```python
x = 256
y = 256
print(x is y)  # Output: True (due to small integer caching)
```
However, for larger integers or other types, `is` may return `False`:
```python
x = 1000
y = 1000
print(x is y)  # Output: False
```

---

## 🔹 **5. Best Practices for Core Concepts**

1. **Use keywords appropriately:**
   - Avoid using keywords as variable names.

2. **Maintain consistent indentation:**
   - Use 4 spaces per indentation level.
   - Avoid mixing spaces and tabs.

3. **Understand namespaces:**
   - Use local variables inside functions to avoid conflicts.
   - Avoid over-reliance on global variables.

4. **Use `==` for value comparison:**
   - Reserve `is` for checking object identity.

5. **Be aware of Python's caching:**
   - Small integers and short strings may be cached and reused, leading to unexpected results with `is`.

---

## 🔹 **6. Practice Challenges**

### **Challenge 1: Understanding Keywords**
Identify and correct the error in the following code:
```python
def class():
    return 42
```

### **Challenge 2: Equality vs. Identity**
Write a function that demonstrates the difference between `==` and `is` using two different lists.
```python
def compare_lists():
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b)  # True
    print(a is b)  # False
```

### **Challenge 3: Resolving Variable Scope**
What will be the output of the following code?
```python
x = "global"

def test_scope():
    x = "local"
    print(x)

test_scope()
print(x)
```

---

## 🔹 **7. Summary**
Understanding Python's keywords, whitespace rules, namespaces, and object comparisons is essential for writing clean and maintainable code. By following best practices and avoiding common pitfalls, you can prevent bugs and ensure that your programs behave as expected.

Continue to the next section: **[Exception Handling](exception-handling.md)**