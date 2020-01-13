class employee():
  def __init__(self):
     self.age=21
     self.name='preeti'
     self.salary=70000000
     self.id=1000

emp1=employee()
print(id(employee))
print('inst',id(emp1))
"""
emp2=employee('akshat',32,10000000,1001)
print(emp1.__dict__)
print(emp2.__dict__)
class child(employee):
  
  def display(self):
    print(self.id,self.age,self.salary,self.name)
  
obj=child()
obj.display()"""
