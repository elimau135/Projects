import professor
import faculty
import assistant

class Executable:
    prof = professor()
    fac = faculty()
    assi = assistant()


    def main(self, prof, fac, assi):
        self.prof = prof
        self.fac = fac
        self.assi = assi
        print("Hello wordl")
    


ex = Executable()
ex.main()

