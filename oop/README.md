# Object-Oriented Programming (OOP) — Python

This folder contains my complete **Object-Oriented Programming journey in Python**, progressing from basic classes and objects to inheritance, polymorphism, abstraction, special methods, object relationships, and a final Student Management System.

Each file focuses on one concept and contains a small practical example.

---

# 📚 File-by-File Learning

## 01 — Class & Object

**File:** `01_class_object.py`

### Concept

Introduction to classes and objects.

### What I learned

* A **class** is a blueprint.
* An **object** is an instance created from a class.
* Methods define the behavior of objects.

### Key idea

```text
Class → Blueprint
Object → Instance
```

---

## 02 — Attributes

**File:** `02_attributes.py`

### Concept

Object attributes.

### What I learned

* Attributes store information about an object.
* Attributes can be accessed using the dot `.` operator.
* Example: `student1.name`

### Key idea

```text
Object → Data/Attributes
```

---

## 03 — Constructor

**File:** `03_constructor.py`

### Concept

The `__init__()` constructor.

### What I learned

* `__init__()` runs automatically when an object is created.
* It is commonly used to initialize object attributes.

### Key idea

```python
student1 = Student("Subathra", 18)
```

The constructor receives the values and stores them in the object.

---

## 04 — Multiple Objects

**File:** `04_multiple_objects.py`

### Concept

Creating multiple objects from one class.

### What I learned

* One class can create many objects.
* Each object can contain different data.

### Key idea

```text
One Class
   ↓
Object 1
Object 2
Object 3
```

---

## 05 — Instance Methods

**File:** `05_instance_method.py`

### Concept

Methods that work with individual objects.

### What I learned

* Instance methods use `self`.
* `self` refers to the current object.

### Key idea

```python
student1.introduce()
```

---

## 06 — Changing Object Attributes

**File:** `06_change_attributes.py`

### Concept

Updating object data.

### What I learned

Object attributes can be changed after creating an object.

```python
student1.age = 19
```

---

## 07 — Multiple Attributes

**File:** `07_multiple_attributes.py`

### Concept

Using multiple attributes in one object.

### What I learned

A single object can store several related pieces of information such as:

```text
Name
Age
Department
```

---

## 08 — Method Parameters

**File:** `08_method_parameters.py`

### Concept

Passing arguments to methods.

### What I learned

Methods can accept additional parameters apart from `self`.

Example:

```python
student1.study("Python")
```

---

## 09 — Method Return Values

**File:** `09_method_return.py`

### Concept

Returning values from methods.

### What I learned

* `print()` displays a value.
* `return` sends a value back to the caller.

Example:

```python
result = student1.get_result()
```

---

## 10 — Multiple Method Parameters

**File:** `10_method_multiple_parameters.py`

### Concept

Methods with multiple arguments.

### What I learned

A method can accept several values and use them together.

Example:

```python
student1.show_marks("Python", 95)
```

---

## 11 — Modifying Object Attributes

**File:** `11_modify_attributes.py`

### Concept

Changing object data through a method.

### What I learned

A method can directly modify the object's attributes.

Example:

```python
self.age = self.age + 1
```

---

# 🏫 Class Variables

## 12 — Class Variable

**File:** `12_class_variable.py`

### Concept

Variables shared by objects.

### What I learned

A class variable belongs to the class and is shared by its objects.

Example:

```python
college = "VCEW"
```

---

## 13 — Class vs Instance Variables

**File:** `13_class_vs_instance.py`

### Concept

Difference between class and instance variables.

### What I learned

| Type              | Belongs to        |
| ----------------- | ----------------- |
| Class variable    | Class             |
| Instance variable | Individual object |

Example:

```text
college → shared
name    → individual
age     → individual
```

---

## 14 — Accessing Class Variables

**File:** `14_class_variable_access.py`

### Concept

Accessing class variables through objects and the class.

### What I learned

Both can be used:

```python
student1.college
Student.college
```

---

## 15 — Modifying Class Variables

**File:** `15_modify_class_variable.py`

### Concept

Changing shared class data.

### What I learned

```python
Student.college = "Vivekanandha College"
```

Changing the class variable changes the shared class-level value.

---

## 16 — Default Constructor Values

**File:** `16_default_values.py`

### Concept

Default arguments in constructors.

### What I learned

A constructor parameter can have a default value.

```python
def __init__(self, name, department="AI & ML"):
```

If the department is not supplied, the default is used.

---

# 🔐 Encapsulation

## 17 — Encapsulation Basics

**File:** `17_encapsulation.py`

### Concept

Protecting internal object data.

### What I learned

Double underscore creates a private-style attribute:

```python
self.__marks = marks
```

Python uses **name mangling** for double-underscore attributes.

---

## 18 — Getter Method

**File:** `18_getter_method.py`

### Concept

Reading encapsulated data.

### What I learned

A getter method provides controlled access to internal data.

```python
def get_marks(self):
    return self.__marks
```

---

## 19 — Setter Method

**File:** `19_setter_method.py`

### Concept

Changing encapsulated data.

### What I learned

A setter method allows an attribute to be modified through a controlled method.

```python
student1.set_marks(95)
```

---

## 20 — Setter with Validation

**File:** `20_setter_validation.py`

### Concept

Validating data before storing it.

### What I learned

A setter can prevent invalid values.

Example:

```python
if 0 <= marks <= 100:
```

This prevents marks such as `120`.

---

## 21 — Property Decorator

**File:** `21_property.py`

### Concept

Using `@property` and property setters.

### What I learned

Properties allow methods to behave like normal attributes.

```python
student1.marks
student1.marks = 95
```

This provides cleaner access while still allowing validation.

---

# 🧬 Inheritance

## 22 — Basic Inheritance

**File:** `22_inheritance.py`

### Concept

Inheritance between classes.

### What I learned

A child class can reuse functionality from a parent class.

```text
Person
   ↓
Student
```

---

## 23 — Inheritance with Constructor

**File:** `23_inheritance_constructor.py`

### Concept

Using a parent's constructor in a child class.

### What I learned

If the child doesn't define its own constructor, it can use the inherited parent constructor.

---

## 24 — `super()`

**File:** `24_super.py`

### Concept

Calling the parent constructor.

### What I learned

```python
super().__init__(name)
```

`super()` allows the child class to access functionality from its parent.

---

## 25 — Method Overriding

**File:** `25_method_overriding.py`

### Concept

Replacing a parent method in a child class.

### What I learned

A child class can define a method with the same name as the parent and provide different behavior.

---

## 26 — Calling Parent Method with `super()`

**File:** `26_super_method.py`

### Concept

Calling a parent method from a child class.

### What I learned

```python
super().introduce()
```

This allows the child to reuse the parent's method before adding its own behavior.

---

## 27 — Multiple Inheritance

**File:** `27_multiple_inheritance.py`

### Concept

A class inheriting from multiple parent classes.

### What I learned

```python
class Student(Father, Mother):
```

A class can inherit functionality from more than one parent.

---

## 28 — Multilevel Inheritance

**File:** `28_multilevel_inheritance.py`

### Concept

Inheritance in a chain.

### What I learned

```text
Person
  ↓
Student
  ↓
CollegeStudent
```

The final child can access inherited functionality through the chain.

---

## 29 — Hierarchical Inheritance

**File:** `29_hierarchical_inheritance.py`

### Concept

Multiple child classes sharing one parent.

### What I learned

```text
       Person
       /    \
 Student   Teacher
```

---

## 30 — Hybrid Inheritance

**File:** `30_hybrid_inheritance.py`

### Concept

Combination of multiple inheritance structures.

### What I learned

Python allows inheritance structures that combine different inheritance patterns.

---

# 🔄 Polymorphism

## 31 — Polymorphism

**File:** `31_polymorphism.py`

### Concept

Same method name, different behavior.

### What I learned

Different classes can implement the same method differently.

```text
Student.introduce()
Teacher.introduce()
```

---

## 32 — Polymorphism with Loop

**File:** `32_polymorphism_loop.py`

### Concept

Using polymorphism inside a loop.

### What I learned

Objects of different classes can be processed through a common interface.

```python
for person in people:
    person.introduce()
```

---

## 33 — Duck Typing

**File:** `33_duck_typing.py`

### Concept

Python's duck typing approach.

### What I learned

Python focuses on what an object **can do**, rather than strictly checking what type it is.

### Memory trick

> "If it behaves like the required object, use it."

---

# 🎯 Abstraction

## 34 — Abstract Class

**File:** `34_abstract_class.py`

### Concept

Abstract classes and abstract methods.

### What I learned

Abstract classes define methods that child classes are expected to implement.

Python provides this through:

```python
from abc import ABC, abstractmethod
```

---

## 35 — Multiple Abstract Methods

**File:** `35_multiple_abstract_methods.py`

### Concept

Abstract classes with more than one required method.

### What I learned

A concrete child class must implement all required abstract methods before it can be instantiated.

---

## 36 — Abstract Class with Constructor

**File:** `36_abstract_constructor.py`

### Concept

Combining abstraction with constructors.

### What I learned

An abstract class can still have:

* Constructor
* Normal methods
* Abstract methods
* Attributes

---

# ⚙️ Method Types

## 37 — Class Method

**Concept:** Class-level methods.

### What I learned

A class method uses `cls` and works with class-level data.

> **Note:** This topic was accidentally skipped in the original file numbering and was later included in the method-types discussion.

Typical syntax:

```python
@classmethod
def show_college(cls):
    print(cls.college)
```

---

## 38 — Static Method

**File:** `38_static_method.py`

### Concept

Static methods.

### What I learned

A static method does not require either `self` or `cls`.

```python
@staticmethod
def college_info():
    ...
```

It is useful for utility functionality related to a class.

---

## 39 — Instance vs Class vs Static Method

**File:** `39_method_types.py`

### Concept

Comparing the three major method types.

### What I learned

| Method   | First parameter | Works mainly with   |
| -------- | --------------- | ------------------- |
| Instance | `self`          | Object data         |
| Class    | `cls`           | Class data          |
| Static   | None            | Independent utility |

### Memory trick

```text
self → object
cls  → class
none → utility
```

---

# 🪄 Special / Dunder Methods

## 40 — `__str__()`

**File:** `40_str_method.py`

### Concept

Custom string representation.

### What I learned

`__str__()` controls what is displayed when an object is printed.

```python
print(student1)
```

---

## 41 — `__repr__()`

**File:** `41_repr_method.py`

### Concept

Developer-friendly object representation.

### What I learned

`__repr__()` provides a useful representation of an object, especially for debugging.

---

## 42 — `__len__()`

**File:** `42_len_method.py`

### Concept

Customizing the `len()` function.

### What I learned

```python
len(student1)
```

internally uses:

```python
student1.__len__()
```

---

## 43 — `__eq__()`

**File:** `43_eq_method.py`

### Concept

Custom equality comparison.

### What I learned

`__eq__()` controls how objects behave with:

```python
student1 == student2
```

---

## 44 — `__add__()`

**File:** `44_add_method.py`

### Concept

Operator overloading.

### What I learned

`__add__()` allows objects to define their own behavior for:

```python
student1 + student2
```

---

## 45 — Comparison Operator

**File:** `45_comparison_operator.py`

### Concept

Custom comparison using special methods.

### What I learned

For example:

```python
__gt__()
```

controls the `>` operator.

Other comparison dunder methods include:

```text
__eq__ → ==
__gt__ → >
__lt__ → <
__ge__ → >=
__le__ → <=
__ne__ → !=
```

---

# 🔗 Object Relationships

## 46 — Composition

**File:** `46_composition.py`

### Concept

Strong HAS-A relationship.

### What I learned

```text
Car
 └── Engine
```

The `Car` creates and contains its `Engine`.

### Memory trick

> Composition = strong ownership.

---

## 47 — Aggregation

**File:** `47_aggregation.py`

### Concept

Weak HAS-A relationship.

### What I learned

```text
College
 └── Teacher
```

The `Teacher` can exist independently of the `College`.

### Memory trick

> Aggregation = independent objects connected together.

---

# 🚀 Mini Project

## 48 — Student Management: Class Design

**File:** `48_student_management.py`

### Concept

Applying basic OOP concepts to a small project.

### What I learned

Designed a `Student` class containing:

```text
Name
Age
Department
```

and an `introduce()` method.

This combines:

* Class
* Object
* Constructor
* Attributes
* Instance method

---

## 49 — Student Management: Marks & Result

**File:** `49_student_management.py`

### Concept

Adding functionality to the Student Management System.

### What I learned

Added:

```text
Marks
Result
```

and implemented a method to determine whether the student has passed.

This combines:

* Constructor
* Attributes
* Methods
* Return values
* Conditional logic

---

## 50 — Final Student Management System

**File:** `50_student_management_final.py`

### Concept

Final OOP mini project combining the major concepts.

### What I learned

The final class contains:

```text
Student
│
├── Class Variable
│   └── college
│
├── Instance Attributes
│   ├── name
│   ├── age
│   └── department
│
├── Encapsulated Attribute
│   └── __marks
│
├── Methods
│   ├── introduce()
│   ├── get_marks()
│   ├── set_marks()
│   └── get_result()
│
└── Validation
    └── Marks must be 0–100
```

### Concepts combined

* Class and Object
* Constructor
* Instance attributes
* Class variables
* Instance methods
* Encapsulation
* Getter
* Setter
* Validation
* Conditional logic
* Return values

---

# 🧠 OOP Master Revision

```text
01–11 → Classes, Objects & Methods
12–16 → Class Variables
17–21 → Encapsulation
22–30 → Inheritance
31–33 → Polymorphism
34–36 → Abstraction
38–39 → Method Types
40–45 → Special Methods
46–47 → Object Relationships
48–50 → Mini Project
```

## The Big Picture

```text
CLASS
  ↓
OBJECT
  ↓
ATTRIBUTES + METHODS
  ↓
ENCAPSULATION
  ↓
INHERITANCE
  ↓
POLYMORPHISM
  ↓
ABSTRACTION
  ↓
SPECIAL METHODS
  ↓
COMPOSITION / AGGREGATION
  ↓
REAL PROJECT
```

---

# 📌 Important OOP Memory Points

| Concept           | Remember                           |
| ----------------- | ---------------------------------- |
| Class             | Blueprint                          |
| Object            | Instance                           |
| Attribute         | Data                               |
| Method            | Behavior                           |
| `self`            | Current object                     |
| `cls`             | Current class                      |
| `__init__()`      | Constructor                        |
| Class variable    | Shared data                        |
| Instance variable | Object-specific data               |
| Encapsulation     | Controlled data access             |
| Getter            | Read data                          |
| Setter            | Modify data                        |
| Inheritance       | Reuse                              |
| `super()`         | Parent functionality               |
| Overriding        | Replace parent behavior            |
| Polymorphism      | Same interface, different behavior |
| Duck typing       | Behavior matters                   |
| Abstraction       | Hide implementation details        |
| `@staticmethod`   | No `self`/`cls`                    |
| `__str__()`       | Human-readable object              |
| `__repr__()`      | Developer representation           |
| `__eq__()`        | Equality                           |
| `__add__()`       | `+`                                |
| Composition       | Strong HAS-A                       |
| Aggregation       | Weak HAS-A                         |

---

# ✅ Completion Status

**OOP-01 → OOP-50 completed.** 🎉

This section helped me move from writing individual Python statements and functions toward designing programs using **objects, reusable classes, relationships, and structured behavior**.

### Final Learning Pattern

> **Learn → Code → Run → Understand → Build → Document → Improve**
