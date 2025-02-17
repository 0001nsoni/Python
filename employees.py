'''
Classes:- a class is a blueprint or a template for creating objects and it defines the 
structure and behaviour of that objects.
'''
'''
Objects:-
An objects is an instance of a class. with its own unique data and the ability to perform
actions
'''

class Employees:
    def __init__(self,name,email,dept,salary):
        self.name=name
        self.email=email
        self.dept=dept
        self.salary=salary
        
    def emp_info(self):
        print("\n")
        print("*"*30)
        print(f'Name is {self.name}')
        print(f'Name is {self.email}')
        print(f'Name is {self.dept}')
        print(f'Name is {self.salary}')
        print("*"*30)

      

    def change_dept(self,new_dept):
        self.dept=new_dept



    pass
emp1= Employees("Raju","raju@gmail.com","sales",50000)
emp2= Employees("ShaM","SHAM@gmail.com","QA",70000)

emp1.emp_info()
emp1.change_dept("OPS")
emp1.emp_info()
