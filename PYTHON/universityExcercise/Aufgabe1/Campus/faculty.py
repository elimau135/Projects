import assistant
import  professor

class Faculty:
   
   attr_assistant = assistant.Assistant()
   attr_professor = professor.Self_Professor()


   def __init__(self, assis, profs):
        self.attr_assistant = assis
        self.attr_professor = profs

        
   # def main(self):
       