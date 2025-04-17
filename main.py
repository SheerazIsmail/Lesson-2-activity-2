# parent class
class Person( object ):

    # __init__ is known as the constructur
    def __init__(self, name, idnumber):
            self.name = name
            self.idnumber = idnumber
    def display(self):
          print(self.name)
          print(self.idnumber)

# child class
class Employee( Person ):
      def __init__(self, name, idnumber, salary, post):
             self.salary = salary
             self.post = post

             # invoking the __init__ of the parent class
             Person.__init__(self, name, idnumber)

# creating of an object variable or an instance
a = Employee('Sarmad', 164700786, 20000, "Intern")
b = Employee('Sadeeqa', 19876444, 30000, "Manager")
c = Employee('Ahmed', 12234567, 50000, "CEO")

# calling a function  of the class Person using its Instance
a.display()
b.display()
c.display()

            
        