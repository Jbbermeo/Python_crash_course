# List Comprehensions and Lambda Functions in Python

List comprehensions and lambda functions are powerful tools in Python for writing concise, readable, and efficient code. In Object-Oriented Programming (OOP), these features are often used to streamline data transformations and functional operations within class methods.

---

## 🔹 **1. What Are List Comprehensions?**

A **list comprehension** is a compact way to generate lists. It combines iteration and optional filtering into a single expression.

### **Syntax:**
```python
[expression for item in iterable if condition]
```

### **Example:**
```python
squares = [x * x for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

### **With Filtering:**
```python
even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]
```

---

## 🔹 **2. Benefits of List Comprehensions**

1. **Conciseness:**
   - Reduce the amount of code compared to traditional loops.

2. **Readability:**
   - Clearly express the intent of list creation in a single line.

3. **Performance:**
   - Often faster than manually building a list using `append()` in a loop.

### **Example Comparison:**
**Using a loop:**
```python
squares = []
for x in range(5):
    squares.append(x * x)
```

**Using a list comprehension:**
```python
squares = [x * x for x in range(5)]
```

---

## 🔹 **3. Nested List Comprehensions**

List comprehensions can be nested to work with multi-dimensional data.

### **Example:**
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 🔹 **4. What Are Lambda Functions?**

A **lambda function** is an anonymous function defined using the `lambda` keyword. It can take any number of arguments but contains only a single expression.

### **Syntax:**
```python
lambda arguments: expression
```

### **Example:**
```python
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
```

Lambda functions are often used with higher-order functions like `map()`, `filter()`, and `sorted()`.

---

## 🔹 **5. Differences Between `map()`, `filter()`, and `sorted()`**

Python provides these higher-order functions to apply lambda functions efficiently to iterable data structures.

### **1. `map()`:**
- Applies a function to each element in an iterable and returns an iterator.
- Suitable for transforming data.

**Example:**
```python
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16]
```

### **2. `filter()`:**
- Applies a function to each element in an iterable and returns only the elements that satisfy a condition (i.e., for which the function returns `True`).
- Useful for data filtering.

**Example:**
```python
even_numbers = list(filter(lambda x: x % 2 == 0, range(10)))
print(even_numbers)  # Output: [0, 2, 4, 6, 8]
```

### **3. `sorted()`:**
- Sorts an iterable based on a key function.
- By default, it sorts in ascending order, but you can customize it with a lambda function.

**Example:**
```python
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)  # Output: ['apple', 'cherry', 'banana']
```

| Function  | Purpose                | Output Example                         |
|-----------|------------------------|-----------------------------------------|
| `map()`   | Data transformation     | `[1, 4, 9, 16]`                         |
| `filter()`| Data filtering          | `[0, 2, 4, 6, 8]`                       |
| `sorted()`| Sorting by custom rule  | `['apple', 'cherry', 'banana']`         |

---

## 🔹 **6. Combining List Comprehensions and Lambda Functions in OOP**

In Object-Oriented Programming, list comprehensions and lambda functions can be used to streamline methods that manipulate data.

### **Example:**
```python
class DataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_and_square(self):
        return [x * x for x in self.data if x % 2 == 0]

    def apply_custom_function(self, func):
        return [func(x) for x in self.data]

processor = DataProcessor([1, 2, 3, 4, 5])
print(processor.filter_and_square())  # Output: [4, 16]
print(processor.apply_custom_function(lambda x: x + 10))  # Output: [11, 12, 13, 14, 15]
```

---

## 🔹 **7. Best Practices**

1. **Keep expressions simple:**
   - Avoid overly complex list comprehensions or lambda functions that reduce readability.

2. **Use named functions when necessary:**
   - If a lambda function becomes too complex, define a regular function instead.

3. **Use comprehensions for clarity:**
   - Prefer list comprehensions over `map()` and `filter()` for better readability.

4. **Avoid nested comprehensions:**
   - Use loops if nesting becomes difficult to understand.

---

## 🔹 **8. Practice Challenges**

### **Challenge 1: List Comprehension**
Create a list comprehension that generates the cubes of even numbers from 1 to 10.
```python
even_cubes = [x ** 3 for x in range(1, 11) if x % 2 == 0]
print(even_cubes)  # Output: [8, 64, 216, 512, 1000]
```

### **Challenge 2: Lambda Function**
Write a lambda function that multiplies a number by 5 and apply it to a list of numbers using `map()`.
```python
multiply_by_five = lambda x: x * 5
numbers = [1, 2, 3, 4]
result = list(map(multiply_by_five, numbers))
print(result)  # Output: [5, 10, 15, 20]
```

---

## 🔹 **9. Summary**
List comprehensions and lambda functions enhance Python’s readability and efficiency. By using these tools effectively, you can streamline data processing tasks and simplify method implementations in OOP. Functions like `map()`, `filter()`, and `sorted()` leverage lambda functions to transform, filter, and sort data concisely. Understanding when and how to use these features will help you write cleaner, more maintainable code.

Continue to the next section: **[Decorators in Python](11_decorators-in-python.md)**.
