class Course:

    name = "IT academy"
    lang = "Python"
    group = "Winter2021"


    def lessons(self):
        print("Список уроков")

    def exams(self):
        print("Экзамен")


course_1 = Course()

course_2 = Course()

print(course_2.group)