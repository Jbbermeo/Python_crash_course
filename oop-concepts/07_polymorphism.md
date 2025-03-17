# 🔹Polymorphism in Python 
Polymorphism might sound complex, but at its core, it simply means **"one name, multiple behaviors."**

Think of a word like "run"—you can run a marathon, a business, or a program. The action depends on the context. This is exactly what polymorphism does in Python!

Let's take an example:
```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
```
**Output:**
```
Woof!
Meow!
```
Here, both `Dog` and `Cat` have a `speak()` method, but each behaves differently. The key idea? **Same method name, different behaviors!**

---

## 🔹Why is Polymorphism Useful?
- **Less Code, More Power:** One method can handle multiple types.
- **Flexibility:** New types can be added without changing existing code.
- **Readability:** Code becomes more natural and easier to follow.

Now, let's explore the different types of polymorphism in Python.

---

## 🔹1. Method Overloading (Fake it till you make it!)
Some languages allow multiple methods with the same name but different parameters. Python doesn't support this directly, but we can mimic it using default arguments or `*args`. This Method overloading allows a function to have different implementations based on the number or type of parameters passed. While Python doesn't support true method overloading like Java or C++, it can be simulated using default arguments or `*args`.


### Example:
```python
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))    # Output: 5
print(calc.add(2, 3, 4)) # Output: 9
```
Here, we use a default value for `c` to allow flexibility.

**Why use this?**
- When you want a function to handle different numbers of inputs gracefully.

---

## 🔹2. Method Overriding (Customizing Behavior)
Sometimes, a child class needs to **modify** a method from its parent class. This is called **method overriding** and occurs when a subclass provides a specific implementation for a method that is already defined in its parent class. This allows customization of inherited behavior without modifying the parent class.


### Example:
```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())
```
**Output:**
```
Woof!
Meow!
Some sound
```
The `Dog` and `Cat` classes **override** the `speak()` method, customizing it to their own behavior.

**Why use this?**
- When you need different behavior for subclasses while keeping a common interface.

---

## 🔹3. Operator Overloading (Making Custom Objects Behave Naturally)
Ever wondered why `2 + 3` works, but adding two custom objects doesn’t? Python allows us to **redefine** how operators (`+`, `-`, `*`, etc.) work on objects, in other words, this operator allows objects of user-defined classes to interact with built-in operators such as `+`, `-`, `*`, etc. By defining special methods (dunder methods), objects can behave intuitively in arithmetic operations.


### Example:
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # Output: Vector(6, 8)
```
Here, we **overloaded** the `+` operator to add vectors naturally.

**Why use this?**
- To make user-defined objects behave like built-in types (numbers, strings, etc.).

---

## 🔹4. Duck Typing (If it walks like a duck...)
Python doesn’t care about **what** an object is, only **what it can do**. Duck typing is a dynamic feature in Python where an object's compatibility is determined by its methods and properties, rather than its class. If an object implements the required behavior, it is considered valid.


### Example:
```python
class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

class Fish:
    def swim(self):
        print("Fish is swimming")

# Function using Duck Typing
def make_it_fly(entity):
    entity.fly()

bird = Bird()
plane = Airplane()
fish = Fish()

make_it_fly(bird)   # Output: Bird is flying
make_it_fly(plane)  # Output: Airplane is flying
# make_it_fly(fish)  # Would cause an error
```
The function doesn’t check **what** the object is—just whether it has a `fly()` method. 

**Why use this?**
- Encourages a flexible, loosely coupled design.
- Eliminates the need for strict class hierarchies.

---

## 🔹Summary (Wrapping It Up)
| Type | Description | Example |
|------|------------|---------|
| **Method Overloading** | Same method, different parameters | `add(a, b, c=0)` |
| **Method Overriding** | Subclass modifies inherited method | `Dog.speak()` vs. `Animal.speak()` |
| **Operator Overloading** | Custom behavior for `+`, `-`, etc. | `Vector(2,3) + Vector(4,5)` |
| **Duck Typing** | Behavior over type checking | Any object with `fly()` can fly |

Polymorphism makes Python code **elegant, flexible, and powerful**. Understanding these techniques will help you write **cleaner, smarter** code. 🚀

Continue to the next section: **[Abstraction](08_abstraction.md)**.