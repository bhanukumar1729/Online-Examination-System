# Online Examination System

A simple, lightweight console-based Online Examination System written in Python. This project is designed as a practical assignment for demonstrating Git and GitHub workflows.

---

## 📌 Project Overview

The **Online Examination System** provides a clean command-line interface for conducting multiple-choice examinations. It prompts candidates for their details, presents questions one by one with validation, computes their score, and outputs a complete performance report.

---

## 🚀 Features

- **Candidate Login:** Simple authentication required before the exam begins (Demo credentials: username `admin`, password `password123`).
- **Candidate Registration:** Prompts the examinee for their name before starting.
- **Multiple-Choice Questions:** Formatted questions with 4 selectable choices (`A`, `B`, `C`, `D`).
- **Input Validation:** Rejects invalid option entries and allows retries without breaking. Case-insensitive (accepts both uppercase and lowercase letters).
- **Automated Scoring:** Calculates total questions, correct answers, wrong answers, and overall percentage.
- **Pass/Fail Evaluation:** Automatically assesses whether the candidate passed (threshold: 50%).
- **Easy Customization:** Easily add, edit, or remove questions directly in the `QUESTIONS` list inside `main.py`.

---

## 📁 Project Structure

```text
Online-Examination-System/
│
├── main.py          # Main application script containing exam logic and questions
├── .gitignore       # Git ignore rules for Python bytecode and editor files
└── README.md        # Project documentation and usage guide
```

---

## ⚙️ Prerequisites & Installation

- **Python 3.x** installed on your system.

To check if Python is installed, run:
```bash
python --version
# or on Windows
py --version
```

---

## 💻 How to Run the Application

1. Open your terminal or command prompt in the project directory.
2. Run the application:
   ```bash
   python main.py
   ```
   *(On Windows systems using the Python launcher, you can also use `py main.py`)*

3. Follow the on-screen prompts:
   - Log in using the demo credentials (Username: `admin`, Password: `password123`).
   - Enter your name.
   - Type your selected option (`A`, `B`, `C`, or `D`) for each question and press Enter.
   - View your final score summary!

---

## ✏️ How to Add or Modify Questions

Open `main.py` and locate the `QUESTIONS` list. You can append new questions using the following template:

```python
{
    "question": "Your question text here?",
    "options": [
        "A. Option 1",
        "B. Option 2",
        "C. Option 3",
        "D. Option 4"
    ],
    "answer": "A"  # Correct choice letter (A, B, C, or D)
}
```

---

## 🛠️ Git & GitHub Practical Workflow

This project is prepared for Git and GitHub practical exercises. Common commands to use during your lab:

### 1. Check repository status
```bash
git status
```

### 2. Stage all project files
```bash
git add .
```

### 3. Commit your changes
```bash
git commit -m "Initial commit: Add Online Examination System project"
```

### 4. Create and switch to a new feature branch
```bash
git checkout -b feature/add-questions
```

### 5. Link to your GitHub repository and push
```bash
git remote add origin https://github.com/<your-username>/Online-Examination-System.git
git branch -M main
git push -u origin main
```

---

## 📝 License
This project is open-source and free to use for educational and learning purposes.
