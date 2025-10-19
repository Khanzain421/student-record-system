# -----------------------------------------
# Student Record System (File-Based)
# Author: Zain's Python Project
# -----------------------------------------

import os

# File to store student data
FILENAME = "students.txt"


# ---------- Utility Functions ----------
def read_students():
    """Read all students from file and return a list of dicts."""
    students = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    roll, name, age, grade = parts
                    students.append({
                        "roll": roll,
                        "name": name,
                        "age": age,
                        "grade": grade
                    })
    return students


def write_students(students):
    """Write all students to file."""
    with open(FILENAME, "w") as file:
        for s in students:
            file.write(f"{s['roll']},{s['name']},{s['age']},{s['grade']}\n")


# ---------- Core Functions ----------
def add_student():
    students = read_students()
    roll = input("Enter Roll Number: ").strip()

    # Check if roll already exists
    for s in students:
        if s["roll"] == roll:
            print("❌ Student with this roll number already exists!")
            return

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    grade = input("Enter Grade: ").strip()

    students.append({
        "roll": roll,
        "name": name,
        "age": age,
        "grade": grade
    })

    write_students(students)
    print("✅ Student added successfully!")


def view_students():
    students = read_students()
    if not students:
        print("No student records found.")
        return

    print("\n------ All Students ------")
    print("{:<10} {:<20} {:<10} {:<10}".format("Roll", "Name", "Age", "Grade"))
    print("-" * 50)
    for s in students:
        print("{:<10} {:<20} {:<10} {:<10}".format(
            s["roll"], s["name"], s["age"], s["grade"]))
    print()


def search_student():
    roll = input("Enter Roll Number to Search: ").strip()
    students = read_students()
    for s in students:
        if s["roll"] == roll:
            print("\n✅ Student Found:")
            print(f"Roll: {s['roll']}")
            print(f"Name: {s['name']}")
            print(f"Age: {s['age']}")
            print(f"Grade: {s['grade']}")
            return
    print("❌ Student not found!")


def update_student():
    roll = input("Enter Roll Number to Update: ").strip()
    students = read_students()

    for s in students:
        if s["roll"] == roll:
            print("Enter new details (press Enter to keep old value):")
            name = input(f"New Name ({s['name']}): ").strip() or s["name"]
            age = input(f"New Age ({s['age']}): ").strip() or s["age"]
            grade = input(f"New Grade ({s['grade']}): ").strip() or s["grade"]

            s["name"], s["age"], s["grade"] = name, age, grade
            write_students(students)
            print("✅ Student record updated successfully!")
            return

    print("❌ Student not found!")


def delete_student():
    roll = input("Enter Roll Number to Delete: ").strip()
    students = read_students()
    new_students = [s for s in students if s["roll"] != roll]

    if len(new_students) == len(students):
        print("❌ Student not found!")
        return

    write_students(new_students)
    print("✅ Student deleted successfully!")


# ---------- Main Menu ----------
def main_menu():
    while True:
        print("\n===== STUDENT RECORD SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")


# ---------- Run Program ----------
if __name__ == "__main__":
    main_menu()
1