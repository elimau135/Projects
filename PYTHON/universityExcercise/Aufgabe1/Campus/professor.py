
#import faculty

class Self_Professor:

    attr_age = None 
    attr_talking = False 
    attr_name = None 
    #attr_fac = faculty.Faculty()   # Initialize as None

    def __init__(self, name, age, talking):
        self.attr_name = name
        self.attr_age = age
        self.attr_talking = talking
        #self.attr_fac

  #  def set_faculty(self, faculty_instance):
   #     self.attr_fac = faculty_instance  # Use a method to set 'fac' attribute

    def get_method(self):
        print(self.attr_age, self.attr_name, self.attr_talking)

    def set_method(self,name, age, talking):
        self.attr_age = age
        self.attr_name = name
        self.attr_talking = talking


professor_Instance = Self_Professor("Elias", 21, False)
 
professor_Instance.get_method()