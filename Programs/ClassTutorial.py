

class Employee:

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.firsst = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	# @classmethod
	# def set_raise_amt(cls, amount):
	# 	cls.raise_amount = amount

	# @classmethod
	# def from_string(cls, emp_str):
	# 	first, last, pay = emp_str.split('-')
	# 	return cls(first, last, pay)

	# @staticmethod
	# def is_workday(day):
	# 	if day.weekday() == 5 or day.weekday() == 6:
	# 		return False
	# 	return True

class Developer(Employee):

	raise_amount = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang


class Manager(Employee):

	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print ('--> ', emp.fullname())


dev1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev2 = Developer('Test', 'User', 60000, 'C++')

mgr1 = Manager('Sue', 'Smith', 90000, [dev1])

print(mgr1.email)

mgr1.add_emp(dev2)

mgr1.remove_emp(dev1)

mgr1.print_emps()

#print(dev1.email)
#print(dev1.prog_lang)

# import datetime
# my_date = datetime.date(2016, 7, 10)

# print(Employee.is_workday(my_date))

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-60000'
# emp_str_3 = 'Jane-Doe-100000'

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)



