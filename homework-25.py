# Ссылка на UML: ***

class User:
    __last_id = 0

    def __init__(self, name):
        User.__last_id += 1
        self.__id = User.__last_id
        self.name = name
        self.__enrollment_courses = dict()

    def __str__(self):
        return str(self.__id) + '. ' + str(self.name)

    # метод зачисления пользователя на курс
    def enrollment(self, course):
        if type(course) == Course and course.name not in self.__enrollment_courses:
            self.__enrollment_courses[course.name] = None
        else:
            print('=> Пользователь', self.name, 'уже был зачислен на курс', course.name)

    # метод выставления итоговой оценки пользователю за курс
    def grade(self, grade, course):
        if course.name in self.__enrollment_courses:
            self.__enrollment_courses[course.name] = grade
        else:
            print('=> Пользователь', self.name, 'не зачислен на курс', course.name)

    # метод получения словаря курсов с оценками, на которые зачислен пользователь
    def get_enrollment(self):
        return str(self.__enrollment_courses)

    # метод получения спика курсов, на которые зачислен пользователь
    # def get_enrollment(self):
    #     return list(self.__enrollment_courses.keys())

    # метод получения итоговой оценки
    def get_grade(self, cource):
        return str(self.__enrollment_courses.get(cource.name))


class Course:
    __last_id = 1

    def __init__(self, course_name):
        Course.__last_id += 1
        self.__id = Course.__last_id
        self.name = course_name

    def __str__(self):
        return str(self.__id) + '. ' + str(self.name)


# создание курсов
mathematics = Course('Математика')
physics = Course('Физика')
hystory = Course('История')

# создание пользователей
user1 = User('Иванов Пётр Вячеславович')
user2 = User('Степанов Игорь Николавич')
user3 = User('Смирнов Леонид Игоревич')

# зачисление студентов
user1.enrollment(mathematics)
user1.enrollment(physics)
user2.enrollment(physics)
user2.enrollment(hystory)
user1.enrollment(mathematics)   # повторное зачисление, проверка

# выставление итоговых оценок по курсам
user1.grade(5, mathematics)
user1.grade(4, physics)
user2.grade(4, hystory)
user2.grade(5, mathematics)     # user2 не зачислен на курс по математике, проверка
user3.grade(2, physics)         # user3 не зачислен на курс по физике, проверка

# инфа по пользователям
print()
print(user1, ', зачислен на курсы: ', user1.get_enrollment(), sep='')
print(user2, ', зачислен на курсы: ', user2.get_enrollment(), sep='')
print(user3, ', зачислен на курсы: ', user3.get_enrollment(), sep='')

# получение оценки пользователя за курс
print()
print('Итоговая оценка пользователя ', user1.name, ' по курсу ',
      mathematics.name, ': ', user1.get_grade(mathematics), sep='')
print('Итоговая оценка пользователя ', user2.name, ' по курсу ',
      hystory.name, ': ', user2.get_grade(hystory), sep='')
