"""
Online Examination System
A simple console-based examination application built with Python.
Designed for Git and GitHub practical demonstrations.
"""

# Question Bank
# Questions can easily be added, updated, or removed from this list.
QUESTIONS = [
    {
        "question": "What is the primary purpose of Git?",
        "options": [
            "A. Compiling code",
            "B. Version control system",
            "C. Hosting databases",
            "D. Designing user interfaces"
        ],
        "answer": "B"
    },
    {
        "question": "Which command is used to record changes to the repository in Git?",
        "options": [
            "A. git push",
            "B. git add",
            "C. git commit",
            "D. git checkout"
        ],
        "answer": "C"
    },
    {
        "question": "Which of the following is an immutable data type in Python?",
        "options": [
            "A. List",
            "B. Dictionary",
            "C. Set",
            "D. Tuple"
        ],
        "answer": "D"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": [
            "A. func",
            "B. def",
            "C. function",
            "D. define"
        ],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for in computer systems?",
        "options": [
            "A. Central Processing Unit",
            "B. Central Performance Utility",
            "C. Computer Personal Unit",
            "D. Control Processing User"
        ],
        "answer": "A"
    }
]


# Demo Login Credentials
DEMO_USERNAME = "admin"
DEMO_PASSWORD = "password123"


def display_banner():
    """Displays a welcoming banner for the examination system."""
    print("=" * 55)
    print("        ONLINE EXAMINATION SYSTEM        ")
    print("=" * 55)


def login():
    """Authenticates the user using demo credentials."""
    print("\n--- Candidate Login ---")
    print("(Demo Credentials: username = admin, password = password123)")
    while True:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        if username == DEMO_USERNAME and password == DEMO_PASSWORD:
            print("Login successful!\n")
            return True
        print("Invalid username or password. Please try again.\n")


def get_student_info():
    """Prompts the user to enter their name."""
    while True:
        name = input("Enter candidate name: ").strip()
        if name:
            return name
        print("Candidate name cannot be empty. Please enter your name.")


def get_user_answer():
    """
    Prompts the user for an answer and validates input.
    Accepts options: A, B, C, or D (case-insensitive).
    """
    valid_choices = ["A", "B", "C", "D"]
    while True:
        choice = input("Your answer (A/B/C/D): ").strip().upper()
        if choice in valid_choices:
            return choice
        print("Invalid choice! Please enter A, B, C, or D.")


def conduct_exam(questions):
    """Conducts the exam and calculates the score."""
    score = 0
    total = len(questions)

    print(f"\nExam Started! Total Questions: {total}\n" + "-" * 55)

    for index, item in enumerate(questions, start=1):
        print(f"\nQuestion {index} of {total}:")
        print(item["question"])
        for option in item["options"]:
            print(f"  {option}")

        user_choice = get_user_answer()
        if user_choice == item["answer"]:
            score += 1

    return score, total


def display_results(candidate_name, score, total):
    """Displays the final examination result summary."""
    incorrect = total - score
    percentage = (score / total) * 100 if total > 0 else 0
    passed = percentage >= 50

    print("\n" + "=" * 55)
    print("            EXAM RESULT SUMMARY            ")
    print("=" * 55)
    print(f"Candidate Name    : {candidate_name}")
    print(f"Total questions   : {total}")
    print(f"Correct answers   : {score}")
    print(f"Incorrect answers : {incorrect}")
    print(f"Final score       : {score}/{total} ({percentage:.1f}%)")
    print(f"Status            : {'PASSED' if passed else 'FAILED'}")
    print("=" * 55)


def main():
    """Main execution function."""
    display_banner()
    login()
    candidate_name = get_student_info()
    score, total = conduct_exam(QUESTIONS)
    display_results(candidate_name, score, total)
    print("\nThank you for taking the exam!\n")


if __name__ == "__main__":
    main()
