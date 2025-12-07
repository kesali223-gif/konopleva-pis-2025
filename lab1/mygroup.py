groupmates = [
    {
        "name": "Ольга",
        "surname": "Брух",
        "exams": ["Информатика", "1С", "Web"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Виктория",
        "surname": "Анисимова",
        "exams": ["История", "СиАОД", "УИТ"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Артём",
        "surname": "Чалый",
        "exams": ["Философия", "АИС", "КТП"],
        "marks": [5, 3, 5]
    },
    {
        "name": "Егор",
        "surname": "Медведев",
        "exams": ["Математика", "Физика", "Программирование"],
        "marks": [5, 4, 3]
    },
    {
        "name": "Максим",
        "surname": "Гладышев",
        "exams": ["Английский", "БД", "Web"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Ирина",
        "surname": "Семёнова",
        "exams": ["Французкий", "СИИ", "ОБРИС"],
        "marks": [3, 5, 4]
    }
]


def print_students(students):
    max_name_len = max(len(s["name"]) for s in students) + 2
    max_surname_len = max(len(s["surname"]) for s in students) + 2
    max_exams_len = max(len(str(s["exams"])) for s in students) + 2
    max_marks_len = max(len(str(s["marks"])) for s in students) + 2

    header = f"{'Имя'.ljust(max_name_len)}{'Фамилия'.ljust(max_surname_len)}{'Экзамены'.ljust(max_exams_len)}{'Оценки'.ljust(max_marks_len)}"
    print(header)
    print("-" * len(header)) 

    for student in students:
        name = student["name"].ljust(max_name_len)
        surname = student["surname"].ljust(max_surname_len)
        exams = str(student["exams"]).ljust(max_exams_len)
        marks = str(student["marks"]).ljust(max_marks_len)
        print(f"{name}{surname}{exams}{marks}")

def filter_and_print(students, threshold):
    """Фильтрует студентов по среднему баллу > threshold и выводит их в таблице."""
    filtered = []
    for student in students:
        avg_mark = sum(student["marks"]) / len(student["marks"])
        if avg_mark > threshold:
            filtered.append(student)
    
    if filtered:
        print(f"\nСтуденты со средним баллом выше {threshold}:")
        print_students(filtered)
    else:
        print(f"\nНет студентов со средним баллом выше {threshold}.")

if __name__ == "__main__":
    print("Все студенты:")
    print_students(groupmates)
    
    try:
        threshold = float(input("\nВведите пороговое значение среднего балла: "))
        filter_and_print(groupmates, threshold)
    except ValueError:
        print("Ошибка: введите корректное число (например, 4.0).")