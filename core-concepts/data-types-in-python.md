# Data Types in Python

Understanding data types is fundamental in Python programming. Mastering how they work, interact, and can be optimized is crucial as you move into Object-Oriented Programming (OOP). This section explores Python's core data types and offers insights into advanced usage for efficiency and scalability.

---

## 🔹 **1. Core Data Types**
Python's main built-in data types include:

- **string Types:**
  - `str` (String): A sequence of characters (e.g., `'Hello'`, `"Python"`).

- **Numeric Types:**
  - `int` (Integer): Whole numbers (e.g., `42`, `-7`).
  - `float` (Floating-point): Decimal numbers (e.g., `3.14`, `-0.001`).
  - `complex`: Numbers with a real and imaginary part (e.g., `3 + 4j`).

- **Boolean Type:**
  - `bool`: Represents truth values (`True`, `False`).

- **None Type:**
  - `NoneType`: Represents the absence of a value (`None`).

---

## 🔹 **2. String Type**

### What is a String?
A string is a sequence of characters that can include letters, digits, symbols, and whitespace. In Python, strings are represented by the `str` type. They are **immutable**, meaning they cannot be modified after they are created. Any operation that appears to modify a string will actually create a new string in memory.

### String Literals and Usage
String literals define text data in Python. You can use different types of quotes depending on the scenario:

- **Single quotes (' ')**: Commonly used for short, simple strings.
  ```python
  single_quote_str = 'Hello'
  ```

- **Double quotes (" ")**: Used when the string itself contains single quotes to avoid escaping.
  ```python
  double_quote_str = "It's a sunny day!"
  ```

- **Triple quotes (''' ''' or """ """)**: Used for multi-line strings or documentation strings (docstrings).
  ```python
  triple_quote_str = """This is 
  a multi-line string."""
  ```

### When to Use Each Literal Type
- Use **single quotes** or **double quotes** for regular text.
- Use **triple quotes** for text that spans multiple lines or for strings that include both single and double quotes.

### String Operations and Concepts
Python strings support a wide variety of operations, including concatenation, repetition, indexing, slicing, and substring testing.

#### 1. **Concatenation**
Concatenation refers to joining two or more strings together using the `+` operator. It is commonly used to build longer strings from smaller pieces.

Example:
```python
greeting = "Hello, " + "World!"
print(greeting)  # Output: Hello, World!
```

Concatenation does **not** modify the original strings. Instead, a new string is created.

#### 2. **Repetition**
Repeating a string multiple times is done using the `*` operator. This is useful when you need repeated patterns in a string.

Example:
```python
repeat = "Hi! " * 3
print(repeat)  # Output: Hi! Hi! Hi! 
```

#### 3. **Indexing**
Indexing allows you to access individual characters in a string. In Python, string indices start from 0. Negative indices can be used to access characters from the end of the string.

Example:
```python
text = "Python"
print(text[0])    # Output: P
print(text[-1])   # Output: n
```

#### 4. **Slicing**
Slicing is a technique to extract a portion of a string using the format `start:end:step`. The slice includes characters from the start index up to, but not including, the end index.

Examples:
```python
text = "Python"
print(text[1:4])  # Output: yth
print(text[:3])   # Output: Pyt
print(text[::2])  # Output: Pto
```

Slicing does **not** modify the original string. It returns a new substring.

#### 5. **Substring Testing**
You can check if a substring exists within a string using the `in` keyword.

Example:
```python
print("Py" in "Python")  # Output: True
print("Java" in "Python")  # Output: False
```

### Common String Methods
Python provides several built-in methods to manipulate strings. Some commonly used methods include:

- **`str.upper()`**: Converts all characters to uppercase.
  ```python
  print("hello".upper())  # Output: HELLO
  ```

- **`str.lower()`**: Converts all characters to lowercase.
  ```python
  print("HELLO".lower())  # Output: hello
  ```

- **`str.strip()`**: Removes leading and trailing whitespace.
  ```python
  print("  hello  ".strip())  # Output: hello
  ```

- **`str.replace()`**: Replaces occurrences of a substring with another substring.
  ```python
  print("Hello World".replace("World", "Python"))  # Output: Hello Python
  ```

- **`str.split()`**: Splits a string into a list of substrings based on a delimiter.
  ```python
  print("one,two,three".split(","))  # Output: ['one', 'two', 'three']
  ```

- **`str.join()`**: Joins a list of strings into a single string, using a separator.
  ```python
  words = ["Hello", "World"]
  print(" ".join(words))  # Output: Hello World
  ```

### Immutability of Strings
Strings in Python are **immutable**, meaning once a string is created, its contents cannot be changed. Instead, any string operation results in a new string.

Example:
```python
original = "Hello"
modified = original + " World"
print(original)  # Output: Hello
print(modified)  # Output: Hello World
```

Here, the `original` string remains unchanged.

### String and Other Data Types

#### Combining Strings with Other Data Types
Python does not allow implicit concatenation of strings with other data types. You must explicitly convert other types to strings using `str()`.

Example:
```python
age = 25
message = "I am " + str(age) + " years old."
print(message)  # Output: I am 25 years old.
```

#### String Representation of Booleans and None
- Boolean values convert to strings as `"True"` or `"False"`.
  ```python
  print("The result is: " + str(True))  # Output: The result is: True
  ```

- `None` converts to the string `"None"`.
  ```python
  print("Value: " + str(None))  # Output: Value: None
  ```

### Escape Characters
Escape characters allow you to include special characters in strings, such as newlines or tabs, that are not easily typed.

#### Common Escape Characters
- `\n`: Newline
- `\t`: Tab
- `\\`: Backslash
- `\"`: Double quote
- `\'`: Single quote

#### Example Usage:
```python
text = "Line 1\nLine 2"
print(text)
# Output:
# Line 1
# Line 2
```

Escape sequences are essential when working with special characters or formatting text output.

## 🔹 **3. Numeric Type in Python**

### What are Numeric Data Types?
Numeric data types in Python represent numbers and allow various arithmetic operations. Python supports three primary numeric types:

1. **Integers (`int`)**: Whole numbers, positive or negative, without a decimal point.
2. **Floating-point numbers (`float`)**: Numbers with a decimal point.
3. **Complex numbers (`complex`)**: Numbers with both real and imaginary parts.

### Integer (`int`)
An integer is a whole number, positive or negative, without a fractional part.

#### Examples:
```python
x = 42
negative_number = -10
large_number = 10_000_000  # Underscores can be used for readability
```

#### Characteristics:
- Supports arithmetic operations (addition, subtraction, multiplication, etc.).
- No maximum size limitation (limited only by available memory).

### Floating-point (`float`)
A floating-point number has a decimal point and is used to represent real numbers.

#### Examples:
```python
pi = 3.14159
negative_float = -0.01
scientific_notation = 1.23e4  # Equivalent to 12300.0
```

#### Characteristics:
- Precision is platform-dependent but generally accurate to about 15-17 decimal places.
- Useful for scientific calculations, measurements, and financial data.

### Complex Numbers (`complex`)
A complex number has a real part and an imaginary part, represented as `a + bj`.

#### Examples:
```python
complex_num = 3 + 4j
print(complex_num.real)  # Output: 3.0
print(complex_num.imag)  # Output: 4.0
```

### Arithmetic Operations
Python supports standard arithmetic operations on numeric types.

#### Addition (`+`):
```python
result = 5 + 10  # Output: 15
```

#### Subtraction (`-`):
```python
result = 20 - 5  # Output: 15
```

#### Multiplication (`*`):
```python
result = 3 * 4  # Output: 12
```

#### Division (`/`):
```python
result = 10 / 2  # Output: 5.0 (always returns a float)
```

#### Floor Division (`//`):
Performs division and returns the largest integer less than or equal to the result.
```python
result = 10 // 3  # Output: 3
```

#### Modulus (`%`):
Returns the remainder of a division.
```python
result = 10 % 3  # Output: 1
```

#### Exponentiation (`**`):
Raises a number to the power of another number.
```python
result = 2 ** 3  # Output: 8
```

### Type Conversion
You can convert between different numeric types using built-in functions.

#### Conversion Examples:
```python
x = 10          # Integer
y = float(x)    # Converts to 10.0 (float)
z = int(3.14)   # Converts to 3 (integer)
```

### Mathematical Functions
Python provides various mathematical functions through the `math` module.

#### Examples:
```python
import math

# Square root
print(math.sqrt(16))  # Output: 4.0

# Power
print(math.pow(2, 3))  # Output: 8.0

# Rounding
print(round(3.14159, 2))  # Output: 3.14

# Absolute value
print(abs(-10))  # Output: 10

# Ceiling and floor
print(math.ceil(4.2))  # Output: 5
print(math.floor(4.8))  # Output: 4
```

### Accuracy and Precision
Python's numeric types have different levels of accuracy and precision:

- **Integers** have unlimited precision, meaning they can grow as large as the available memory allows.
- **Floats** have a precision of about 15-17 decimal places. However, due to the limitations of binary floating-point arithmetic, some values may not be represented exactly.

#### Example of floating-point imprecision:
```python
result = 0.1 + 0.2
print(result)  # Output: 0.30000000000000004
```

To handle floating-point inaccuracies, consider using the `decimal` module for high-precision arithmetic.

#### Example with `decimal`:
```python
from decimal import Decimal

x = Decimal('0.1') + Decimal('0.2')
print(x)  # Output: 0.3
```

### Comparison Operations
Numeric types support comparison operations, which return boolean values.

#### Examples:
```python
print(10 > 5)     # Output: True
print(10 == 5)    # Output: False
print(10 != 5)    # Output: True
```

### Numeric Data Type Interactions
Python automatically handles operations between numeric types. However, when combining integers and floats, the result is always a float.

#### Example:
```python
result = 5 + 2.5  # Output: 7.5 (float)
```

When working with complex numbers, operations involving other numeric types will return a complex result.

#### Example:
```python
result = (2 + 3j) + 5  # Output: (7 + 3j)
```

### Infinity and NaN (Not a Number)
Python's `float` type can represent special values such as infinity and NaN.

#### Examples:
```python
positive_infinity = float('inf')
negative_infinity = float('-inf')
not_a_number = float('nan')

print(positive_infinity > 1_000_000)  # Output: True
print(math.isnan(not_a_number))       # Output: True
```
## 🔹 **3. Boolean Types in Python**

### What is a Boolean Data Type?
The Boolean data type (`bool`) represents one of two values: **True** or **False**. Booleans are often used in conditional statements, loops, and logical operations to control program flow.

### Boolean Values
In Python, the `bool` type has two constant values:
- `True`
- `False`

#### Example:
```python
is_sunny = True
is_raining = False
print(is_sunny)  # Output: True
```

Booleans are case-sensitive; `true` and `false` (lowercase) are not valid.

### Boolean Conversion
You can convert other data types to boolean values using the `bool()` function. In Python, the following values are considered **False**:
- `None`
- `0` (for numeric types)
- `0.0`, `0j` (for floats and complex numbers)
- Empty sequences and collections (`[]`, `()`, `{}`, `''`)

All other values are considered **True**.

#### Examples:
```python
print(bool(0))        # Output: False
print(bool(1))        # Output: True
print(bool("Python")) # Output: True
print(bool([]))       # Output: False
```

### Boolean Operators
Python supports logical operators that work with boolean values:

#### **Logical AND (`and`)**
Returns `True` if both operands are `True`.
```python
print(True and True)   # Output: True
print(True and False)  # Output: False
```

#### **Logical OR (`or`)**
Returns `True` if at least one operand is `True`.
```python
print(True or False)   # Output: True
print(False or False)  # Output: False
```

#### **Logical NOT (`not`)**
Returns the opposite of the boolean value.
```python
print(not True)        # Output: False
print(not False)       # Output: True
```

### Comparison Operations
Comparison operators return boolean values and are commonly used in conditions.

#### Comparison Operators:
- `==` (equal to)
- `!=` (not equal to)
- `>` (greater than)
- `<` (less than)
- `>=` (greater than or equal to)
- `<=` (less than or equal to)

#### Examples:
```python
x = 10
y = 5
print(x > y)          # Output: True
print(x == y)         # Output: False
print(x != y)         # Output: True
```

### Boolean Short-circuiting
Python uses short-circuit evaluation for boolean expressions. This means:
- In an `and` expression, if the first operand is `False`, the rest of the expression is not evaluated.
- In an `or` expression, if the first operand is `True`, the rest of the expression is not evaluated.

#### Example:
```python
def expensive_check():
    print("This won't run if short-circuited.")
    return True

print(False and expensive_check())  # Output: False
print(True or expensive_check())    # Output: True
```

### Booleans in Conditional Statements
Booleans are frequently used in `if`, `elif`, and `else` statements to control program flow.

#### Example:
```python
is_logged_in = True
if is_logged_in:
    print("Welcome!")
else:
    print("Please log in.")
```

### Booleans in Loops
Boolean expressions can also control loops.

#### Example:
```python
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1
```

### Boolean Arithmetic
In Python, boolean values can be used in arithmetic operations. `True` is treated as `1` and `False` as `0`.

#### Example:
```python
print(True + True)   # Output: 2
print(False * 5)     # Output: 0
```

### Boolean Methods
Python provides several methods that return boolean values when applied to strings, lists, and other objects.

#### Examples:
- **`str.isalpha()`**: Returns `True` if all characters in the string are alphabetic.
  ```python
  print("Hello".isalpha())  # Output: True
  ```
- **`list.is_empty()` (manual check)**: Check if a list is empty.
  ```python
  my_list = []
  print(bool(my_list))  # Output: False
  ```
## 🔹 **4. NoneType in Python**

### What is NoneType?
`NoneType` is a special data type in Python that represents the absence of a value or a null value. It has a single constant value: `None`. The `None` keyword is commonly used to indicate that a variable does not have a meaningful value.

### Characteristics of `NoneType`
- `None` is the only value of the `NoneType` data type.
- `None` is often used as a placeholder or default return value.
- It is commonly used to signify that a function does not return a value.

#### Example:
```python
def example_function():
    print("This function returns nothing")

result = example_function()
print(result)  # Output: None
```

### Checking for `None`
To check if a variable is `None`, you should use the `is` operator instead of `==`. This is because `None` is a singleton object.

#### Example:
```python
x = None
if x is None:
    print("x is None")
```

Avoid using `==` for comparison with `None`, as it can lead to unexpected results if overridden by custom equality logic.

### Common Uses of `None`

#### 1. **Default Values for Function Parameters**
`None` is often used as a default argument in functions.

Example:
```python
def greet(name=None):
    if name is None:
        print("Hello, Guest!")
    else:
        print(f"Hello, {name}!")

greet()          # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!
```

#### 2. **Function Return Value**
Functions that do not explicitly return a value will return `None` by default.

Example:
```python
def do_nothing():
    pass

print(do_nothing())  # Output: None
```

#### 3. **Placeholders in Data Structures**
`None` can be used as a placeholder in lists, dictionaries, and other data structures.

Example:
```python
data = [1, 2, None, 4]
print(data)  # Output: [1, 2, None, 4]
```

#### 4. **Representing Missing or Optional Values**
In applications, `None` is often used to represent missing or optional data.

Example:
```python
user_info = {"name": "John", "age": None}
if user_info["age"] is None:
    print("Age is missing")
```

### Operations with `None`
`None` cannot be used in arithmetic operations or comparisons with numeric types.

Example:
```python
# This will raise a TypeError:
# result = None + 5
```

However, you can compare `None` with other values using logical operators like `is` and `is not`.

Example:
```python
x = None
print(x is not None)  # Output: False
```

### Boolean Representation of `None`
`None` is considered a **falsy** value in Python. When used in a boolean context, it evaluates to `False`.

Example:
```python
x = None
if not x:
    print("x is falsy")  # Output: x is falsy
```

### Avoiding Common Mistakes with `None`
- Do not use `None` in arithmetic operations.
- Always use `is` or `is not` for comparison instead of `==`.
- Be cautious when checking for `None` in loops or conditions, as it evaluates to `False` in boolean contexts.

## 🔹 **5. Next Steps**
Understanding data types is essential as you move forward into OOP concepts like **attributes**, **methods**, and **class design**. These foundational skills will help you design more efficient and scalable object-oriented applications.

Continue to the next section: **[Data Structures in Python](data-structures.md)**.
