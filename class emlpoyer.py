class Employee () :

    def __init__(self, number, name, sales, bonus_hrs, base_salary):
        self.number = number
        self.name = name
        self.sales = sales
        self.bonus_hrs = bonus_hrs
        self.base_salary = base_salary

   

emp1 = Employee(1, "Kbour", 20000, 42, 30000)
emp2 = Employee(2, "Bouchaib", 1500, 74, 15000)

print("The employee name is {} and base salary is: {}".format(emp1.name, emp1.base_salary))
print("The employee name is {} and base salary is: {}".format(emp2.name, emp2.base_salary))




