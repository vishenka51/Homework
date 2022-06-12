class Student:
    students_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.students_list.append(self)


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

    def __lt__(self, other):
        student_1_average_grades = self.average_grades()
        student_2_average_grades = other.average_grades()
        return student_1_average_grades < student_2_average_grades
    def __gt__(self, other):
        student_1_average_grades = self.average_grades()
        student_2_average_grades = other.average_grades()
        return student_1_average_grades > student_2_average_grades
    def __eq__(self, other):
        student_1_average_grades = self.average_grades()
        student_2_average_grades = other.average_grades()
        return student_1_average_grades == student_2_average_grades

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturers_list = []
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
        Lecturer.lecturers_list.append(self)

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

    def __lt__(self, other):
        lecturer_1_average_grades = self.average_grades()
        lecturer_2_average_grades = other.average_grades()
        return lecturer_1_average_grades < lecturer_2_average_grades
    def __gt__(self, other):
        lecturer_1_average_grades = self.average_grades()
        lecturer_2_average_grades = other.average_grades()
        return lecturer_1_average_grades > lecturer_2_average_grades
    def __eq__(self, other):
        lecturer_1_average_grades = self.average_grades()
        lecturer_2_average_grades = other.average_grades()
        return lecturer_1_average_grades == lecturer_2_average_grades
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

print(best_student_2)
print("--------------")
print(best_student_3)
print("--------------")
print(good_lecturer_2)
print("--------------")
print(good_lecturer_3)
print("--------------")
print(cool_reviewer_2)
print("--------------")
print(cool_reviewer_3)
print("--------------")

is_lt = print(best_student_2 < best_student_3)
is_gt = print(best_student_2 > best_student_3)
is_eq= print(best_student_2 == best_student_3)
print("--------------")
is_lt = print(good_lecturer < good_lecturer_3)
is_gt = print(good_lecturer > good_lecturer_3)
is_eq= print(good_lecturer == good_lecturer_3)
print("--------------")
print(Student.students_list[0])

def average_mark_hw(students_list, course_hw):
    mark_list=[]
    mark_sum = 0
    for student in students_list:
     if course_hw in student.grades.keys():
        for marks in student.grades.values():
            for mark in marks:
                mark_list.append(mark)
    mark_list_len = len(mark_list)
    for mark in mark_list:
        mark_sum= mark_sum+mark
    return print(mark_sum/mark_list_len)

def average_mark_lct(lecturers_list, course_lct):
    mark_list=[]
    mark_sum = 0
    for lecturer in lecturers_list:
     if course_lct in lecturer.grades.keys():
        for marks in lecturer.grades.values():
            for mark in marks:
                mark_list.append(mark)
    mark_list_len = len(mark_list)
    for mark in mark_list:
        mark_sum= mark_sum+mark
    return print(mark_sum/mark_list_len)

course_hw = input('Введите название курса для оценки студентов:')
average_mark_hw(Student.students_list, course_hw)
print("--------------")
course_lct = input('Введите название курса для оценки лекторов:')
average_mark_hw(Lecturer.lecturers_list, course_lct)
