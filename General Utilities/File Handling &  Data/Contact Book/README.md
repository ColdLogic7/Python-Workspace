# 📒 Contact Book

A command-line Contact Book built with Python as part of my Python learning roadmap.

This project allows users to add, search, update, view, and delete contacts while storing data permanently using JSON.

---

## ✨ Features

* Add new contacts
* Search contacts by name
* View all saved contacts
* Update existing contacts
* Delete contacts with confirmation
* Store data in a JSON file
* Case-insensitive search
* Input validation
* Graceful exit with `Ctrl + C`

---

## 🛠 Skills Practiced

* JSON file handling
* Dictionaries & Lists
* Functions
* File abstraction
* Data validation
* String formatting
* Exception handling
* Program structure

---

## 🚀 How To Run

Clone the repository:

```bash id="d8f1g2"
git clone https://github.com/ColdLogic7/contact-book.git
```

Move into the project directory:

```bash id="h3j4k5"
cd contact-book
```

Run the program:

```bash id="l6m7n8"
python Contact_Book.py
```

---

## 📂 Project Structure

```text id="p9q1r2"
contact-book/
│
├── Contact_Book.py
├── contacts.json
└── README.md
```

---

## 📚 What I Learned — Project 9

### Key Concepts

* **Working with JSON**

  Learned to use `json.dump()` and `json.load()` for storing and retrieving structured data. Unlike CSV, JSON naturally represents objects with named fields.

* **Abstracting file operations**

  Created dedicated `read_json()` and `write_json()` functions so every part of the program uses the same file-handling logic.

* **Safe defaults**

  Returning an empty list when the JSON file doesn't exist allows the program to work correctly on its first run without extra setup.

* **Load → Modify → Save**

  Instead of appending data directly, I learned to load contacts into memory, modify them, and write the updated list back to the file.

* **Updating dictionaries directly**

  Modified contact information using dictionary references inside a list, making updates simple and efficient.

* **Normalizing input**

  Used `str.title()` to store names in a consistent format, regardless of how the user enters them.

* **Consistent searching**

  Applied case-insensitive partial matching across search, update, and delete features to create a better user experience.

* **Confirmation before deletion**

  Added a confirmation prompt before permanently deleting contacts, following a common user interface pattern.

---

## ⚠️ Lessons Worth Remembering

* Flags that track whether something was found should be initialized before the loop and only updated when a match is found.
* Read data from a file once, store it in a variable, and reuse it instead of reading the same file multiple times.
* Trust well-designed helper functions. Avoid repeating checks that are already handled inside them.

---

## 💡 Biggest Takeaway

This project helped me think more about **program design** than individual lines of code.

Separating file handling into reusable functions, keeping data consistent at input time, and recognizing my habit of jumping straight to solutions taught me that good programming starts with understanding the problem before writing code.

---

## 🔮 Future Improvements

* Search by phone number or email
* Sort contacts alphabetically
* Favorite contacts
* Import/Export contacts
* Duplicate contact detection
* Birthday reminders

---

## 📈 Roadmap Progress

**Projects Completed: 9 / 26**

✅ Number Guessing Game
✅ Simple Calculator
✅ Temperature Converter
✅ Password Generator
✅ Times Table Printer
✅ Simple Quiz Game
✅ Personal Diary CLI
✅ Expense Tracker
✅ Contact Book

**Next Project:** Web Scraper

---

## 👨‍💻 Author

**ColdLogic7**

Learning Python through project-based practice and documenting lessons learned after every project.
