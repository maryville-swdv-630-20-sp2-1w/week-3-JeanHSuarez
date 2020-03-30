import unittest
from persons import Persons
from persons import Individual
from persons import Staff
from persons import CaseWorker

class TestPersons(unittest.TestCase):

	def test_fullName(self):
		person_1 = Persons('Jeff', 'Miller')
		person_2 = Persons('Jordan', 'Chamberlain')

		self.assertEqual(person_1.__str__(), 'Jeff Miller')
		self.assertEqual(person_2.__str__(), 'Jordan Chamberlain')

		indiv_1 = Individual('Jeff', 'Miller', '123121234')
		indiv_2 = Individual('Jordan', 'Chamberlain', '345343456')

		self.assertEqual(indiv_1.__str__(), 'Jeff Miller')
		self.assertEqual(indiv_2.__str__(), 'Jordan Chamberlain')

		staff_1 = Staff('Jeff', 'Miller', '123121234', 35.00)
		staff_2 = Staff('Jordan', 'Chamberlain', '345343456', 20.00)

		self.assertEqual(staff_1.__str__(), 'Jeff Miller')
		self.assertEqual(staff_2.__str__(), 'Jordan Chamberlain')

		caseworker_1 = CaseWorker('Jeff', 'Miller', 'Service Access Management')
		caseworker_2 = CaseWorker('Jordan', 'Chamberlain', 'Hope Counseling Center')

		self.assertEqual(caseworker_1.__str__(), 'Jeff Miller')
		self.assertEqual(caseworker_2.__str__(), 'Jordan Chamberlain')


if __name__== '__main__':
	unittest.main()
