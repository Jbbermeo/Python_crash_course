# File Handling in Python

File handling in Python allows you to read, write, and manipulate files on your system. It is essential for tasks like data storage, logging, and file-based input/output operations. In Object-Oriented Programming (OOP), file handling helps manage persistent data efficiently.

---

## 🔹 **1. Opening and Closing Files**

Python provides the `open()` function to work with files. You must specify the file name and the mode in which you want to open it.

### **File Modes:**
- `'r'`: Read (default mode, raises an error if the file does not exist).
- `'w'`: Write (creates a new file or overwrites an existing one).
- `'a'`: Append (adds data to the end of the file without overwriting).
- `'b'`: Binary mode (used for non-text files like images).

### **Example:**
```python
file = open('example.txt', 'w')
file.write('Hello, world!')
file.close()
```

### **Using `with` Statement:**
The `with` statement ensures that the file is properly closed after its operations are complete.
```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

---

## 🔹 **2. Reading Files**

You can read the contents of a file using various methods:

### **Methods:**
- `read()`: Reads the entire file.
- `readline()`: Reads one line at a time.
- `readlines()`: Reads all lines and returns them as a list.

### **Example:**
```python
with open('example.txt', 'r') as file:
    print(file.read())
```

Reading line-by-line:
```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

---

## 🔹 **3. Writing to Files**

You can write data to a file using the `write()` or `writelines()` methods.

### **Example:**
```python
with open('output.txt', 'w') as file:
    file.write('This is a new line of text.')
```

Writing multiple lines:
```python
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('output.txt', 'w') as file:
    file.writelines(lines)
```

---

## 🔹 **4. Appending to Files**

Use the `'a'` mode to append data without overwriting the existing content.

### **Example:**
```python
with open('output.txt', 'a') as file:
    file.write('This line is appended.')
```

---

## 🔹 **5. Working with Binary Files**

For non-text files (e.g., images), use the `'b'` mode.

### **Example:**
```python
with open('image.jpg', 'rb') as file:
    data = file.read()

with open('copy.jpg', 'wb') as file:
    file.write(data)
```

---

## 🔹 **6. Handling Exceptions**

File operations can raise exceptions, such as `FileNotFoundError`. Use `try-except` blocks to handle errors gracefully.

### **Example:**
```python
try:
    with open('non_existent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('File not found.')
```

---

## 🔹 **7. File Handling in OOP**

In OOP, file handling can be encapsulated in methods within a class.

### **Example:**
```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return 'File not found.'

    def write_file(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)

manager = FileManager('data.txt')
manager.write_file('Hello OOP!')
print(manager.read_file())
```

---

## 🔹 **8. Best Practices**

1. **Use the `with` statement:**
   - Ensures that files are properly closed after operations.

2. **Handle exceptions:**
   - Anticipate and handle file-related errors (e.g., missing files).

3. **Avoid hardcoding paths:**
   - Use dynamic or configurable file paths.

4. **Use binary mode for non-text files:**
   - Prevents data corruption when reading or writing binary data.

5. **Manage large files efficiently:**
   - Read large files in chunks to avoid memory issues.

---

## 🔹 **9. Practice Challenges**

### **Challenge 1: Read and Write a File**
Write a program that reads a file and writes its content to another file.
```python
def copy_file(source, destination):
    with open(source, 'r') as src:
        content = src.read()
    with open(destination, 'w') as dest:
        dest.write(content)

copy_file('source.txt', 'destination.txt')
```

### **Challenge 2: Append Data to a File**
Write a function that appends a list of strings to a file.
```python
def append_lines(filename, lines):
    with open(filename, 'a') as file:
        file.writelines(lines)

append_lines('log.txt', ['Log entry 1\n', 'Log entry 2\n'])
```

---

## 🔹 **10. Summary**
File handling in Python enables you to manage data storage and retrieval efficiently. By mastering file operations such as reading, writing, and appending, you can build robust applications that interact with the filesystem. In OOP, encapsulating file operations in classes enhances code organization and reusability.

Continue to the next section: **[Context Managers](14_context-managers.md)**.
