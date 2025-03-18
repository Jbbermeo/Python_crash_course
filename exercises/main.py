"""
# 🏆 Python Assessment - Script

## 📌 Objective
This script will evaluate Python knowledge through a multiple-choice quiz. The questions cover:
- Core Python concepts (data types, functions, exception handling, file handling, etc.).
- Object-Oriented Programming (OOP) concepts (classes, inheritance, encapsulation, etc.).

---

## 📝 How to Use this Script
1. Run the script to start the quiz.
2. Answer each question by selecting the correct option.
3. At the end, you will see your final score.

Let's begin!
"""

import json
from IPython.display import display
import ipywidgets as widgets

# Define quiz questions
questions = [
    # Data Types in Python
    {"question": "Which of the following is NOT a valid Python data type?",
     "options": ["int", "str", "char", "float"],
     "answer": "char"},
    {"question": "What is the result of `type(5.0)`?",
     "options": ["int", "float", "double", "str"],
     "answer": "float"},
     {"question": "Which data type is used to store a collection of key-value pairs?",
     "options": ["List", "Tuple", "Dictionary", "Set"],
     "answer": "Dictionary"},
    {"question": "What will `bool(0)` return?",
     "options": ["True", "False", "None", "Error"],
     "answer": "False"},

    # Data Structures
    {"question": "Which of the following data structures is immutable?",
     "options": ["List", "Dictionary", "Set", "Tuple"],
     "answer": "Tuple"},
    {"question": "Which method is used to add an item to a set?",
     "options": ["append()", "add()", "insert()", "extend()"],
     "answer": "add()"},
     {"question": "Which data structure maintains order and allows duplicate values?",
     "options": ["Set", "List", "Dictionary", "Tuple"],
     "answer": "List"},
    {"question": "Which method is used to remove an item from a dictionary?",
     "options": ["remove()", "del", "pop()", "discard()"],
     "answer": "pop()"},

    # Mutable and Immutable Objects
    {"question": "Which of the following is mutable in Python?",
     "options": ["Tuple", "String", "List", "Integer"],
     "answer": "List"},
    {"question": "Which of the following statements about immutability is correct?",
     "options": ["Strings are immutable", "Lists are immutable", "Sets are immutable", "Dictionaries are immutable"],
     "answer": "Strings are immutable"},
     {"question": "Which of these is NOT an immutable object in Python?",
     "options": ["Integer", "String", "Tuple", "Set"],
     "answer": "Set"},
    {"question": "What happens when you try to modify a tuple?",
     "options": ["It raises a TypeError", "It modifies the tuple", "It creates a new tuple", "It deletes the tuple"],
     "answer": "It raises a TypeError"},

    # Hashable Objects in Python
    {"question": "Which of the following is a hashable data type?",
     "options": ["List", "Dictionary", "Tuple", "Set"],
     "answer": "Tuple"},
    {"question": "Why must dictionary keys be hashable?",
     "options": ["To ensure order", "To allow fast lookups", "To prevent duplicates", "To use more memory"],
     "answer": "To allow fast lookups"},
     {"question": "Which of the following is a hashable data type?",
     "options": ["List", "Dictionary", "Tuple", "Set"],
     "answer": "Tuple"},

    # Functions and Variable Scope
    {"question": "What is the default return value of a function that does not explicitly return anything?",
     "options": ["None", "0", "False", "Empty string"],
     "answer": "None"},
    {"question": "What keyword is used to define a function in Python?",
     "options": ["function", "def", "func", "define"],
     "answer": "def"},

    # *args and **kwargs
    {"question": "What does *args allow you to do in a function?",
     "options": ["Pass multiple keyword arguments", "Pass multiple positional arguments", "Return multiple values", "Modify arguments"],
     "answer": "Pass multiple positional arguments"},
    {"question": "How do you access keyword arguments inside a function using **kwargs?",
     "options": ["As a list", "As a tuple", "As a dictionary", "As a set"],
     "answer": "As a dictionary"},

    # Keywords
    {"question": "Which of the following is a Python keyword?",
     "options": ["class", "object", "main", "define"],
     "answer": "class"},
    {"question": "What is the purpose of the `yield` keyword?",
     "options": ["To return multiple values", "To define a lambda function", "To create a generator", "To declare an exception"],
     "answer": "To create a generator"},

    # Exception Handling
    {"question": "Which keyword is used to catch exceptions in Python?",
     "options": ["catch", "except", "error", "try"],
     "answer": "except"},
    {"question": "What type of error does `ZeroDivisionError` represent?",
     "options": ["Syntax Error", "Runtime Error", "Logical Error", "Attribute Error"],
     "answer": "Runtime Error"},

    # Iterators and Generators
    {"question": "What function is used to get the next value from an iterator?",
     "options": ["next()", "iter()", "advance()", "move()"],
     "answer": "next()"},
    {"question": "What does a generator function return?",
     "options": ["A list", "An iterator", "A set", "A dictionary"],
     "answer": "An iterator"},

    # List Comprehensions and Lambda Functions
    {"question": "What does the following list comprehension do? `[x*2 for x in range(3)]`",
     "options": ["[0, 2, 4]", "[2, 4, 6]", "[1, 2, 3]", "[0, 1, 2]"],
     "answer": "[0, 2, 4]"},
    {"question": "Which of the following is a valid lambda function?",
     "options": ["lambda x: x**2", "lambda (x): return x**2", "lambda x => x**2", "def lambda(x): x**2"],
     "answer": "lambda x: x**2"},

     # What is Object-Oriented Programming?
    {"question": "What is the main goal of Object-Oriented Programming?",
     "options": ["To make programming more complex", "To improve code readability and reusability", "To avoid using functions", "To write only procedural code"],
     "answer": "To improve code readability and reusability"},
    {"question": "Which of the following is NOT a principle of OOP?",
     "options": ["Encapsulation", "Polymorphism", "Abstraction", "Iteration"],
     "answer": "Iteration"},
    {"question": "Which statement best defines Object-Oriented Programming?",
     "options": ["A way to structure code into functions", "A paradigm that models real-world entities as objects", "A method to create only immutable variables", "A programming technique for handling databases"],
     "answer": "A paradigm that models real-world entities as objects"},

    # OOP - Classes and Objects
    {"question": "Which keyword is used to define a class in Python?",
     "options": ["define", "class", "object", "type"],
     "answer": "class"},
    {"question": "Which method is called when an object is created?",
     "options": ["__init__", "__new__", "__start__", "__create__"],
     "answer": "__init__"},
     {"question": "What is an instance of a class called?",
     "options": ["A function", "A method", "An object", "A module"],
     "answer": "An object"},

     # Attributes and Methods
    {"question": "Which of the following best describes an attribute in Python classes?",
     "options": ["A function inside a class", "A variable belonging to an object", "A global variable", "A method that runs automatically"],
     "answer": "A variable belonging to an object"},
    {"question": "What is a method in Python classes?",
     "options": ["A function inside a class", "A class inside a function", "A variable in a function", "An independent function"],
     "answer": "A function inside a class"},
    {"question": "What is the difference between an instance attribute and a class attribute?",
     "options": ["Instance attributes belong to one object; class attributes are shared across all instances", "There is no difference", "Class attributes are immutable", "Instance attributes are defined outside __init__"],
     "answer": "Instance attributes belong to one object; class attributes are shared across all instances"},

     # Encapsulation
    {"question": "What is encapsulation in OOP?",
     "options": ["A way to restrict direct access to some components of an object", "A method to execute multiple objects at once", "A technique to iterate through objects", "A way to define multiple classes in one file"],
     "answer": "A way to restrict direct access to some components of an object"},
    {"question": "Which symbol is used to define a private attribute in Python?",
     "options": ["_", "__", "#", "$"],
     "answer": "__"},
    {"question": "What is the main benefit of encapsulation?",
     "options": ["It makes code shorter", "It hides implementation details and protects data", "It speeds up execution", "It avoids using constructors"],
     "answer": "It hides implementation details and protects data"},

    # Special Methods (Dunder Methods)
    {"question": "Which of the following is a dunder (double underscore) method in Python?",
     "options": ["__main__", "__add__", "__method__", "__import__"],
     "answer": "__add__"},
    {"question": "What does the __str__ method do?",
     "options": ["Defines string representation of an object", "Creates a new object", "Deletes an object", "Handles addition operations"],
     "answer": "Defines string representation of an object"},
    {"question": "Which dunder method is used for defining behavior of the `+` operator?",
     "options": ["__add__", "__plus__", "__sum__", "__concat__"],
     "answer": "__add__"},
     

    # OOP - Inheritance
    {"question": "What is inheritance in Python?",
     "options": ["A way to copy objects", "A way to define a new class from an existing class", "A way to create private attributes", "A way to override methods"],
     "answer": "A way to define a new class from an existing class"},
    {"question": "Which keyword is used to inherit from a parent class?",
     "options": ["inherit", "super", "extends", "parent"],
     "answer": "super"},
     {"question": "What is multiple inheritance?",
     "options": ["A class inheriting from multiple classes", "A class that can only be inherited once", "A class with multiple methods", "A method that returns multiple values"],
     "answer": "A class inheriting from multiple classes"},

     # Polymorphism
    {"question": "What does polymorphism allow in OOP?",
     "options": ["Using multiple objects as one", "Defining multiple constructors", "Hiding attributes", "Creating only one object"],
     "answer": "Using multiple objects as one"},
    {"question": "Which of the following demonstrates polymorphism?",
     "options": ["A method overridden in a subclass", "A private method", "A function inside a class", "A constructor function"],
     "answer": "A method overridden in a subclass"},
    {"question": "What is method overriding?",
     "options": ["Redefining a method in a subclass", "Creating a private method", "Defining multiple methods in a class", "Calling multiple methods at once"],
     "answer": "Redefining a method in a subclass"},

     # Abstraction
    {"question": "What is abstraction in OOP?",
     "options": ["Hiding implementation details and exposing only necessary features", "A way to define a new class from an existing class", "A method to execute multiple objects at once", "A technique to create immutable objects"],
     "answer": "Hiding implementation details and exposing only necessary features"},
    {"question": "Which of the following is used to achieve abstraction in Python?",
     "options": ["Abstract classes and interfaces", "Private attributes", "Method overloading", "Multiple inheritance"],
     "answer": "Abstract classes and interfaces"},
    {"question": "Which module provides support for abstract classes in Python?",
     "options": ["abc", "oop", "abstract", "meta"],
     "answer": "abc"},

     # Composition and Aggregation
    {"question": "What is composition in OOP?",
     "options": ["A class containing an instance of another class", "A class inheriting from another class", "A method that returns multiple values", "A way to execute multiple functions in a class"],
     "answer": "A class containing an instance of another class"},
    {"question": "How does aggregation differ from composition?",
     "options": ["In aggregation, objects can exist independently; in composition, they cannot", "They are the same", "Aggregation is more complex than composition", "Composition allows objects to exist independently"],
     "answer": "In aggregation, objects can exist independently; in composition, they cannot"},
    {"question": "Which of the following best demonstrates composition?",
     "options": ["A Car class that contains an Engine object", "A class inheriting from another class", "A method overriding another method", "Using an abstract class"],
     "answer": "A Car class that contains an Engine object"},

     # Operator Overloading
    {"question": "What is operator overloading?",
     "options": ["Defining custom behavior for operators like + and -", "Creating multiple constructors", "Overriding a method in a subclass", "Using multiple loops in a function"],
     "answer": "Defining custom behavior for operators like + and -"},
    {"question": "Which dunder method is used to overload the addition (+) operator?",
     "options": ["__add__", "__sum__", "__concat__", "__plus__"],
     "answer": "__add__"},
    {"question": "Which of the following is a correct example of operator overloading?",
     "options": ["Defining __add__ in a class", "Using multiple loops in a function", "Using polymorphism", "Defining multiple constructors"],
     "answer": "Defining __add__ in a class"},

     # Metaclasses in Python
    {"question": "What is a metaclass in Python?",
     "options": ["A class that defines how other classes behave", "A class used only for inheritance", "A built-in class for data storage", "A function that modifies objects"],
     "answer": "A class that defines how other classes behave"},
    {"question": "Which of the following is the default metaclass in Python?",
     "options": ["type", "object", "meta", "base"],
     "answer": "type"},
    {"question": "How do you define a custom metaclass in Python?",
     "options": ["By inheriting from type", "By using class keyword", "By defining a lambda function", "By creating a function with decorators"],
     "answer": "By inheriting from type"}
]


# Function to display quiz
def run_quiz():
    score = 0
    
    for q in questions:
        print(q["question"])
        radio = widgets.RadioButtons(options=q["options"], description='Answer:', style={'description_width': 'initial'})
        button = widgets.Button(description="Submit")
        output = widgets.Output()
        
        def check_answer(b, q=q, radio=radio, output=output):
            with output:
                output.clear_output()
                if radio.value == q["answer"]:
                    print("✅ Correct!")
                    nonlocal score
                    score += 1
                else:
                    print(f"❌ Incorrect. The correct answer is: {q['answer']}")
        
        button.on_click(check_answer)
        display(radio, button, output)
    
    print(f"Your final score: {score}/{len(questions)}")
