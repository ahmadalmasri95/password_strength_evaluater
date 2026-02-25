# Password Strength Evaluator 🛡️

A Python-based security tool that performs a multi-layered analysis of password strength. This script goes beyond simple length checks by evaluating complexity, identifying common sequences, and cross-referencing passwords against known leaked wordlists.

## 🚀 Features

* **Length Verification:** Checks if the password meets the minimum security standard (8+ characters).
* **Complexity Analysis:** Identifies the presence of Uppercase, Lowercase, Numbers, and Special Characters.
* **Pattern Recognition:** Detects common keyboard sequences and predictable strings (e.g., "123", "qwerty").
* **Wordlist Cross-Referencing:** Compares the input against a local database of leaked or common passwords (`test_file.txt`).
* **Security Categorization:** Assigns a "Password Class" based on the variety of character types used.

## 🛠️ How It Works

The script evaluates the "Entropy" of a password by checking how many character pools it draws from. 



The more character types (Uppercase + Lowercase + Symbols + Numbers) and the longer the string, the higher the mathematical resistance to brute-force attacks.

## 📋 Requirements

* Python 3.x
* A text file named `test_file.txt` in the same directory (containing a list of common passwords, one per line).

## 💻 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmadalmasri95/password_strength_evaluater.git
  
