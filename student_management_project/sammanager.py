""""""
# List to hold student records
students = []

# Function to add a new student record with name, age, and marks
def add_student():
    """"""
    name = input("\nEnter student name: ")
    age = int(input("Enter student age: "))
    marks = int(input("Enter the amount of marks (1-100): "))

    student = {'name': name, 'age': age, 'marks': marks}
    students.append(student)
    print(f"\nStudent {name} added successfully!")

# Function to display all student records
def display_students():
    """"""
    if students:
        print("\nStudent Records:")
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")
    else:
        print("No students to display.")

# Function to delete a student record by name
def delete_student():
    """"""
    name = input("\nEnter student to be deleted: ")

    global students
    students = [student for student in students if student['name'].lower() != name.lower()]
    print(f"Student with name {name} has been deleted.")

def main():
    """"""
    while True:
        print("\n1. Add student")
        print("2. Display student")
        print("3. Delete student")
        user = input("Enter 1-3: ")
        match user:
            case "1": add_student()
            case "2": display_students()
            case "3": delete_student()

main()
