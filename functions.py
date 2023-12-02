import json


def check_fitness(student_data, profession):
    """
    Возвращает словарь соответствия студента профессии
    """
    # Какие вообще языки знает студент
    skills = set(student_data["skills"])

    # Какие языки не знает студент, но они необходимы для профессии
    lacks = profession.difference(skills)

    # Какие языки из требуемых для профессии знает студент
    cross = profession.intersection(skills)

    # Вычисление процента годности для профессии
    fit_percent = round(len(cross) / len(profession) * 100)

    rezults = {
        "has": list(cross),
        "lacks": list(lacks),
        "fit_percent": fit_percent
    }

    return rezults


def get_student_by_pk(students_data, pk):
    """
    Получает словарь с данными студента по его pk
    """
    student_data = {
        "pk": students_data[pk - 1]["pk"],
        "full_name": students_data[pk - 1]["full_name"],
        "skills": students_data[pk - 1]["skills"]
    }

    return student_data


def get_profession_by_title(title, job):
    """
    Получает словарь с инфо о профе по названию
    """
    i = 0
    for el in title:
        if job == title[i]["title"]:
            profession = title[i]["skills"]
        i += 1

    return set(profession)


def count_student(content):
    """
    Определяет количество студетов
    """
    for el in content:
        count = el["pk"]

    return count


def load_students(file_name):
    """
    Загружает список студентов из файла
    """
    with open(file_name, encoding='utf-8') as file:
        content = file.read()
        students_data = json.loads(content)

    return students_data


def check_professions(content, job):
    """
    Определяет наличие введенной пользователем профессии
    """
    count = False
    for el in content:
        if el["title"] == job:
            count = True

    return count


def load_professions(file_name):
    """
    Загружает список профессий из файла
    """
    with open(file_name, encoding='utf-8') as file:
        content = file.read()
        professions_data = json.loads(content)

    return professions_data


def output_skills(student_data):
    """
    Вывод навыков студента
     """
    print(f'Студент: {student_data["full_name"]}')
    print(f'Знает: {', '.join(student_data["skills"])}\n')


def output_rezults(rezults, student_data):
    """
    Вывод результатов
    """
    print(f'Пригодность: {rezults["fit_percent"]}%')
    if len(rezults["has"]) == 0:
        print(f'{student_data["full_name"]} не знает ни одного языка, необходимого для этой профессии.')
    else:
        print(f'{student_data["full_name"]} знает {', '.join(rezults["has"])}')

    if len(rezults["lacks"]) == 0:
        print(f'{student_data["full_name"]} знает все языки, необходимые для этой профессии.')
    else:
        print(f'{student_data["full_name"]} не знает {', '.join(rezults["lacks"])}')
