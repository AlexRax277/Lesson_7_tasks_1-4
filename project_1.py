
class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}

    def rate_hw(self, person, course, grade):
        if grade in range(10):
            if course in person.grades:
                person.grades[course] += [grade]
            else:
                person.grades[course] = [grade]

    def middle_grade(self):
        if len(sum(self.grades.values(), [])) != 0:
            middle_grade = sum(map(sum, self.grades.values())) / len(sum(self.grades.values(), []))
            return middle_grade
        return

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def __lt__(self, other):
        if type(self) != type(other):
            return 'Ошибка! Вы пытаетесь сравнить представителей разных классов!'
        return self.middle_grade() < other.middle_grade()


class Student(Human):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.finished_courses = []
        self.courses_in_progress = []

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            super().rate_hw(lecturer, course, grade)
        else:
            return 'Ошибка'

    def __str__(self):
        return super(Student, self).__str__() + \
               f'\nСредняя оценка за д/з: {self.middle_grade()} из 10.0' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
               f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'


class Mentor(Human):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


class Lecturer(Mentor):
    def __str__(self):
        return super(Lecturer, self).__str__() + f'\nСредняя оценка за лекции: {self.middle_grade()} из 10.0'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            super().rate_hw(student, course, grade)
        else:
            return 'Ошибка'


best_student = Student('Roy', 'Eman')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Python3']
best_student.finished_courses += ['Start in programming']

weak_student = Student('Biff', 'Stroganoff')
weak_student.courses_in_progress += ['Python']
weak_student.courses_in_progress += ['Python3']

strong_lecturer = Lecturer('Alfred', 'Pennyworth')
strong_lecturer.courses_attached += ['Python']
strong_lecturer.courses_attached += ['Python3']

so_so_lecturer = Lecturer('Steve', 'Rogers')
so_so_lecturer.courses_attached += ['Python']
so_so_lecturer.courses_attached += ['Python3']

nice_reviewer = Reviewer('Black', 'Jack')
nice_reviewer.courses_attached += ['Python']
nice_reviewer.courses_attached += ['Python3']

good_reviewer = Reviewer('Fred', 'Perry')
good_reviewer.courses_attached += ['Python']
good_reviewer.courses_attached += ['Python3']

nice_reviewer.rate_hw(best_student, 'Python', 9)
nice_reviewer.rate_hw(best_student, 'Python', 8)
nice_reviewer.rate_hw(best_student, 'Python3', 8)

good_reviewer.rate_hw(weak_student, 'Python', 2)
good_reviewer.rate_hw(weak_student, 'Python', 5)
good_reviewer.rate_hw(weak_student, 'Python3', 5)

best_student.rate_hw(strong_lecturer, 'Python', 8)
best_student.rate_hw(strong_lecturer, 'Python3', 9)

weak_student.rate_hw(so_so_lecturer, 'Python', 1)
weak_student.rate_hw(so_so_lecturer, 'Python3', 4)


# print(best_student)
# print(strong_lecturer.middle_grade())
# print(weak_student < best_student)


def middle_student_grade_course(*nickname_student, course):
    list_students = list(nickname_student)
    list_students_grades = []
    for student in list_students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            list_students_grades.append(student.grades[course])
        else:
            return f'Ошибка! Это фунция подсчета средних оценок только для класса {Student} в рамках одного курса. ' \
                   f'Проверьте правильность введенных данных!'
    middle_grade = sum(map(sum, list_students_grades)) / len(sum(list_students_grades, []))
    return f'Средняя оценка за домашние задания по всем студентам в рамках курса {course} - {middle_grade} из 10.0'


# x = middle_student_grade_course(best_student, weak_student, course='Python')
# print(x)


def middle_lecturer_grade_course(*nickname_lecturer, course):
    list_lecturers = list(nickname_lecturer)
    list_lecturers_grades = []
    for lecturer in list_lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            list_lecturers_grades.append(lecturer.grades[course])
        else:
            return f'Ошибка! Это фунция подсчета средних оценок только для класса {Lecturer} в рамках одного курса. ' \
                   f'Проверьте правильность введенных данных!'
    middle_grade = sum(map(sum, list_lecturers_grades)) / len(sum(list_lecturers_grades, []))
    return f'Средняя оценка за лекции всех лекторов в рамках курса {course} - {middle_grade} из 10.0'


# y = middle_lecturer_grade_course(strong_lecturer, so_so_lecturer, course='Python')
# print(y)
