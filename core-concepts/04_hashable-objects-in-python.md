# Hashable Objects in Python

Hashable objects are essential in Python for efficient data storage and retrieval, especially when using collections like dictionaries and sets. In Object-Oriented Programming (OOP), understanding hashability helps ensure data integrity and enables the use of custom objects in key-value structures.

---

## 🔹 **1. What Are Hashable Objects?**

An object is considered **hashable** if:
1. It has a fixed hash value throughout its lifetime (i.e., it does not change).
2. It can be compared to other objects using equality operations.

This is achieved by implementing the `__hash__()` and `__eq__()` methods. Python uses the hash value of an object to quickly look it up in dictionaries and sets.

### **Examples of hashable objects:**
- Immutable types like strings, integers, floats, and tuples (with hashable elements).

### **Examples of non-hashable objects:**
- Mutable types like lists, dictionaries, and sets.

---

## 🔹 **2. The `hash()` Function in Python**
Python provides a built-in `hash()` function that returns the hash value of an object. This function is useful for understanding how objects are managed in hash-based collections like dictionaries and sets.

### **Example:**
```python
x = (1, 2, 3)
print(hash(x))  # Output: A unique integer representing the hash value
```

### **Using `hash()` on Mutable Objects:**
If you try to use `hash()` on a mutable object like a list, Python will raise a `TypeError` because mutable objects do not have a consistent hash value.

Example:
```python
my_list = [1, 2, 3]
# This raises a TypeError: unhashable type: 'list'
print(hash(my_list))
```

This behavior ensures that hash-based collections maintain data integrity by preventing modifications to keys or elements.

---

## 🔹 **3. Why Are Hashable Objects Important?**
Hashable objects enable efficient data structures such as dictionaries and sets to perform fast lookups and store unique values.

### **Dictionaries:**
Dictionaries rely on hash values to quickly retrieve values associated with keys.
```python
user_cache = {
    'user_123': {'name': 'Alice', 'age': 30}
}
print(user_cache['user_123'])  # Fast lookup using the key's hash value
```

### **Sets:**
Sets use hash values to ensure that each element is unique.
```python
unique_items = {1, 2, 3}
unique_items.add(2)  # No duplicate added because 2 already exists
print(unique_items)  # Output: {1, 2, 3}
```

### **Hash Tables:**
Both dictionaries and sets internally use a hash table, where the hash value determines the location of the object in memory.

---

## 🔹 **4. Custom Hashable Objects**
You can define your own hashable objects by implementing the `__hash__()` and `__eq__()` methods in a class.

### **Example:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name and self.age == other.age

# Using Person objects in a set
person1 = Person('Alice', 30)
person2 = Person('Alice', 30)
people = {person1}
print(person2 in people)  # Output: True (because they have the same hash and are equal)
```

---

## 🔹 **5. Mutability and Hashability**

### **Why Can't Mutable Objects Be Hashable?**
If a mutable object changes, its hash value would also change, breaking the integrity of hash-based collections. For example, if a list were allowed as a dictionary key, modifying the list would make it impossible to retrieve the corresponding value.

Example of non-hashable object:
```python
my_list = [1, 2, 3]
# This raises a TypeError because lists are not hashable
my_dict = {my_list: 'value'}
```

### **Immutable Wrappers:**
To make mutable data usable as a key, you can wrap it in an immutable container, like a tuple.
```python
data_key = (1, 2, 3)  # Tuple is hashable
my_dict = {data_key: 'value'}
print(my_dict[data_key])  # Output: value
```

---

## 🔹 **6. Best Practices for Hashable Objects**

1. **Use immutable objects** as keys in dictionaries or elements in sets.
2. **Avoid modifying objects** that are used in hash-based collections.
3. **Implement custom hash and equality methods** for user-defined objects to ensure correct behavior in collections.
4. **Use the `hash()` function** to inspect how objects are hashed, especially when designing custom classes.

## 🔹 **7. Summary**
Hashable objects are fundamental to Python's data structures like dictionaries and sets. The `hash()` function allows you to inspect how Python calculates hash values. By understanding how hashability works, you can design more efficient and reliable OOP solutions. Custom objects can also be made hashable to fit seamlessly into these collections.

Continue to the next section: **[Functions and Variable Scope](05_functions-and-variable-scope.md)**.
