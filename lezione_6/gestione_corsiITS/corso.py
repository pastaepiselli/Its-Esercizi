class Room:

    def __init__(self, id: str, floor: str, seats: int):

        self.id = id 
        self.floor = floor
        self.seats = seats
        self.area = seats * 2

    def get_id(self):

        return self.id
    
    def get_floor(self):

        return self.floor
    
    def get_seats(self):

        return self.seats
    
    def get_area(self):

        return self.area
    

class Building:

    def __init__(self, name: str, address: str, floors: tuple[int, int]):


        self.name = name
        self.address = address
        self.floors = floors
        self.rooms: list[Room] = []

    def get_floors(self):

        return self.floors
    
    def get_rooms(self):

        return self.rooms
    
    def add_room(self, new_room: Room):

        if new_room not in self.rooms:

            if self.floors[0] <= new_room.get_floor() <= self.floors[1]:
                self.rooms.append(new_room)

           
        

    def area(self):
        sum: int = 0

        for stanze in self.rooms:

            sum += stanze.get_area()


        return sum
        


class Person:

    def __init__(self, cf: str, name: str, surname: str, age: int):

        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age



class Student(Person):

    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)
        self.group = None

    def set_group(self, group: str):

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



class Course:

    def __init__(self, name: str):

        self.name = name
        self.groups: list[Group] = []

    def register(self, student: Student):

        for elem in self.groups:

            if elem.get_students < elem.get_limit():

                elem.add_student(student)
                break


    def get_groups(self):

        return self.groups
    
    def add_group(self, group: Group):

        self.groups.append(group)
    
        