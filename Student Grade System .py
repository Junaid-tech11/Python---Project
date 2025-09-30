#initial dictionary:
student_grades = {}


#Add a new_student
def add_student(name, grade):
    student_grades[name] = grade
    #[Ali] = 100
    print(f"Added {name} with a {grade}")
    #Added Ali with a 100

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks are updated {grade}")
        
    else:
        print(f"{name} is not found")
        
#Delete a Student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!")
        

#view all student
def display_all_student():
    if student_grades:
        for name, grades in student_grades.items():
            print(f"{name} and {grades}")
            
    else:
        print("No Students found/Added")
        
def main():
    while True:
        print('\n Student Grades Management System')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit!")
        
        choice = int(input("Enter Your choice " ))
        if choice == 1:
            name = input("Enter student name = ")
            grade = input("Enter Student grade =")
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter Student name =")
            grade = input("Enter student grade =")
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter student name =")
            delete_student (name)
            
        elif choice ==  4:
            display_all_student()
            
        elif choice == 5:
            print("Closing the program....")
            break
        else:
            print("Invalid input!!")
main()
