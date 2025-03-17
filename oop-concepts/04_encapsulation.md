# 🔹Encapsulation in Python

Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP). It refers to the practice of restricting direct access to some of an object's components, which helps prevent unintended interference and misuse. In Python, encapsulation is implemented using access modifiers.

## 🔹Access Modifiers in Python
Python provides three levels of encapsulation:

1. **Public Members**: Accessible from anywhere.
2. **Protected Members**: Indicated with a single underscore `_`, intended to be used within the class and its subclasses.
3. **Private Members**: Indicated with a double underscore `__`, meant to be used only within the class.

### Is Encapsulation a Convention in Python?
Unlike some other programming languages that enforce strict access control, Python follows a convention-based approach. This means that private and protected attributes are not truly restricted but are instead marked as such by convention. Developers are expected to respect these conventions rather than being technically prevented from accessing them.

## 🔹Public Members
Public attributes and methods can be accessed from anywhere, both inside and outside of the class.

### Example:
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute

    def display(self):
        print(f"Car: {self.brand} {self.model}")

# Usage
car = Car("Toyota", "Corolla")
print(car.brand)  # Accessible
print(car.model)  # Accessible
car.display()
```

## 🔹Protected Members
Protected members are indicated by a single underscore `_`. This is a convention to indicate that these attributes should not be accessed directly but can still be accessed if needed. Subclasses can still access these attributes.

### Example:
```python
class Car:
    def __init__(self, brand, model):
        self._brand = brand  # Protected attribute
        self._model = model  # Protected attribute

    def _display(self):
        print(f"Car: {self._brand} {self._model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def show_details(self):
        print(f"Electric Car: {self._brand} {self._model} with {self.battery} battery")

# Usage
e_car = ElectricCar("Tesla", "Model S", "100 kWh")
e_car.show_details()  # Protected members accessible in subclass
print(e_car._brand)  # Accessible but discouraged
```

## 🔹Private Members
Private members are indicated by a double underscore `__`. Python performs name mangling, which modifies the variable name to prevent accidental access. However, they can still be accessed in a non-recommended way.

### Example:
```python
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  # Private attribute

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

# Usage
car = Car("BMW", "X5", 50000)
print(car.get_price())  # Allowed
car.set_price(55000)  # Allowed
print(car.get_price())

# Attempting direct access
# print(car.__price)  # Error: AttributeError
```

### What Happens If We Try to Access a Private Attribute Directly?
Python applies **name mangling** to private attributes, which means they are stored internally with a modified name. For example, `__price` becomes `_Car__price`.

However, we can still access them using this mangled name:
```python
print(car._Car__price)  # Works, but should be avoided
```
Even though this is possible, it is not recommended as it goes against the principles of encapsulation.

### What Happens If We Try to Overwrite an Encapsulated Attribute?
If an attribute is protected (`_attribute`) or private (`__attribute`), we can still overwrite it, but it is not recommended. 

Example:
```python
car.__price = 10000  # This does NOT modify the original __price attribute!
print(car.get_price())  # Still prints the original value
```
Instead, a new attribute `__price` is created at the instance level, and the original private attribute remains unchanged.

## 🔹Summary
- **Data Hiding**: Prevents direct modification of important attributes.
- **Improved Code Maintainability**: Reduces complexity and makes debugging easier.
- **Controlled Access**: Provides getter and setter methods for validation.
- **Prevents Accidental Modification**: Encapsulation ensures that attributes are modified only in a controlled manner.

Encapsulation in Python helps in writing clean and maintainable code by ensuring that internal object details are not exposed unnecessarily. Proper use of access modifiers allows developers to build robust applications while following OOP principles.

Continue to the next section: **[Special Methods](05_special-methods.md)**.

