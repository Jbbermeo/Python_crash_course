# Data Types in Python

Understanding data types is fundamental in Python programming. Mastering how they work, interact, and can be optimized is crucial as you move into Object-Oriented Programming (OOP). This section explores Python's core data types and offers insights into advanced usage for efficiency and scalability.

---

## 🔹 **1. Core Data Types**
Python's main built-in data types include:

- **Numeric Types:**
  - `int` (Integer): Whole numbers (e.g., `42`, `-7`).
  - `float` (Floating-point): Decimal numbers (e.g., `3.14`, `-0.001`).
  - `complex`: Numbers with a real and imaginary part (e.g., `3 + 4j`).

- **Sequence Types:**
  - `str` (String): A sequence of characters (e.g., `'Hello'`, `"Python"`).
  - `list`: Ordered and mutable collections (e.g., `[1, 2, 3]`).
  - `tuple`: Ordered and immutable collections (e.g., `(1, 2, 3)`).
  
- **Mapping Type:**
  - `dict`: Unordered key-value pairs (e.g., `{'name': 'Alice', 'age': 30}`).

- **Set Types:**
  - `set`: Unordered collections of unique elements (e.g., `{1, 2, 3}`).
  - `frozenset`: Immutable version of a set.

- **Boolean Type:**
  - `bool`: Represents truth values (`True`, `False`).

- **None Type:**
  - `NoneType`: Represents the absence of a value (`None`).

---

## 🔹 **2. Type Conversion**
Python allows conversion between different data types:

- **Implicit Conversion:** Python sometimes converts types automatically (e.g., `int` to `float`).
  ```python
  result = 3 + 4.5  # result is a float: 7.5
  ```

- **Explicit Conversion:** Use built-in functions to convert types manually.
  ```python
  age_str = "25"
  age_int = int(age_str)  # Converts string to integer
  ```

Efficient type conversion is crucial when working with large data structures, improving both performance and memory usage.

---

## 🔹 **3. Immutability and Performance**
Some data types, such as `tuple` and `str`, are **immutable**, meaning they cannot be changed after creation. This immutability provides several benefits:

- **Efficiency:** Immutable objects are faster to access and hash.
- **Safety:** Reduces the risk of unintended side effects in your code.
- **Use in OOP:** Immutable types are ideal for creating hashable keys in `dict` and attributes in classes that should remain constant.

Example:
```python
my_tuple = (1, 2, 3)
# This will raise an error: my_tuple[0] = 10
```

---

## 🔹 **4. Memory Management and Data Types**
Understanding how Python manages memory is key for optimization. Python uses **reference counting** and **garbage collection** to manage objects.

Tips for efficient memory usage:
- Prefer `tuple` over `list` when immutability is required.
- Use `frozenset` instead of `set` when performance and immutability are important.
- Avoid excessive object creation inside loops.

Example:
```python
# Inefficient
for _ in range(1000000):
    data = [1, 2, 3]

# Efficient
data = [1, 2, 3]
for _ in range(1000000):
    # Reuse the same object
    process(data)
```

---

## 🔹 **5. Practice Challenges**

### 🔸 **Challenge 1: Identify Data Types**
You have been given the following data points:
```python
values = [42, 3.14, "Hello World", [1, 2, 3], {"name": "Alice"}, (5, 6), True, None]
```
**Task:** Iterate over the list and print the data type of each element.

**Expected Output:**
```
int
float
str
list
dict
tuple
bool
NoneType
```

---

### 🔸 **Challenge 2: Type Conversion**
You receive data from an API that looks like this:
```python
data = {"age": "30", "height": "175.5", "is_member": "True"}
```
**Task:** Convert the values to their appropriate data types (`int`, `float`, `bool`).

**Example Solution:**
```python
data["age"] = int(data["age"])
data["height"] = float(data["height"])
data["is_member"] = data["is_member"] == "True"
```

---

### 🔸 **Challenge 3: Immutability Test**
Create a function that tries to modify a tuple:
```python
def modify_tuple(input_tuple):
    try:
        input_tuple[0] = 100
    except TypeError as e:
        return str(e)

# Test the function
result = modify_tuple((1, 2, 3))
print(result)
```
**Task:** Explain why the error occurs and how immutability helps in software design.

---

## 🔹 **6. Next Steps**
Understanding data types is essential as you move forward into OOP concepts like **attributes**, **methods**, and **class design**. These foundational skills will help you design more efficient and scalable object-oriented applications.

Continue to the next section: **[Data Structures in Python](data-structures.md)**.
