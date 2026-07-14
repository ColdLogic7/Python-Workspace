# 📔 Personal Diary CLI

A command-line personal diary built with Python as part of my Python learning roadmap.

This project lets users write, view, and delete diary entries while introducing file handling, persistent storage, and basic data management.

---

## ✨ Features

* Write diary entries with today's date
* View all saved entries
* Delete entries by date
* Persistent storage using a text file
* Input validation
* Graceful exit with `Ctrl + C`

---

## 🛠 Skills Practiced

* File handling (`r`, `w`, `a`)
* `with open()`
* `os.path.exists()`
* String formatting
* List comprehensions
* Functions
* Input validation
* File rewriting
* Program structure

---

## 🚀 How To Run

Clone the repository:

```bash
git clone https://github.com/ColdLogic7/personal-diary-cli.git
```

Move into the project directory:

```bash
cd personal-diary-cli
```

Run the program:

```bash
python diary.py
```

---

## 📂 Project Structure

```text
personal-diary-cli/
│
├── diary.py
├── diary.txt
└── README.md
```

---

## 📚 What I Learned — Project 7

### Key Concepts

#### File modes

I learned when each file mode should be used:

* `'a'` → append without deleting existing data
* `'r'` → read existing data
* `'w'` → rewrite the entire file

Understanding the difference between these modes is essential for any program that works with files.

---

#### `with open()`

Using a context manager automatically closes files, even if an error occurs.

```python
with open(filename, "r") as file:
    ...
```

This has become my standard way of working with files.

---

#### Checking if a file exists

Before reading the diary, I verify that it actually exists.

```python
os.path.exists(DIARY_FILE)
```

This prevents the program from crashing the first time it runs.

---

#### Structuring plain text files

Instead of storing raw text continuously, I separated entries using a custom marker:

```text
===
```

This makes it possible to split the file back into individual diary entries.

---

#### Read → Filter → Rewrite

Deleting data from a text file isn't direct.

The process is:

1. Read all entries.
2. Remove the one that should be deleted.
3. Rewrite the updated content.

This pattern is common when working with flat files.

---

#### List Comprehensions

I used a list comprehension to both clean and filter diary entries:

```python
entries = [e.strip() for e in entries if e.strip()]
```

This removes unnecessary whitespace and ignores empty entries in one concise statement.

---

## ⚠️ Lessons Worth Remembering

* Validation should stop execution using `return` or `continue`, not just print a warning.
* Constants should have one responsibility. Avoid using data-format constants as display elements.
* Invisible whitespace bugs can silently corrupt file formats. When unsure, inspect strings with `repr()`.

---

## 💡 Biggest Takeaway

This project was my first experience working with persistent data stored in files.

More importantly, it taught me that struggling through an unfamiliar problem, researching solutions, and understanding them is part of becoming a programmer. The confidence gained from solving difficult problems is just as valuable as learning new Python syntax.

---

## 🔮 Future Improvements

* Edit existing diary entries
* Search entries by keyword
* Password protection
* Export diary entries
* Store data in JSON instead of plain text

---

## 📈 Roadmap Progress

**Projects Completed: 7 / 26**

✅ Number Guessing Game
✅ Simple Calculator
✅ Temperature Converter
✅ Password Generator
✅ Times Table Printer
✅ Simple Quiz Game
✅ Personal Diary CLI

**Next Project:** Expense Tracker

---

## 👨‍💻 Author

**ColdLogic7**

Learning Python through project-based practice and documenting lessons learned after every project.
