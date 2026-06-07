# #create a class for a student with attributes like name, age, grade, subject, score
# #methods like get_score to access private score attribute and set_score to set private score attribute

class Student:
    def __init__(self,name,age,grade,subject,score):
          self.name = name
          self.age = age
          self.grade = grade
          self.subject = subject
          self.score = score

    def _get_score(self):
         return self.score
    
    def __set_score(self,new_score):
         if new_score <= 100:
              self.score = new_score
         else:
              print("Score cannot be more than 100. ")

    def update_score(self,new_score):
         self.__set_score(new_score)
    
std1 = Student('Ram', 24, 3.5, 'math', 50)

print(std1._get_score())
std1.update_score(60)

print(std1._get_score())