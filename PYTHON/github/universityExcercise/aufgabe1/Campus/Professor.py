import Faculty

class Professor:
    
    attr_name = None
    attr_age = None
    attr_researchArea = None
    #attr_faculty = Faculty 
    attr_talking = True 
    
    
    def __init__(self, name, age, researchArea, fac, talking):
        self.attr_name = name
        self.attr_age = age
        self.attr_researchArea = researchArea
        self.attr_faculty = fac
        self.attr_talking = talking
       
    def get_name_method(self):
        return self.attr_name
    
    def get_age_method(self):
        return self.attr_age
        
    def get_researchArea_method(self):
        return self.attr_researchArea
        
    def get_faculty_method(self):
        return self.attr_faculty

    def get_talking_method(self):
        return self.attr_talking
    
    def set_name_method(self, name):
        self.attr_name = name
  
    def set_age_method(self, age):
        self.attr_age = age
    
    def set_researchArea_method(self, researchArea):
        self.attr_researchArea = researchArea
        
    def set_faculty_method(self):
        self.attr_faculty = Faculty.Faculty()
        
    def set_talking_method(self, talking):
        self.attr_talking = talking

