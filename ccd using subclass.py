# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 19:01:37 2018

@author: SONY
"""

class ccd():
    
    def __init__(self,first,last):
        
        self.first=first
        self.last=last
        self.email=first+'.'+'last'+'@email.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
class Employee(ccd):
    
    no_of_Employee_mattikeri=0
    no_of_Employee_yeshwantapur=0
    no_of_Employee_BEL=0
    
    def __init__(self, first, last, branch):
        super().__init__(first, last)
        self.branch=branch
        
class Manager(ccd):

    def __init__(self, first, last,email, employees=None):
        super().__init__(first, last)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
        if (self.Employee=="mattikeri"):
            no_of_Employee_mattikeri=+1
        if(self.Employee=="Yeshwantapur"):
            no_of_Employee_yeshwantapur=+1
        if(self.Employee=="BEL"):
            no_of_Employee_BEL=+1
            
if __name__ == '__main__':
    emp1=Employee('suma','sk','mattikeri')
    emp2=Employee('manu','dk','yeshwantapur')
    emp3=Employee('ram','jk','BEL')
    emp4=Employee('kamala','mk','mattikeri')
    emp5=Employee('zeba','hm','yeshwantapur')
    emp6=Employee('shilpa','rk','BEL')
    mgr=Manager('priya','sn',emp1)
    
    #mgr=Manager('priya','sn',[emp2,emp5])
    #mgr=Manager('priya','sn',[emp3,emp6])
    
    print(mgr.email)
    print(mgr.__dict__)   
    #mgr.print_emps()    
            
            
            
            
        
    