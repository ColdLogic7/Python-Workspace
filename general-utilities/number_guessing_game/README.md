# 🔢 Number Guessing Game
## Overview

This is a classic console-based **Number Guessing Game** written in Python. The objective is to guess a random number selected by the computer, which is between 1 and 100, within a maximum of **10 attempts**.

The game provides immediate feedback ("too small" or "too big") after each guess to help you narrow down the range.

## 🛠️ Technology Used

- **Python 3**: The entire game logic is built using standard Python and its random module.
  
## 📜 Game Rules

The rules are simple and displayed at the start of every game session:
1. The computer chooses a secret number between **1 and 100** .
2. You have exactly **10 chances** to guess the correct number.
3. After each attempt, you will receive a hint: **"too big" or "too small"**.
4. The game ends when you guess the number correctly or run out of attempts.
5. Input validation is included to ensure you enter a valid number.
   
## 🚀 How to Run

### Prerequisites

You only need **Python 3** installed on your system.

### Running the Script
1. Save your code into a file named, for example, number_guesser.py.
2. Open your terminal or command prompt.
3. Navigate to the directory where you saved the file.
4. Execute the game using the Python interpreter:
   
   `bash python number_guesser.py`
   
## Example Gameplay

 👋 Hello, Welcome to my Number Guessing Game!
 Rules:
   1. Choose a number between 1 and 100.
   2. I will also choose a number between 1 and 100.
   3. You have 10 chances to guess my number.
   4. After each guess, I'll give you a hint.
   5. Enjoy!

 Enter your number: 50

 It is too big , think a little bit smaller number........

 Enter your number: 25

 It is too small , think a little bit bigger number........

 Enter your number: 37

 Congratulation , I don't believe that you guess the exact number which is :37
 