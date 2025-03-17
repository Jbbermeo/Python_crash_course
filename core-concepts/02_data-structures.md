# Data Structures in Python

Data structures are critical for efficient data management and performance optimization in Python. In Object-Oriented Programming (OOP), choosing the right data structure can significantly impact the scalability and maintainability of your application.

This section provides an in-depth exploration of Python's core data structures, their internal mechanisms, memory considerations, and their role in OOP.

---

## 🔹 **1. Core Data Structures**
Python provides a variety of built-in data structures, each with distinct properties and use cases.

- **List:**
  - Ordered, mutable collection of elements (e.g., `[1, 2, 3]`).
  - Efficient for dynamic data storage but requires resizing when capacity is exceeded.
  - Lists offer in-place modification through methods like `append()`, which is more efficient than using the `+` operator because it avoids creating a new list and reallocating memory.

- **Tuple:**
  - Ordered, immutable collection of elements (e.g., `(1, 2, 3)`).
  - More memory-efficient than lists and useful when data should remain constant.
  - Tuples are immutable, but can contain mutable elements like lists, which may introduce unintended changes if modified.

- **Dictionary (`dict`):**
  - Unordered collection of key-value pairs (e.g., `{'name': 'Alice', 'age': 30}`).
  - Optimized for fast lookups and updates using hash tables.
  - Keys must be immutable and hashable, making dictionaries ideal for caching and indexing.

- **Set:**
  - Unordered collection of unique elements (e.g., `{1, 2, 3}`).
  - Supports fast membership testing and mathematical set operations.
  - Useful for filtering duplicates and fast lookups.

- **Frozenset:**
  - Immutable version of a set.
  - Provides the same advantages as sets but with added immutability for data that should remain constant.

---

## 🔹 **2. Lists in Python**

### What is a List?
A list in Python is an ordered, mutable collection of items. Lists can hold elements of different data types, including other lists. They are one of the most versatile and commonly used data structures in Python.

#### Example:
```python
my_list = [1, "apple", 3.14, [5, 6, 7]]
print(my_list)  # Output: [1, 'apple', 3.14, [5, 6, 7]]
```

### Characteristics of Lists
- **Ordered**: The order of elements is preserved.
- **Mutable**: Elements can be added, removed, or modified without creating a new list in memory.
- **Dynamic**: Lists can grow and shrink in size.
- **Supports Multiple Data Types**: Elements can be of different data types.

#### **Mutability**
The mutability of lists means that operations that change the contents of a list (e.g., adding, removing, or modifying elements) affect the list directly in memory rather than creating a new list. This allows efficient in-place modifications but can lead to unintended side effects if multiple references point to the same list.

#### Example of mutability:
```python
a = [1, 2, 3]
b = a  # 'b' points to the same list as 'a'
b.append(4)
print(a)  # Output: [1, 2, 3, 4] - both 'a' and 'b' are affected
```

To avoid this, you can create a copy of the list using the `copy()` method or slicing.
```python
b = a.copy()  # Creates a new list in memory
```

---

### Creating Lists
You can create lists using square brackets (`[]`).

#### Examples:
```python
empty_list = []
numbers = [1, 2, 3, 4]
```

You can also use the `list()` function to create lists.
```python
my_list = list((1, 2, 3))
print(my_list)  # Output: [1, 2, 3]
```

---

### Accessing List Elements
Elements in a list can be accessed using their index. Python supports both positive and negative indexing.

#### Examples:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # Output: apple
print(fruits[-1])  # Output: cherry (negative index)
```

### Modifying List Elements
You can modify an element by assigning a new value to its index.
```python
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
```

---

### List Operations vs. List Methods
Python provides both **operations** and **methods** to work with lists. Understanding the difference is essential:

#### **List Operations**
Operations are performed using Python's built-in operators. These operations often involve creating new lists.

- **Concatenation (`+`)**: Combines two lists to create a new list.
  ```python
  list1 = [1, 2]
  list2 = [3, 4]
  combined = list1 + list2
  print(combined)  # Output: [1, 2, 3, 4]
  ```

- **Repetition (`*`)**: Repeats a list multiple times to create a new list.
  ```python
  repeated = ["a"] * 3
  print(repeated)  # Output: ['a', 'a', 'a']
  ```

- **Membership Testing (`in`)**: Checks if an element is present in the list.
  ```python
  print("apple" in fruits)  # Output: True
  ```

#### **List Methods**
Methods are functions specific to the list object. They modify the list in place, affecting the same object in memory.

- **`append()`**: Adds an element to the end of the list.
  ```python
  numbers = [1, 2, 3]
  numbers.append(4)
  print(numbers)  # Output: [1, 2, 3, 4]
  ```

- **`extend()`**: Appends elements from another iterable to the list.
  ```python
  numbers.extend([5, 6])
  print(numbers)  # Output: [1, 2, 3, 4, 5, 6]
  ```

- **`remove()`**: Removes the first occurrence of a specified element.
  ```python
  numbers.remove(2)
  print(numbers)  # Output: [1, 3, 4, 5, 6]
  ```

---

### List Methods Summary
Here are some common list methods and their uses:

- **`insert()`**: Inserts an element at a specific index.
  ```python
  numbers.insert(2, 10)
  print(numbers)  # Output: [1, 3, 10, 4, 5, 6]
  ```

- **`pop()`**: Removes and returns an element at a specific index (or the last element by default).
  ```python
  element = numbers.pop()
  print(element)  # Output: 6
  print(numbers)  # Output: [1, 3, 10, 4, 5]
  ```

- **`count()`**: Counts the occurrences of an element.
  ```python
  print(numbers.count(3))  # Output: 1
  ```

- **`sort()`**: Sorts the list in ascending order.
  ```python
  numbers.sort()
  print(numbers)  # Output: [1, 3, 4, 5, 10]
  ```

- **`reverse()`**: Reverses the order of elements.
  ```python
  numbers.reverse()
  print(numbers)  # Output: [10, 5, 4, 3, 1]
  ```

---

### Memory and Performance Considerations
Lists are dynamic data structures that allocate memory as needed. Python's list implementation uses an array under the hood, meaning:

1. **Contiguous Memory Allocation**: Lists store elements in a contiguous block of memory, which allows for fast indexing.
2. **Resizing**: When elements are added beyond the list's current capacity, Python allocates a larger block of memory and copies the existing elements to the new location.
3. **In-place Modifications**: Methods like `append()`, `remove()`, and `sort()` modify the list in memory without creating new objects, which can improve performance for large data sets.

#### Example of resizing behavior:
```python
import sys
numbers = []
print(sys.getsizeof(numbers))  # Output: initial size in bytes
numbers.append(1)
print(sys.getsizeof(numbers))  # Output: increased size
```

---

### Iterating Over a List
You can iterate over a list using a `for` loop.

#### Example:
```python
for fruit in fruits:
    print(fruit)
```

---

### List Comprehensions
List comprehensions provide a concise way to create lists.

#### Example:
```python
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

---

### Nested Lists
Lists can contain other lists, creating a nested structure.

#### Example:
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Output: 6
```
---
## 🔹 **3. Tuples in Python**

### What is a Tuple?
A tuple in Python is an ordered, immutable collection of items. Like lists, tuples can store elements of different data types, but unlike lists, tuples cannot be modified after they are created.

#### Example:
```python
my_tuple = (1, "apple", 3.14)
print(my_tuple)  # Output: (1, 'apple', 3.14)
```

### Characteristics of Tuples
- **Ordered**: The order of elements is preserved.
- **Immutable**: Once created, elements in a tuple cannot be changed, added, or removed.
- **Supports Multiple Data Types**: Elements can be of different data types.
- **Allows Duplicates**: Tuples can contain duplicate values.
- **Can Contain Mutable Elements**: Although tuples themselves are immutable, they can contain mutable elements, such as lists. Modifying the mutable element affects the tuple indirectly.

#### Example:
```python
mutable_inside_tuple = (1, [2, 3], "text")
mutable_inside_tuple[1].append(4)
print(mutable_inside_tuple)  # Output: (1, [2, 3, 4], 'text')
```

#### Implications of Mutable Elements
1. **Unexpected Behavior**: Even though a tuple is immutable, changes to mutable elements can lead to unexpected behavior if not handled carefully.
2. **Hashability**: Tuples with mutable elements are not hashable and cannot be used as dictionary keys.

#### Example:
```python
my_tuple = (1, [2, 3])
# This will raise a TypeError:
# my_dict = {my_tuple: "value"}
```

---

### Creating Tuples
You can create tuples using parentheses `()` or the `tuple()` function.

#### Examples:
```python
empty_tuple = ()
my_tuple = (1, 2, 3)
```

You can also create a tuple without parentheses by separating values with commas.
```python
tuple_without_parentheses = 1, 2, 3
print(tuple_without_parentheses)  # Output: (1, 2, 3)
```

To create a tuple with a single element, you must include a comma after the element.
```python
single_element_tuple = (42,)
print(type(single_element_tuple))  # Output: <class 'tuple'>
```

---

### Accessing Tuple Elements
Elements in a tuple can be accessed using their index. Python supports both positive and negative indexing.

#### Examples:
```python
tuple_example = ("apple", "banana", "cherry")
print(tuple_example[0])   # Output: apple
print(tuple_example[-1])  # Output: cherry (negative index)
```

---

### Tuple Operations
Python provides operations for tuples, similar to lists. However, since tuples are immutable, these operations do not modify the tuple itself.

#### **1. Concatenation (`+`)**
Combines two tuples to create a new tuple.
```python
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2
print(combined)  # Output: (1, 2, 3, 4)
```

#### **2. Repetition (`*`)**
Repeats a tuple multiple times to create a new tuple.
```python
repeated = ("a",) * 3
print(repeated)  # Output: ('a', 'a', 'a')
```

#### **3. Membership Testing (`in`)**
Checks if an element is present in the tuple.
```python
print("apple" in tuple_example)  # Output: True
```

---

### Tuple Methods
Tuples have a limited number of built-in methods due to their immutability.

#### **1. `count()`**
Counts the occurrences of a specified element.
```python
numbers = (1, 2, 2, 3)
print(numbers.count(2))  # Output: 2
```

#### **2. `index()`**
Returns the index of the first occurrence of a specified element.
```python
print(numbers.index(2))  # Output: 1
```

---

### Tuple Immutability and Performance
Since tuples are immutable, they offer some performance advantages over lists in certain situations.

#### **Benefits of Immutability**:
1. **Memory Efficiency**: Tuples use less memory than lists because they do not require additional overhead to support dynamic resizing.
2. **Hashability**: Tuples can be used as keys in dictionaries because they are hashable, unlike lists.

#### Example:
```python
my_dict = {(1, 2): "value"}
print(my_dict[(1, 2)])  # Output: value
```

---

### Tuple Packing and Unpacking

#### **Tuple Packing**
Packing refers to combining multiple values into a tuple.
```python
packed_tuple = 1, 2, 3
print(packed_tuple)  # Output: (1, 2, 3)
```

#### **Tuple Unpacking**
Unpacking allows you to assign elements of a tuple to multiple variables.
```python
a, b, c = packed_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
```

You can also use the `*` operator to unpack remaining elements into a list.
```python
first, *rest = (1, 2, 3, 4)
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4]
```

---

### Iterating Over a Tuple
You can iterate over a tuple using a `for` loop.

#### Example:
```python
tuple_items = ("apple", "banana", "cherry")
for item in tuple_items:
    print(item)
```

---

### Nested Tuples
Tuples can contain other tuples, creating a nested structure.

#### Example:
```python
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[1][0])  # Output: 3
```

---

## 🔹 **4. Dictionaries in Python**

### What is a Dictionary?
A dictionary in Python is an unordered, mutable collection of key-value pairs. Keys must be unique and immutable, while values can be of any data type and may be duplicated. Dictionaries provide fast lookups, insertions, and deletions.

#### Example:
```python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

### Characteristics of Dictionaries
- **Unordered**: The order of elements is not guaranteed (prior to Python 3.7).
- **Mutable**: You can add, remove, or modify key-value pairs.
- **Key-Value Structure**: Each key maps to a corresponding value.
- **Unique Keys**: Keys must be unique within the dictionary.

---

### Creating Dictionaries
You can create dictionaries using curly braces `{}` or the `dict()` function.

#### Examples:
```python
# Using curly braces
my_dict = {"name": "Bob", "age": 25}

# Using the dict() function
my_dict = dict(name="Bob", age=25)
```

You can also create an empty dictionary.
```python
empty_dict = {}
```

---

### Accessing Elements
Access dictionary values using their keys.

#### Example:
```python
my_dict = {"name": "Alice", "age": 30}
print(my_dict["name"])  # Output: Alice
```

If the key does not exist, accessing it with square brackets will raise a `KeyError`. To avoid this, use the `get()` method.
```python
print(my_dict.get("address", "Not found"))  # Output: Not found
```

---

### Modifying Dictionaries
You can add, update, or delete key-value pairs in a dictionary.

#### Adding and Updating Elements
```python
my_dict["city"] = "Los Angeles"  # Adding a new key-value pair
my_dict["age"] = 31               # Updating an existing key
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'Los Angeles'}
```

#### Deleting Elements
```python
del my_dict["age"]
print(my_dict)  # Output: {'name': 'Alice', 'city': 'Los Angeles'}
```

You can also use the `pop()` method to remove a key and return its value.
```python
value = my_dict.pop("name")
print(value)     # Output: Alice
print(my_dict)   # Output: {'city': 'Los Angeles'}
```

---

### Dictionary Methods
Python provides several built-in methods to work with dictionaries.

#### **1. `keys()`**
Returns a view object of all the keys in the dictionary.
```python
print(my_dict.keys())  # Output: dict_keys(['city'])
```

#### **2. `values()`**
Returns a view object of all the values in the dictionary.
```python
print(my_dict.values())  # Output: dict_values(['Los Angeles'])
```

#### **3. `items()`**
Returns a view object of all key-value pairs in the dictionary.
```python
print(my_dict.items())  # Output: dict_items([('city', 'Los Angeles')])
```

#### **4. `update()`**
Updates the dictionary with key-value pairs from another dictionary or iterable.
```python
my_dict.update({"state": "California"})
print(my_dict)  # Output: {'city': 'Los Angeles', 'state': 'California'}
```

#### **5. `clear()`**
Removes all elements from the dictionary.
```python
my_dict.clear()
print(my_dict)  # Output: {}
```

---

### Copying Dictionaries
To copy a dictionary, use the `copy()` method. Avoid copying by reference, as it can lead to unintended changes.

#### Example:
```python
original = {"name": "Alice"}
copy_dict = original.copy()
copy_dict["age"] = 30
print(original)    # Output: {'name': 'Alice'}
print(copy_dict)   # Output: {'name': 'Alice', 'age': 30}
```

---

### Iterating Over Dictionaries
You can iterate over keys, values, or key-value pairs using a `for` loop.

#### Examples:
```python
# Iterating over keys
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)
```

---

### Dictionary Operations

#### **Membership Testing (`in`)**
Check if a key exists in the dictionary.
```python
print("name" in my_dict)  # Output: True
```

#### **Dictionary Length (`len()`)**
Returns the number of key-value pairs in the dictionary.
```python
print(len(my_dict))  # Output: 1
```

---

### Nested Dictionaries
Dictionaries can contain other dictionaries, creating a nested structure.

#### Example:
```python
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
print(nested_dict["person1"]["name"])  # Output: Alice
```

---

### Dictionary Comprehensions
Dictionary comprehensions provide a concise way to create dictionaries.

#### Example:
```python
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---
## 🔹 **5. Sets and Frozensets in Python**

### What is a Set?
A set in Python is an unordered, mutable collection of unique elements. Sets are useful for performing mathematical set operations like union, intersection, and difference. They do not allow duplicate values.

#### Example:
```python
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}
```

### Characteristics of Sets
- **Unordered**: The elements have no defined order.
- **Mutable**: Elements can be added or removed.
- **Unique Elements**: Duplicate values are not allowed.
- **Non-Indexed**: Elements cannot be accessed by index.

---

### What is a Frozenset?
A frozenset is an immutable version of a set. Once created, elements in a frozenset cannot be added, removed, or modified. Frozensets are hashable and can be used as keys in dictionaries.

#### Example:
```python
frozen = frozenset([1, 2, 3])
print(frozen)  # Output: frozenset({1, 2, 3})
```

### Creating Sets and Frozensets

#### Creating a Set:
```python
# Using curly braces
my_set = {"apple", "banana", "cherry"}

# Using the set() function
my_set = set([1, 2, 3])
```

#### Creating an Empty Set:
```python
empty_set = set()  # Note: {} creates an empty dictionary, not a set
```

#### Creating a Frozenset:
```python
my_frozenset = frozenset(["apple", "banana", "cherry"])
```

---

### Set Operations
Sets support various operations to perform mathematical set operations.

#### **1. Union (`|` or `union()`)**
Returns a new set containing all unique elements from both sets.
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 | set2
print(result)  # Output: {1, 2, 3, 4, 5}
```
Or using the method:
```python
result = set1.union(set2)
```

#### **2. Intersection (`&` or `intersection()`)**
Returns a new set containing elements that are common to both sets.
```python
result = set1 & set2
print(result)  # Output: {3}
```
Or using the method:
```python
result = set1.intersection(set2)
```

#### **3. Difference (`-` or `difference()`)**
Returns a new set containing elements that are in the first set but not in the second.
```python
result = set1 - set2
print(result)  # Output: {1, 2}
```
Or using the method:
```python
result = set1.difference(set2)
```

#### **4. Symmetric Difference (`^` or `symmetric_difference()`)**
Returns a new set containing elements that are in either set but not in both.
```python
result = set1 ^ set2
print(result)  # Output: {1, 2, 4, 5}
```
Or using the method:
```python
result = set1.symmetric_difference(set2)
```

---

### Set Methods
Sets provide various built-in methods for modifying and querying elements.

#### **1. `add()`**
Adds an element to the set.
```python
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}
```

#### **2. `remove()`**
Removes a specific element from the set. Raises a `KeyError` if the element is not found.
```python
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5}
```

#### **3. `discard()`**
Removes a specific element from the set. Does not raise an error if the element is not found.
```python
my_set.discard(10)  # No error raised
```

#### **4. `pop()`**
Removes and returns an arbitrary element from the set.
```python
element = my_set.pop()
print(element)
print(my_set)
```

#### **5. `clear()`**
Removes all elements from the set.
```python
my_set.clear()
print(my_set)  # Output: set()
```

#### **6. `copy()`**
Creates a shallow copy of the set.
```python
set_copy = my_set.copy()
print(set_copy)
```

#### **7. `issubset()`**
Checks if the set is a subset of another set.
```python
print({1, 2}.issubset({1, 2, 3}))  # Output: True
```

#### **8. `issuperset()`**
Checks if the set is a superset of another set.
```python
print({1, 2, 3}.issuperset({1, 2}))  # Output: True
```

#### **9. `isdisjoint()`**
Checks if two sets have no elements in common.
```python
print({1, 2}.isdisjoint({3, 4}))  # Output: True
```

---

### Frozenset Methods
Frozensets share most of the methods with sets but do not have methods that modify the set (e.g., `add()`, `remove()`).

---

### Iterating Over a Set
You can iterate over a set using a `for` loop.

#### Example:
```python
for item in my_set:
    print(item)
```

---

### Set Comprehensions
Set comprehensions provide a concise way to create sets.

#### Example:
```python
squared_set = {x**2 for x in range(5)}
print(squared_set)  # Output: {0, 1, 4, 9, 16}
```

---

## 🔹 **6. Next Steps**
Mastering data structures enhances your ability to design and implement robust OOP solutions. Understanding how Python manages memory helps prevent performance bottlenecks and unintended behavior.

Continue to the next section: **[Mutable and Immutable Objects](03_mutable-and-immutable-objects.md)**.
