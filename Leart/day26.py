from abc import ABCMeta, abstractclassmethod


class Employee(metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name
    
    @abstractclassmethod
    def get_salary(self):
        pass

class Manager(Employee):
    def get_salary(self):
        return 15000
class Programmer(Employee):
    def __init__(self, name, hours = 0):
        self.hours = hours
        super().__init__(name)
    def get_salary(self):
        return 200* self.hours
class Salesman(Employee):
    def __init__(self, name, sales = 0):
        self.sales = sales
        super().__init__(name)
    def get_salary(self):
        return 1800+ self.sales *0.05

class Factory():
    @staticmethod
    def create(emp_type, *args, **kwargs):
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp
def main():
    """主函数"""
    emps = [
        Factory.create('M', '曹操'), 
        Factory.create('P', '荀彧', 120),
        Factory.create('P', '郭嘉', 85), 
        Factory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print('%s: %.2f元' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
        
    
    
