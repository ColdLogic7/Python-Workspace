# 💰 Expense Tracker

A command-line Expense Tracker built with Python as part of my Python learning roadmap.

This project allows users to record daily expenses, organize them by category, view summaries, and manage records using CSV files. It introduced me to working with structured data and persistent storage.

---

## ✨ Features

* Add expenses with category, amount, and description
* Store data in a CSV file
* View all recorded expenses
* View expense summary by category
* Delete expenses
* Dynamic table formatting
* Input validation
* Graceful exit with `Ctrl + C`

---

## 🛠 Skills Practiced

* CSV file handling
* `csv.DictWriter` & `csv.DictReader`
* File handling
* Dictionaries
* List operations
* Dynamic table formatting
* Exception handling
* Program structure

---

## 🚀 How To Run

Clone the repository:

```bash
git clone https://github.com/ColdLogic7/expense-tracker.git
```

Move into the project directory:

```bash
cd expense-tracker
```

Run the program:

```bash
python Exp_Tracker.py
```

---

## 📂 Project Structure

```text
expense-tracker/
│
├── Exp_Tracker.py
├── expense.csv
└── README.md
```

---

## 📚 What I Learned — Project 8

### Key Concepts

* **Working with CSV files**

  Learned to use `csv.DictWriter` and `csv.DictReader`, where each row is represented as a dictionary using column names as keys.

* **Writing CSV files correctly**

  Using `newline=''` prevents extra blank lines when writing CSV files on Windows.

* **Writing headers only once**

  Combined `os.path.exists()` with `os.path.getsize()` to detect whether the CSV file needs its header before appending new data.

* **Safe dictionary access**

  Used:

  ```python
  row.get("Amount(₹)", 0.0)
  ```

  instead of direct indexing to avoid errors when a key is missing.

* **Dictionary-based accumulation**

  Used:

  ```python
  category_totals.get(category, 0.0) + amount
  ```

  to build category totals without extra condition checks.

* **Pythonic file handling**

  Used `try/except FileNotFoundError` to safely access files instead of checking their existence beforehand.

* **Deleting by index**

  Learned to remove items using:

  ```python
  del rows[index]
  ```

  before rewriting the updated CSV file.

* **Dynamic table formatting**

  Calculated column widths from the actual data so tables remain properly aligned regardless of content size.

---

## ⚠️ Lessons Worth Remembering

* Use `+=` when accumulating values inside loops. Using `=` replaces the total instead of adding to it.
* Anything that depends on an open file should stay inside the `with open()` block.
* If display logic feels complicated, the program structure probably needs simplifying.
* A safe workflow for file operations is:

  > Read → Process in Memory → Write Back

---

## 💡 Biggest Takeaway

This project reinforced a reliable pattern for working with files:

* Open files safely.
* Read everything into memory.
* Process the data.
* Write changes back only once.

This workflow makes file-based programs simpler, safer, and easier to maintain.

---

## 🔮 Future Improvements

* Edit existing expenses
* Search expenses by category or date
* Monthly expense reports
* Export summaries
* Budget tracking
* Charts and graphs

---

## 📈 Roadmap Progress

**Projects Completed: 8 / 26**

✅ Number Guessing Game
✅ Simple Calculator
✅ Temperature Converter
✅ Password Generator
✅ Times Table Printer
✅ Simple Quiz Game
✅ Personal Diary CLI
✅ Expense Tracker

**Next Project:** Contact Book

---

## 👨‍💻 Author

**ColdLogic7**

Learning Python through project-based practice and documenting lessons learned after every project.
