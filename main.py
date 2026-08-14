##python

students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number:")
        course = input("Enter course:")

        student = {
            "name": name,
            "roll_no": roll_no,
            "course": course

        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")  
        else:
            print("\nStudent Records:")
            for student in students:
                print(
                    f"Name: {student['name']}, "
                    f"Roll No: {student['roll_no']}, "
                    f"Course: {student['course']}"
                )    

    elif choice == "3":
        print("thankyou for uding the student management system!")
        break

    else:
        print("invalide choice. please try again.") 
