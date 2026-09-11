# Python Basics

This folder contains my Python fundamentals and beginner programs.

The purpose of this section is to build a strong understanding of Python's core syntax and behavior before moving into more advanced topics such as control flow, data structures, functions, OOP, DSA, and machine learning.

---

## 📚 Topics Covered

* Hello World
* Variables
* Data Types
* Input and Output
* Type Conversion
* Arithmetic Operators
* Comparison Operators
* Logical Operators
* Assignment Operators
* Basic Python expressions

---

## 1. Hello World

The first step in learning Python is understanding how to display output.

```python
print("Hello, World!")
```

The `print()` function displays information in the console.

### Example

```python
name = "Subathra"

print("Hello,", name)
```

### Key Idea

`print()` is commonly used for:

* Displaying results
* Showing messages to users
* Checking values while debugging
* Testing small programs

---

## 2. Variables

A variable is a name used to store a value.

```python
name = "Subathra"
age = 18
```

Python determines the data type automatically based on the assigned value.

### Example

```python
name = "Subathra"
age = 18
gpa = 9.1
is_student = True
```

Here:

* `name` stores text
* `age` stores a whole number
* `gpa` stores a decimal number
* `is_student` stores a Boolean value

### Variable Naming Rules

* Use letters, numbers, and underscores.
* Do not start a variable name with a number.
* Do not use Python keywords as variable names.
* Variable names are case-sensitive.
* Use meaningful names whenever possible.

Good:

```python
student_name = "Subathra"
```

Less descriptive:

```python
x = "Subathra"
```

Meaningful variable names make programs easier to understand.

---

## 3. Data Types

A data type describes the kind of value stored in a variable.

Some important built-in Python data types are:

| Data Type | Example    | Purpose           |
| --------- | ---------- | ----------------- |
| `int`     | `18`       | Whole numbers     |
| `float`   | `9.1`      | Decimal numbers   |
| `str`     | `"Python"` | Text              |
| `bool`    | `True`     | True/false values |

### Checking a Data Type

The `type()` function can be used to check the type of a value.

```python
age = 18

print(type(age))
```

Output:

```text
<class 'int'>
```

### Example

```python
name = "Subathra"
age = 18
percentage = 95.5
is_student = True

print(type(name))
print(type(age))
print(type(percentage))
print(type(is_student))
```

Understanding data types is important because different types behave differently when used in operations.

---

## 4. Input and Output

Python can receive information from the user using `input()`.

### Example

```python
name = input("Enter your name: ")

print("Hello,", name)
```

The program waits for the user to enter a value.

### Important

`input()` always returns the user's input as a **string**.

For example:

```python
age = input("Enter your age: ")
```

Even if the user enters:

```text
18
```

Python initially treats it as:

```python
"18"
```

not:

```python
18
```

This is why type conversion is often required.

---

## 5. Type Conversion

Type conversion means changing a value from one data type to another.

Common conversion functions include:

```python
int()
float()
str()
bool()
```

### Example

```python
age = int(input("Enter your age: "))

print(age + 1)
```

Here, the input is converted from a string into an integer.

### Common Conversions

```python
number = int("25")

price = float("99.50")

text = str(100)

value = bool(1)
```

### Why Type Conversion Matters

Consider:

```python
age = input("Enter your age: ")

print(age + 1)
```

This causes an error because `age` is a string.

Instead:

```python
age = int(input("Enter your age: "))

print(age + 1)
```

Now Python can perform numerical addition.

### Common Error

This can fail:

```python
age = int(input("Enter your age: "))
```

if the user enters something such as:

```text
abc
```

because `"abc"` cannot be converted into an integer.

---

# 6. Operators

Operators are symbols or keywords used to perform operations on values.

Python provides several types of operators.

---

## 6.1 Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Meaning        | Example   |
| -------- | -------------- | --------- |
| `+`      | Addition       | `10 + 5`  |
| `-`      | Subtraction    | `10 - 5`  |
| `*`      | Multiplication | `10 * 5`  |
| `/`      | Division       | `10 / 5`  |
| `//`     | Floor division | `10 // 3` |
| `%`      | Modulus        | `10 % 3`  |
| `**`     | Exponentiation | `2 ** 3`  |

### Example

```python
number = 10

print(number + 5)
print(number - 5)
print(number * 2)
print(number / 2)
print(number // 3)
print(number % 3)
print(number ** 2)
```

### `/` vs `//`

Normal division:

```python
10 / 3
```

produces a decimal result.

Floor division:

```python
10 // 3
```

returns the floor value of the division.

---

## 6.2 Comparison Operators

Comparison operators compare two values.

The result is always:

```python
True
```

or:

```python
False
```

### Common Comparison Operators

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

### Example

```python
age = 18

print(age > 18)
print(age == 18)
print(age != 20)
print(age >= 18)
```

Output:

```text
False
True
True
True
```

These operators become especially useful when learning **conditional statements and control flow**.

---

## 6.3 Logical Operators

Logical operators are used to combine conditions.

Python provides:

* `and`
* `or`
* `not`

### `and`

Both conditions must be true.

```python
age = 18
is_student = True

print(age >= 18 and is_student)
```

### `or`

At least one condition must be true.

```python
has_id = True
has_pass = False

print(has_id or has_pass)
```

### `not`

Reverses a Boolean value.

```python
is_raining = False

print(not is_raining)
```

Logical operators become very important when working with complex conditions.

---

## 6.4 Assignment Operators

Assignment operators are used to assign or update values.

Basic assignment:

```python
score = 10
```

Other common forms include:

```python
score += 5
score -= 2
score *= 2
score /= 2
```

### Example

```python
score = 10

score += 5

print(score)
```

Output:

```text
15
```

The statement:

```python
score += 5
```

is equivalent to:

```python
score = score + 5
```

---

# 🔄 How These Concepts Connect

The basic concepts of Python are not isolated. They work together to create useful programs.

### Example

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

next_year_age = age + 1

print("Hello,", name)
print("Next year you will be", next_year_age)
```

This small program uses:

1. Variables
2. User input
3. Strings
4. Type conversion
5. Arithmetic operators
6. Output

These simple building blocks are the foundation for larger programs.

---

# ⚠️ Common Beginner Mistakes

## 1. Forgetting that `input()` returns a string

```python
age = input("Enter your age: ")
```

If numerical operations are required, convert it:

```python
age = int(input("Enter your age: "))
```

---

## 2. Confusing `=` and `==`

```python
x = 10
```

means assignment.

```python
x == 10
```

means comparison.

They have different purposes.

---

## 3. Mixing incompatible data types

This can cause a `TypeError`:

```python
age = 18

# print("Age: " + age)
```

A simple alternative is:

```python
print("Age:", age)
```

or:

```python
print("Age: " + str(age))
```

---

## 4. Confusing `/` and `//`

```python
10 / 3
```

performs normal division.

```python
10 // 3
```

performs floor division.

---

## 5. Using unclear variable names

Instead of:

```python
x = 95
```

prefer:

```python
student_mark = 95
```

when the purpose of the value is known.

---

# 🌍 Real-World Applications

These basic concepts appear in almost every Python application.

### User Applications

User registration and login systems use:

* Variables
* Input
* Strings
* Boolean values
* Comparison operators

### Finance

Financial programs use:

* Integers
* Floating-point numbers
* Arithmetic operators
* Type conversion

### Machine Learning

Machine-learning programs heavily depend on:

* Variables
* Numeric data
* Expressions
* Data types
* Input processing

### IoT

IoT applications receive values from sensors and process them using:

* Variables
* Numeric data
* Arithmetic operators
* Boolean conditions

### Cybersecurity

Security programs use:

* Strings
* Boolean values
* Comparisons
* Logical operators
* User input

---

# 🗂️ Programs in This Folder

| File                              | Concept                        |
| --------------------------------- | ------------------------------ |
| `01_hello_world.py`               | Basic output                   |
| `02_variables_and_data_types.py`  | Variables and data types       |
| `03_input_and_type_conversion.py` | User input and type conversion |
| `04_operators.py`                 | Python operators               |

---

# 🎯 Learning Goal

The goal of this section is to build a strong understanding of Python's fundamental syntax and behavior.

Before moving to advanced programming concepts, I should be comfortable with:

* Creating variables
* Understanding basic data types
* Taking user input
* Converting data types
* Performing calculations
* Comparing values
* Combining conditions
* Updating variables

---

# 🧠 Key Takeaways

* `print()` is used to display output.
* Variables store values.
* Python has built-in data types such as `int`, `float`, `str`, and `bool`.
* `input()` returns user input as a string.
* Type conversion changes values from one type to another.
* Arithmetic operators perform calculations.
* Comparison operators produce `True` or `False`.
* Logical operators combine conditions.
* Assignment operators update variable values.
* These concepts form the foundation of larger Python programs.

---

## 🚀 Learning Approach

**Learn → Practice → Test → Understand → Build**

This folder represents the starting point of my Python learning journey and provides the foundation for the topics that follow.
