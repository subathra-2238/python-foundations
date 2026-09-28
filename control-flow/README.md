# Python Control Flow

This folder contains my Python programs for understanding **control flow**.

Control flow determines the order in which statements are executed in a program. It allows a program to repeat tasks, make decisions, and control when execution should continue or stop.

This section builds on the Python fundamentals learned in `basics/`.

---

## 📚 Topics Covered

* `for` loops
* `while` loops
* `break`
* `continue`
* Loop conditions
* Iteration
* Repetition
* Basic loop control

---

# 1. What is Control Flow?

Normally, Python executes statements from top to bottom.

```python
print("First")
print("Second")
print("Third")
```

Output:

```text
First
Second
Third
```

Control flow allows us to change this normal sequence.

For example, we can:

* Repeat a block of code
* Stop a loop early
* Skip a particular iteration
* Continue execution while a condition is true

This is essential for building programs that respond to different situations.

---

# 2. `for` Loop

A `for` loop is used when we want to repeat a block of code for each item in a sequence or iterable.

### Basic Syntax

```python
for variable in sequence:
    # code to execute
```

### Example

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

The loop runs once for every value produced by `range(5)`.

---

## Using `range()`

`range()` is commonly used with `for` loops.

```python
range(5)
```

produces:

```text
0 1 2 3 4
```

The ending value is not included.

### Example

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

---

## Looping Through a List

A `for` loop can also process items in a list.

```python
subjects = ["Python", "DSA", "Machine Learning"]

for subject in subjects:
    print(subject)
```

Output:

```text
Python
DSA
Machine Learning
```

This is useful when processing collections of data.

---

# 3. `while` Loop

A `while` loop repeats a block of code **as long as a condition is true**.

### Basic Syntax

```python
while condition:
    # code to execute
```

### Example

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Output:

```text
1
2
3
4
5
```

The condition is checked before each iteration.

---

## How a `while` Loop Works

Consider:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

The process is:

1. `number` starts at `1`.
2. Python checks `number <= 5`.
3. The condition is true.
4. The value is printed.
5. `number` is increased.
6. Python checks the condition again.
7. The process continues until the condition becomes false.

When `number` becomes `6`, the loop stops.

---

# 4. `for` vs `while`

Both loops repeat code, but they are commonly used in different situations.

| `for` Loop                                         | `while` Loop                                  |
| -------------------------------------------------- | --------------------------------------------- |
| Used to iterate over a sequence                    | Used while a condition remains true           |
| Common when the number of iterations is known      | Useful when the stopping condition is dynamic |
| Works naturally with lists, strings, and `range()` | Depends on a Boolean condition                |
| Usually easier for counting through a collection   | Useful for condition-based repetition         |

### Example

Use `for` when processing a known collection:

```python
for subject in subjects:
    print(subject)
```

Use `while` when repetition depends on a condition:

```python
while password != "python123":
    password = input("Enter password: ")
```

---

# 5. `break`

The `break` statement immediately stops a loop.

### Example

```python
for number in range(1, 10):
    if number == 5:
        break

    print(number)
```

Output:

```text
1
2
3
4
```

When `number` becomes `5`, `break` stops the loop completely.

---

## Why Use `break`?

`break` is useful when:

* The required value has been found
* A user wants to stop an operation
* A condition requires immediate termination
* Continuing the loop is no longer necessary

### Example

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        print("Number found!")
        break
```

Once `30` is found, there is no reason to continue searching.

---

# 6. `continue`

The `continue` statement skips the current iteration and moves to the next iteration of the loop.

### Example

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

When the value is `3`, Python skips the `print()` statement for that iteration.

---

## `break` vs `continue`

This difference is important.

### `break`

**Stops the entire loop.**

```text
1
2
3
STOP
```

### `continue`

**Skips only the current iteration.**

```text
1
2
SKIP 3
4
5
```

| Statement  | Effect                      |
| ---------- | --------------------------- |
| `break`    | Terminates the loop         |
| `continue` | Skips the current iteration |

---

# 🔄 Combining Conditions and Loops

Control-flow statements become more powerful when combined with conditions.

### Example

```python
for number in range(1, 11):

    if number % 2 == 0:
        print(number)
```

Output:

```text
2
4
6
8
10
```

Here:

* `for` repeats the operation.
* `if` checks the condition.
* `%` determines whether the number is divisible by 2.

This is the beginning of writing logic-based programs.

---

# ⚠️ Common Beginner Mistakes

## 1. Forgetting to update a `while` loop variable

This can create an infinite loop.

Incorrect:

```python
number = 1

while number <= 5:
    print(number)
```

The value of `number` never changes.

Correct:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

---

## 2. Incorrect indentation

Python uses indentation to define blocks.

Correct:

```python
for number in range(5):
    print(number)
```

Incorrect:

```python
for number in range(5):
print(number)
```

Indentation is part of Python syntax.

---

## 3. Confusing `break` and `continue`

Remember:

```text
break    → stop the loop
continue → skip this iteration
```

---

## 4. Off-by-one errors with `range()`

Remember that the ending value is excluded.

```python
range(1, 6)
```

produces:

```text
1 2 3 4 5
```

not `6`.

---

# 🌍 Real-World Applications

Control flow is used throughout software development.

### User Interfaces

Programs repeatedly wait for and process user actions.

### Authentication

A system may repeatedly ask for credentials until:

* Correct credentials are entered
* The maximum number of attempts is reached

### Data Processing

Loops can process thousands or millions of records.

```python
for record in records:
    process(record)
```

### Machine Learning

Training algorithms repeatedly process data during multiple iterations.

### IoT

IoT programs continuously monitor sensor values.

```python
while True:
    sensor_value = read_sensor()
    process(sensor_value)
```

### Cybersecurity

Security systems can continuously monitor events and stop processing when a threat is detected.

---

# 🗂️ Programs in This Folder

| File                       | Concept                                   |
| -------------------------- | ----------------------------------------- |
| `01_for_loop.py`           | `for` loops and iteration                 |
| `02_while_loop.py`         | `while` loops and conditions              |
| `03_break_and_continue.py` | Loop control using `break` and `continue` |

---

# 🎯 Learning Goal

The goal of this section is to understand how Python controls program execution.

After completing this section, I should be comfortable with:

* Repeating code using `for`
* Repeating code using `while`
* Understanding loop conditions
* Using `range()`
* Stopping loops with `break`
* Skipping iterations with `continue`
* Avoiding infinite loops
* Combining loops with conditions

---

# 🧠 Key Takeaways

* Control flow determines how a program executes.
* `for` loops are useful for iterating through sequences.
* `while` loops repeat while a condition remains true.
* `break` completely stops a loop.
* `continue` skips the current iteration.
* `range()` is commonly used for controlled iteration.
* Correct indentation is essential in Python.
* Loops become powerful when combined with conditions.

---

## 🚀 Learning Approach

**Learn → Practice → Test → Understand → Build**

Control flow is an important step toward writing programs that can make decisions, repeat operations, process data, and respond dynamically to different situations.
