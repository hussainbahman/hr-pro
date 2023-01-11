class Employee():
    def __init__(self, name, age, salary, employment_years, ):
       self.name = name
       self.age = age
       self.salary = salary
       self.employment_years = employment_years
    def get_annual_salary(self):
        return self.salary*12


    def __str__(self):
        return f"my name is {self.name} i'm {self.age} years old my salary {self.salary} working {self.employment_years} years "
        

    



       


   #Employee class here

class Manager(Employee):
    def __init__(self, name, age, salary, employment_years, bonus_percentage ):
        super().__init__(name, age, salary,employment_years )
        self.bonus_percentage = bonus_percentage


        def info(self):
            print("the bonus is {bonus_percentage}")


print(Employee("hussain",18,5000,5))




    #Manager class here
        
def main(self):
	# main code here

 if __name__ == '__main__':
	 main()
    
