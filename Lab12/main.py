import json

students = [
    {"name": "Marina", "surname": "Baranova", "grades": {"Python": 83, "Numerical Methods": 79, "Algorithms": 90, "MMDO": 85, "IT-Business": 78}},
    {"name": "Sofia", "surname": "Baranova", "grades": {"Python": 88, "Numerical Methods": 81, "Algorithms": 93, "MMDO": 80, "IT-Business": 75}},
    {"name": "Yulia", "surname": "Dyachenko", "grades": {"Python": 78, "Numerical Methods": 85, "Algorithms": 87, "MMDO": 76, "IT-Business": 82}},
    {"name": "Polina", "surname": "Zavhorodnia", "grades": {"Python": 90, "Numerical Methods": 82, "Algorithms": 91, "MMDO": 88, "IT-Business": 80}},
    {"name": "Timothy", "surname": "Ivzhenko", "grades": {"Python": 79, "Numerical Methods": 77, "Algorithms": 84, "MMDO": 83, "IT-Business": 81}},
    {"name": "Mykyta", "surname": "Lenda", "grades": {"Python": 85, "Numerical Methods": 80, "Algorithms": 89, "MMDO": 82, "IT-Business": 76}},
    {"name": "Ivan", "surname": "Rozhchenko", "grades": {"Python": 70, "Numerical Methods": 78, "Algorithms": 75, "MMDO": 72, "IT-Business": 69}},
    {"name": "Daryna", "surname": "Rudenko", "grades": {"Python": 91, "Numerical Methods": 85, "Algorithms": 89, "MMDO": 86, "IT-Business": 84}},
    {"name": "Yulia", "surname": "Sidelnik", "grades": {"Python": 88, "Numerical Methods": 90, "Algorithms": 94, "MMDO": 92, "IT-Business": 86}},
    {"name": "Oleksandr", "surname": "Shmat", "grades": {"Python": 79, "Numerical Methods": 81, "Algorithms": 84, "MMDO": 78, "IT-Business": 80}}
]


with open("StudentsData.json", "wt") as file:
    json.dump(students, file , indent=4)

with open("StudentsAverages.json", "wt") as file:
    json.dump([], file , indent=4)


def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found")


def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def output_start_file_data(filename):
    data = load_data(filename)
    if data:
        for student in data:
            print(f"Ім'я: {student['name']}")
            print(f"Прізвище: {student['surname']}")
            print("Оцінки:")
            for subject, grade in student["grades"].items():
                print(f"  {subject}: {grade}")
            print('-' * 20)
    else:
        print("Список студентів порожній.")


def output_end_file_data(filename):
    data = load_data(filename)
    if data:
        for student in data:
            print(f"Ім'я: {student['name']}")
            print(f"Прізвище: {student['surname']}")
            print(f"Середня оцінка: {student['average grade']}")
            print('-' * 20)
    else:
        print("Список студентів порожній.")


def add_student(name, surname, grades, filename):
    data = load_data(filename)

    for student in data:
        if student['name'] == name and student['surname'] == surname:
            print(f"Студент {name} {surname} вже є у списку.")
            return

    data.append({"name": name, "surname": surname, "grades": grades})
    save_data(data, filename)
    print(f"Студента {name} {surname} додано.")


def remove_student(name, surname, filename):
    data = load_data(filename)
    new_data = [student for student in data if student['surname'] != surname or student['name'] != name]

    if len(new_data) < len(data):
        save_data(new_data, filename)
        print(f"Студента {name} {surname} видалено.")
    else:
        print(f"Студента {name} {surname} не знайдено.")


def calculate_student_average(name, surname, filename):
    data = load_data(filename)
    for student in data:
        if student["surname"] == surname and student["name"] == name:
            average_grade = sum(student["grades"].values()) / len(student["grades"])
            print(f"Студент: {student['name']} {student['surname']}")
            print(f"Середня оцінка: {average_grade:.2f}")
            return average_grade
    print(f"Студента {name} {surname} не знайдено.")
    return None


def save_averages_to_file(averages_filename, name, surname, average_grade):
    averages_data = load_data(averages_filename)
    averages_data.append({"name": name, "surname": surname, "average grade": average_grade})

    save_data(averages_data, averages_filename)


def calculate_group_average(filename):
    data = load_data(filename)
    if data:
        total_sum = 0
        total_count = 0
        for student in data:
            total_sum += sum(student["grades"].values())
            total_count += len(student["grades"])
        average_grade = total_sum / total_count
        print(f"Середня оцінка групи: {average_grade:.2f}")

        print("Студенти з оцінками вище середньої:")
        for student in data:
            student_average = sum(student["grades"].values()) / len(student["grades"])
            if student_average > average_grade:
                print(f"{student['name']} {student['surname']} - середня оцінка: {student_average:.2f}")
    else:
        print("Список студентів порожній.")


start_file = "StudentsData.json"
end_file = "StudentsAverages.json"

number = 0
while True:
    if number == 0:
        print("\n<1>Вивести список студентів з даними"
              "\n<2>Додати студента"
              "\n<3>Видалити студента"
              "\n<4>Порахувати середню оцінку студента"
              "\n<5>Порахувати середню оцінку групи і вивести студентів з вищою"
              "\n<0>Завершити програму")
        number += 1

    answer = int(input("\nВиберіть дію: "))
    if answer == 0:
        output_end_file_data(end_file)
        break
    elif answer == 1:
        output_start_file_data(start_file)
    elif answer == 2:
        name = input("Введіть ім'я: ")
        surname = input("Введіть прізвище: ")
        grades = {}
        subjects = ["Python", "Numerical Methods", "Algorithms", "MMDO", "IT-Business"]
        for subject in subjects:
            grade = float(input(f"Введіть оцінку з {subject}: "))
            grades[subject] = grade
        add_student(name, surname, grades, start_file)
    elif answer == 3:
        name = input("Введіть ім'я студента для видалення: ")
        surname = input("Введіть прізвище студента для видалення: ")
        remove_student(name, surname, start_file)
    elif answer == 4:
        name = input("Введіть ім'я студента для обчислення середньої оцінки: ")
        surname = input("Введіть прізвище студента для обчислення середньої оцінки: ")
        average_grade = calculate_student_average(name, surname, start_file)
        if average_grade is not None:
            save_averages_to_file(end_file, name, surname, average_grade)
    elif answer == 5:
        calculate_group_average(start_file)
    else:
        print("Помилка введення")

print("Програму завершено")