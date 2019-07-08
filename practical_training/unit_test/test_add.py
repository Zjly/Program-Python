from unittest import TestCase

from practical_training.unit_test import unit_test


class TestAdd(TestCase):
	def test_add(self):
		# m = 10
		# n = 8
		# result = 18
		# o = unit_test.add(m, n)
		# assert result == o

		m = 5
		n = 10
		result = 10
		o = unit_test.add(m, n)
		assert result == o