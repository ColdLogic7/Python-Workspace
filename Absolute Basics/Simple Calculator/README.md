# 🧮 Simple Calculator

A command-line calculator built with Python as part of my Python learning roadmap.

This project allows users to perform basic arithmetic operations while practicing important Python concepts such as functions, exception handling, input validation, and clean code organization.

---

## 📖 About The Project

The calculator supports the four basic mathematical operations:

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)

The program validates user input, handles errors gracefully, and allows multiple calculations in a single session.

---

## ✨ Features

* Supports all four basic arithmetic operations
* Accepts both integers and decimal numbers
* Input validation using `try/except`
* Handles division by zero safely
* Re-prompts for invalid operations
* Rounds results to 2 decimal places
* Allows repeated calculations
* Gracefully exits with `Ctrl + C`

---

## 🛠 Skills Practiced

During this project, I practiced:

* Functions
* Constants
* `float()`
* `try/except`
* `ValueError`
* `KeyboardInterrupt`
* Returning values from functions
* Using `None` as a special return value
* Input validation
* DRY (Don't Repeat Yourself) principle

---

## 🚀 How To Run

Clone the repository:

```bash
git clone https://github.com/your-username/simple-calculator.git
```

Move into the project directory:

```bash
cd simple-calculator
```

Run the program:

```bash
python Calculator.py
```

---

## 📂 Project Structure

```text
simple-calculator/
│
├── Calculator.py
└── README.md
```

---

## 🎮 Example Usage

```text
- Welcome to our simple calculator program -

Operations Menu : ['+', '-', '*', '/']

Enter first number here: 10
Choose an operation: *
Enter second number here: 5

Result: 50.0
```

---

## ✅ Verification Checklist

The following tests were completed successfully:

* Accepts decimal numbers (e.g. `3.14`)
* Rejects invalid numeric input (`abc`)
* Handles division by zero without crashing
* Supports all four operations correctly
* Re-prompts after invalid operation input
* Displays results after every calculation
* Allows multiple calculations using `y`
* Exits correctly using `n`
* Handles `Ctrl + C` gracefully

---

## 📚 Key Lessons Learned

### 1. DRY Principle

Instead of creating separate functions for every number input, one reusable function with a `prompt` parameter keeps the code cleaner.

### 2. Using `None` Effectively

Returning `None` from the calculation function allows error handling to remain separate from calculation logic.

### 3. Proper Exception Handling

Using `try/except` prevents the program from crashing when users enter invalid input.

### 4. Float Conversion

Using `float()` directly allows both whole numbers and decimal numbers to be accepted.

### 5. Graceful Program Exit

Handling `KeyboardInterrupt` provides a better user experience when exiting the application.

---

## 🔮 Future Improvements

* Add calculation history
* Show the last 5 calculations before exiting
* Support exponent (`^`) operations
* Support square root calculations
* Create a GUI version using Tkinter
* Add scientific calculator features

---

## 📈 Progress

**Python Roadmap Progress:** 2 / 26 Projects Complete ✅

Completed Projects:

1. Number Guessing Game
2. Simple Calculator

Next Project:

➡️ Temperature Converter

---

## 👨‍💻 Author

**ColdLogic7**

Learning Python through project-based practice and building one project at a time.

---

## ⭐ Support

If you found this project useful or interesting, consider giving it a star on GitHub.
