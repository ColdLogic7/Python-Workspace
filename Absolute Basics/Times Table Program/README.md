# 🧮 Times Table Printer

A command-line Times Table Printer built with Python as part of my Python learning roadmap.

This project generates neatly formatted multiplication tables for any number and allows users to choose how far the table should extend. The focus of this project was learning formatted output, dynamic spacing, and clean function design.

---

## 📖 About The Project

Multiplication tables are simple to generate, but displaying them cleanly for any input size requires thoughtful formatting.

This application allows users to:

* Select any number
* Choose how far the table should go
* Display results in a properly aligned format
* Generate multiple tables in one session

The project helped me practice user input handling, dynamic formatting, and separating responsibilities between functions.

---

## ✨ Features

* Generate multiplication tables for any integer
* Custom table range
* Default range of 10 when no value is entered
* Dynamic alignment for large numbers
* Clean and readable output formatting
* Input validation
* Multiple table generation in one session
* Graceful exit using `Ctrl + C`

---

## 🛠 Skills Practiced

During this project, I practiced:

* Functions
* Loops
* Integer conversion
* Input validation
* Default values using `or`
* Dynamic string formatting
* f-strings
* Column alignment
* Program structure
* Single Responsibility Principle (SRP)

---

## 🚀 How To Run

Clone the repository:

```bash id="a1b2c3"
git clone https://github.com/ColdLogic7/times-table-printer.git
```

Move into the project directory:

```bash id="d4e5f6"
cd times-table-printer
```

Run the program:

```bash id="g7h8i9"
python Times_table_printer.py
```

---

## 🎮 Example Usage

```text id="m4n5o6"
🧩 Which number's table do you want: 12

🚀 How far should this table go [default: 10]: 15

🍰 Your Desired Table -

12 x  1 =  12
12 x  2 =  24
12 x  3 =  36
...
12 x 15 = 180
```

---

# 📚 What I Learned — Project 5

This project looked simple at first, but it taught me valuable lessons about formatting, scalability, and clean program structure.

---

## ✅ Good Decisions

### Matching The Loop Structure To The Problem

Initially, I considered whether nested loops were needed.

After thinking through the problem, I realized that a single loop was sufficient because only the multiplier changes while the table number remains constant.

```python id="p1q2r3"
for i in range(1, end_numb + 1):
```

This reinforced an important principle:

> Don't add complexity unless the problem actually requires it.

---

### Reusing The Default Value Pattern

I reused a pattern learned in Project 4:

```python id="s4t5u6"
input(...).strip() or '10'
```

If the user presses Enter without typing anything, the program automatically uses a default value.

This approach is concise and avoids unnecessary conditional statements.

---

### Dynamic Column Width

The most important improvement in this project was calculating column width dynamically:

```python id="v7w8x9"
max_result = table_numb * end_numb
result_width = len(str(max_result))
```

Instead of guessing how wide the output should be, the program determines it based on the largest possible result.

This ensures alignment remains correct regardless of the table size.

Examples:

* Small tables remain clean
* Large tables remain aligned
* No formatting adjustments are needed

This same technique can be applied to:

* Reports
* Data tables
* CLI dashboards
* Financial summaries
* Spreadsheet exports

---

### Clean Function Separation

Each function has a single responsibility:

* `times_table()` → gets the table number
* `how_far()` → gets the maximum multiplier
* `align_formatting()` → formats and displays results

This separation makes the program easier to understand, test, and maintain.

---

## 🔮 Future Improvements

* Print multiple tables at once
* Export tables to a text file
* Add colorized terminal output
* Generate addition, subtraction, and division tables
* Display tables in a boxed format
* Save recently generated tables

---

## 📈 Roadmap Progress

**Projects Completed: 5 / 26**

✅ Number Guessing Game
✅ Simple Calculator
✅ Temperature Converter
✅ Password Generator
✅ Times Table Printer

**Next Project:** Simple Quiz App

---

## 👨‍💻 Author

**ColdLogic7**

Learning Python through project-based practice and documenting lessons learned after every project.

---

## ⭐ Support

If you found this project interesting, consider giving it a star on GitHub and following my learning journey.
