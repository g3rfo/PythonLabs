students = {"Student_01": [9, 11, 3, 12, 11, 12, 9, 8, 9, 3, 8, 6],
            "Student_02": [5, 9, 7, 7, 10, 7, 7, 7, 7, 11, 3, 11],
            "Student_03": [12, 2, 12, 7, 12, 9, 7, 9, 9, 11, 3, 6],
            "Student_04": [7, 8, 4, 12, 7, 6, 1, 6, 6, 5, 6, 3],
            "Student_05": [8, 6, 10, 6, 11, 9, 1, 11, 9, 12, 12, 9],
            "Student_06": [8, 8, 11, 7, 12, 8, 6, 2, 7, 11, 9, 10],
            "Student_07": [8, 8, 11, 12, 6, 11, 12, 6, 4, 9, 1, 8],
            "Student_08": [11, 10, 8, 5, 10, 5, 8, 10, 9, 12, 11, 6],
            "Student_09": [3, 12, 9, 9, 9, 2, 8, 7, 6, 6, 11, 11],
            "Student_10": [10, 8, 9, 6, 6, 11, 10, 4, 6, 8, 3, 9]}

def data_print(students):
    print()
    for key in students:
        print(key,":", students[key])

def data_add(students, key, grade):
    if key in students:
        students[key].append(grade)
        print(key,":", students[key])
    else:
        print("<--Student is not found-->")

def data_remove(students, key, grade):
    if key in students:
        if grade in students[key]:
            students[key].remove(grade)
            print(key, ":", students[key])
        else:
            print("<--Grade is not found-->")
    else:
        print("<--Student is not found-->")

def data_sort(students, key):
    if key in students:
        students[key].sort()
        print(key, ":", students[key])
    else:
        print("<--Student is not found-->")

def average_grade_of_student(students, key):
    if key in students:
        average = sum(students[key]) / len(students[key])
        return average
    else:
        print("Student is not found")

def average_grade_of_group(students):
    total_average = 0
    for key in students:
        total_average += sum(students[key]) / len(students[key])
    group_average = total_average / len(students)
    return group_average

def greater_than_average_print(students):
    group_average = average_grade_of_group(students)
    print("\nGroup average :", group_average)
    for key in students:
        personal_average = average_grade_of_student(students, key)
        if personal_average > group_average:
            print(key,":", personal_average)

number = 1
while True:
    if number == 1:
        print("\n<1>To print a list of students"
            "\n<2>To add student grades"
            "\n<3>To remove student grades"
            "\n<4>To sort student grades"
            "\n<5>To calculate student's personal average grades"
            "\n<6>To calculate group average grades"
            "\n<0>To exit")
    answer = int(input("\nChoose an action:"))
    if answer == 0:
        break;
    elif answer == 1:
        data_print(students)
    elif answer == 2:
        student = input("Enter student name:")
        grade = int(input("Enter grade to add:"))
        data_add(students, student, grade)
    elif answer == 3:
        student = input("Enter student name:")
        grade = int(input("Enter grade to remove:"))
        data_remove(students, student, grade)
    elif answer == 4:
        student = input("Enter student name:")
        data_sort(students, student)
    elif answer == 5:
        student = input("Enter student name:")
        print(student,":",average_grade_of_student(students, student))
    elif answer == 6:
        greater_than_average_print(students)
    else:
        print("\nInvalid input")
    number += 1