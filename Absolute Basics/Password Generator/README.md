# 🔐 Password Generator

A command-line Password Generator built with Python as part of my Python learning roadmap.

This project generates random passwords using different character sets, allowing users to choose between lowercase letters, uppercase letters, digits, symbols, or a mixed combination of all character types.

---

## 📖 About The Project

Creating secure passwords manually is difficult and often leads to predictable choices.

This application solves that problem by generating random passwords based on user preferences while introducing important Python concepts such as modules, dictionaries, dynamic menus, and random string generation.

---

## ✨ Features

* Generate passwords of custom length
* Choose from multiple character sets:

  * Lowercase letters
  * Uppercase letters
  * Digits
  * Symbols
  * Mixed (all character types)
* Default option when no character type is entered
* Dynamic menu generation using a dictionary
* Input validation for password length
* Generate multiple passwords in one session
* Graceful exit using `Ctrl + C`

---

## 🛠 Skills Practiced

During this project, I practiced:

* Dictionaries
* Loops
* Functions
* Constants
* Input validation
* Python's `string` module
* Python's `random` module
* `random.choices()`
* String joining with `''.join()`
* Default values using `or`
* Single Responsibility Principle (SRP)
* Dynamic menu generation

---

## 🚀 How To Run

Clone the repository:

```bash id="p9u6c1"
git clone https://github.com/ColdLogic7/password-generator.git
```

Move into the project directory:

```bash id="f5w7x2"
cd password-generator
```

Run the program:

```bash id="h4n8m3"
python password_generator.py
```

---

## 📂 Project Structure

```text id="q1r2s3"
password-generator/
│
├── password_generator.py
└── README.md
```

---

## 🎮 Example Usage

```text id="k8j2d5"
🍔 PASSWORD MENU :

L — Lowercase
U — Uppercase
D — Digits
S — Symbols
M — Mixed

🧐 Choose CHARACTERS TYPE in MENU [default: mixed]: M

🤔 Choose PASSWORD LENGTH here [greater than 16]: 20

    🍜 Your Password Generated: J3!kT7@bX9#pL2&vW8$q
```

---

## ✅ Verification Checklist

The following scenarios were tested successfully:

* Valid password length generates a password correctly
* Empty character-type input defaults to Mixed mode
* Invalid character-type input re-prompts the user
* Invalid numeric input is rejected cleanly
* Password length validation works correctly
* Password generation works for all menu options
* Multiple passwords can be generated in one session
* Program exits correctly with `n`
* Program exits gracefully using `Ctrl + C`

---

# 📚 What I Learned — Project 4

This project was less about passwords and more about learning reusable Python patterns that appear in many real-world programs.

---

## ✅ New Concepts and Patterns

### The `string` Module

Python provides ready-made character sets:

```python id="s7h4k2"
string.ascii_lowercase
string.ascii_uppercase
string.digits
string.punctuation
```

Instead of manually typing alphabets and symbols, I learned to use Python's built-in collections.

**Lesson:** Whenever I need a set of characters, I should check the `string` module before creating my own.

---

### `random.choices()` + `''.join()`

Password generation follows a common pattern:

```python id="r4f7n1"
characters = random.choices(pool, k=length)
password = ''.join(characters)
```

First generate a list of random characters, then join them into a single string.

This same pattern is used in:

* Password generators
* Captcha generators
* Token generators
* Verification code systems
* Random identifier creation

---

### Default Values Using `or`

One useful shortcut I learned:

```python id="z9t2w4"
choice = input(...).strip().upper() or 'M'
```

If the user simply presses Enter, Python treats the empty string as False and automatically uses `'M'`.

This eliminates the need for extra `if` statements.

---

### Dynamic Menus From Dictionaries

Instead of hardcoding menu options, I stored them in a dictionary and displayed them dynamically.

```python id="n5x8p6"
for key, value in PASS_MENU.items():
    print(key, value)
```

Adding a new menu option automatically updates the display.

This introduced me to an important software design idea:

> One source of truth.

The data and the display stay synchronized automatically.

---

### Separating Display From Input

I split responsibilities between functions:

* `show_pass_menu()` → displays the menu
* `char_type()` → gets user input

Initially I displayed the menu only once and quickly realized users couldn't easily remember the available options.

That discomfort helped me understand why separating responsibilities makes programs easier to use and maintain.

---

## ⚠️ Mistakes Worth Remembering

### Inconsistent Messages

At one point:

* Prompt said "greater than 16"
* Validation checked `< 16`
* Error message mentioned a different value

The same rule existed in multiple places, making it easy for them to become inconsistent.

A better solution:

```python id="g3m9v8"
MIN_LENGTH = 16
```

Then use the constant everywhere.

**Lesson:** If the same value appears multiple times, it probably belongs in a constant.

---

### Arbitrary Constraints

I changed the minimum password length several times without a clear reason.

That taught me an important question:

> Why this number?

Before adding validation rules, I should be able to explain why the rule exists.

If I can't justify the number or restriction, it's probably not a good constraint.

---

## 💡 Biggest Takeaway

This project taught me that many programming problems can be solved by combining small reusable patterns:

* Build a character pool
* Generate a list of random values
* Join them into a string
* Validate input early
* Keep display and logic separate

The more of these patterns I learn, the easier future projects become.

---

## 🔮 Future Improvements

* Guarantee at least one character from each selected category
* Allow selecting multiple character types simultaneously
* Add password strength analysis
* Copy generated password to clipboard
* Save generated passwords to a file
* Generate secure passphrases
* Add a graphical interface using Tkinter

---

## 📈 Roadmap Progress

**Projects Completed: 4 / 26**

✅ Number Guessing Game
✅ Simple Calculator
✅ Temperature Converter
✅ Password Generator

**Next Project:** Times Table Printer

---

## 👨‍💻 Author

**ColdLogic7**

Learning Python through project-based practice and documenting lessons learned after every project.

---

## ⭐ Support

If you found this project interesting, consider giving it a star on GitHub and following my learning journey.
