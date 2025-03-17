# 🔹Object Serialization in Python (pickle, json)

Object serialization is the process of **converting Python objects into a format** that can be stored, transmitted, or reconstructed later. Python provides two popular modules for serialization: **pickle** and **json**.

## 🔹Why Use Serialization?
- **Data Persistence**: Save objects to disk for later use.
- **Inter-Process Communication**: Exchange objects between different Python programs.
- **Data Transmission**: Send data over networks or APIs.
- **Caching Mechanisms**: Store precomputed results for faster access.

---

## 🔹1. Using `pickle` for Binary Serialization
The `pickle` module allows **storing Python objects in binary format**.

### 🔹Pickling (Serializing an Object)
```python
import pickle

data = {"name": "Alice", "age": 30, "city": "New York"}

# Serialize and save to file
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)
```
### Unpickling (Deserializing an Object)
```python
# Load the serialized object
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```
**Key Features of `pickle`:**
- Stores objects **as binary files**, making them **efficient but non-human-readable**.
- Supports **complex objects** (lists, dictionaries, custom classes).
- Only works in Python **(not cross-platform compatible)**.

---

## 🔹2. Using `json` for Human-Readable Serialization
The `json` module provides a **text-based format**, making it **widely compatible** across platforms and languages.

### 🔹Serializing to JSON (Encoding)
```python
import json

data = {"name": "Alice", "age": 30, "city": "New York"}

# Convert dictionary to JSON string
json_string = json.dumps(data, indent=4)
print(json_string)
```
### 🔹Saving JSON to a File
```python
# Save JSON to a file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
```
### 🔹Loading JSON (Decoding)
```python
# Load JSON from a file
with open("data.json", "r") as file:
    loaded_json = json.load(file)

print(loaded_json)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```
**Key Features of `json`:**
- **Human-readable**, text-based format.
- **Cross-platform compatible** (used in APIs, web apps, and databases).
- **Does not support custom Python objects directly**.

---

## 🔹3. Serializing Custom Objects
Since `json` does not support custom objects by default, we need a custom encoder.

### 🔹Custom Encoding with `json`
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {"name": self.name, "age": self.age}

p = Person("Alice", 30)
json_string = json.dumps(p.to_dict(), indent=4)
print(json_string)
```

Alternatively, we can use a **custom JSON encoder**:
```python
class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return obj.__dict__
        return super().default(obj)

json_string = json.dumps(p, cls=PersonEncoder, indent=4)
print(json_string)
```

### Custom Decoding with `json`
```python
def person_decoder(dct):
    return Person(dct['name'], dct['age'])

p_obj = json.loads(json_string, object_hook=person_decoder)
print(p_obj.name, p_obj.age)  # Output: Alice 30
```

---

## 🔹4. Choosing Between `pickle` and `json`
| Feature | `pickle` | `json` |
|---------|---------|--------|
| **Format** | Binary | Text (JSON) |
| **Human Readable?** | ❌ No | ✅ Yes |
| **Cross-Language Compatible?** | ❌ No | ✅ Yes |
| **Supports Custom Objects?** | ✅ Yes | ❌ No (requires custom encoding) |
| **Security Risks?** | ⚠️ High (can execute arbitrary code) | ✅ Safe |

### 🔹Summary:
- Use `pickle` **when working within Python** and **need to store complex objects** efficiently.
- Use `json` **for cross-platform compatibility**, APIs, and **human-readable data storage**.
- Avoid untrusted `pickle` files, as they can execute **arbitrary code** when deserialized.

Both serialization methods serve different purposes, and understanding their differences ensures you choose the right one for your needs.
Continue to the next section: **[Refactoring with OOP](06_refactoring-with-oop.md)**.