class Persons:
	def __init__ (self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName


	def set_firstName(self, firstName):
		self.firstName = firstName
		return self.firstName

	def get_firstName(self):
		return self.firstName

	def set_lastName(self, lastName):
		self.lastName = lastName
		return self.lastName

	def __str__(self):
		return "{} {}".format(self.firstName, self.lastName)


class Individual(Persons):

	def __init__ (self, firstName, lastName, ssNumber, *args, **kwargs):
		super(Individual, self).__init__(firstName, lastName)
		self.ssNumber = ssNumber
		self.program = []
		
	def set_ssNumber(self, ssNumber):
		self.ssNumber = ssNumber
		return self.ssNumber

	def get_ssNumber(self):
		return self.ssNumber

	def intake(self, programList):
		self.program.append(programList)


class Staff(Persons):

	def __init__ (self, firstName, lastName, ssNumber, pay):
		super(Staff, self).__init__(firstName, lastName)
		self.ssNumber = ssNumber
		self.pay = float(pay)


	def set_ssNumber(self, ssNumber):
		self.ssNumber = ssNumber
		return self.ssNumber

	def get_ssNumber(self):
		return self.ssNumber

	def set_pay(self, pay):
		self.pay = pay
		return self.pay

	def get_pay(self):
		return self.pay


class CaseWorker(Persons):

	def __init__ (self, firstName, lastName, agency):
		super(CaseWorker, self).__init__(firstName, lastName)
		self.agency = agency


	def set_agency(self, agency):
		self.agency = agency
		return self.agency

	def get_agency(self):
		return self.agency

