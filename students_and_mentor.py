class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}
        Student.student_list.append(self)

    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade_student(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades_student:
            grades_count += len(self.grades_student[grade])
            grades_sum += sum(self.grades_student[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0


    def __gt__(self, other):
        if not isinstance(other, Student):
            return
        return self._average_grade_student() > other._average_grade_student()
    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self._average_grade_student() < other._average_grade_student()
    def __eq__(self, other):
        if not isinstance(other, Student):
            return
        return self._average_grade_student() == other._average_grade_student()


    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {round(self._average_grade_student(), 1)}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}\n")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_lecturer = {}
        Lecturer.lecturer_list.append(self)


    def _average_grade_lecturer(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades_lecturer:
            grades_count += len(self.grades_lecturer[grade])
            grades_sum += sum(self.grades_lecturer[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0


    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self._average_grade_lecturer() > other._average_grade_lecturer()
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self._average_grade_lecturer() < other._average_grade_lecturer()
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self._average_grade_lecturer() == other._average_grade_lecturer()

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {round(self._average_grade_lecturer(), 1)}\n")


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_student:
                student.grades_student[course] += [grade]
            else:
                student.grades_student[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")                                                                   


student_first = Student('Federico', 'Valverde', 'your_gender')
student_first.courses_in_progress += ['Python']
student_first.courses_in_progress += ['Git']
student_first.courses_in_progress += ['Django']
student_first.finished_courses += ['Введение в программирование']

student_second = Student('Kevin', 'De Bruyne', 'your_gender')
student_second.courses_in_progress += ['Python']
student_second.courses_in_progress += ['Git']
student_second.courses_in_progress += ['Django']
student_second.finished_courses += ['Введение в программирование']

reviewer_first = Reviewer('David', 'Bacham')
reviewer_first.courses_attached += ['Python']
reviewer_first.courses_attached += ['Git']
reviewer_first.courses_attached += ['Django']

reviewer_second = Reviewer('Steven', 'Gerrard')
reviewer_second.courses_attached += ['Python']
reviewer_second.courses_attached += ['Git']
reviewer_second.courses_attached += ['Django']

lecturer_first = Lecturer('Jurgen', 'Klopp')
lecturer_first.courses_attached += ['Python']
lecturer_first.courses_attached += ['Git']
lecturer_first.courses_attached += ['Django']

lecturer_second = Lecturer('Xabi', 'Alonso')
lecturer_second.courses_attached += ['Python']
lecturer_second.courses_attached += ['Git']
lecturer_second.courses_attached += ['Django']

reviewer_first.rate_hw_student(student_first, 'Python', 7)
reviewer_first.rate_hw_student(student_first, 'Git', 8)
reviewer_first.rate_hw_student(student_first, 'Django', 8)

reviewer_first.rate_hw_student(student_second, 'Python', 8)
reviewer_first.rate_hw_student(student_second, 'Git', 9)
reviewer_first.rate_hw_student(student_second, 'Django', 8)

student_first.rate_hw_lecturer(lecturer_first, 'Django', 10)
student_first.rate_hw_lecturer(lecturer_first, 'Python', 6)
student_first.rate_hw_lecturer(lecturer_first, 'Git', 9)

student_second.rate_hw_lecturer(lecturer_second, 'Git', 8)
student_second.rate_hw_lecturer(lecturer_second, 'Django', 8)
student_second.rate_hw_lecturer(lecturer_second, 'Python', 9)

print(reviewer_first)
print(reviewer_second)
print(lecturer_first)
print(lecturer_second)
print(student_first)
print(student_second)


if student_first > student_second:
    print(f'Средняя оценка {student_first.name} {student_first.surname} больше, чем средняя оценка {student_second.name} {student_second.surname}')
elif student_first < student_second:
    print(f'Средняя оценка {student_first.name} {student_first.surname} меньше, чем средняя оценка {student_second.name} {student_second.surname}')
else:
    print(f'Средняя оценка {student_first.name} {student_first.surname} равна средней оценке {student_second.name} {student_second.surname}')
print()

if lecturer_first > lecturer_second:
    print(f'Средняя оценка {lecturer_first.name} {lecturer_first.surname} больше, чем средняя оценка {lecturer_second.name} {lecturer_second.surname}')
elif lecturer_first < lecturer_second:
    print(f'Средняя оценка {lecturer_first.name} {lecturer_first.surname} меньше, чем средняя оценка {lecturer_second.name} {lecturer_second.surname}')
else:
    print(f'Средняя оценка {lecturer_first.name} {lecturer_first.surname} равна средней оценке {lecturer_second.name} {lecturer_second.surname}')
print()


def students_average_grade_course(student_list, course):
        list_average_all = []
        for student in student_list:
            for cours_name, average in student.grades_student.items():
                if course == cours_name:
                    sum_average = sum(average) / len(average)
                    list_average_all.append(sum_average)
        sum_average_all = (sum(list_average_all) / len(list_average_all))
        print(f"Курс студента: {course}\n"
              f"Cредняя оценка за домашние задания: {round(sum_average_all, 1)}\n") 

def lecturer_average_grade_course(lecturer_list, course):
        list_average_all = []
        for lecturer in lecturer_list:
            for cours_name, average in lecturer.grades_lecturer.items():
                if course == cours_name:
                    sum_average = sum(average) / len(average)
                    list_average_all.append(sum_average)
        sum_average_all = (sum(list_average_all) / len(list_average_all))
        print(f"Курс лектора: {course}\n"
              f"Cредняя оценка за лекции: {round(sum_average_all, 1)}\n")     

students_average_grade_course(Student.student_list, 'Git')
students_average_grade_course(Student.student_list, 'Python')
students_average_grade_course(Student.student_list, 'Django')

lecturer_average_grade_course(Lecturer.lecturer_list, 'Git')
lecturer_average_grade_course(Lecturer.lecturer_list, 'Python')
lecturer_average_grade_course(Lecturer.lecturer_list, 'Django')