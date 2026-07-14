# 🧠 Simple Quiz Game

A command-line quiz game built with Python as part of my Python learning roadmap.

The game randomly selects questions from a question bank, presents multiple-choice options, validates user input, and tracks attempts until the game ends.

---

## ✨ Features

* Random question selection
* Multiple-choice answers
* Input validation
* No repeated questions in a session
* Displays the correct answer when the user is wrong
* Fixed number of attempts per game
* Play multiple rounds
* Graceful exit with `Ctrl + C`

---

## 🛠 Skills Practiced

* Lists
* Dictionaries
* Functions
* Random module
* Loops
* Input validation
* Tuple unpacking
* Index-based lookups
* Program state management

---

## 🚀 How To Run

Clone the repository:

```bash id="r1a2n3"
git clone https://github.com/ColdLogic7/simple-quiz-game.git
```

Enter the project folder:

```bash id="t4b5c6"
cd simple-quiz-game
```

Run the program:

```bash id="u7d8e9"
python Simple_quiz.py
```

---

## 📂 Project Structure

```text id="f1g2h3"
simple-quiz-game/
│
├── Simple_quiz.py
└── README.md
```

---

## 🎮 Example

```text id="i4j5k6"
Question: What is 2+2?

1. 2
2. 3
3. 4
4. 5

Enter Your Answer No. Here: 3

✨ Correct Answer
```

---

## 📚 What I Learned — Project 6

### Key Concepts

**List of dictionaries**

Each question stores its own data:

```python id="m7n8o9"
{
    "question": "...",
    "options": [...],
    "answer": "..."
}
```

This "list of records" pattern is common in real applications such as contact books, inventory systems, student records, and product catalogs.

---

**Returning multiple values**

Functions can return multiple values naturally:

```python id="p1q2r3"
return True, answer
```

and receive them with:

```python id="s4t5u6"
answer_check, answer = check_answer(...)
```

This makes related data easy to return together.

---

**Index-based answer validation**

Instead of comparing text strings directly, the program maps the user's numeric choice to an option index and compares it with the correct answer.

This approach is cleaner and less error-prone than string matching.

---

**Dynamic data-driven logic**

Rather than hardcoding the number of options:

```python id="v7w8x9"
options_len = len(question_pool[q_index]["options"])
```

The program adapts automatically to the actual data.

---

**Filtered random selection**

A nested `while True` loop keeps selecting random questions until it finds one that hasn't already been asked.

This pattern is useful whenever random choices must satisfy a condition.

---

**Game state separation**

One game session is handled inside `main()`, while replay logic is handled outside it.

This automatically resets attempts, question history, and other game state each time a new session starts.

---

### Lessons Worth Remembering

**Missing commas can create invisible bugs**

Python automatically joins adjacent string literals:

```python id="y1z2a3"
"Gold" "Iron"
```

becomes:

```python id="b4c5d6"
"GoldIron"
```

without any error message.

When reviewing lists of strings, always check for missing commas.

---

**Retry logic usually means a loop**

A single `if` only retries once.

When the requirement is:

> Keep trying until a condition is satisfied

the correct solution is usually a `while` loop.

---

**Validate both boundaries**

Instead of checking only one side:

```python id="e7f8g9"
value <= upper_bound
```

think about the complete range:

```python id="h1i2j3"
lower_bound <= value <= upper_bound
```

This prevents invalid values from slipping through.

---

## 💡 Biggest Takeaway

This was the first project where I started designing game mechanics myself instead of only following instructions.

Features such as:

* Random question selection
* Showing the correct answer
* Attempt tracking
* Preventing repeated questions

were decisions made during development rather than requirements given beforehand.

That shift—from simply implementing features to thinking about how a game should behave—was the biggest learning experience from this project.

---

## 🔮 Future Improvements

* Add a scoring system
* Difficulty levels
* Category-based questions
* Question loading from a JSON file
* High score tracking
* Timer for each question

---

## 📈 Roadmap Progress

**Projects Completed: 6 / 26**

✅ Number Guessing Game
✅ Simple Calculator
✅ Temperature Converter
✅ Password Generator
✅ Times Table Printer
✅ Simple Quiz Game

**Next Project:** Personal Diary CLI

---

## 👨‍💻 Author

**ColdLogic7**

Building Python projects and documenting lessons learned along the way.
