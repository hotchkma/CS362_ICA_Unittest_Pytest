import palindrome
import unittest

class testCaseCalc(unittest.TestCase):
	def test_add(self):
		self.assertEqual(palindrome.palindrome("racecar"),1)
		self.assertEqual(palindrome.palindrome("mom"),1)
		self.assertEqual(palindrome.palindrome("raccar"),1)
		self.assertEqual(palindrome.palindrome("d"),1)
		self.assertEqual(palindrome.palindrome("da"),0)
		self.assertEqual(palindrome.palindrome("dad"),1)
		self.assertEqual(palindrome.palindrome(""),1)
		self.assertEqual(palindrome.palindrome(" "),1)
		self.assertEqual(palindrome.palindrome("lol"),1)
		self.assertEqual(palindrome.palindrome("pp"),1)
		self.assertEqual(palindrome.palindrome("p p"),1)
		self.assertEqual(palindrome.palindrome("d d d d"),1)

if __name__ == "__main__":
	unittest.main()
