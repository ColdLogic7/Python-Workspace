# 🎓 Student Grade Report

A command-line Student Grade Report built with Python as part of my Python learning roadmap.

This project manages student subjects and marks, calculates grades, and generates a report using JSON for persistent data storage.

---

## ✨ Features

* Add subjects and marks
* Calculate grades automatically
* View student grade report
* Update subject marks
* Delete subjects
* Identify strongest and weakest subjects
* Check overall pass status
* Store data using JSON
* Input validation
* Confirmation before deletion

---

## 🛠 Skills Practiced

* Functions
* JSON file handling
* Dictionaries & Lists
* `all()` and generator expressions
* `max()` / `min()` with `key=lambda`
* Exception handling
* Data validation
* File abstraction
* Tuple returns
* Program structure

---

## 🚀 How To Run

Clone the repository:

```bash
git clone https://github.com/ColdLogic7/student-grade-report.git
```

Move into the project directory:

```bash
cd student-grade-report
```

Run the program:

```bash
python Student_Grade_Report.py
```

---

## 📂 Project Structure

```text
student-grade-report/
│
├── Student_Grade_Report.py
├── student_data.json
└── README.md
```

---

## 📚 What I Learned — Project 10

### Key Concepts

**Pure calculation functions**

`calculate_grade()` takes input, performs the calculation, and returns the result without handling files or printing output.

This was my cleanest example so far of the **Single Responsibility Principle**.

---

**`all()` with generator expressions**

```python
all(item['status'] == 'Pass' for item in file_data)
```

This provides a clean way to check whether every student/subject record satisfies a condition.

---

**`max()` and `min()` with `key=lambda`**

```python
max(file_data, key=lambda x: x['marks'])
```

I learned how to find the strongest and weakest subjects based on a dictionary field without manually writing sorting logic.

---

**Handling `JSONDecodeError`**

I added handling for corrupted or empty JSON files instead of only handling missing files.

This introduced me to more defensive file handling.

---

**Default confirmation with `or`**

```python
input(...).strip().lower() or 'y'
```

Pressing Enter automatically uses `'y'`.

This reused the default-input pattern from Project 4 in a new situation.

---

**Building in the right order**

I followed a more disciplined development process:

1. Build `calculate_grade()`
2. Build file operations
3. Add individual features
4. Test each part
5. Connect everything together

This reduced the chance of building multiple features on top of a broken foundation.

---

## ⚠️ Lessons Worth Remembering

* **Read once, use the variable:** avoid calling `read_json()` multiple times when the data is already loaded.
* **Keep validation consistent:** if the same field is validated in multiple functions, use one validation function so the rules cannot disagree.
* **Follow Python naming conventions:** function names should consistently use `snake_case`.
* **Handle realistic failure cases:** files can exist but still contain invalid or corrupted data.

---

## 💡 Biggest Takeaway

The biggest change from the earlier projects is that file handling has started to become **infrastructure rather than the main problem**.

In Project 7, reading, writing, and deleting file data felt like the difficult part.

By Project 10, those patterns became familiar enough that I could focus on what to do with the data instead.

That is the biggest lesson from Stage 3:

> **Stop thinking only about how to handle the data and start thinking about what you can build with it.**

---

## 🔮 Future Improvements

* Calculate overall percentage and GPA
* Add multiple students
* Generate printable reports
* Add subject-wise statistics
* Export reports to CSV/PDF
* Convert the project to an object-oriented design

---

## 📈 Roadmap Progress

**Projects Completed: 10 / 26**

✅ Number Guessing Game
✅ Simple Calculator
✅ Temperature Converter
✅ Password Generator
✅ Times Table Printer
✅ Simple Quiz Game
✅ Personal Diary CLI
✅ Expense Tracker
✅ Contact Book
✅ Student Grade Report

**Next Project:** Continue to the next project in the roadmap.

---

## 👨‍💻 Author

**ColdLogic7**

Learning Python through project-based practice and documenting lessons learned after every project.
