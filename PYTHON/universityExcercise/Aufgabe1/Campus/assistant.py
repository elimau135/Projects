import  professor
import faculty

class Assistant:

    attr_faculty = faculty.Faculty()
    attr_professor = professor.Self_Professor()

    def __init__(self):
        self.boss = professor.Professor()
        self.name = ""
        self.age = 0
        self.fac = faculty.Facutly()

    def main(self, name, age, prof, fac):
        self.boss = prof
        self.name = name
        self.age = age
        self.fac = fac

    
