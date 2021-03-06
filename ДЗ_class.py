class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {sum([sum(element) for element in self.grades.values()])/sum([len(element) for element in self.grades.values()])} \n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'
 # добавим возможность сравнения
    def __lt__(self, other):
        avg_st1 = sum([sum(element) for element in self.grades.values()]) / sum([len(element) for element in self.grades.values()])
        avg_st2 = sum([sum(element) for element in other.grades.values()]) / sum([len(element) for element in other.grades.values()])
        return avg_st1 < avg_st2

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {sum([sum(element) for element in self.grades.values()])/sum([len(element) for element in self.grades.values()])}'
    # добавим возможность сравнения
    def __lt__(self, other):
        avg_mt1 = sum([sum(element) for element in self.grades.values()]) / sum([len(element) for element in self.grades.values()])
        avg_mt2 = sum([sum(element) for element in other.grades.values()]) / sum([len(element) for element in other.grades.values()])
        return avg_mt1 < avg_mt2

class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)

# print(best_student.grades)


# оценка от студента
best_lecturer = Lecturer('Alpharius', 'Omegon')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['C++']

stup_student = Student('Magnus', 'Red', 'your_gender')
stup_student.courses_in_progress += ['Python']


# print(stup_student.courses_in_progress)

stup_student.rate_lec(best_lecturer, 'Python', 10)
stup_student.rate_lec(best_lecturer, 'Python', 9)
stup_student.rate_lec(best_lecturer, 'Python', 9)


# print(best_lecturer.grades)

# задание 3
print()

# print(stup_student)


print()
print(best_lecturer)
print()
# print(best_student)

# сравнение оценок студентов
best_student2 = Student('Leman', 'Russ', 'your_gender')
best_student2.courses_in_progress += ['Python']

cool_mentor.rate_hw(best_student2, 'Python', 10)
cool_mentor.rate_hw(best_student2, 'Python', 10)
cool_mentor.rate_hw(best_student2, 'Python', 8)
# сравнение оценок по студентам
print(best_student2)
print(best_student > best_student2)

best_lecturer2 = Lecturer('Lucas', 'Wolf')
best_lecturer2.courses_attached += ['Python']

stup_student = Student('Magnus', 'Red', 'your_gender')
stup_student.courses_in_progress += ['Python']

# print(stup_student.courses_in_progress)

stup_student.rate_lec(best_lecturer2, 'Python', 10)
stup_student.rate_lec(best_lecturer2, 'Python',7)
stup_student.rate_lec(best_lecturer2, 'Python', 9)

# сравнение оценок по преподам
print(best_lecturer2)
print(best_lecturer > best_lecturer2)
print()
