from functions import load_students, get_student_by_pk, load_professions, get_profession_by_title
from functions import check_fitness, count_student, check_professions, output_rezults, output_skills


def main():
    number = int(input('Введите номер студента: '))

    # Получаем список студентов и содержимое файла 'students.json'
    students_data = load_students('students.json')

    # Проверяем есть ли такой студент
    if number > count_student(students_data):
        print('У нас нет такого студента!')
        quit()

    # Получаем словарь с данными студента
    student_data = get_student_by_pk(students_data, number)

    job = input(f'Выберите специальность для оценки студента {student_data["full_name"]}: ').title()

    # Получаем список профессий и содержимое файла 'professions.json'
    professions_data = load_professions('professions.json')

    # Проверяем наличие введенной пользователем профессии
    if check_professions(professions_data, job) is False:
        print('У нас нет такой специальности!')
        quit()

    # Выводим навыки студента
    output_skills(student_data)

    # Получаем словарь с инфо о профе по названию
    profession = get_profession_by_title(professions_data, job)

    # Подсчет результа соответствия студента профессии
    rezults = check_fitness(student_data, profession)

    # Выводим результаты
    output_rezults(rezults, student_data)

#lxcvjlxkc
if __name__ == '__main__':
    main()
