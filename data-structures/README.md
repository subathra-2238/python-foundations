# Python Data Structures

This folder contains my Python programs for understanding the fundamental **data structures** provided by Python.

Data structures are ways of organizing and storing data so that it can be accessed, modified, and processed efficiently.

The concepts in this section build on the Python fundamentals and control flow learned earlier.

---

## 📚 Topics Covered

* Lists
* List methods
* Tuples
* Sets
* Dictionaries
* Mutable vs immutable data
* Ordered vs unordered collections
* Key-value pairs
* Iterating through collections
* Choosing the appropriate data structure

---

# 1. What Are Data Structures?

A data structure is a way of organizing data inside a program.

For example, if we want to store the names of several students, we could use a list:

```python
students = ["Subathra", "Thilaga", "Sivasri"]
```

Instead of creating separate variables:

```python
student1 = "Subathra"
student2 = "Thilaga"
student3 = "Sivasri"
```

A data structure allows related data to be stored together.

Python provides several built-in collection types, including:

* `list`
* `tuple`
* `set`
* `dict`

---

# 2. Lists

A **list** is an ordered and mutable collection of items.

### Syntax

```python
items = [item1, item2, item3]
```

### Example

```python
subjects = ["Python", "DSA", "Machine Learning"]

print(subjects)
```

Output:

```text
['Python', 'DSA', 'Machine Learning']
```

---

## List Characteristics

Lists:

* Are ordered
* Allow duplicate values
* Are mutable
* Can contain different data types
* Support indexing and slicing

### Example

```python
data = ["Python", 10, 9.5, True]
```

A list can contain different types of values.

---

# 3. Accessing List Elements

List elements are accessed using indexes.

```python
subjects = ["Python", "DSA", "Machine Learning"]

print(subjects[0])
print(subjects[1])
print(subjects[2])
```

Output:

```text
Python
DSA
Machine Learning
```

Python uses **zero-based indexing**.

That means:

```text
First element  → index 0
Second element → index 1
Third element  → index 2
```

---

## Negative Indexing

Python also supports negative indexes.

```python
subjects = ["Python", "DSA", "Machine Learning"]

print(subjects[-1])
```

Output:

```text
Machine Learning
```

Here:

```text
-1 → last element
-2 → second-last element
```

---

# 4. List Slicing

Slicing allows us to extract a portion of a list.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

The starting index is included, but the ending index is excluded.

---

# 5. Modifying Lists

Lists are mutable, meaning their contents can be changed.

```python
subjects = ["Python", "DSA", "Machine Learning"]

subjects[1] = "Cybersecurity"

print(subjects)
```

Output:

```text
['Python', 'Cybersecurity', 'Machine Learning']
```

---

# 6. List Methods

Python provides built-in methods for working with lists.

## `append()`

Adds an item to the end.

```python
subjects = ["Python", "DSA"]

subjects.append("Machine Learning")

print(subjects)
```

---

## `insert()`

Adds an item at a specific position.

```python
subjects = ["Python", "Machine Learning"]

subjects.insert(1, "DSA")

print(subjects)
```

---

## `remove()`

Removes a specific value.

```python
subjects = ["Python", "DSA", "Machine Learning"]

subjects.remove("DSA")
```

---

## `pop()`

Removes an item using its index.

```python
subjects = ["Python", "DSA", "Machine Learning"]

subjects.pop(1)
```

If no index is provided, `pop()` removes the last item.

```python
subjects.pop()
```

---

## `sort()`

Sorts a list.

```python
numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)
```

Output:

```text
[1, 2, 5, 8]
```

---

## `reverse()`

Reverses the order of the list.

```python
numbers = [1, 2, 3, 4]

numbers.reverse()

print(numbers)
```

---

## `len()`

Returns the number of elements.

```python
numbers = [10, 20, 30]

print(len(numbers))
```

Output:

```text
3
```

---

# 7. Tuples

A **tuple** is an ordered and immutable collection.

### Syntax

```python
items = (item1, item2, item3)
```

### Example

```python
coordinates = (10, 20)

print(coordinates)
```

---

## Tuple Characteristics

Tuples:

* Are ordered
* Allow duplicate values
* Are immutable
* Support indexing
* Support slicing
* Can contain different data types

### Example

```python
student = ("Subathra", 18, "AI & ML")
```

---

# 8. List vs Tuple

The main difference is **mutability**.

| List            | Tuple                             |
| --------------- | --------------------------------- |
| Mutable         | Immutable                         |
| Uses `[]`       | Uses `()`                         |
| Can be modified | Cannot be modified after creation |
| More flexible   | Useful for fixed data             |

### List

```python
subjects = ["Python", "DSA"]

subjects[0] = "Java"
```

This is valid.

### Tuple

```python
subjects = ("Python", "DSA")

# subjects[0] = "Java"
```

This causes an error because tuples cannot be modified.

---

# 9. Sets

A **set** is a collection of unique values.

### Syntax

```python
items = {item1, item2, item3}
```

### Example

```python
numbers = {1, 2, 3, 3, 4}

print(numbers)
```

The duplicate `3` is automatically removed.

Output will contain each value only once.

---

## Set Characteristics

Sets:

* Store unique values
* Do not support normal indexing
* Are mutable
* Are useful for membership testing
* Support mathematical set operations

### Example

```python
skills = {"Python", "AI", "IoT"}

print("Python" in skills)
```

Output:

```text
True
```

---

# 10. Set Operations

Sets support mathematical operations.

### Union

Combines values from both sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

### Intersection

Returns common values.

```python
print(a & b)
```

Output:

```text
{3}
```

### Difference

Returns values present in the first set but not the second.

```python
print(a - b)
```

Sets are particularly useful when duplicate values should be removed or when comparing groups of data.

---

# 11. Dictionaries

A **dictionary** stores data as **key-value pairs**.

### Syntax

```python
dictionary = {
    "key": "value"
}
```

### Example

```python
student = {
    "name": "Subathra",
    "age": 18,
    "department": "AI & ML"
}
```

Here:

```text
"name"       → key
"Subathra"   → value

"age"        → key
18           → value
```

---

# 12. Accessing Dictionary Values

Values can be accessed using their keys.

```python
student = {
    "name": "Subathra",
    "age": 18
}

print(student["name"])
print(student["age"])
```

Output:

```text
Subathra
18
```

---

# 13. Modifying Dictionaries

Dictionaries are mutable.

### Add a New Item

```python
student["year"] = 2
```

### Modify a Value

```python
student["age"] = 19
```

### Remove an Item

```python
student.pop("age")
```

---

# 14. Dictionary Methods

Useful dictionary methods include:

### `keys()`

Returns the keys.

```python
print(student.keys())
```

### `values()`

Returns the values.

```python
print(student.values())
```

### `items()`

Returns key-value pairs.

```python
print(student.items())
```

---

# 15. Iterating Through Data Structures

Loops can be used to process collection data.

### List

```python
subjects = ["Python", "DSA", "AI"]

for subject in subjects:
    print(subject)
```

### Dictionary

```python
student = {
    "name": "Subathra",
    "department": "AI & ML"
}

for key, value in student.items():
    print(key, ":", value)
```

This combination of **data structures + loops** is extremely important in Python programming.

---

# 🔍 Choosing the Right Data Structure

Different situations require different structures.

| Data Structure | Best Used When                               |
| -------------- | -------------------------------------------- |
| List           | You need an ordered, changeable collection   |
| Tuple          | You need ordered data that should not change |
| Set            | You need unique values                       |
| Dictionary     | You need key-value relationships             |

### Example

Store a sequence of subjects:

```python
subjects = ["Python", "DSA", "AI"]
```

Store fixed coordinates:

```python
coordinates = (10, 20)
```

Store unique skills:

```python
skills = {"Python", "AI", "Python"}
```

Store student information:

```python
student = {
    "name": "Subathra",
    "department": "AI & ML"
}
```

---

# 🧠 Mutable vs Immutable

One of the most important concepts in this section is **mutability**.

### Mutable

Can be changed after creation.

Examples:

```text
list
set
dictionary
```

### Immutable

Cannot be changed after creation.

Example:

```text
tuple
```

Understanding mutability becomes important later when learning functions, memory behavior, and object-oriented programming.

---

# ⚠️ Common Beginner Mistakes

## 1. Using the wrong index

```python
subjects = ["Python", "DSA"]

print(subjects[2])
```

This causes an `IndexError` because index `2` does not exist.

---

## 2. Trying to modify a tuple

```python
subjects = ("Python", "DSA")

# subjects[0] = "Java"
```

Tuples are immutable.

---

## 3. Expecting duplicates in a set

```python
numbers = {1, 2, 2, 3}
```

The duplicate value is removed automatically.

---

## 4. Accessing a dictionary using the wrong key

```python
student = {
    "name": "Subathra"
}

# print(student["age"])
```

This can produce a `KeyError`.

---

## 5. Confusing list methods

For example:

```python
numbers.append(10)
```

adds an item.

Whereas:

```python
numbers.remove(10)
```

removes a value.

Understanding what each method does is important.

---

# 🌍 Real-World Applications

Data structures are used throughout software development.

### Machine Learning

Datasets, feature values, labels, and configuration information are often represented using collections and data structures.

### Cybersecurity

Security systems can store:

* IP addresses
* User information
* Threat indicators
* Access permissions
* Event information

Sets are particularly useful when duplicate indicators need to be removed.

### IoT

Sensor readings can be collected and organized using lists or dictionaries.

```python
sensor_data = {
    "temperature": 28.5,
    "humidity": 65
}
```

### Web Development

Dictionaries are commonly used to represent structured information.

### Data Analysis

Collections are fundamental when loading, filtering, transforming, and organizing data.

---

# 🗂️ Programs in This Folder

| File                 | Concept                          |
| -------------------- | -------------------------------- |
| `01_lists.py`        | Creating and working with lists  |
| `02_list_methods.py` | Common list methods              |
| `03_tuples.py`       | Tuples and immutable collections |
| `04_sets.py`         | Sets and unique values           |
| `05_dictionaries.py` | Dictionaries and key-value pairs |

---

# 🎯 Learning Goal

The goal of this section is to understand how Python stores and organizes collections of data.

After completing this section, I should be comfortable with:

* Creating lists
* Accessing list elements
* Modifying lists
* Using common list methods
* Creating and using tuples
* Understanding immutability
* Creating sets
* Removing duplicate values
* Performing basic set operations
* Creating dictionaries
* Accessing and modifying dictionary values
* Iterating through collections
* Choosing an appropriate data structure

---

# 🧠 Key Takeaways

* Lists are ordered and mutable.
* Tuples are ordered and immutable.
* Sets store unique values.
* Dictionaries store key-value pairs.
* Lists and dictionaries are commonly used for structured application data.
* Sets are useful for uniqueness and membership testing.
* Tuples are useful for fixed collections of values.
* Choosing the correct data structure makes programs easier to design and maintain.
* Combining data structures with loops allows programs to process collections efficiently.

---

## 🚀 Learning Approach

**Learn → Practice → Test → Understand → Build**

Data structures are a major foundation for Python programming and will be used extensively in the upcoming **functions, OOP, DSA, data analysis, and machine-learning** sections.
