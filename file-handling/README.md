# Python File Handling

This folder contains my Python programs for learning **File Handling and File System Operations**.

The programs progress from basic file operations to practical tasks such as file searching, analysis, backups, logging, directory management, and user-data storage.

---

## 📚 What I Learned

This section covers:

* Opening and closing files
* Reading files
* Writing files
* Appending content
* Reading lines and characters
* File modes
* The `with` statement
* File positions using `tell()` and `seek()`
* File and directory management
* File existence checks
* File information and size
* File extensions
* Searching files
* Counting files and file contents
* Text replacement
* File cleaning
* Copying and moving files
* Renaming files and directories
* Backup operations
* File comparison
* Logging
* Timestamps
* User input storage
* Basic file-system automation

---

# 🧠 What Is File Handling?

File handling means using Python to interact with files stored on a computer.

A Python program can use file handling to:

```text
Create
  ↓
Read
  ↓
Write
  ↓
Modify
  ↓
Copy
  ↓
Move
  ↓
Rename
  ↓
Analyze
  ↓
Backup
```

Files provide **persistent storage**, allowing information to remain available even after a Python program finishes.

---

# 📂 File-by-File Learning

## 01 — `01_read_file.py`

### Concept

Reading the complete contents of a file.

### What I learned

* `open()`
* Read mode `"r"`
* `read()`
* `close()`

### Key idea

```python
with open("file.txt", "r") as file:
    content = file.read()
```

This was my introduction to reading data stored in a file.

---

## 02 — `02_write_file.py`

### Concept

Writing data into a file.

### What I learned

* Write mode `"w"`
* `write()`
* Creating a new file
* Overwriting existing content

### Key idea

```python
with open("file.txt", "w") as file:
    file.write("Hello Python")
```

Write mode creates the file if it does not exist.

---

## 03 — `03_append_to_file.py`

### Concept

Adding new content to an existing file.

### What I learned

* Append mode `"a"`
* Adding content without replacing existing content

### Key idea

```python
with open("file.txt", "a") as file:
    file.write("\nNew content")
```

Append mode is useful for logs and continuously updated files.

---

## 04 — `04_read_lines.py`

### Concept

Reading a file one line at a time.

### What I learned

* Iterating through a file
* Processing individual lines
* `strip()`

### Key idea

```python
for line in file:
    print(line.strip())
```

This is useful when files contain multiple records or lines of information.

---

## 05 — `05_with_statement.py`

### Concept

Using the `with` statement for safe file handling.

### What I learned

* Automatic file closing
* Context managers
* Cleaner file-handling code

### Key idea

```python
with open("file.txt", "r") as file:
    content = file.read()
```

The file is automatically closed when the block ends.

---

## 06 — `06_write_with_statement.py`

### Concept

Writing files using the `with` statement.

### What I learned

* Combining write mode with `with`
* Safely creating files
* Writing multiple lines

This improved the earlier write operation by using safer resource management.

---

## 07 — `07_read_characters.py`

### Concept

Reading a specific number of characters.

### What I learned

`read()` can accept a number specifying how many characters to read.

```python
content = file.read(10)
```

This is useful when only part of a file is required.

---

## 08 — `08_readline.py`

### Concept

Reading one line from a file.

### What I learned

* `readline()`
* Reading a single line
* Processing line-based data

```python
line = file.readline()
```

---

## 09 — `09_read_all_lines.py`

### Concept

Reading all lines into a list.

### What I learned

* `readlines()`
* Lists of file lines
* Iterating through returned lines

```python
lines = file.readlines()
```

---

## 10 — `10_file_position.py`

### Concept

Understanding the current position inside a file.

### What I learned

* `tell()`
* `seek()`
* File cursor position

```python
file.tell()
file.seek(0)
```

This demonstrated how Python tracks where it currently is while reading a file.

---

## 11 — `11_check_file_exists.py`

### Concept

Checking whether a file exists.

### What I learned

* `os.path.exists()`
* Basic file validation

```python
if os.path.exists(file_path):
    print("File exists!")
```

Checking existence before performing operations makes programs safer.

---

## 12 — `12_delete_file.py`

### Concept

Deleting a file programmatically.

### What I learned

* `os.remove()`
* File existence checking
* Safe deletion

```python
if os.path.exists(file_path):
    os.remove(file_path)
```

This introduced file deletion and the importance of checking before removing files.

---

## 13 — `13_file_exceptions.py`

### Concept

Handling file-related errors.

### What I learned

* `try`
* `except`
* `FileNotFoundError`

```python
try:
    with open(file_path, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
```

Error handling prevents a program from crashing unexpectedly.

---

## 14 — `14_file_modes.py`

### Concept

Understanding different file modes.

### What I learned

* Read mode
* Write mode
* Append mode
* How different modes affect file content

This connected the earlier file operations into one example.

---

## 15 — `15_create_directory.py`

### Concept

Creating directories using Python.

### What I learned

* `os.mkdir()`
* Checking directory existence

```python
os.mkdir(folder_path)
```

This introduced programmatic folder management.

---

## 16 — `16_list_directory.py`

### Concept

Listing the contents of a directory.

### What I learned

* `os.listdir()`
* Working with files and folders

```python
items = os.listdir(folder_path)
```

The program displays everything inside a directory.

---

## 17 — `17_remove_directory.py`

### Concept

Removing a directory.

### What I learned

* `os.rmdir()`
* `PermissionError`
* Why operating-system permissions and file locks matter

This lesson also gave practical experience with Windows directory permissions.

---

## 18 — `18_copy_file.py`

### Concept

Copying a file.

### What I learned

* `shutil`
* `shutil.copy()`
* Source and destination paths

```python
shutil.copy(source, destination)
```

Copying files is useful for backups and file organization.

---

## 19 — `19_move_file.py`

### Concept

Moving a file from one location to another.

### What I learned

* `shutil.move()`
* Source and destination paths

```python
shutil.move(source, destination)
```

---

## 20 — `20_rename_file.py`

### Concept

Renaming a file.

### What I learned

* `os.rename()`
* Old and new file names

```python
os.rename(old_name, new_name)
```

---

## 21 — `21_rename_directory.py`

### Concept

Renaming a directory.

### What I learned

* `os.rename()`
* Applying file-system operations to folders

This demonstrated that `os.rename()` can work with directories as well as files.

---

## 22 — `22_check_directory.py`

### Concept

Checking whether a directory exists.

### What I learned

* `os.path.exists()`
* Directory validation

This introduced basic safety checks before directory operations.

---

## 23 — `23_current_directory.py`

### Concept

Finding the current working directory.

### What I learned

* `os.getcwd()`

```python
current_directory = os.getcwd()
```

The working directory determines how relative file paths are interpreted.

---

## 24 — `24_change_directory.py`

### Concept

Changing the current working directory of the Python process.

### What I learned

* `os.chdir()`
* Working directory concepts

```python
os.chdir("file-handling")
```

Important: this changes the working directory **inside the running Python process**, not permanently in PowerShell.

---

## 25 — `25_create_nested_directories.py`

### Concept

Creating multiple levels of directories.

### What I learned

* `os.makedirs()`
* Nested directory structures
* `exist_ok=True`

```python
os.makedirs(folder_path, exist_ok=True)
```

---

## 26 — `26_file_size.py`

### Concept

Finding the size of a file.

### What I learned

* `os.path.getsize()`
* File size in bytes

```python
size = os.path.getsize(file_path)
```

This is useful for storage monitoring and file analysis.

---

## 27 — `27_file_information.py`

### Concept

Retrieving information about a file.

### What I learned

* `os.stat()`
* `os.path.basename()`
* `os.path.abspath()`
* File metadata

This introduced the idea of examining a file beyond just its contents.

---

## 28 — `28_file_extension.py`

### Concept

Extracting the file extension.

### What I learned

* `os.path.splitext()`
* Separating filename and extension

Example:

```text
sample.txt
   ↓
sample + .txt
```

This is useful for organizing files by type.

---

## 29 — `29_list_files.py`

### Concept

Listing only files inside a directory.

### What I learned

* `os.path.isfile()`
* Combining `os.listdir()` with path operations

The program filters out directories.

---

## 30 — `30_list_directories.py`

### Concept

Listing only directories.

### What I learned

* `os.path.isdir()`
* Filtering directory entries

This is the opposite of the previous exercise.

---

## 31 — `31_walk_directory.py`

### Concept

Recursively exploring a directory.

### What I learned

* `os.walk()`
* Root directory
* Subdirectories
* Files

```python
for root, directories, files in os.walk(folder_path):
    ...
```

This is an important foundation for automated file-system tools.

---

## 32 — `32_find_file.py`

### Concept

Finding a specific file inside a directory tree.

### What I learned

* `os.walk()`
* Searching filenames
* `os.path.join()`

This demonstrated how to build a basic file-search utility.

---

## 33 — `33_find_files_by_extension.py`

### Concept

Finding files based on their extension.

### What I learned

* `endswith()`
* Extension filtering
* Recursive searching

Example:

```python
if file.endswith(".txt"):
    ...
```

---

## 34 — `34_count_files_by_extension.py`

### Concept

Counting files with a specific extension.

### What I learned

* Counters
* File filtering
* Recursive directory traversal

This combines file-system operations with basic programming logic.

---

## 35 — `35_count_lines.py`

### Concept

Counting the number of lines in a file.

### What I learned

* `readlines()`
* `len()`
* Basic text analysis

```python
print(len(lines))
```

---

## 36 — `36_count_words.py`

### Concept

Counting words in a file.

### What I learned

* `read()`
* `split()`
* `len()`

```python
words = content.split()
```

This was an introduction to basic text processing.

---

## 37 — `37_count_characters.py`

### Concept

Counting characters in a file.

### What I learned

* Reading file content
* `len()`
* Character-level analysis

---

## 38 — `38_remove_empty_lines.py`

### Concept

Ignoring blank lines.

### What I learned

* `strip()`
* Detecting empty lines
* Basic file cleaning

```python
if line.strip():
    print(line.strip())
```

---

## 39 — `39_count_word.py`

### Concept

Counting occurrences of a specific word.

### What I learned

* `split()`
* Loops
* String cleaning
* Word comparison

```python
if word.strip(".,!?") == target_word:
    count += 1
```

This introduced slightly more realistic text analysis.

---

## 40 — `40_file_statistics.py`

### Concept

Generating basic statistics about a file.

### What I learned

* Number of lines
* Number of words
* Number of characters
* Combining multiple operations

This brought several earlier concepts together into one small utility.

---

## 41 — `41_search_word.py`

### Concept

Searching for a word inside a file.

### What I learned

* Membership testing using `in`
* String searching

```python
if target_word in content:
    print("Word found!")
```

---

## 42 — `42_search_word_lines.py`

### Concept

Finding the lines containing a specific word.

### What I learned

* `enumerate()`
* Line numbers
* String searching

```python
for line_number, line in enumerate(file, start=1):
    ...
```

This makes search results more useful because the exact line can be identified.

---

## 43 — `43_replace_word.py`

### Concept

Replacing text inside file content.

### What I learned

* `str.replace()`
* Creating updated content

```python
updated_content = content.replace(old_word, new_word)
```

---

## 44 — `44_save_replaced_content.py`

### Concept

Saving modified content into a new file.

### What I learned

* Reading one file
* Modifying its content
* Writing the result to another file

This introduced a basic **read → transform → save** workflow.

---

## 45 — `45_copy_file_contents.py`

### Concept

Copying the contents of one file into another.

### What I learned

* Reading source content
* Writing destination content
* Working with two files

This demonstrated copying at the content level rather than using `shutil`.

---

## 46 — `46_writelines.py`

### Concept

Writing multiple lines using `writelines()`.

### What I learned

* `writelines()`
* Lists of strings
* Writing multiple records

```python
file.writelines(subjects)
```

---

## 47 — `47_readline_loop.py`

### Concept

Reading a file repeatedly using `readline()`.

### What I learned

* `readline()`
* `while` loops
* Detecting the end of a file

```python
while True:
    line = file.readline()

    if not line:
        break
```

This connected file handling with control flow.

---

## 48 — `48_count_matching_lines.py`

### Concept

Counting lines containing a particular word.

### What I learned

* File iteration
* Conditional statements
* Counters
* String searching

This combines several previously learned concepts.

---

## 49 — `49_clean_file.py`

### Concept

Removing blank lines and saving a cleaned version.

### What I learned

* Reading all lines
* Filtering content
* Creating a cleaned list
* Writing the cleaned result

This introduced a simple data-cleaning workflow.

---

## 50 — `50_file_logger.py`

### Concept

Creating a simple activity log.

### What I learned

* Append mode
* Log files
* Recording program activity

```python
with open(log_file, "a") as file:
    file.write(message + "\n")
```

This is the foundation of practical logging systems.

---

## 51 — `51_timestamp_logger.py`

### Concept

Adding timestamps to log entries.

### What I learned

* `datetime`
* `datetime.now()`
* Combining timestamps with file logging

This makes log information more useful because each event gets a time.

---

## 52 — `52_file_report.py`

### Concept

Generating a report about a file.

### What I learned

* File existence
* File size
* Filename
* Lines
* Words
* Characters
* Combining `os` and file handling

This was one of the first exercises that combined several file-handling concepts into a practical utility.

---

## 53 — `53_backup_file.py`

### Concept

Creating a backup copy of a file.

### What I learned

* `shutil.copy()`
* Checking file existence
* Basic backup logic

Backups are an important real-world application of file handling.

---

## 54 — `54_compare_files.py`

### Concept

Comparing the contents of two files.

### What I learned

* Reading multiple files
* Comparing strings
* Equality checking

```python
if content1 == content2:
    print("The files have the same content.")
```

---

## 55 — `55_timestamp_backup.py`

### Concept

Creating uniquely named backups using timestamps.

### What I learned

* `datetime`
* `strftime()`
* Dynamic filenames
* `shutil.copy()`

Example filename pattern:

```text
sample_backup_20260911_171500.txt
```

This prevents different backups from overwriting one another.

---

## 56 — `56_copy_multiple_files.py`

### Concept

Copying multiple files automatically.

### What I learned

* Directory iteration
* Extension filtering
* `shutil.copy()`
* Creating destination directories

This introduced batch file operations.

---

## 57 — `57_move_multiple_files.py`

### Concept

Moving multiple files automatically.

### What I learned

* `shutil.move()`
* Loops
* Directory filtering
* Batch file organization

This is a simple example of file-system automation.

---

## 58 — `58_largest_file.py`

### Concept

Finding the largest file inside a directory tree.

### What I learned

* `os.walk()`
* `os.path.getsize()`
* Comparing values
* Tracking the largest result

This combines file searching, recursion through directories, and comparison logic.

---

## 59 — `59_delete_txt_files.py`

### Concept

Deleting files based on their extension.

### What I learned

* Extension filtering
* `os.remove()`
* Automated cleanup

This lesson also reinforced an important practical rule:

> Automated deletion operations must be tested carefully because they can permanently remove files.

---

## 60 — `60_backup_folder.py`

### Concept

Creating a dedicated backup directory.

### What I learned

* Directory creation
* `os.makedirs()`
* Checking whether a folder exists

This established a structured location for future backups.

---

## 61 — `61_backup_to_folder.py`

### Concept

Copying a file into a backup directory.

### What I learned

* `shutil.copy()`
* `os.path.join()`
* Creating directories when necessary
* Structured backup paths

This improved the earlier backup example by separating backups from normal files.

---

## 62 — `62_list_backup_files.py`

### Concept

Listing files stored inside a backup folder.

### What I learned

* Directory existence checking
* `os.listdir()`
* Processing backup contents

This demonstrated how a program can inspect its backup storage.

---

## 63 — `63_find_large_files.py`

### Concept

Finding files larger than a specified size.

### What I learned

* File-size filtering
* `os.path.getsize()`
* `os.walk()`
* Conditional thresholds

Example:

```python
if size > minimum_size:
    print(file)
```

This is useful for storage-management tools.

---

## 64 — `64_extension_counts.py`

### Concept

Counting files based on their extensions.

### What I learned

* Dictionaries
* `os.path.splitext()`
* Counting
* Directory traversal

Example result:

```text
.py : 10
.txt : 5
.log : 2
```

This connects **data structures** with file-system operations.

---

## 65 — `65_find_empty_files.py`

### Concept

Finding files with zero bytes.

### What I learned

* `os.path.getsize()`
* File filtering
* Boolean flags
* Recursive searching

```python
if os.path.getsize(file_path) == 0:
    ...
```

This can be useful when checking for incomplete or unused files.

---

## 66 — `66_append_multiple_lines.py`

### Concept

Appending multiple lines to an existing file.

### What I learned

* Append mode
* Lists
* `writelines()`
* Adding multiple records

This combined earlier concepts into a more practical operation.

---

## 67 — `67_number_lines.py`

### Concept

Displaying every line with its line number.

### What I learned

* `enumerate()`
* File iteration
* Line numbering

Example:

```text
1 : Hello, I am Subathra.
2 : I am learning Python.
3 : This is my Python Foundations journey.
```

---

## 68 — `68_count_word_lines.py`

### Concept

Finding and counting all lines containing a specific word.

### What I learned

* `enumerate()`
* String searching
* Counters
* Line-based analysis

This combines search and counting into one program.

---

## 69 — `69_remove_duplicate_lines.py`

### Concept

Removing duplicate lines from a file.

### What I learned

* Lists
* Sets
* Duplicate detection
* File cleaning
* Writing processed content

A `set` is used to remember which lines have already appeared.

This connects the **Data Structures** section with **File Handling**.

---

## 70 — `70_user_input_to_file.py`

### Concept

Saving user input into a file.

### What I learned

* `input()`
* String formatting/concatenation
* Writing user-provided information
* Persistent storage

This demonstrated how a program can collect information from a user and save it for later.

---

## 71 — `71_read_user_notes.py`

### Concept

Reading previously saved user information.

### What I learned

* Reading stored data
* `try` / `except`
* `FileNotFoundError`
* Persistent user information

This completes the basic **write → store → read** workflow.

---

## 72 — `72_append_user_input.py`

### Concept

Appending new user notes to an existing file.

### What I learned

* User input
* Append mode
* Dynamic file content
* Persistent notes

```python
note = input("Enter a new note: ")

with open(file_path, "a") as file:
    file.write("Note: " + note + "\n")
```

This combines several concepts learned throughout the File Handling section.

---

# 🔗 How the Lessons Connect

The exercises were designed to progress gradually:

```text
01–10
Basic File Operations
        ↓
11–17
File & Directory Management
        ↓
18–30
Copy / Move / Rename / Path Operations
        ↓
31–40
Searching & File Analysis
        ↓
41–49
Text Searching, Replacement & Cleaning
        ↓
50–55
Logging, Reports & Backups
        ↓
56–65
Multiple Files & File-System Automation
        ↓
66–69
Advanced Text Processing
        ↓
70–72
User Input & Persistent Storage
```

---

# 🛠️ Important Python Modules

## `os`

Used for interacting with the operating system.

Examples:

```python
os.path.exists()
os.path.isfile()
os.path.isdir()
os.path.getsize()
os.listdir()
os.walk()
os.mkdir()
os.makedirs()
os.remove()
os.rename()
os.getcwd()
os.chdir()
```

---

## `shutil`

Used for higher-level file operations.

Examples:

```python
shutil.copy()
shutil.move()
```

It is particularly useful for copying, moving, and managing files.

---

## `datetime`

Used for timestamps.

```python
from datetime import datetime

datetime.now()
```

It became useful in the logging and timestamped-backup exercises.

---

# 🌍 Real-World Applications

File handling is used in many areas of software development.

### 🤖 AI & Machine Learning

Files are used for:

* Datasets
* CSV files
* JSON files
* Model files
* Configuration
* Training data

### 🔐 Cybersecurity

Security systems frequently process:

* Log files
* Event records
* Threat indicators
* System information
* Audit data

### 📡 IoT

IoT applications may store:

* Sensor readings
* Device logs
* Configuration information
* System events

### ⚙️ Automation

Python can automatically:

* Organize files
* Rename files
* Search folders
* Create backups
* Generate reports
* Remove temporary files

### 💻 Software Development

Files are commonly used for:

* Configuration
* Logging
* Reports
* Persistent data
* Temporary storage

---

# ⚠️ Important Safety Lessons

Some file operations can permanently change or delete data.

Be especially careful with:

```python
os.remove()
os.rmdir()
shutil.move()
open(file, "w")
```

Before performing destructive operations:

1. Check the path.
2. Check whether the file exists.
3. Understand the selected mode.
4. Avoid testing on important files.
5. Use backups when appropriate.

---

# 🎯 Learning Goal

The goal of this section was to understand how Python interacts with files and directories.

After completing these exercises, I can:

* Read files
* Write files
* Append content
* Read individual lines
* Read multiple lines
* Read specific characters
* Manage file positions
* Handle file errors
* Create directories
* List directories
* Search files
* Filter files by extension
* Analyze file contents
* Count lines, words, and characters
* Replace text
* Clean files
* Copy files
* Move files
* Rename files
* Delete files
* Create backups
* Compare files
* Create logs
* Add timestamps
* Store user information
* Perform basic file-system automation

---

# 🧠 Key Takeaways

* `open()` is used to work with files.
* `"r"` reads files.
* `"w"` writes and can overwrite files.
* `"a"` appends content.
* `with` safely manages file resources.
* `read()`, `readline()`, and `readlines()` provide different ways to read files.
* `tell()` and `seek()` manage file positions.
* The `os` module provides operating-system and file-system operations.
* The `shutil` module provides convenient copying and moving operations.
* `os.walk()` is useful for recursive directory searching.
* Exception handling makes file operations more reliable.
* File handling can be combined with lists, sets, dictionaries, loops, and functions.
* File handling is an important foundation for automation, data processing, cybersecurity, AI, and IoT.

---

# 📈 My Progress

**72 file-handling exercises completed**

```text
████████████████████████████████████████████████████████████████████████████████ 72%
```

The progression moved from simple:

```text
Read → Write → Append
```

to:

```text
Search → Analyze → Modify → Organize → Backup → Automate → Store User Data
```

This section helped me move from basic Python syntax toward **practical Python programming**.

---

## 🔄 Learning Approach

**Learn → Practice → Run → Understand → Document → Automate**

The objective was not only to memorize file-handling methods, but to understand how they can be combined to solve real programming problems.


# 📚 File Handling — Learning & Revision Notes

## Topics 73–100

These notes are designed for **revision and understanding**.
When revisiting File Handling, focus on the **concept first**, then look at the code.

---

# 73. `pathlib` Basics

### 🧠 What is `pathlib`?

`pathlib` is Python's modern way of working with file and directory paths.

Instead of manually building paths as strings, we create a `Path` object.

```python
from pathlib import Path

file_path = Path("data.txt")
```

### 🔑 Important methods

```python
file_path.exists()
file_path.is_file()
file_path.is_dir()
```

| Method      | Meaning              |
| ----------- | -------------------- |
| `exists()`  | Does the path exist? |
| `is_file()` | Is it a file?        |
| `is_dir()`  | Is it a directory?   |

### ⚠️ Common mistake

```python
Path = "data.txt"
Path.exists()
```

This doesn't work because `"data.txt"` is just a string.

### ✅ Correct

```python
from pathlib import Path

file_path = Path("data.txt")
print(file_path.exists())
```

### 🎯 Remember

> `Path` = object used to represent a file or directory location.

---

# 74. Path Components

A path contains different parts.

```python
from pathlib import Path

file_path = Path("file-handling/sample.txt")

print(file_path.parent)
print(file_path.name)
print(file_path.stem)
print(file_path.suffix)
```

### 🔑 Understand this

For:

```text
file-handling/sample.txt
```

```text
parent → file-handling
name   → sample.txt
stem   → sample
suffix → .txt
```

### 🧠 Memory trick

```text
.name   → complete name
.stem   → name without extension
.suffix → extension
.parent → folder containing it
```

### ⚠️ Common mistake

Thinking:

```python
file_path.stem
```

returns `sample.txt`.

It returns:

```text
sample
```

---

# 75. Relative vs Absolute Paths

### Relative path

```python
Path("file-handling/sample.txt")
```

The location is interpreted relative to the current working directory.

### Absolute path

Example:

```text
C:\Users\SUBATHRA\Documents\project\file-handling\sample.txt
```

It gives the complete location.

### Useful methods

```python
path.absolute()
path.resolve()
```

### 🧠 Remember

```text
Relative → "where from here?"
Absolute  → "exactly where?"
```

### ⚠️ Common error

Running a Python file from a different directory may cause:

```text
FileNotFoundError
```

### 🛠️ Solution

Check the current directory:

```python
from pathlib import Path

print(Path.cwd())
```

Then make sure your relative path is correct.

---

# 76. Creating a Directory

```python
from pathlib import Path

folder = Path("test_folder")

folder.mkdir(exist_ok=True)
```

### `mkdir()`

Creates a directory.

### `exist_ok=True`

Prevents an error if the directory already exists.

### ⚠️ Without `exist_ok=True`

If the folder already exists:

```text
FileExistsError
```

### ✅ Solution

```python
folder.mkdir(exist_ok=True)
```

### 🎯 Real-world use

Creating:

* Project folders
* Dataset folders
* Output folders
* Backup folders

---

# 77. Creating Nested Directories

Example:

```text
data/
└── projects/
    └── python/
```

Use:

```python
folder.mkdir(parents=True, exist_ok=True)
```

### 🔑 Difference

```text
parents=False → parent folders must already exist
parents=True  → create missing parent folders
```

### ⚠️ Common error

```text
FileNotFoundError
```

can occur when trying to create a deep path without its parents.

### ✅ Solution

```python
folder.mkdir(parents=True, exist_ok=True)
```

### 🧠 Remember

> `parents=True` = create the whole path if necessary.

---

# 78. Reading Directory Contents

Use:

```python
folder.iterdir()
```

Example:

```python
for item in folder.iterdir():
    print(item)
```

This gives each item inside the directory.

### ⚠️ Important

`iterdir()` does **not** recursively search every subfolder.

For recursive searching, use `rglob()`.

### 🎯 Use when

You want to:

* List files
* Check folders
* Process directory contents

---

# 79. `glob()`

`glob()` searches for files matching a pattern.

```python
folder.glob("*.py")
```

### What does `*.py` mean?

```text
*   → any filename
.py → Python extension
```

So it finds:

```text
hello.py
main.py
test.py
```

### Other examples

```python
folder.glob("*.txt")
folder.glob("*.csv")
folder.glob("data*")
```

### ⚠️ Common mistake

Expecting:

```python
glob("*.py")
```

to search all subdirectories.

It only searches the specified directory.

### 🧠 Remember

> `glob()` = pattern matching in a directory.

---

# 80. `rglob()` — Recursive Search

`rglob()` searches through subdirectories too.

```python
folder.rglob("*.py")
```

### Difference

```text
glob()  → one directory
rglob() → directory + subdirectories
```

Example:

```text
project/
├── main.py
├── basics/
│   └── hello.py
└── tests/
    └── test.py
```

`glob("*.py")` may find only:

```text
main.py
```

`rglob("*.py")` finds all three.

### 🎯 Real-world use

Finding:

* All Python files
* All CSV datasets
* All images
* All log files

---

# 81. File vs Directory

Use:

```python
item.is_file()
item.is_dir()
```

Example:

```python
for item in folder.iterdir():

    if item.is_file():
        print("FILE:", item)

    elif item.is_dir():
        print("FOLDER:", item)
```

### 🧠 Why check?

Because a directory can contain both:

```text
files
folders
```

Trying to process both as files can cause errors.

### 🎯 Remember

```text
is_file() → file?
is_dir()  → folder?
```

---

# 82. File Size

Use:

```python
file_path.stat().st_size
```

The result is in **bytes**.

Example:

```python
size = file_path.stat().st_size
```

### Convert bytes

```python
kb = size / 1024
mb = size / (1024 ** 2)
```

### ⚠️ Common confusion

`st_size` does NOT return KB or MB.

It returns:

```text
bytes
```

### 🎯 Real-world use

Useful for:

* Checking large files
* Storage management
* Upload validation
* Backup systems

---

# 83. File Modification Time

```python
info = file_path.stat()

modified = info.st_mtime
```

This gives a timestamp.

Convert it:

```python
from datetime import datetime

readable = datetime.fromtimestamp(info.st_mtime)
```

### 🧠 Important

`st_mtime` = last modification time.

### 🎯 Use

Useful for:

* Detecting recently changed files
* Backup systems
* Log monitoring
* File synchronization

---

# 84. File Metadata

Metadata = information **about a file**, not its actual content.

```python
info = file_path.stat()
```

Useful properties:

```python
info.st_size
info.st_mtime
info.st_ctime
```

### Think of it as

```text
File
 ├── content
 └── metadata
      ├── size
      ├── modified time
      └── timestamps
```

### ⚠️ Important platform difference

`st_ctime` does not mean exactly the same thing on every operating system.

On Windows it generally represents creation time.

On Unix-like systems it can represent metadata change time.

### 🎯 Remember

> `stat()` = get information about the file.

---

# 85. Rename a File

```python
old_file.rename(new_file)
```

Example:

```python
old_file = Path("old.txt")
new_file = Path("new.txt")

old_file.rename(new_file)
```

### 🧠 Important

`rename()` can also move a file if the destination is another path.

### ⚠️ Common error

```text
FileNotFoundError
```

if the source file doesn't exist.

### 🛠️ Solution

```python
if old_file.exists():
    old_file.rename(new_file)
```

---

# 86. Move a File

Example:

```python
source = Path("old_folder/file.txt")
destination = Path("new_folder/file.txt")

source.rename(destination)
```

### 🧠 Key idea

A move changes the file's location.

```text
Before:
old_folder/file.txt

After:
new_folder/file.txt
```

The original file is no longer at the old location.

### ⚠️ Possible issue

Destination folder must generally exist.

### ✅ Solution

```python
destination.parent.mkdir(parents=True, exist_ok=True)
```

Then move the file.

---

# 87. Delete a File

Use:

```python
file_path.unlink()
```

### Safer version

```python
if file_path.exists() and file_path.is_file():
    file_path.unlink()
```

### ⚠️ Common errors

#### `FileNotFoundError`

The file doesn't exist.

#### `PermissionError`

Python doesn't have permission to delete it or another process is using it.

#### `IsADirectoryError`

You tried to use `unlink()` on a directory.

### 🧠 Remember

```text
unlink() → file
rmdir()  → empty directory
rmtree() → directory tree
```

---

# 88. Delete an Empty Directory

Use:

```python
folder.rmdir()
```

### ⚠️ Very important

`rmdir()` only works if the directory is empty.

If the folder contains files:

```text
OSError
```

may occur.

### 🎯 Memory

```text
rmdir()
   ↓
empty folder only
```

---

# 89. Delete a Directory Tree

Use:

```python
import shutil

shutil.rmtree(folder)
```

Unlike `rmdir()`, this can delete:

```text
folder
├── file1
├── file2
└── subfolder
    └── file3
```

### ⚠️ DANGER

`rmtree()` is destructive.

There is usually no normal recycle-bin style recovery.

### 🛡️ Safety rule

Never blindly do:

```python
shutil.rmtree(some_path)
```

Always verify the path first.

### 🧠 Remember

```text
rmdir()  → empty folder
rmtree() → folder + everything inside
```

---

# 90. Copy a File

Use:

```python
shutil.copy2(source, destination)
```

### `copy2()`

Copies the file and attempts to preserve metadata.

### Difference between copy and move

```text
copy → original remains
move → original changes location
```

### 🧠 Remember

```text
copy2() → duplicate
move()  → relocate
```

### ⚠️ Common error

```text
FileNotFoundError
```

if the source doesn't exist.

---

# 91. Copy a Directory

Use:

```python
shutil.copytree(source, destination)
```

It copies the entire directory structure.

### Example

```text
source/
├── a.txt
└── b.txt
```

becomes:

```text
backup/
├── a.txt
└── b.txt
```

### ⚠️ Common error

If the destination already exists, older Python versions/usage can produce:

```text
FileExistsError
```

### Modern solution

When appropriate:

```python
shutil.copytree(source, destination, dirs_exist_ok=True)
```

### 🧠 Remember

```text
copy2()    → one file
copytree() → directory
```

---

# 92. Move a Directory

Use:

```python
shutil.move(source, destination)
```

This can move an entire directory.

### Difference

```text
shutil.copytree() → duplicate
shutil.move()     → relocate
```

### 🎯 Real-world use

Moving:

* Project folders
* Backup folders
* Dataset folders
* Processed files

---

# 93. Disk Usage

Use:

```python
shutil.disk_usage("C:\\")
```

It returns:

```text
total
used
free
```

All values are in bytes.

### Convert to GB

```python
gb = 1024 ** 3

print(total / gb)
```

### 🧠 Remember

```text
total → entire storage
used  → currently occupied
free  → available
```

### 🎯 Real-world use

Storage monitoring applications can use this information to warn when disk space is low.

---

# 94. Temporary Files

Python provides:

```python
tempfile.NamedTemporaryFile()
```

Temporary files are useful when data is needed only for a short period.

### Example uses

* Testing
* Temporary processing
* Intermediate calculations
* Download processing

### Important

```python
delete=False
```

means Python will not automatically delete the temporary file when the context ends.

Therefore, we manually clean it:

```python
temp_path.unlink()
```

### ⚠️ Common mistake

Creating temporary files and never deleting them can leave unnecessary files behind.

### 🧠 Remember

> Temporary data should have a cleanup strategy.

---

# 95. Temporary Directory

Use:

```python
tempfile.TemporaryDirectory()
```

Example:

```python
with tempfile.TemporaryDirectory() as temp_dir:
    ...
```

When the `with` block ends, Python automatically cleans the directory.

### 🧠 Why `with`?

The context manager handles cleanup.

```text
create
  ↓
use
  ↓
with block ends
  ↓
automatic cleanup
```

### 🎯 Best practice

For temporary directories, prefer `TemporaryDirectory()` when possible because cleanup is automatic.

---

# 96. JSON Files

JSON = **JavaScript Object Notation**

It is a common format for structured data.

Example:

```json
{
    "name": "Subathra",
    "age": 18
}
```

### Python → JSON

```python
json.dump(data, file)
```

### JSON → Python

```python
data = json.load(file)
```

### 🧠 Most important thing

```text
dump → write
load → read
```

Think:

```text
dump = put data into file
load = load data from file
```

### ⚠️ Common error

```text
JSONDecodeError
```

This usually means the JSON content is invalid or malformed.

### Example problem

```json
{
    "name": "Subathra",
}
```

The trailing comma can make the JSON invalid.

### 🛠️ Solution

Use valid JSON syntax.

---

# 97. CSV Files

CSV = **Comma-Separated Values**

Example:

```text
Name,Age,Department
Subathra,18,AI & ML
Sivasri,18,CSE
```

### Writing

```python
writer = csv.writer(file)
writer.writerows(data)
```

### Reading

```python
reader = csv.reader(file)

for row in reader:
    print(row)
```

### 🧠 Remember

```text
writer → CSV creation
reader → CSV reading
```

### ⚠️ Common mistake

Forgetting:

```python
newline=""
```

when opening CSV files can sometimes cause unwanted blank lines, particularly on Windows.

### ✅ Recommended

```python
with open("data.csv", "w", newline="") as file:
```

### 🎯 AI/ML connection

CSV is extremely common for:

* Datasets
* Student records
* Sales data
* Sensor data
* Machine-learning preprocessing

---

# 98. ZIP Files

ZIP files allow multiple files to be stored inside one compressed archive.

Python module:

```python
import zipfile
```

### Create ZIP

```python
with zipfile.ZipFile("backup.zip", "w") as zip_file:
    zip_file.write("file1.txt")
```

### List files

```python
zip_file.namelist()
```

### Modes

```text
"w" → create/write
"r" → read
```

### 🧠 Think of ZIP as

```text
Several files
     ↓
  ZIP archive
     ↓
One portable package
```

### 🎯 Uses

* Backups
* Sharing projects
* Packaging files
* Archiving

### ⚠️ Common mistake

Using:

```python
"w"
```

when you intended to add to an existing archive can replace/recreate the archive.

Understand the mode before opening a ZIP.

---

# 99. File Encoding — UTF-8

Encoding tells Python how characters are represented in a file.

Use:

```python
encoding="utf-8"
```

### Example

```python
file_path.write_text(
    content,
    encoding="utf-8"
)
```

and:

```python
text = file_path.read_text(
    encoding="utf-8"
)
```

### Why UTF-8?

It supports:

```text
English
Tamil
Hindi
Chinese
Emojis 😀
Special characters
```

### ⚠️ Common error

```text
UnicodeDecodeError
```

This can happen when Python tries to read data using an incompatible encoding.

### 🛠️ First solution

Try explicitly specifying the correct encoding:

```python
open("file.txt", encoding="utf-8")
```

### 🧠 Remember

> Encoding = how characters are stored/read.

---

# 100. Mini File Organizer Project

This is the final project of the File Handling section.

### 🎯 Goal

Automatically organize files according to their extensions.

Example:

```text
organizer_demo/
│
├── notes.txt
├── data.csv
├── config.json
└── program.py
```

becomes:

```text
organizer_demo/
│
├── text_files/
│   └── notes.txt
│
├── csv_files/
│   └── data.csv
│
├── json_files/
│   └── config.json
│
└── python_files/
    └── program.py
```

### 🔑 Concepts used

This project combines:

```text
Path()
   ↓
mkdir()
   ↓
iterdir()
   ↓
is_file()
   ↓
suffix
   ↓
dictionary
   ↓
shutil.move()
```

### 🧠 The important logic

```python
extension = file.suffix.lower()
```

Find the extension.

Then:

```python
if extension in folders:
```

Check whether we have a category for that extension.

Then:

```python
destination_folder = source_folder / folders[extension]
```

Find the destination folder.

Finally:

```python
shutil.move(...)
```

Move the file.

---

# ⚠️ Common File Organizer Errors

## 1. `FileNotFoundError`

The source path doesn't exist.

### Check:

```python
print(source_folder.resolve())
print(source_folder.exists())
```

---

## 2. `FileExistsError`

A directory you're trying to create already exists.

### Solution:

```python
mkdir(exist_ok=True)
```

---

## 3. `PermissionError`

Python doesn't have permission to modify/delete the path.

Possible reasons:

* File is being used by another program
* OneDrive synchronization
* Read-only/restricted attributes
* Insufficient permissions

### First steps

Close programs using the file and check the file/folder attributes.

---

## 4. `IsADirectoryError`

You expected a file but got a directory.

### Solution

Check:

```python
if path.is_file():
```

before performing file operations.

---

## 5. `NotADirectoryError`

You expected a directory but the path points to a file.

### Solution

```python
if path.is_dir():
```

---

## 6. `PermissionError` with `rmdir()`

If the directory is empty but deletion still fails on Windows, the directory may have special attributes or may be managed by synchronization software such as OneDrive.

### Check using PowerShell

```powershell
Get-Item "file-handling\test_folder" | Format-List *
```

If necessary, inspect attributes and remove a read-only attribute:

```powershell
attrib -R "file-handling\test_folder"
```

Then retry the Python program.

### Important lesson

> An "empty folder" does not always mean Python can delete it. Filesystem attributes and synchronization software can affect operations.

---

# 🧠 MASTER REVISION — File Handling

## Path Operations

```python
Path()
.exists()
.is_file()
.is_dir()
.parent
.name
.stem
.suffix
.absolute()
.resolve()
```

---

## Directory Operations

```python
.mkdir()
.iterdir()
.glob()
.rglob()
.rmdir()
```

---

## File Operations

```python
.read_text()
.write_text()
.open()
.rename()
.unlink()
.stat()
```

---

## `shutil`

```python
shutil.copy2()
shutil.copytree()
shutil.move()
shutil.rmtree()
shutil.disk_usage()
```

---

## Temporary Data

```python
tempfile.NamedTemporaryFile()
tempfile.TemporaryDirectory()
```

---

## Data Formats

```text
JSON → structured application/data exchange
CSV  → tabular datasets
ZIP  → compressed archive
```

---

# 🔥 Error → Solution Cheat Sheet

| Error                     | Usually means                       | First thing to check                  |
| ------------------------- | ----------------------------------- | ------------------------------------- |
| `FileNotFoundError`       | Path doesn't exist                  | Check path and `cwd`                  |
| `FileExistsError`         | Target already exists               | Use `exist_ok=True` where appropriate |
| `PermissionError`         | Access denied                       | Close file/check permissions/OneDrive |
| `IsADirectoryError`       | Expected file, got directory        | Use `is_file()`                       |
| `NotADirectoryError`      | Expected directory, got file        | Use `is_dir()`                        |
| `OSError`                 | General filesystem operation failed | Check path/state/permissions          |
| `UnicodeDecodeError`      | Wrong text encoding                 | Try correct encoding                  |
| `JSONDecodeError`         | Invalid JSON                        | Check JSON syntax                     |
| `shutil.rmtree()` problem | Folder may be protected/in use      | Verify target and permissions         |

---

# 🎯 MOST IMPORTANT THINGS TO REMEMBER

### 1. `pathlib`

> Used to work with paths cleanly.

### 2. `glob` vs `rglob`

```text
glob  → current directory
rglob → recursive
```

### 3. `unlink` vs `rmdir` vs `rmtree`

```text
unlink → file
rmdir  → empty directory
rmtree → directory + contents
```

### 4. Copy vs Move

```text
copy → original remains
move → original changes location
```

### 5. JSON

```text
dump → write
load → read
```

### 6. CSV

```text
writer → write
reader → read
```

### 7. Encoding

```python
encoding="utf-8"
```

### 8. Metadata

```python
path.stat()
```

### 9. Temporary data

```python
tempfile
```

### 10. Automation

`pathlib + shutil` can turn repetitive file-management work into an automated Python program.

---

# 🏆 FINAL LEARNING OUTCOME

After completing Topics **73–100**, I should be able to:

> **Navigate the filesystem, create and inspect paths, search directories, read file metadata, create/copy/move/delete files and folders, work with JSON and CSV data, create ZIP archives, handle text encoding, use temporary files, and build simple file-automation tools using Python.**

## Final Project

**Mini File Organizer**

This project demonstrates that I can take the individual File Handling concepts and combine them into a practical automation program.

---

# 🔁 HOW TO REVISE THIS SECTION

When revising, don't memorize all 28 programs.

Instead remember the **concept → method → purpose** relationship:

```text
Need a path?
→ Path()

Need to check?
→ exists(), is_file(), is_dir()

Need to create?
→ mkdir()

Need to search?
→ glob(), rglob()

Need information?
→ stat()

Need to rename/move?
→ rename()

Need to delete a file?
→ unlink()

Need to delete an empty folder?
→ rmdir()

Need to delete a folder tree?
→ shutil.rmtree()

Need to copy?
→ shutil.copy2(), copytree()

Need to move?
→ shutil.move()

Need temporary data?
→ tempfile

Need structured data?
→ JSON

Need tabular data?
→ CSV

Need compression?
→ zipfile

Need multilingual text?
→ UTF-8

Need automation?
→ pathlib + shutil
```

**This is the real revision sheet.** If I understand this final map, I don't need to memorize every program line-by-line.
