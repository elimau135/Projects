import Faculty
import Professor

class Assistant:
    
    attr_name = None
    attr_age = None 
    attr_faculty = Faculty
    attr_boss = Professor     
    
    
    def __init__(self, name, age, fac, prof):
        self.attr_name = name
        self.attr_age = age
        self.attr_faculty = fac
        self.attr_boss = prof

    def get_name_method(self):
        return self.attr_name     

    def get_age_method(self):
        return self.attr_age
        
    def get_faculty_method(self):
        return self.attr_faculty
    
    def get_boss_method(self):
        return self.attr_boss
        
    def set_name_method(self, name):
        self.attr_name = name
        
    def set_age_method(self, age):
        self.attr_age = age
    
    def set_faculty_method(self):
        self.attr_faculty = Faculty.Faculty()
        
    def set_boss_method(self):
        self.attr_boss = Professor.Professor()
        
     
 