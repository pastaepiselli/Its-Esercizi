class Student:
    def __init__(self, name, studyProgam, age, gender):
        self.name = name
        self.studyProgram = studyProgam
        self.age = age
        self.gender = gender
    
    def printInfo(self):
        print(self.name, self.studyProgram, self.age, self.gender)
        