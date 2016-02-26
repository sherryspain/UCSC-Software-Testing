import unittest
from python.src import get_factorial

class test_factorial(unittest.TestCase):
	def test_factorial_returns_24(self):
		self.assertEqual(24, get_factorial.factorial(4))
		
