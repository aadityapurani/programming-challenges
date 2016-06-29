#Day 12 Inheritance 30 Days of Code
#Coded by Aaditya Purani
#Python 2
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = map(int, scores)
        
    def calculate(self):
        a = float(sum(self.scores))/len(self.scores)
        if (a >= 90):
            return 'O'
        elif (a >= 80):
            return 'E'
        elif (a >= 70):
            return 'A'
        elif (a >= 55):
            return 'P'
        elif (a >= 40):
            return 'D'
        else:
            return 'T'
    
#Python 3 Solution
#Coded by Aaditya Purani
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super(Student, self).__init__(firstName, lastName, idNumber)
        self.scores = scores
    
    def calculate(self):
        average = sum(scores)/len(scores)
        if average <= 100 and average >= 90:
            return "O"
        if average <90 and average >= 80:
            return "E"
        if average <80 and average >= 70:
            return "A"
        if average < 70 and average >= 55:
            return "P"
        elif average < 55 and average >= 40:
            return "D"
        else:
            return "T"
  
