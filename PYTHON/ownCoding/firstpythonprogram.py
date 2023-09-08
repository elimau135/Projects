
x = int(6)
x = str("Hello my dear")
X = "What is popping"
print(type(x))
#print(X + type(X)) -> results in error because of the plus
print(X,type(X))


class Person:
    def _init_(self, fname, lname):
        self.firstname =fname
        self.lastname =lname

    def printname(self):
        print(self.firstname, self.lastname)
    
X = Person("ELias" , "Maurer")
X.printname