#import Professor
#import Assistant
#import Faculty

class Main:
    
    def main():
        x = int(input("Write a number "))
        if x < 0:
            x = 0
            print("Negative changed to zero")
            
        elif x == 0:
            print('Zero')
        
        elif x ==1:
            print("single")
            
        else:
            print('More')

s = Main

s.main()