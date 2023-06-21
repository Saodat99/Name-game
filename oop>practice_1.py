# ** Practice OOP Vocabulary Challange
# Instructions:
# 1) Create a class called Treehouse
# 2) Add a class attribute called product that is equal to the string 'coding courses'
# 3) Add an initialize method that takes a parameter called name 
# 4) Add a name instance attribute set equal to the parameter being passed in
# 5) Create a method called learn. Inside the method return a string that contains the name instance attribute so you would get something like "Tim is learning to code!" where Tim is the name passed into the class
# 6) Create an instance of the class and save it to a variable named my_treehouse. Pass in your name as the name parameter
# 7) Call your learn method and print out result

class Treehohouse:
    product = 'coding courses'

    def __init__(self, name):
        self.name = name

    def learn(self):
        return f"{self.name} is learning to code"
    

my_treehouse = Treehohouse("Saodat")


print(my_treehouse.learn())

