class Person:

    def __init__(self, cf: str, name: str, surname: str, age: int):

        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age



class Student(Person):

    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)
        self.group = ''

    def set_group(self, group):

        self.group = group
        


class Lecturer(Person):

    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)
        
        
class Group:

    def __init__(self, name: str, limit: int):

        self.name = name
        self.limit = limit
        self.students: list[Student] = []
        self.lecturers: list[Lecturer] = []

    def get_name(self):

        return self.name
    
    def get_limit(self):

        return self.limit
    
    def get_students(self):

        return self.students
    
    def get_limit_lecturers(self):

        return max(1, len(self.students) // 10)
    
    def add_student(self, student: Student):

        if len(self.students) < self.limit:

            self.students.append(student)
            student.set_group(self)

        
        else:

            print('Limite studenti raggiunto')

    def add_lecturer(self, lecturer: Lecturer):

        if len(self.lecturers) < self.get_limit_lecturers():

            self.lecturers.append(lecturer)

        else:

            print('Limite insegnanti raggiunto')



