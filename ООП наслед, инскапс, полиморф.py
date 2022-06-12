class Student:
    students_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.students_list.append(self)


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in \
                self.courses_in_progress:
            if grade >= 10:
                return print('Оценка не может быть больше 10 баллов')
            else:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        grades_list = []
        grades_total = 0
        for grades_values in self.grades.values():
            grades_list = grades_list + grades_values
            #print(grades_list)
            for grades_el in grades_values:
                grades_total = grades_total + grades_el
        return grades_total / len(grades_list)

    def courses_in_progress_print(self):
        for course in self.courses_in_progress:
            return course

    def finished_courses_print(self):
        for course in self.finished_courses:
            return course

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades()}\
        \nКурсы в процессе изучения:{self.courses_in_progress_print()}\nЗавершенные курсы:{self.finished_courses_print()}"

    def compare_students(self, student_1, student_2): #функция для сравнения оценок студентов между собой
        if student_1.average_grades() > student_2.average_grades():
            print('ок')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}


    def average_grades(self):
        grades_list = []
        grades_total = 0
        for grades_values in self.grades.values():
            grades_list = grades_list+grades_values
            #print(grades_list)
            for grades_el in grades_values:
                grades_total = grades_total+grades_el
        return grades_total/len(grades_list)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades()}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

good_lecturer = Lecturer('Ivan', 'Ivanov')
good_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(good_lecturer, 'Python', 5)
best_student.rate_lecturer(good_lecturer, 'Python', 6)
best_student.rate_lecturer(good_lecturer, 'Python', 7)

# print(cool_reviewer)
# print(good_lecturer)
# print(best_student)

best_student_2 = Student('Jack', 'Johnes', 'male')
best_student_2.courses_in_progress += ['Finance']
best_student_2.finished_courses += ['Economics']

best_student_3 = Student('Maria', 'Mily', 'female')
best_student_3.courses_in_progress += ['Trial']
best_student_3.finished_courses += ['Law']

good_lecturer_2 = Lecturer('Boris', 'Petrov')
good_lecturer_2.courses_attached += ['Finance']

good_lecturer_3 = Lecturer('Vasiliy', 'Morozov')
good_lecturer_3.courses_attached += ['Trial']

cool_reviewer_2 = Reviewer('Jane', 'Ostin')
cool_reviewer_2.courses_attached += ['Finance']

cool_reviewer_3 = Reviewer('Mark', 'Twain')
cool_reviewer_3.courses_attached += ['Trial']

cool_reviewer_2.rate_hw(best_student_2, 'Finance', 8)
cool_reviewer_2.rate_hw(best_student_2, 'Finance', 8)
cool_reviewer_2.rate_hw(best_student_2, 'Finance', 8)

cool_reviewer_3.rate_hw(best_student_3, 'Trial', 6)
cool_reviewer_3.rate_hw(best_student_3, 'Trial', 6)
cool_reviewer_3.rate_hw(best_student_3, 'Trial', 6)

best_student_2.rate_lecturer(good_lecturer_2, 'Finance', 4)
best_student_2.rate_lecturer(good_lecturer_2, 'Finance', 5)
best_student_2.rate_lecturer(good_lecturer_2, 'Finance', 6)

best_student_3.rate_lecturer(good_lecturer_3, 'Trial', 7)
best_student_3.rate_lecturer(good_lecturer_3, 'Trial', 8)
best_student_3.rate_lecturer(good_lecturer_3, 'Trial', 9)

#print(best_student_2)
#print(best_student_3)
#print(good_lecturer_2)
#print(good_lecturer_3)
#print(cool_reviewer_2)
#print(cool_reviewer_3)

student_1 = input("Введите первого студента для сравнения:")
student_2 = input("Введите второго студента для сравнения:")
Student.compare_students(student_1, student_2)

# def average_rate_total(course, students_list):
#     course = input("Введите название курса:")
#     students_list = Student.students_list
#     for student in students_list:
#         if course in Student.courses_in_progress or course in self.finished_courses:




