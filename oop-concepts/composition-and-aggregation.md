# Composition and Aggregation in Object-Oriented Programming

Composition and Aggregation are two key concepts in **Object-Oriented Programming (OOP)** that describe relationships between objects. Both allow objects to interact, but they define different levels of dependency between them.

## Why Are Composition and Aggregation Important?
- **Encapsulating Complexity**: Helps break down large systems into smaller, manageable parts.
- **Code Reusability**: Allows objects to be reused across multiple classes.
- **Better Maintainability**: Changes in one object have minimal impact on others.
- **Improved Modularity**: Helps create a well-structured and scalable system.

---

## 1. Composition (Strong Relationship)
Composition represents a **"has-a"** relationship where one object **owns** another object. If the **parent (container) object is destroyed, the child (contained) object is also destroyed**. This signifies a **strong dependency**.

### Key Characteristics:
- The **child object cannot exist independently** of the parent.
- The **parent object creates and manages** the child object.
- **Used when one object is fundamentally part of another.**

### Example:
A **Car** cannot function without an **Engine**. If the car is destroyed, so is its engine.

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print("Engine is starting...")

class Car:
    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine(horsepower)  # Composition

    def drive(self):
        self.engine.start()
        print(f"{self.model} is driving!")

car = Car("Tesla", 400)
car.drive()
```

### Explanation:
- The `Car` **owns** an `Engine` instance.
- If a `Car` object is deleted, the `Engine` instance is also lost.
- This is a **strong relationship** because the child (`Engine`) depends entirely on the parent (`Car`).

---

## 2. Aggregation (Weak Relationship)
Aggregation is a **"has-a"** relationship where one object **contains** another object but does **not own it**. If the **parent object is destroyed, the child object still exists**. This signifies a **weaker dependency**.

### Key Characteristics:
- The **child object can exist independently** of the parent.
- The **parent class stores a reference** to an existing child object.
- **Used when objects can exist separately but are related.**

### Example:
A **Team** has **Players**, but a Player can exist even if the Team is deleted.

```python
class Player:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Player: {self.name}")

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []  # Aggregation (list of Player objects)

    def add_player(self, player):
        self.players.append(player)

    def show_team(self):
        print(f"Team: {self.name}")
        for player in self.players:
            player.display()

# Creating independent Player objects
player1 = Player("Alice")
player2 = Player("Bob")

team = Team("Warriors")
team.add_player(player1)
team.add_player(player2)
team.show_team()
```

### Explanation:
- `Player` instances **exist independently** of `Team`.
- The `Team` class **holds references** to existing `Player` objects.
- If `Team` is deleted, `Player` objects still exist and can be reused.
- This is a **weak relationship** because `Player` is not fully dependent on `Team`.

---

## Key Differences Between Composition and Aggregation
| Feature | Composition | Aggregation |
|---------|------------|------------|
| **Dependency** | Strong | Weak |
| **Ownership** | Parent **owns** child | Parent **refers to** child |
| **Child existence** | Child **cannot** exist without parent | Child **can** exist independently |
| **Example** | Car and Engine | Team and Player |

---

## When to Use Composition vs. Aggregation
| Scenario | Use Composition | Use Aggregation |
|----------|----------------|----------------|
| If the child **cannot exist independently** | ✅ | ❌ |
| If the child **should be reusable elsewhere** | ❌ | ✅ |
| If the parent **should fully manage** the child | ✅ | ❌ |
| If the parent **just references** the child | ❌ | ✅ |

---

## Conclusion
- **Composition** creates a strong relationship where one object is **a core part** of another.
- **Aggregation** creates a weak relationship where objects **cooperate but remain independent**.
- Both approaches **promote modularity, reusability, and maintainability**.
- The right choice depends on whether the contained object **should or should not exist independently** of the parent.

Understanding **composition and aggregation** allows you to design **scalable, flexible, and efficient** object-oriented systems. 🚀
