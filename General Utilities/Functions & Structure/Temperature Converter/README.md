# 🌡️ Temperature Converter

A command-line Temperature Converter built with Python as part of my Python learning roadmap.

This project converts temperatures between Celsius, Fahrenheit, and Kelvin while validating physically impossible temperatures such as values below absolute zero.

---

## 📖 About The Project

The application allows users to:

* Select a source temperature unit
* Select a target temperature unit
* Enter a temperature value
* Convert between Celsius, Fahrenheit, and Kelvin
* Reject temperatures below absolute zero
* Perform multiple conversions in one session

The goal of this project was not only to practice temperature conversion formulas, but also to strengthen function design, input validation, and program structure.

---

## ✨ Features

* Supports Celsius (°C), Fahrenheit (°F), and Kelvin (K)
* Converts between all unit combinations
* Validates user input
* Rejects physically impossible temperatures
* Clean output formatting
* Retry mechanism for invalid temperatures
* Repeat conversions without restarting the program
* Graceful exit with `Ctrl + C`

---

## 🛠 Skills Practiced

During this project, I practiced:

* Functions
* Nested loops
* Function parameters
* Input validation
* Floating-point arithmetic
* Conditional logic
* Early returns
* Program flow control
* Single Responsibility Principle (SRP)
* Exception handling (`ValueError`, `KeyboardInterrupt`)

---

## 🚀 How To Run

Clone the repository:

```bash
git clone https://github.com/your-username/temperature-converter.git
```

Move into the project directory:

```bash
cd temperature-converter
```

Run the program:

```bash
python temperature_converter.py
```

---

## 📂 Project Structure

```text
temperature-converter/
│
├── temperature_converter.py
└── README.md
```

---

## 🎮 Example Usage

```text
🍸 Units Menu: 'C' - Celsius, 'F' - Fahrenheit, 'K' - Kelvin

📌 Pick a Unit as SOURCE unit: C
📌 Pick a Unit as TARGET unit: F

🌡️ Enter TEMPERATURE VALUE for Conversion: 100

🍨 Your Desired Result: 212.0 °F
```

---

## ✅ Verification Checklist

The following scenarios were tested successfully:

* Valid conversions between all supported units
* Decimal temperature values accepted correctly
* Invalid unit selections are rejected and re-prompted
* Invalid numeric input does not crash the program
* Temperatures below absolute zero are rejected
* Converting to the same unit returns the original value
* Multiple conversions work correctly in one session
* Program exits cleanly with `n`
* Program exits gracefully using `Ctrl + C`

---

# 📚 What I Learned In Project 3

This project taught me more about program structure than mathematical formulas.

---

## ✅ New Concepts Applied Correctly

### Unit-Aware Validation

The `absolute_zero()` function accepts both the temperature value and the source unit because the same numeric value can be valid in one unit and impossible in another.

Examples:

* `-200°C` → valid
* `-200K` → impossible

This reinforced the importance of passing enough context into a function instead of relying on assumptions.

---

### Nested Loops For Dependent Retries

When a temperature is invalid, the program asks only for a new temperature value instead of forcing the user to reselect units.

I solved this by using an inner `while True` loop inside the main application loop.

This introduced me to the concept of different retry scopes within CLI programs.

---

### Early Return To Simplify Logic

Instead of letting conversion logic continue unnecessarily, I handled the special case first:

```python
if from_unit == to_unit:
    return float(value)
```

This removes complexity and reduces the risk of bugs caused by variables that may never be assigned.

---

### Separating Conversion From Display

I created a dedicated function for displaying results instead of printing directly inside the conversion logic.

This follows the Single Responsibility Principle:

* `convert()` → performs calculations
* `substitute_result()` → handles presentation

Each function owns one responsibility.

---

## ⚠️ Mistakes That Taught Me Important Lessons

### String Comparison Bugs

One bug came from using:

```python
'k'
```

instead of:

```python
'K'
```

Python didn't raise any error.

The condition simply never matched.

Lesson:

> Always normalize user input and keep comparisons consistent throughout the codebase.

---

### Thinking About Physics Instead Of Logic

I initially focused on the concept of absolute zero rather than the implementation details.

Questions I should always ask:

* What exact value should be used?
* Should I use `<`, `<=`, `==`, or another operator?

Writing the intended rule as a comment first makes validation logic easier to implement correctly.

---

### Hidden Risk: Undefined Variables

A function that returns a variable must guarantee that variable exists on every execution path.

Otherwise Python may eventually raise errors such as:

```python
NameError
```

Using early returns reduces this risk and makes logic easier to reason about.

---

## 💡 Biggest Takeaway

The most valuable lesson from this project wasn't temperature conversion.

It was learning to mentally trace a complete execution path before running the code.

Every bug I encountered came from skipping that step:

* String comparison mistakes
* Incorrect validation boundaries
* Potentially undefined variables

Before executing code, I now try to walk through one complete example from start to finish and ask:

> "What happens next?"

That habit will be useful in every future Python project.

---

## 🔮 Future Improvements

* Add conversion history
* Save previous conversions to a file
* Support scientific notation
* Create a GUI version using Tkinter
* Add batch conversions
* Package the converter as a reusable Python module

---

## 📈 Roadmap Progress

**Projects Completed: 3 / 26**

✅ Number Guessing Game
✅ Simple Calculator
✅ Temperature Converter

**Next Project:** Password Generator

---

## 👨‍💻 Author

**ColdLogic7**

Learning Python through project-based practice and documenting lessons learned after every project.

---

## ⭐ Support

If you found this project interesting, consider giving it a star on GitHub.
