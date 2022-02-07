import void as void

from cap_3.Exceptions.invalid_employee_type_exception import InvalidEmployeeTypeException

# Part 1
class Money:
    def calculatePay(self, e: Employee):
        # Function so extended and if create a new functionary will need to implement and modify the function,
        # this function do more than one thing, broke the sole responsibility and open/close principles because have more than one
        # reason to modify the function and need to modify the function always when create a new type
            switch = {
                'COMMISSIONED': calculateCommissionedPay(e),
                'Hourly' : calculateHourly(e),
                'SALARIED': calculateSalariedPay(e),
                'default': InvalidEmployeeTypeException

# Part 2
class Employee:
    # Abstract class with abstract methods, so in the class which call the methods will be torn on a concrete method
    def isPayday(self) -> bool:
        pass

    def calculatePay(self) -> Money:
        pass

    def deliverPay(self) -> void:
        pass

class EmployeeFactory(Employee):
    def makeEmployee(self, r: EmployeeRecord) -> Employee:
        try:
            return
        except:
            InvalidEmployeeTypeException

class EmployeeFactoryImpl(EmployeeFactory):
    def makeEmployee(self, r: EmployeeRecord) -> Employee:
        switch = {
            'COMMISSIONED': CommissionedEmployee(r),
            'HOURLY': HourlyEmployee(r),
            'SALARIED': SalariedEmployee(r)
            'default': InvalidEmployeeTypeException
        }

