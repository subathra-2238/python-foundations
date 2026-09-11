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
